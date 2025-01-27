import sqlite3
from sqlite3 import Cursor
from typing import List, Any
from datetime import date, datetime
import os

from Obiekty import *

# ! todo: change this in the final project!!!
DB_CREATION_QUERY_PATH = "db_creation_query.sql"
# todo: Czy metody to modyfikowania bazy powinny automatycznie commitować zmiany?
# todo: error/none handling
# ! todo: w wielu metodach zapomniałem zrobić self.commit() ups, trzeba będzie to naprawić
# todo: upewnić się, że metody zwracają informację czy kwerenda była poprawna. W końcu jaką mam pewność, że Ryszard poprawnie sprawdzi czy Pokój istnieje?
# todo: dodać pierwszego admina
# ! todo: allow Admin and others to change password

class SQLLiteDB:
    # todo: metoda do implementacji
    @classmethod
    def baza_istnieje(cls, path) -> bool:
        return os.path.exists(path)

    def __init__(self, file_path: str) -> None:
        init_database = not os.path.exists(file_path)
        path_is_a_dir = os.path.isdir(file_path)
        
        if path_is_a_dir:
            raise ValueError("given path is a directory - database cannot be created nor loaded. Path should point to an initialized database, or a not existing path (database will be created there).")

        self.connection = sqlite3.connect(file_path, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        self.cursor = self.connection.cursor()
        self.path = file_path # todo: should be a property of a project
        
        if init_database:
            self.initialize_database()
    
    def initialize_database(self):
        with open(DB_CREATION_QUERY_PATH, "r", encoding="utf-8") as query:
            for statement in query.read().split(";"):
                self.execute(statement)

        self.commit()

    def execute(self, query: str, *args: List[Any]) -> Cursor:
        return self.cursor.execute(query, tuple(args)) # ? Do I need to turn args into a tuple?

    def commit(self) -> None:
        self.connection.commit()

    def exec_and_commit(self, query: str, *args: List[Any]):
        self.execute(query, *args)
        self.commit()
    
    def rollback(self) -> None:
        self.connection.rollback()

    def close(self) -> None:
        self.connection.close()

    def __del__(self) -> None:
        self.connection.close()


    # helper functions
    def nick_to_login(self, nick: str):
        self.execute(
            "SELECT login FROM Uzytkownicy WHERE nazwa = ?",
            nick
        )

        return self.cursor.fetchone()[0]
    
    def login_to_nick(self, login: str):
        self.execute(
            "SELECT nazwa FROM Uzytkownicy WHERE login = ?",
            login
        )

        return self.cursor.fetchone()[0]


    # --------------- Logowanie ---------------

    def czy_login_istnieje(self, login:str) -> bool:
        self.execute(
            "SELECT * FROM Uzytkownicy WHERE login = ?",
            login
        )

        return self.cursor.fetchone() is not None
    
    def czy_nick_istnieje(self, nick:str) -> bool:
        self.execute(
            "SELECT * FROM Uzytkownicy WHERE nazwa = ?",
            nick
        )

        return self.cursor.fetchone() is not None
    
    def czy_rola_istnieje(self, rola:str) -> bool:
        self.execute(
            "SELECT * FROM Role WHERE nazwa = ?",
            rola
        )

        return self.cursor.fetchone() is not None

    def authenticate(self, login: str, token: str) -> bool:
        self.execute(
            "SELECT * FROM Uzytkownicy WHERE login = ? AND token = ?",
            login,
            token
        )

        return self.cursor.fetchone() is not None
    
    def rola_uzytkownika(self, login: str) -> str:
        self.execute(
            "SELECT rola FROM Uzytkownicy WHERE login = ?",
            login
        )

        return self.cursor.fetchone()[0]

    def log_in(self, login: str, haslo: str) -> bool:
        self.execute(
            "SELECT * FROM Uzytkownicy WHERE login = ? AND haslo = ?",
            login,
            haslo
        )

        return self.cursor.fetchone() is not None
    
    def czy_zweryfikowany(self, login: str) -> bool:
        self.execute(
            "SELECT * FROM Uzytkownicy WHERE login = ? AND rola = 'Niezweryfikowany'",
            login
        )

        return self.cursor.fetchone() is None


    # --------------- kody zaproszeniowe ---------------

    def istnieje_kod_zpr(self, kod_zapr: str) -> bool:
        self.execute(
            "SELECT * FROM KodyZaproszeniowe WHERE kod = ?",
            kod_zapr
        )
        return self.cursor.fetchone() is not None

    def dodaj_kod_zaproszniowy(self, kod_zapr: str):
        self.exec_and_commit(
            "INSERT INTO KodyZaproszeniowe VALUES (?, CURRENT_DATE)",
            kod_zapr
        )

    def usun_kod_zaproszeniowy(self, kod_zapr: str):
        self.exec_and_commit(
            "DELETE FROM KodyZaproszeniowe WHERE kod = ?",
            kod_zapr
        )



    # --------------- Użytkownicy ---------------
    def wstaw_uzytkownika(self, login: str, haslo: str, token: str, rola: str, nick: str):
        self.exec_and_commit(
            "INSERT INTO Uzytkownicy(login, haslo, token, rola, nazwa) VALUES (?, ?, ?, ?, ?)",
            login,
            haslo,
            token,
            rola,
            nick
        )
    
    def ustaw_date_aktywnosci_teraz(self, login: str):
        self.exec_and_commit(
            "UPDATE Uzytkownicy SET last_update = CURRENT_DATE WHERE login = ?",
            login
        )

    def ustaw_token(self, login: str, token: str) -> None:
        self.exec_and_commit(
            "UPDATE Uzytkownicy SET Token = ? WHERE login = ?",
            token,
            login
        )

    def czyszczenie_polnocne(self):
        self.exec_and_commit(
            "DELETE FROM KodyZaproszeniowe WHERE (julianday(CURRENT_DATE) - julianday(data_dodania)) > 1"
        )

        self.exec_and_commit(
            "UPDATE Uzytkownicy SET token = NULL WHERE (julianday(CURRENT_DATE) - julianday(last_update)) > 1"
        )

    def ustaw_role(self, loginZmienianego: str, nowaRola: str):
        self.exec_and_commit(
            "UPDATE Uzytkownicy SET rola = ? WHERE login = ?",
            nowaRola,
            loginZmienianego
        )

    def lista_niezweryfikowanych(self):
        self.execute(
            "SELECT nazwa FROM Uzytkownicy WHERE rola = 'Niezweryfikowany'"
        )

        return self.cursor.fetchall()


    # --------------- Pokoje ---------------
    def istnieje_pokoj(self, nazwa_pokoju: str) -> bool:
        self.execute(
            "SELECT * FROM Pokoje WHERE nazwa = ?",
            nazwa_pokoju
        )
        
        return self.cursor.fetchone() is not None

    
    def stworz_pokoj(self, nazwa_pokoju: str):
        self.exec_and_commit(
            "INSERT INTO Pokoje VALUES (?)",
            nazwa_pokoju
        )


    def usun_pokoj(self, nazwa_pokoju: str):
        self.exec_and_commit(
            "DELETE FROM Pokoje WHERE nazwa = ?",
            nazwa_pokoju
        )


    def dodaj_do_pokoju(self, nazwa_pokoju: str, dodawany_login: str):
        self.exec_and_commit(
            "INSERT INTO CzlonkowiePokojow(uzytkownik, pokoj) VALUES (?, ?)",
            dodawany_login,
            nazwa_pokoju,
        )


    def usun_z_pokoju(self, nazwa_pokoju: str, usuwany_login: str):
        self.exec_and_commit(
            "DELETE FROM CzlonkowiePokojow WHERE uzytkownik = ? AND pokoj = ?",
            usuwany_login,
            nazwa_pokoju
        )


    def czy_uzytkownik_w_pokoju(self, nazwa_pokoju: str, login: str) -> bool:
        self.execute(
            "SELECT * FROM CzlonkowiePokojow WHERE uzytkownik = ? AND pokoj = ?",
            login,
            nazwa_pokoju
        )

        return self.cursor.fetchone() is not None

    # todo: test
    def pokoje_czlonkowskie(self, login: str) -> List[str]:
        self.execute(
            "SELECT pokoj, klucz_publiczny, klucz_prywatny FROM KluczeDoPokojow WHERE uzytkownik = ?",
            login
        )

        return self.cursor.fetchall()



    # --------------- Taski ---------------
    def dodaj_task(self, nazwaPokoju: str, task: Task):
        self.exec_and_commit(
            "INSERT INTO Taski(tekst, zrobiony, pokoj, deadline, canvas_x, canvas_y) VALUES (?, ?, ?, ?, ?, ?)",
            task.nazwa,
            False,
            nazwaPokoju,
            task.get_date(),
            task.x,
            task.y
        )

    def usun_task(self, nazwaPokoju: str, task: Task):
        self.exec_and_commit(
            "DELETE FROM Taski WHERE pokoj = ? AND id = ?",
            nazwaPokoju,
            task.id,
        )
    
    def aktualizuj_task(self, nazwaPokoju: str, task: Task):
        self.exec_and_commit(
            "UPDATE Taski SET tekst = ?, deadline = ?, canvas_x = ?, canvas_y = ? WHERE pokoj = ? AND id = ?",
            task.nazwa,
            task.get_date(),
            task.x,
            task.y,
            nazwaPokoju,
            task.id
        )
    
    def dodaj_zaleznosc_taska(self, idTaska: int, odKtoregoZalezny: int):
        self.exec_and_commit(
            "INSERT INTO KolejnoscTaskow(task,task_wymagany) VALUES (?, ?)",
            idTaska,
            odKtoregoZalezny
        )
    
    def usun_zaleznosci_taska(self, idTaska: int):
        self.exec_and_commit(
            "DELETE FROM KolejnoscTaskow WHERE task = ?",
            idTaska
        )
    
    
    def usun_zaleznosci_od_taska(self, idTaska: int):
        self.exec_and_commit(
            "DELETE FROM KolejnoscTaskow WHERE task_wymagany = ?",
            idTaska
        )
    
    
    def czy_mozna_zaznaczyc(self, idTaska: int):
        self.execute(
            "SELECT * FROM (KolejnoscTaskow JOIN Taski ON (KolejnoscTaskow.task_wymagany = Taski.id)) WHERE KolejnoscTaskow.task = ? AND Taski.zrobiony = 0",
            idTaska
        )

        return self.cursor.fetchone() is None
    
    
    def czy_mozna_odznaczyc(self, idTaska: int):
        self.execute(
            "SELECT * FROM (Taski JOIN KolejnoscTaskow ON (Taski.id = KolejnoscTaskow.task)) WHERE KolejnoscTaskow.task_wymagany = ? AND Taski.zrobiony = 1",
            idTaska
        )

        return self.cursor.fetchone() is None
    
    
    
    def dodaj_taski(self, nazwaPokoju: str, listaTaskow: list[Task]):
        for task in listaTaskow:
            self.dodaj_task(nazwaPokoju, task)
        for task in listaTaskow:
            for zaleznosc in task.wymaganeTaski:
                self.dodaj_zaleznosc_taska(task.id,zaleznosc)
        

    def usun_taski(self, nazwaPokoju: str, listaTaskow: list[Task]):
        for task in listaTaskow:
            self.usun_zaleznosci_taska(task.id)
            self.usun_zaleznosci_od_taska(task.id)
            self.usun_task(nazwaPokoju, task)

    def zaktualizuj_wlasnosci_taskow(self, nazwaPokoju: str, listaTaskow: list[Task]):
        for task in listaTaskow:
            self.aktualizuj_task(nazwaPokoju, task)
        
        for task in listaTaskow:
            self.usun_zaleznosci_taska(task.id)
            for zaleznosc in task.wymaganeTaski:
                self.dodaj_zaleznosc_taska(task.id,zaleznosc)

    def ukoncz_task(self, nazwaPokoju: str, idTaska: int) -> bool:
        self.execute(
            "SELECT * FROM Taski WHERE pokoj=? AND id = ?",
            nazwaPokoju,
            idTaska
        )

        task_exists = self.cursor.fetchone() is not None

        task_isnt_blocked = self.czy_mozna_zaznaczyc(idTaska)

        if task_exists and task_isnt_blocked:
            self.exec_and_commit(
                "UPDATE Taski SET zrobiony = 1 WHERE pokoj=? AND id = ?",
                nazwaPokoju,
                idTaska
            )

        return task_exists and task_isnt_blocked # todo: change to raise 2 different errors

        

    def odznacz_task(self, nazwaPokoju: str, idTaska: int) -> bool:
        # todo: check if it's even possible.
        self.execute(
            "SELECT * FROM Taski WHERE pokoj=? AND id = ?",
            nazwaPokoju,
            idTaska
        )

        task_exists = self.cursor.fetchone() is not None

        task_isnt_blocked = self.czy_mozna_odznaczyc(idTaska)

        if task_exists and task_isnt_blocked:
            self.exec_and_commit(
                "UPDATE Taski SET zrobiony = 0 WHERE pokoj = ? AND id = ?",
                nazwaPokoju,
                idTaska
            )
        return task_exists and task_isnt_blocked # todo: change to raise 2 different errors

    def lista_taskow(self, nazwaPokoju: str):
        self.execute(
            "SELECT * FROM Taski WHERE pokoj = ?",
            nazwaPokoju
        )

        lista = self.cursor.fetchall()
        for i in range(len(lista)):
            lista[i]=list(lista[i])
            self.execute(
                "SELECT * FROM KolejnoscTaskow WHERE task = ?",
                lista[i][0]
            )
            lista[i].append(self.cursor.fetchall())
        
        return lista


    # --------------- Chaty ---------------

    # * w oryginale chciałeś list[str] ale wydaje mi się że ptotrzebujesz więcej info niż tylko same treści (na przykład data wysłania) więc zwracam cały rezultat query
    def pobierz_chat(self, nazwa_pokoju: str, offset: int = 0, liczba_wiadomosci: int = 100):
        self.execute(
            "SELECT autor, data_wyslania, czas_wyslania, tresc FROM Wiadomosci WHERE pokoj = ? ORDER BY data_wyslania, czas_wyslania ASC LIMIT ?, ?",
            nazwa_pokoju,
            offset,
            liczba_wiadomosci
        )

        return self.cursor.fetchall()
        

    def aktualizacja_chatu(self, nazwaPokoju: str, data):
        self.execute(
            "SELECT autor, data_wyslania, czas_wyslania, tresc FROM Wiadomosci WHERE pokoj = ? AND (data_wyslania > ? OR (data_wyslania = ? AND czas_wyslania >= ?)) ORDER BY data_wyslania, czas_wyslania ASC",
            nazwaPokoju,
            data[0],
            data[0],
            data[1]
        )

        return self.cursor.fetchall()
        

    def dodaj_wiadomosc(self, login: str, nazwaPokoju: str, wiadomosc: str):
        nick:str = self.login_to_nick(login)
        self.exec_and_commit(
            "INSERT INTO Wiadomosci (pokoj, tresc, data_wyslania, czas_wyslania, autor) VALUES (?, ?, CURRENT_DATE, CURRENT_TIME, ?)",
            nazwaPokoju,
            wiadomosc,
            nick
        )



    # --------------- Kalendarze ---------------
    def wpis_istnieje(self, nazwaPokoju: str, idWpisu: int) -> bool:
        self.execute(
            "SELECT * FROM Wydarzenia WHERE pokoj = ? AND id = ?",
            nazwaPokoju,
            idWpisu
        )

        return self.cursor.fetchone() is not None

    def kalendarz_dodaj_wpis(self, nazwaPokoju: str, wpis: WpisKalendarza):
        self.exec_and_commit(
            "INSERT INTO Wydarzenia (pokoj, nazwa, data) VALUES (?, ?, ?)",
            nazwaPokoju,
            wpis.nazwa,
            wpis.get_date()
        )
    
    def kalendarz_usun_wpis(self, nazwaPokoju: str, idWpisu: int):        
        self.exec_and_commit(
            "DELETE FROM Wydarzenia WHERE pokoj = ? AND id = ?",
            nazwaPokoju,
            idWpisu
        )

    def kalendarz_modyfikuj_wpis(self, nazwaPokoju: str, idWpisu: int, noweDane: WpisKalendarza):
        self.exec_and_commit(
            "UPDATE Wydarzenia SET nazwa = ?, data = ? WHERE pokoj = ? AND id = ?",
            noweDane.nazwa,
            noweDane.get_date(),
            nazwaPokoju,
            idWpisu
        )

    def pobierz_kalendarz(self, nazwaPokoju: str) -> typing.List[WpisKalendarza]:
        self.execute(
            "SELECT id, nazwa, data FROM Wydarzenia WHERE pokoj = ? ORDER BY data ASC",
            nazwaPokoju
        )

        return self.cursor.fetchall()


    # --------------- Pliki ---------------
    def plik_istnieje(self, nazwaPokoju: str, idPliku: int) -> bool:
        self.execute(
            "SELECT * FROM Pliki WHERE pokoj = ? AND id = ?",
            nazwaPokoju,
            idPliku
        )

        return self.cursor.fetchone() is not None

    def dodaj_plik(self, login: str, nazwaPokoju: str, nazwaPliku: str, zawartoscPliku: bytes):
        nick:str = self.login_to_nick(login)
        self.exec_and_commit(
            "INSERT INTO Pliki (pokoj, nazwa_pliku, autor, zawartosc) VALUES (?, ?, ?, ?)",
            nazwaPokoju,
            nazwaPliku,
            nick,
            zawartoscPliku
        )

    def usun_plik(self, nazwaPokoju: str, idPliku: int):
        self.exec_and_commit(
            "DELETE FROM Pliki WHERE pokoj = ? AND id = ?",
            nazwaPokoju,
            idPliku
        )

    def pobierz_plik(self, nazwaPokoju: str, idPliku: int):
        self.execute(
            "SELECT zawartosc FROM Pliki WHERE pokoj = ? AND id = ?",
            nazwaPokoju,
            idPliku
        )
        
        return self.cursor.fetchone()[0]
    
    def lista_plikow(self, nazwaPokoju: str):
        self.execute(
            "SELECT id, nazwa_pliku, autor FROM Pliki WHERE pokoj = ?",
            nazwaPokoju,
        )
        
        return self.cursor.fetchall()

    def autor_pliku(self, nazwaPokoju: str, idPliku: int, dana: str):
        self.execute(
            "SELECT autor FROM Pliki WHERE pokoj = ? AND id = ?",
            nazwaPokoju,
            idPliku
        )
        
        login: str = self.cursor.fetchone()[0]
        
        if(dana=="login"):
            return login
        
        else:
            return self.login_to_nick(login)



    # --------------- Klucze ---------------
    def klucz_istnieje(self, kluczPub: str):
        self.execute(
            "SELECT * FROM Uzytkownicy WHERE klucz_publiczny = ?",
            kluczPub
        )

        return self.cursor.fetchone() is not None

    def ustaw_klucz(self, login: str, kluczPub: str):
        self.exec_and_commit(
            "UPDATE Uzytkownicy SET klucz_publiczny = ? WHERE login = ?",
            kluczPub,
            login
        )

    def dodaj_klucz_do_pokoju(self, nazwaPokoju: str, kluczPubPokoju: str, kluczPrivPokoju: str, loginPosiadaczaKlucza: str):
        self.exec_and_commit(
            "INSERT INTO KluczeDoPokojow(pokoj, uzytkownik, klucz_publiczny, klucz_prywatny) VALUES (?, ?, ?, ?)",
            nazwaPokoju,
            loginPosiadaczaKlucza,
            kluczPubPokoju,
            kluczPrivPokoju
        )

    def czy_klucz_pokoju_istnieje(self, kluczPubPokoju: str, kluczPrivPokoju: str, loginWlasciciela: str):
        self.execute(
            "SELECT * FROM KluczeDoPokojow WHERE klucz_publiczny = ? AND klucz_prywatny = ? AND uzytkownik = ?",
            kluczPubPokoju,
            kluczPrivPokoju,
            loginWlasciciela,
        )

        return self.cursor.fetchone() is not None


    def usun_klucze_dla_uzytkownika(self, nazwaPokoju: str, loginPosiadaczaKlucza: str):
        self.exec_and_commit(
            "DELETE FROM KluczeDoPokojow WHERE pokoj = ? AND uzytkownik = ?",
            nazwaPokoju,
            loginPosiadaczaKlucza,
        )

    def klucz_uzytkownika(self, loginPosiadaczaKlucza: str) -> str:
        self.execute(
            "SELECT klucz_publiczny FROM Uzytkownicy WHERE login = ?",
            loginPosiadaczaKlucza
        )

        return self.cursor.fetchone()[0] # todo: sprawdzić czy to działa


if __name__ == "__main__":
    db = SQLLiteDB("teaman_database.db")