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
        self.assertFalse(db.istnieje_kod_zpr("nie_istniejący_kod"))

        EXAMPLE_CODE = "example_code"
        db.dodaj_kod_zaproszniowy(EXAMPLE_CODE)
        db.execute(
            "SELECT * FROM KodyZaproszeniowe WHERE kod = ?",
            EXAMPLE_CODE
        )

        self.assertEqual(
            db.cursor.fetchone(),
            (EXAMPLE_CODE, date.today())
        )

        self.assertTrue(db.istnieje_kod_zpr(EXAMPLE_CODE))

    def 
        


if __name__ == "__main__":
    unittest.main()
