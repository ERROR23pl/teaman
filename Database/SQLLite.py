import sqlite3
from sqlite3 import Cursor
from typing import List, Any
from datetime import date, datetime
import os

from Database import Database
from Models import *

# ! todo: change this in the final project!!!
DB_CREATION_QUERY_PATH = "db_creation_query.sql"
# todo: Czy metody to modyfikowania bazy powinny automatycznie commitować zmiany?
# todo: error/none handling
# ! todo: w wielu metodach zapomniałem zrobić self.commit() ups, trzeba będzie to naprawić
# todo: ok serio login powinien być kluczem głównym i chuj
# todo: upewnić się, że metody zwracają informację czy kwerenda była poprawna. W końcu jaką mam pewność, że Ryszard poprawnie sprawdzi czy Pokój istnieje?
# todo: dodać pierwszego admina
# ! todo: allow Admin and others to change password

class SQLLiteDB:
    # todo: metoda do implementacji
    @classmethod
    def baza_istnieje(cls, path):
        ...

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

        return self.cursor.fetchone[0]
    
    def login_to_nick(self, login: str):
        self.execute(
            "SELECT nazwa FROM Uzytkownicy WHERE login = ?",
            login
        )

        return self.cursor.fetchone[0]
    
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

    def authenticate(self, login: str, token: str) -> bool:
        self.execute(
            "SELECT * FROM Uzytkownicy WHERE login = ? AND token = ?",
            login,
            token
        )

        return self.cursor.fetchone() is not None
    
    def rola_uzytkownika(self, login: str, token: str) -> str:
        self.execute(
            "SELECT rola FROM Uzytkownicy WHERE login = ? AND token = ?",
            login,
            token
        )

        return self.cursor.fetchone()[0]

    def log_in(self, login: str, haslo: str) -> bool:
        self.execute(
            "SELECT * FROM Uzytkownicy WHERE login = ? AND haslo = ?",
            login,
            haslo
        )

        return self.cursor.fetchone() is not None


    # --------------- kody zaproszeniowe ---------------
    # todo: test 
    def istnieje_kod_zpr(self, kod_zapr: str) -> bool:
        self.execute(
            "SELECT * FROM KodyZaproszeniowe WHERE kod = ?",
            kod_zapr
        )
        return self.cursor.fetchone() is not None

    # todo: test
    def dodaj_kod_zaproszniowy(self, kod_zapr: str):
        self.exec_and_commit(
            "INSERT INTO KodyZaproszeniowe VALUES (?, CURRENT_DATE)",
            kod_zapr
        )

    # todo: test
    def usun_kod_zaproszeniowy(self, kod_zapr: str):
        self.exec_and_commit(
            "DELETE FROM KodyZaproszeniowe WHERE kod = ?",
            kod_zapr
        )



    # --------------- Użytkownicy ---------------
    # ? todo: czy to nie admin powinien dodawać użytkowników?
    def wstaw_uzytkownika(self, login: str, haslo: str, token: str, rola: str, nick: str):
        self.exec_and_commit(
            "INSERT INTO Uzytownicy(nazwa, login, haslo, token, rola) VALUES (?, ?, ?, ?, ?)",
            login,
            haslo,
            token,
            rola,
            nick
        )
    
    def ustaw_date_aktywnosci_teraz(self, login: str, token: str):
        self.exec_and_commit(
            "UPDATE Uzytownicy SET last_update = CURRENT_DATE WHERE login = ? AND token = ?",
            login,
            token
        )

    def ustaw_token(self, login: str, haslo: str, token: str) -> None:
        self.exec_and_commit(
            "UPDATE Uzytownicy SET Token = ? WHERE login = ? AND haslo = ?",
            token,
            login,
            haslo
        )

    
        

    def czyszczenie_polnocne(self):
        self.exec_and_commit(
            "DELETE FROM KodyZaproszeniowe WHERE (julianday(CURRENT_DATE) - julianday(data_dodania)) > 1"
        )

        self.exec_and_commit(
            "UPDATE Uzytkownicy SET token = NULL WHERE (julianday(CURRENT_DATE) - julianday(last_update)) > 1"
        )

    def ustaw_role(self, login_zmienianego: str, nowa_rola: str):
        ...

    def lista_niezweryfikowanych(self):
        ...
    


    # --------------- Pokoje ---------------
    def istnieje_pokoj(self, nazwa_pokoju: str) -> bool:
        self.execute(
            "SELECT * FROM Pokoj WHERE nazwa = ?",
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
        nick_uzytkownika = self.login_to_nick(dodawany_login)
                
        self.exec_and_commit(
            "INSERT INTO CzlonkowiePokojow(uzytkownik, pokoj) VALUES (?, ?)",
            nick_uzytkownika,
            nazwa_pokoju,
        )



    def usun_z_pokoju(self, nazwa_pokoju: str, usuwany_login: str):
        nick_uzytkownika = self.login_to_nick(usuwany_login)
        
        self.exec_and_commit(
            "DELETE FROM CzlonkowiePokojow WHERE uzytkownik = ? AND pokoj = ?",
            nick_uzytkownika,
            nazwa_pokoju
        )


    def czy_uzytkownik_w_pokoju(self, nazwa_pokoju: str, login: str) -> bool:
        nick_uzytkownika = self.login_to_nick(login)

        self.execute(
            "SELECT * FROM CzlonkowiePokoju WHERE uzytkownik = ? AND pokoj = ?",
            nick_uzytkownika,
            nazwa_pokoju
        )

        return self.cursor.fetchone() is not None

    def pokoje_czlonkowskie(self, login: str) -> List[str]:
        # todo: authenticate
        nick = self.login_to_nick(login)
        
        self.execute(
            "SELECT pokoj, klucz_publiczny, klucz_prywatny FROM KluczeDoPokojow WHERE uzytkownik = ?",
            nick
        )

        return self.cursor.fetchall()



    # --------------- Taski ---------------
    def dodaj_taski(nazwaPokoju: str, listaTaskow: list[Task]):
        for task in listaTaskow:
            ...

    def usun_taski(self, nazwaPokoju: str, listaTaskow: Task):
        for task in listaTaskow:
            ...

    def zaktualizuj_wlasnosci_taskow(self, nazwaPokoju: str, listaTaskow: Task):
        for task in listaTaskow:
            ...

    # ? Czy bool tut
    def ukoncz_task(self, nazwaPokoju: str, idTaska: int) -> bool:
        self.execute(
            "SELECT * FROM Taski WHERE id = ?",
            idTaska
        )

        task_exists = self.cursor.fetchone() is not None

        task_isnt_blocked = True # todo: change this into a prepared statement 

        if task_exists and task_isnt_blocked:
            self.exec_and_commit(
                "UPDATE Taski SET zrobiony = 'TRUE' WHERE id = ?",
                idTaska
            )

        return task_isnt_blocked # todo: change to raise 2 different errors

        

    def odznacz_task(self, nazwaPokoju: str, idTaska: int) -> bool:
        ...

    def lista_taskow(self, nazwaPokoju: str):
        ...


    # --------------- Chaty ---------------

    # * w oryginale chciałeś list[str] ale wydaje mi się że ptotrzebujesz więcej info niż tylko same treści (na przykład data wysłania) więc zwracam cały rezultat query
    def pobierz_chat(self, nazwa_pokoju: str, offset: int = 0, liczba_wiadomosci: int = 100):
        self.execute(
            "SELECT * FROM Wiadomosci WHERE pokoj = ? ORDER BY data_wyslania DESC LIMIT ?, ?",
            nazwa_pokoju,
            offset,
            liczba_wiadomosci
        )

        return self.cursor.fetchall()
        
    # * wszystkie daty będą przechowywane w obiekcie date z modułu datetime
    # * stworzenie daty ze stringa: date.fromisoformat("YYYY-MM-DD")
    # * wszystkie time będą w obiekcie datetime
    def aktualizacja_chatu(self, nazwaPokoju: str, autorOstatnioPosiadanej: str, dataOstatnioPosiadanej: date):
        ...

    def dodaj_wiadomosc(self, login: str, azwaPokoju: str, wiadomosc: str, data: int):
        ...



    # --------------- Kalendarze ---------------
    def wpis_istnieje(self, nazwaPokoju: str, wpis):
        ...

    def kalendarz_dodaj_wpis(self, nazwaPokoju: str, wpis):
        ...
    
    def kalendarz_usun_wpis(self, nazwaPokoju: str, wpis):
        ...

    def kalendarz_modyfikuj_wpis(self, nazwaPokoju: str, wpis, noweDane):
        ...

    def pobierz_kalendarz(self, nazwaPokoju: str):
        ...


    # --------------- Pliki ---------------
    def plik_istnieje(self, nazwaPokoju: str, nazwaPliku: str) -> bool:
        ...

    def dodaj_plik(self, login: str, nazwaPokoju: str, nazwaPliku: str, zawartoscPliku: bytes):
        ...

    def usun_plik(self, nazwaPokoju: str, nazwaPliku: str):
        ...

    def pobierz_plik(self, nazwaPokoju: str, nazwaPliku: str):
        ...
    
    def lista_plikow(self, nazwaPokoju: str):
        ...

    def autor_pliku(self, nazwaPokoju: str, nazwaPliku: str, dana: str):
        ...



    # --------------- Klucze ---------------
    def klucz_istnieje(self, kluczPub: str):
        ...

    def ustaw_klucz(self, login: str, kluczPub: str):
        ...

    def dodaj_klucz_do_pokoju(self, nazwaPokoju: str, kluczPubPokoju: str, kluczPrivPokoju: str, loginPosiadaczaKlucza: str):
        ...

    # todo: nie potrzebna jest taka funkcja, wystarczy skorzystać z powyższej i ona zwróci czy istnieje?
    def czy_klucz_pokoju_istnieje(self, kluczPubPokoju: str, kluczPrivPokoju: str, loginWlasciciela: str):
        ...

    def czy_zweryfikowany(login: str) -> bool:
        ...

    def usun_klucze_dla_uzytkownika(self, nazwaPokoju: str, loginPosiadaczaKlucza: str):
        ...

    def klucz_uzytkownika(self, nickPosiadaczaKlucza: str) -> str:
        ...

    

if __name__ == "__main__":
    db = SQLLiteDB("teaman_database.db")