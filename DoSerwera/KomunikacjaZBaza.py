import typing
import Obiekty as o
# import sys
# sys.path.insert(1, '../Database')
# import SQLLite as Baza
import Database.SQLLite as Baza # todo: Ryszard sprawdź czy ci teraz działa

# todo: zaimplementować w bazie danych

def czyLoginIstnieje(baza: Baza.SQLLiteDB, login: str) -> bool:
    #login zahashowany oraz przetestowany pod względem bezpieczeństwa

    wynik: bool = baza.czy_login_istnieje(login)
    return wynik


def probaLogowania(baza: Baza.SQLLiteDB, login: str, haslo: str) -> bool:
    #login i hasło zahashowane oraz przetestowane pod względem bezpieczeństwa
    
    wynik: bool = baza.log_in(login,haslo)
    return wynik


def autoryzacjaTokenem(baza: Baza.SQLLiteDB, login: str, token: str) -> bool:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa

    wynik: bool = baza.authenticate(login,token)
    return wynik


def czyNickIstnieje(baza: Baza.SQLLiteDB, nickPubliczny: str) -> bool:
    #nick przetstowany pod względem bezpieczeństwa

    wynik: bool = baza.czy_nick_istnieje(nickPubliczny)
    return wynik


# todo: zaimplementować w bazie danych
def rolaUzytkownika(baza: Baza.SQLLiteDB, login: str, token: str) -> str:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa
    
    rola: str = baza.rola_uzytkownika(login,token)
    return rola


def czyJestKod(baza: Baza.SQLLiteDB, kodZapr: str) -> bool:
    #kod zahashowany i przetestowany pod względem bezpieczeństwa
    
    wynik: bool = baza.istnieje_kod_zpr(kodZapr)
    return wynik

def dataAktywnosci(baza: Baza.SQLLiteDB, login: str, token: str) -> None:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa
    
    baza.ustaw_date_aktywnosci_teraz(login,token)
    return None

def ustawToken(baza: Baza.SQLLiteDB, login: str, haslo: str, token: str) -> None:
    #login, haslo i token zahashowane oraz przetestowane pod względem bezpieczeństwa
    
    baza.ustaw_token(login,haslo,token)
    dataAktywnosci(baza,login,token)
    return None

def usunKod(baza: Baza.SQLLiteDB, kodZapr: str) -> None:
    #kod zahashowany i przetestowany pod względem bezpieczeństwa
    
    baza.usun_kod_zaproszeniowy(kodZapr)
    return None

def wstawKod(baza: Baza.SQLLiteDB, login: str, token: str, kodZapr: str) -> None:
    #login, token i kod zahashowane i przetestowane pod względem bezpieczeństwa
    
    baza.dodaj_kod_zaproszniowy(kodZapr)
    dataAktywnosci(baza,login,token)
    return None

def wstawUzytkownika(baza: Baza.SQLLiteDB, login: str, haslo: str, token: str, rola: str, nickPubliczny: str) -> None:
    #login, haslo i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nick przetestowany pod względem bezpieczeństwa
    
    baza.wstaw_uzytkownika(login,haslo,token,rola,nickPubliczny)
    dataAktywnosci(baza,login,token)
    return None

def usunBaze(baza: Baza.SQLLiteDB, nazwaProj: str) -> None:
    #nazwa projektu przetestowana pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do usuwania bazy danych projektu "DROP DATABASE "+nazwaPRoj+";"
    return None

def czyBazaIstnieje(nazwaProj: str) -> bool:
    #nazwa projektu przetestowana pod względem bezpieczeństwa
    
    wynik: bool = Baza.SQLLiteDB.baza_istnieje("./Bazy/"+nazwaProj+".db")
    return wynik

def czyszczeniePolnocowe(baza: Baza.SQLLiteDB) -> None:
    baza.czyszczenie_polnocne
    return None

def czyJestPokoj(baza: Baza.SQLLiteDB, nazwaPokoju: str) -> bool:
    #nazwa pokoju przetestowana pod względem bezpieczeństwa
    
    wynik: bool = baza.istnieje_pokoj(nazwaPokoju)
    return wynik

def stworzPokoj(baza: Baza.SQLLiteDB, login: str, token: str, nazwaPokoju: str) -> None:
    #login, token zahashowane i przetestowane pod względem bezpieczeństwa; nazwa pokoju przetestowana pod względem bezpieczeństwa
    
    baza.stworz_pokoj(nazwaPokoju)
    dataAktywnosci(baza,login,token)
    return None

def usunPokoj(baza: Baza.SQLLiteDB, login: str, token: str, nazwaPokoju: str) -> None:
    #login, token zahashowane i przetestowane pod względem bezpieczeństwa; nazwa pokoju przetestowana pod względem bezpieczeństwa
    
    baza.usun_pokoj(nazwaPokoju)
    dataAktywnosci(baza,login,token)
    return None

def dodajDoPokoju(baza: Baza.SQLLiteDB, loginAdmina: str, tokenAdmina: str, nazwaPokoju: str, dodawanyLogin: str) -> None:
    #loginy i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju przetestowana pod względem bezpieczeństwa
    
    baza.dodaj_do_pokoju(nazwaPokoju,dodawanyLogin)
    dataAktywnosci(loginAdmina,tokenAdmina)
    return None

def usunZPokoju(baza: Baza.SQLLiteDB, loginAdmina: str, tokenAdmina: str, nazwaPokoju: str, usuwanyLogin: str) -> None:
    #loginy i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju przetestowana pod względem bezpieczeństwa
    
    baza.usun_z_pokoju(nazwaPokoju,usuwanyLogin)
    dataAktywnosci(loginAdmina,tokenAdmina)
    return None

def czyUzytkownikJestWPokoju(baza: Baza.SQLLiteDB, nazwaPokoju: str, login: str) -> bool:
    #login zahashowany oraz przetestowany pod względem bezpieczeństwa; nazwa pokoju przetestowana pod względem bezpieczeństwa
    
    wynik: bool = baza.czy_uzytkownik_w_pokoju(nazwaPokoju,login)
    return wynik

# todo: zaimplementować w bazie danych
def pokojeCzlonkowskie(baza: Baza.SQLLiteDB, login: str, token: str) -> typing.List[str]:
    #login zahashowany oraz przetestowany pod względem bezpieczeństwa
    
    wynik: typing.List[str] = baza.pokoje_czlonkowskie(login)
    dataAktywnosci(login, token)
    return wynik

# todo: zaimplementować w bazie danych
def dodajTaski(baza: Baza.SQLLiteDB, login: str, token: str, nazwaPokoju: str, listaTaskow: typing.List[o.Task]) -> None:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju i nazwy tasków przetestowane pod względem bezpieczeństwa
    
    baza.dodaj_taski(nazwaPokoju,listaTaskow)
    dataAktywnosci(baza,login,token)
    return None

# todo: zaimplementować w bazie danych
def usunTaski(baza: Baza.SQLLiteDB, login: str, token: str, nazwaPokoju: str, listaTaskow: typing.List[o.Task]) -> None:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju i nazwy tasków przetestowane pod względem bezpieczeństwa
    
    baza.usun_taski(nazwaPokoju,listaTaskow)
    dataAktywnosci(baza,login,token)
    return None

# todo: zaimplementować w bazie danych
def zauktualizujWlasnosciTaskow(baza: Baza.SQLLiteDB, login: str, token: str, nazwaPokoju: str, listaTaskow: typing.List[o.Task]) -> None:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju i nazwy tasków przetestowane pod względem bezpieczeństwa
    
    baza.zaktualizuj_wlasnosci_taskow(nazwaPokoju,listaTaskow)
    dataAktywnosci(baza,login,token)
    return None

# todo: zaimplementować w bazie danych
def ukonczTask(baza: Baza.SQLLiteDB, login: str, token: str, nazwaPokoju: str, idTaska: int) -> bool:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju przetestowana pod względem bezpieczeństwa
    
    czyMozna: bool = baza.ukoncz_task(nazwaPokoju,idTaska)
    dataAktywnosci(baza,login,token)
    return czyMozna

# todo: zaimplementować w bazie danych
def odznaczTaskJakoNieukonczony(baza: Baza.SQLLiteDB, login: str, token: str, nazwaPokoju: str, idTaska: int) -> bool:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju przetestowana pod względem bezpieczeństwa
    
    czyMozna: bool = baza.odznacz_task(nazwaPokoju,idTaska)
    dataAktywnosci(baza,login,token)
    return czyMozna

# todo: zaimplementować w bazie danych
def listaTaskow(baza: Baza.SQLLiteDB, login: str, token: str, nazwaPokoju: str) -> typing.List[str]:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju przetestowana pod względem bezpieczeństwa
    
    lista: typing.List[str] = baza.lista_taskow(nazwaPokoju)
    dataAktywnosci(baza,login,token)
    return lista

# todo: zaimplementować w bazie danych
def pobierzChat(baza: Baza.SQLLiteDB, login: str, token: str, nazwaPokoju: str) -> typing.List[str]:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju przetestowana pod względem bezpieczeństwa
    
    lista: typing.List[str] = baza.pobierz_chat(nazwaPokoju)
    dataAktywnosci(baza,login,token)
    return lista

# todo: zaimplementować w bazie danych
def aktualizacjaChatu(baza: Baza.SQLLiteDB, login: str, token: str, nazwaPokoju: str, autorOstatnioPosiadanej: str, dataOstatnioPosiadanej: int) -> typing.List[str]:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju i autor ostatniej wiadomości przetestowane pod względem bezpieczeństwa
    
    lista: typing.List[str] = baza.aktualizacja_chatu(nazwaPokoju,autorOstatnioPosiadanej,dataOstatnioPosiadanej)
    dataAktywnosci(baza,login,token)
    return lista

# todo: zaimplementować w bazie danych
def dodajWiadomosc(baza: Baza.SQLLiteDB, login: str, token: str, nazwaPokoju: str, wiadomosc: str, data: int) -> None:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju przetestowana pod względem bezpieczeństwa; treść wiadomości z zabezpieczonymi cudzysłowami
    
    baza.dodaj_wiadomosc(login,nazwaPokoju,wiadomosc,data)
    dataAktywnosci(baza,login,token)
    return None

# todo: zaimplementować w bazie danych
def czyWpisIstnieje(baza: Baza.SQLLiteDB, nazwaPokoju: str, wpis: o.WpisKalendarza) -> bool:
    #nazwa pokoju przetestowana pod względem bezpieczeństwa; treść wpisu z zabezpieczonymi cudzysłowami
    
    wynik: bool = baza.wpis_istnieje(nazwaPokoju,wpis)
    return wynik

# todo: zaimplementować w bazie danych
def dodajWpisDoKalendarza(baza: Baza.SQLLiteDB, login: str, token: str, nazwaPokoju: str, wpis: o.WpisKalendarza) -> None:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju przetestowana pod względem bezpieczeństwa; treść wpisu z zabezpieczonymi cudzysłowami
    
    baza.kalendarz_dodaj_wpis(nazwaPokoju,wpis)
    dataAktywnosci(baza,login,token)
    return None

# todo: zaimplementować w bazie danych
def usunWpisZKalendarza(baza: Baza.SQLLiteDB, login: str, token: str, nazwaPokoju: str, wpis: o.WpisKalendarza) -> None:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju przetestowana pod względem bezpieczeństwa; treść wpisu z zabezpieczonymi cudzysłowami
    
    baza.kalendarz_usun_wpis(nazwaPokoju,wpis)
    dataAktywnosci(baza,login,token)
    return None

# todo: zaimplementować w bazie danych
def modyfikujWpisKalendarza(baza: Baza.SQLLiteDB, login: str, token: str, nazwaPokoju: str, wpis: o.WpisKalendarza, noweDane: o.WpisKalendarza) -> None:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju przetestowana pod względem bezpieczeństwa; treści wpisów z zabezpieczonymi cudzysłowami
    
    baza.kalendarz_modyfikuj_wpis(nazwaPokoju,wpis,noweDane)
    dataAktywnosci(baza,login,token)
    return None

# todo: zaimplementować w bazie danych
def pobierzKalendarz(baza: Baza.SQLLiteDB, login: str, token: str, nazwaPokoju: str) -> typing.List[str]:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju przetestowana pod względem bezpieczeństwa
    
    lista: typing.List[str] = baza.pobierz_kalendarz(nazwaPokoju)
    dataAktywnosci(baza,login,token)
    return lista

# todo: zaimplementować w bazie danych
def czyPlikIstnieje(baza: Baza.SQLLiteDB, nazwaPokoju: str, nazwaPliku: str) -> bool:
    #nazwy pokoju i pliku przetestowane pod względem bezpieczeństwa
    
    wynik: bool = baza.plik_istnieje(nazwaPokoju,nazwaPliku)
    return wynik

# todo: zaimplementować w bazie danych
def dodajPlik(baza: Baza.SQLLiteDB, login: str, token: str, nazwaPokoju: str, nazwaPliku: str, zawartoscPliku: bytes) -> None:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwy pokoju i pliku przetestowane pod względem bezpieczeństwa
    
    baza.dodaj_plik(login,nazwaPokoju,nazwaPliku,zawartoscPliku)
    dataAktywnosci(baza,login,token)
    return None

# todo: zaimplementować w bazie danych
def usunPlik(baza: Baza.SQLLiteDB, login: str, token: str, nazwaPokoju: str, nazwaPliku: str) -> None:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwy pokoju i pliku przetestowane pod względem bezpieczeństwa
    
    baza.usun_plik(nazwaPokoju,nazwaPliku)
    dataAktywnosci(baza,login,token)
    return None

# todo: zaimplementować w bazie danych
def pobierzPlik(baza: Baza.SQLLiteDB, login: str, token: str, nazwaPokoju: str, nazwaPliku: str):
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwy pokoju i pliku przetestowane pod względem bezpieczeństwa
    
    wynik = baza.pobierz_plik(nazwaPokoju,nazwaPliku)
    dataAktywnosci(baza,login,token)
    return wynik

# todo: zaimplementować w bazie danych
def listaPlikow(baza: Baza.SQLLiteDB, login: str, token: str, nazwaPokoju: str) -> typing.List[str]:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju przetestowana pod względem bezpieczeństwa
    
    wynik: typing.List[str] = baza.lista_plikow(nazwaPokoju)
    dataAktywnosci(baza,login,token)
    return wynik

# todo: zaimplementować w bazie danych
def autorPliku(baza: Baza.SQLLiteDB, nazwaPokoju: str, nazwaPliku: str, dana: str = "nick") -> str:
    #nazwy pokoju i pliku przetestowane pod względem bezpieczeństwa
    
    wynik: str = baza.autor_pliku(nazwaPokoju,nazwaPliku,dana)    
    return wynik

# todo: zaimplementować w bazie danych
def czyKluczIstnieje(baza: Baza.SQLLiteDB, kluczPub: str) -> bool:
    #klucz przetestowany pod względem bezpieczeństwa
    
    wynik: bool = baza.klucz_istnieje(kluczPub)
    return wynik

# todo: zaimplementować w bazie danych
def ustawKlucz(baza: Baza.SQLLiteDB, login: str, token: str, kluczPub: str) -> None:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; klucz przetestowany pod względem bezpieczeństwa
    
    baza.ustaw_klucz(login,kluczPub)
    dataAktywnosci(login,token)
    return None

# todo: zaimplementować w bazie danych
def dodajKluczPokoju(baza: Baza.SQLLiteDB, loginAdmina: str, tokenAdmina: str, nazwaPokoju: str, kluczPubPokoju: str, kluczPrivPokoju: str, loginPosiadaczaKlucza: str):
    #loginy i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju i klucze przetestowane pod względem bezpieczeństwa
    
    baza.dodaj_klucz_do_pokoju(nazwaPokoju,kluczPubPokoju,kluczPrivPokoju,loginPosiadaczaKlucza)
    dataAktywnosci(loginAdmina,tokenAdmina)
    return None

# todo: zaimplementować w bazie danych
def czyKluczPokojuJuzIstnieje(baza: Baza.SQLLiteDB, kluczPubPokoju: str, kluczPrivPokoju: str, loginWlasciciela: str) -> bool:
    #login zahashowany oraz przetestowany pod względem bezpieczeństwa; klucze przetestowane pod względem bezpieczeństwa
    
    wynik: bool = baza.czy_klucz_pokoju_istnieje(kluczPubPokoju,kluczPrivPokoju,loginWlasciciela)
    return wynik

# todo: zaimplementować w bazie danych
def czyZweryfikowany(baza: Baza.SQLLiteDB, login: str) -> bool:
    #login zahashowany oraz przetestowany pod względem bezpieczeństwa
    
    wynik: bool = baza.czy_zweryfikowany(login)
    return wynik

# todo: zaimplementować w bazie danych
def usunKluczeDlaUzytkownika(baza: Baza.SQLLiteDB, loginAdmina: str, tokenAdmina: str, nazwaPokoju: str, loginPosiadaczaKlucza: str):
    #loginy i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju przetestowana pod względem bezpieczeństwa
    
    baza.usun_klucze_dla_uzytkownika(nazwaPokoju,loginPosiadaczaKlucza)
    dataAktywnosci(loginAdmina,tokenAdmina)
    return None

# todo: zaimplementować w bazie danych
def kluczUzytkownika(baza: Baza.SQLLiteDB, loginAdmina: str, tokenAdmina: str, loginPosiadaczaKlucza: str) -> str:
    #loginy i token zahashowane oraz przetestowane pod względem bezpieczeństwa
    
    wynik: str = baza.klucz_uzytkownika(loginPosiadaczaKlucza)
    dataAktywnosci(loginAdmina,tokenAdmina)
    return wynik

# todo: zaimplementować w bazie danych
def loginUzytkownika(baza: Baza.SQLLiteDB, nick: str) -> str:
    #nick przetestowany pod względem bezpieczeństwa
    
    wynik: str = baza.nick_to_login(nick)
    return wynik

# todo: zaimplementować w bazie danych
def ustawRole(baza: Baza.SQLLiteDB, loginAdmina: str, tokenAdmina: str, loginZmienianego: str, nowaRola: str) -> None:
    #loginy i token zahashowane oraz przetestowane pod względem bezpieczeństwa; rola przetestowana pod względem bezpieczeństwa
    
    baza.ustaw_role(loginZmienianego,nowaRola)
    dataAktywnosci(loginAdmina,tokenAdmina)
    return None

# todo: zaimplementować w bazie danych
def listaNiezweryfikowanych(baza: Baza.SQLLiteDB, login: str, token: str) -> typing.List[str]:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa
    
    lista: typing.List[str] = baza.lista_niezweryfikowanych()
    dataAktywnosci(baza,login,token)
    return lista
