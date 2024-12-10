import unittest
from SQLLite import *
from datetime import date

def reset_test_db():
    db = SQLLiteDB("test.db")

    with open("db_delete_query.sql", "r", encoding="utf-8") as query:
        for statement in query.read().split(";"):
            db.execute(statement)

    with open("db_creation_query.sql", "r", encoding="utf-8") as query:
        for statement in query.read().split(";"):
            db.execute(statement)
    
    db.commit()
    return db

class TestSqliteFunctions(unittest.TestCase):
    def test_kody_zaproszeniowe(self):
        db: SQLLiteDB = reset_test_db()

        # sprawdzanie nie istniejącego kodu
        NIE_ISTNIEJACY_KOD = KodZaproszeniowy("nie_istniejacy_kod")
        self.assertFalse(
            db.istnieje_kod_zpr(NIE_ISTNIEJACY_KOD)
        )

        # po dodaniu kodu powinien istnieć w bazie z dzisiejszą datą
        ISTNIEJACY_KOD = KodZaproszeniowy("istniejacy_kod")
        db.dodaj_kod_zaproszniowy(ISTNIEJACY_KOD)
        self.assertTrue(
            db.istnieje_kod_zpr(ISTNIEJACY_KOD)
        )

        # po usunięciu nie powinno go już być w bazie
        db.usun_kod_zaproszeniowy(ISTNIEJACY_KOD)
        self.assertFalse(
            db.istnieje_kod_zpr(ISTNIEJACY_KOD)
        )

    def test_uzytkownicy(self):
        db: SQLLiteDB = reset_test_db()

        


if __name__ == "__main__":
    unittest.main()
