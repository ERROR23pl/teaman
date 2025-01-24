import unittest
from datetime import date

from Database.SQLLite import *


def wstaw_uzytkownikow(db: SQLLiteDB):
    for i in range(1, 11):
        db.wstaw_uzytkownika(f"user{i}_login", f"haslo{i}", f"", "user", f"user{i}_nick")


class TestSqliteFunctions(unittest.TestCase):
    def test_tworzenie_bazy_danych(self):
        db = SQLLiteDB("./Database/test_databases/test_tworzenie_bazy_danych.db")
        db.reset_database()

    def test_uzytkownicy(self):
        db = SQLLiteDB("./Database/test_databases/test_uzytkownicy.db")
        db.reset_database()

        wstaw_uzytkownikow(db)

        for i in range(1, 11):
            db.ustaw_date_aktywnosci_teraz(f"user{i}_login")

        for i in range(1, 11):
            db.ustaw_token(f"user{i}_login", f"user{i}_token")

        for i in range(1, 11, 2):
            db.exec_and_commit("UPDATE Uzytkownicy SET last_update = '2025-01-01' WHERE login = ?", f"user{i}_login")

        db.czyszczenie_polnocne()

        db.ustaw_role("user5_login", "Niezweryfikowany")
        
        # print(db.lista_niezweryfikowanych())


    def test_kody_zaproszeniowe(self):
        db = SQLLiteDB("./Database/test_databases/test_kody_zaproszeniowe.db")
        db.reset_database()

        for i in range(1, 11):
            db.dodaj_kod_zaproszniowy(f"kodzapr{i}")

        # sprawdzenie istnienia i nie istnienia kodu
        for i in range(1, 11):
            assert(db.istnieje_kod_zpr(f"kodzapr{i}"))
        assert(not db.istnieje_kod_zpr(f"nie_istniejacy_kod"))

        # test usuwania kodu
        db.usun_kod_zaproszeniowy('kodzapr3')
        assert(not db.istnieje_kod_zpr(f"kodzapr3"))

        # Test czyszczenia północnego
        db.exec_and_commit("INSERT INTO KodyZaproszeniowe VALUES ('stary_kod', '2025-01-01')")
        assert(db.istnieje_kod_zpr(f"stary_kod"))
        db.czyszczenie_polnocne()
        assert(not db.istnieje_kod_zpr(f"stary_kod"))
        assert(db.istnieje_kod_zpr(f"kodzapr1"))


    def test_logowanie(self):
        db = SQLLiteDB("./Database/test_databases/test_logowanie.db")
        db.reset_database()

        wstaw_uzytkownikow(db)

        assert(db.czy_login_istnieje("user1_login"))
        assert(not db.czy_login_istnieje("user_login_nieistniejacy"))

        assert(db.czy_nick_istnieje("user1_nick"))
        assert(not db.czy_login_istnieje("user_nick_nieistniejacy"))

        db.ustaw_token("user1_login", "user1_token")
        assert(db.authenticate("user1_login", "user1_token"))
        assert(not db.authenticate("user1_login", "złytoken"))

        assert(db.rola_uzytkownika("admin_login") == "Admin")
        assert(db.rola_uzytkownika("user1_login") == "user")

        assert(db.log_in("user1_login", "haslo1"))
        assert(not db.log_in("user1_login", "zle_haslo"))

        db.ustaw_role("user10_login", "Niezweryfikowany")
        assert(not db.czy_zweryfikowany("user10_login"))
        assert(db.czy_zweryfikowany("user1_login"))

    
    def test_pokoje(self):
        db = SQLLiteDB("./Database/test_databases/test_pokoje.db")
        db.reset_database()
        wstaw_uzytkownikow(db)

        for i in range(1, 4):
            db.stworz_pokoj(f"pokoj{i}")

        for i in range(1, 4):
            assert(db.istnieje_pokoj(f"pokoj{i}"))
        assert(not db.istnieje_pokoj(f"nie_istniejacy_pokoj"))

        db.usun_pokoj("pokoj3")
        assert(not db.istnieje_pokoj(f"pokoj3"))

        # uzytkownicy w pokojach
        for i in range(1, 6):
            db.dodaj_do_pokoju("pokoj1", f"user{i}_login")
            assert(db.czy_uzytkownik_w_pokoju("pokoj1", f"user{i}_login"))
        assert(not db.czy_uzytkownik_w_pokoju("pokoj1", f"user6_login"))

        assert(db.czy_uzytkownik_w_pokoju("pokoj1", f"user5_login"))
        db.usun_z_pokoju("pokoj1", "user5_login")
        assert(not db.czy_uzytkownik_w_pokoju("pokoj1", f"user5_login"))
        
        db.dodaj_do_pokoju("pokoj2", "user1_login")
        assert(db.czy_uzytkownik_w_pokoju("pokoj2", f"user1_login"))

    def test_klucze(self):
        db = SQLLiteDB("./Database/test_databases/test_klucze.db")
        db.reset_database()
        wstaw_uzytkownikow(db)

        db.stworz_pokoj("pokoj1")
        for i in range(1, 11):
            db.dodaj_do_pokoju("pokoj1", f"user{i}_login")
            db.ustaw_klucz(f"user{i}_login", f"klucz_pub_{i}")
            assert(db.klucz_istnieje(f"klucz_pub_{i}"))

        for i in range(1, 11):
            db.dodaj_klucz_do_pokoju("pokoj1", f"klucz_pub_pokoju_user{i}", f"klucz_priv_pokoju_user{i}", f"user{i}_login")
            assert(db.czy_klucz_pokoju_istnieje(f"klucz_pub_pokoju_user{i}", f"klucz_priv_pokoju_user{i}", f"user{i}_login"))
            assert(db.klucz_uzytkownika(f"user{i}_login") == f"klucz_pub_{i}")

        db.usun_klucze_dla_uzytkownika("pokoj1", "user10_login")
        assert(not db.czy_klucz_pokoju_istnieje(f"klucz_pub_pokoju_user{i}", f"klucz_priv_pokoju_user{i}", f"user{i}_login"))
        # todo: jaka to jest funkcja do sprawdzania kluczy?

    def test_kalendarz(self):
        db = SQLLiteDB("./Database/test_databases/test_kalendarz.db")
        db.reset_database()
        db.stworz_pokoj("pokoj1")

        db.kalendarz_dodaj_wpis("pokoj1", WpisKalendarza.from_date_str("wpis1", "2025-02-01"))
        assert(db.wpis_istnieje("pokoj1", WpisKalendarza.from_date_str("wpis1", "2025-02-01")))
        
        db.kalendarz_modyfikuj_wpis(
            "pokoj1",
            WpisKalendarza.from_date_str("wpis1", "2025-02-01"),
            WpisKalendarza.from_date_str("wpis1", "2025-02-02")
        )
        assert(db.wpis_istnieje("pokoj1", WpisKalendarza.from_date_str("wpis1", "2025-02-02")))
        
        assert(db.pobierz_kalendarz("pokoj1")[0].dzien == "02")
        
        db.kalendarz_usun_wpis("pokoj1", WpisKalendarza.from_date_str("wpis1", "2025-02-02"))
        assert(not db.wpis_istnieje("pokoj1", WpisKalendarza.from_date_str("wpis1", "2025-02-02")))


if __name__ == "__main__":
    unittest.main()