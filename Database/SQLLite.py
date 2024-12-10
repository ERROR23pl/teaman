import sqlite3
from sqlite3 import Cursor
from typing import List, Any
from datetime import date
import os

from Database import Database

# ! todo: change this in the final project!!!
DB_CREATION_QUERY_PATH = "db_creation_query.sql"

# todo: Czy metody to modyfikowania bazy powinny automatycznie commitować zmiany?
# todo: error/none handling
# ! todo: w wielu metodach zapomniałem zrobić self.commit() ups, trzeba będzie to naprawić


class SQLLiteDB():
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
    
    def rollback(self) -> None:
        self.connection.rollback()

    def close(self) -> None:
        self.connection.close()

    def __del__(self) -> None:
        self.connection.close()



    # Prepared statements dla Ryszarda
    def istnieje_kod_zpr(self, kod_zapr: str) -> bool:
        self.cursor.execute("SELECT * FROM KodyZaproszeniowe WHERE kod = ?", (kod_zapr,))
        return self.cursor.fetchone() is not None

    # todo: Kod zaproszeniowy nie jest w żaden sposób validowany
    def dodaj_kod_zaproszniowy(self, kod_zapr: str):
        self.cursor.execute("INSERT INTO KodyZaproszeniowe VALUES (?, CURRENT_DATE)", (kod_zapr,))
        self.connection.commit()

    def usun_kod_zaproszeniowy(self, kod_zapr: str):
        self.cursor.execute("DELETE FROM KodyZaproszeniowe WHERE kod = ?", (kod_zapr,))
        self.connection.commit()

    def ustaw_date_aktywnosci_teraz(self, login: str, token: str):
        self.cursor.execute(
            "UPDATE Uzytownicy SET last_update = CURRENT_DATE WHERE login = ? AND token = ?",
            (login, token)
        )

    # ? Czy to nie serwer powinien tworzyć i zwrócić użytkownikowi token?
    def ustaw_token(self, login: str, haslo: str, token: str) -> None:
        self.cursor.execute(
            "UPDATE Uzytownicy SET Token = ? WHERE login = ? AND haslo = ?",
            (token, login, haslo)
        )

    def wstaw_uzytkownika(self, login: str, haslo: str, token: str, rola: str, nick_publiczny: str):
        self.cursor.execute(
            "INSERT INTO Uzytownicy(login, haslo, nazwa_publiczna, token, rola) VALUES (?, ?, ?, ?, ?)",
            (login, haslo, token, rola, nick_publiczny)
        )

        self.ustaw_date_aktywnosci_teraz(login, token)
        

    # todo: zaimplementować
    def czyszczenie_polnocne(self):
        ...
    
    def jest_pokoj(self, nazwa_pokoju: str) -> bool:
        self.cursor.execute(
            "SELECT * FROM Pokoj WHERE nazwa = ?",
            (nazwa_pokoju,)
        )
        
        return self.cursor.fetchone() is not None

    # todo: upewnić się, że metody zwracają informację czy kwerenda była poprawna. W końcu jaką mam pewność, że Ryszard poprawnie sprawdzi czy Pokój istnieje?
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


if __name__ == "__main__":
    db = SQLLiteDB("teaman_database.db")
    # print(type(date.today()))
    db.dodaj_kod_zaproszniowy("DUPA")