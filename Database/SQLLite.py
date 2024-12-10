import sqlite3
from sqlite3 import Cursor
from typing import List, Any
from datetime import date
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
    def user_nick_to_login():
        ...

    def user_login_to_id():
        ...
    
    def user_nick_to_id():
        ...



    # --------------- kody zaproszeniowe ---------------
    # todo: test 
    def istnieje_kod_zpr(self, kod_zapr: KodZaproszeniowy) -> bool:
        self.execute(
            "SELECT * FROM KodyZaproszeniowe WHERE kod = ?",
            kod_zapr.value
        )
        return self.cursor.fetchone() is not None

    # todo: test
    def dodaj_kod_zaproszniowy(self, kod_zapr: KodZaproszeniowy):
        self.exec_and_commit(
            "INSERT INTO KodyZaproszeniowe VALUES (?, CURRENT_DATE)",
            kod_zapr.value
        )

    # todo: test
    def usun_kod_zaproszeniowy(self, kod_zapr: KodZaproszeniowy):
        self.exec_and_commit(
            "DELETE FROM KodyZaproszeniowe WHERE kod = ?",
            kod_zapr.value
        )



    # --------------- Użytkownicy ---------------
    # ? todo: czy to nie admin powinien dodawać użytkowników?
    def wstaw_uzytkownika(self, login: Login, haslo: Haslo, token: Token, rola: Rola, nick: Nick):
        self.exec_and_commit(
            "INSERT INTO Uzytownicy(nazwa, login, haslo, token, rola) VALUES (?, ?, ?, ?, ?)",
            login.value,
            haslo.value,
            token.value,
            rola.value,
            nick.value
        )

        self.ustaw_date_aktywnosci_teraz(login, token)
    
    def ustaw_date_aktywnosci_teraz(self, login: Login, token: Token):
        self.exec_and_commit(
            "UPDATE Uzytownicy SET last_update = CURRENT_DATE WHERE login = ? AND token = ?",
            login.value,
            token.value
        )

    def ustaw_token(self, login: str, haslo: str, token: str) -> None:
        self.exec_and_commit(
            "UPDATE Uzytownicy SET Token = ? WHERE login = ? AND haslo = ?",
            token.value,
            login.value,
            haslo.value
        )

    
        

    # todo: zaimplementować
    def czyszczenie_polnocne(self):
        self.exec_and_commit(
            "DELETE FROM KodyZaproszeniowe WHERE (julianday(CURRENT_DATE) - julianday(data_dodania)) > 1"
        )

    def loginUzytkownika(nick: str) -> str:
        ...

    def ustaw_role(self, loginAdmina: str, tokenAdmina: str, loginZmienianego: str, nowaRola: str):
        ...

    def lista_niezweryfikowanych(login: str, token: str):
        ...
    


    # --------------- Pokoje ---------------
    def istnieje_pokoj(self, nazwa_pokoju: str) -> bool:
        self.cursor.execute(
            "SELECT * FROM Pokoj WHERE nazwa = ?",
            (nazwa_pokoju,)
        )
        
        return self.cursor.fetchone() is not None

    
    def stworz_pokoj(self, login: str, token: str, nazwa_pokoju: str):
        # ! todo: autentykacja admina
        self.cursor.execute(
            "INSERT INTO Pokoje (nazwa) VALUES (?)",
            (nazwa_pokoju,)
        )

        # todo: update daty admina

    def usun_pokoj(self, login: str, token: str, nazwa_pokoju: str):
        # ! todo: autentykacja admina
        self.cursor.execute(
            "DELETE FROM Pokoje WHERE nazwa = ?",
            (nazwa_pokoju,)
        )

        # todo: update daty admina

    def dodaj_do_pokoju(self, loginAdmina: str, tokenAdmina: str, nazwa_pokoju: str, dodawany_login: str) -> None:
        id_uzytkownika = None # wykonać kwerendę
        id_pokoju = None # wykonać kwerendę
        
        self.cursor.execute(
            "INSERT INTO CzlonkowiePokojow(uzytkownik, pokoj) VALUES (?, ?)",
            (id_uzytkownika, id_pokoju,)
        )

        # todo: update daty admina

        self.commit()

    def usun_z_pokoju(self, loginAdmina: str, tokenAdmina: str, nazwa_pokoju: str, usuwanyLogin: str) -> None:
        id_uzytkownika = None # wykonać kwerendę
        id_pokoju = None # wykonać kwerendę
        
        self.cursor.execute(
            "DELETE FROM CzlonkowiePokojow WHERE uzytkownik = ? AND pokoj = ?",
            (id_uzytkownika, id_pokoju,)
        )

        # todo: update daty admina

        self.commit()

    def czy_uzytkownik_w_pokoju(self, nazwaPokoju: str, login: str) -> bool:
        id_uzytkownika = None # wykonać kwerendę
        id_pokoju = None # wykonać kwerendę

        self.cursor.execute(
            "SELECT * FROM CzlonkowiePokoju WHERE uzytkownik = ? AND pokoj = ?",
            (id_uzytkownika, id_pokoju,)
        )

        return self.cursor.fetchone() is not None

    def pokoje_czlonkowskie(self, login: str, token: str) -> List[str]:
        ...



    # --------------- Taski ---------------
    def dodaj_taski(login: str, token: str, nazwaPokoju: str, listaTaskow) -> None:
        ...

    def usun_taski(self, login: str, token: str, nazwaPokoju: str, listaTaskow):
        ...

    def zaktualizuj_wlasnosci_taskow(self, login: str, token: str, nazwaPokoju: str, listaTaskow):
        ...

    def ukoncz_task(self, login: str, token: str, nazwaPokoju: str, idTaska: int) -> bool:
        ...

    def odznacz_task(self, login: str, token: str, nazwaPokoju: str, idTaska: int) -> bool:
        ...

    def lista_taskow(self, login: str, token: str, nazwaPokoju: str):
        ...


    # --------------- Chaty ---------------
    def pobierz_chat(self, login: str, token: str, nazwaPokoju: str):
        ...

    def aktualizacja_chatu(self, login: str, token: str, nazwaPokoju: str, autorOstatnioPosiadanej: str, dataOstatnioPosiadanej: int):
        ...

    def dodaj_wiadomosc(self, login: str, token: str, nazwaPokoju: str, wiadomosc: str, data: int):
        ...



    # --------------- Kalendarze ---------------
    def wpis_istnieje(self, nazwaPokoju: str, wpis):
        ...

    def kalendarz_dodaj_wpis(self, login: str, token: str, nazwaPokoju: str, wpis):
        ...
    
    def kalendarz_usun_wpis(self, login: str, token: str, nazwaPokoju: str, wpis):
        ...

    def kalendarz_modyfikuj_wpis(self, login: str, token: str, nazwaPokoju: str, wpis, noweDane):
        ...

    def pobierz_kalendarz(self, login: str, token: str, nazwaPokoju: str):
        ...


    # --------------- Pliki ---------------
    def plik_istnieje(self, nazwaPokoju: str, nazwaPliku: str) -> bool:
        ...

    def dodaj_plik(self, login: str, token: str, nazwaPokoju: str, nazwaPliku: str, zawartoscPliku: bytes):
        ...

    def usun_plik(self, login: str, token: str, nazwaPokoju: str, nazwaPliku: str):
        ...

    def pobierz_plik(self, login: str, token: str, nazwaPokoju: str, nazwaPliku: str):
        ...

    def autor_pliku(self, nazwaPokoju: str, nazwaPliku: str, dana: str):
        ...



    # --------------- Klucze ---------------
    def klucz_istnieje(self, kluczPub: str):
        ...

    def ustaw_klucz(self, login: str, token: str, kluczPub: str):
        ...

    def dodaj_klucz_do_pokoju(self, loginAdmina: str, tokenAdmina: str, nazwaPokoju: str, kluczPubPokoju: str, kluczPrivPokoju: str, loginPosiadaczaKlucza: str):
        ...

    # todo: nie potrzebna jest taka funkcja, wystarczy skorzystać z powyższej i ona zwróci czy istnieje?
    def czy_klucz_pokoju_istnieje(self, kluczePubPokoju: str, kluczPrivPokoju: str, loginWlasciciela: str):
        ...

    def czy_zweryfikowany(login: str) -> bool:
        ...

    def usun_klucze_dla_uzytkownika(self, loginAdmina: str, tokenAdmina: str, nazwaPokoju: str, loginPosiadaczaKlucza: str):
        ...

    def klucz_uzytkownika(self, loginAdmina: str, tokenAdmina: str, nickPosiadaczaKlucza: str) -> str:
        ...

    

if __name__ == "__main__":
    db = SQLLiteDB("teaman_database.db")