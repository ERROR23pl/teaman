import typing
import Obiekty as o

# todo: zaimplementować w bazie danych

def czyLoginIstnieje(login: str) -> bool:
    #login zahashowany oraz przetestowany pod względem bezpieczeństwa
    #TODO wywołanie prepared statement do sprawdzenia czy taki login już istnieje "SELECT COUNT * FROM Uzytkownicy WHERE Login="+login+";"
    wynik: bool = False #mock; tu będzie odebranie liczby i zmiana w prawda-fałsz
    
    return wynik


def probaLogowania(login: str, haslo: str) -> bool:
    #login i hasło zahashowane oraz przetestowane pod względem bezpieczeństwa
    #TODO wywołanie prepared statement do próby logowania "SELECT COUNT * FROM Uzytkownicy WHERE Login="+login+" AND Haslo="+haslo+";"
    wynik: bool = False #mock; tu będzie odebranie liczby i zmiana w prawda-fałsz
    
    return wynik


def autoryzacjaTokenem(login: str, token: str) -> bool:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa
    #TODO wywołanie prepared statement do próby autoryzacji sesji "SELECT COUNT * FROM Uzytkownicy WHERE Login="+login+" AND Token="+token+";"
    wynik: bool = False #mock; tu będzie odebranie liczby i zmiana w prawda-fałsz
    
    return wynik


def czyNickIstnieje(nickPubliczny: str) -> bool:
    #nick przetstowany pod względem bezpieczeństwa
    #TODO wywołanie prepared statement do sprawdzenia czy taki nick już istnieje "SELECT COUNT * FROM Uzytkownicy WHERE NickPubliczny="+nickPubliczny+";"
    wynik: bool = False #mock; tu będzie odebranie liczby i zmiana w prawda-fałsz
    
    return wynik


# todo: zaimplementować w bazie danych
def rolaUzytkownika(login: str, token: str) -> str:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do odebrania roli użytkownika "SELECT Rola FROM Uzytkownicy WHERE Login="+login+" AND Token="+token+";"
    rola: str = ""  #mock; tu będzie zamina rezultatu w string
    return rola


def czyJestKod(kodZapr: str) -> bool:
    #kod zahashowany i przetestowany pod względem bezpieczeństwa
    
    # TODO Database.istnieje_kod_zpr(...)
    wynik: bool = False #mock; tu będzie odebranie liczby i zmiana w prawda-fałsz
    
    return wynik

def dataAktywnosci(login: str, token: str) -> None:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa
    #TODO Database.ustaw_date_aktywnosci
    return None

def ustawToken(login: str, haslo: str, token: str) -> None:
    #login, haslo i token zahashowane oraz przetestowane pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do wstawienia tokenu dla użytkownika "UPDATE Uzytownicy SET Token="+token+" WHERE Login="+login+" AND Haslo="haslo+";"
    dataAktywnosci(login,token)
    return None

def usunKod(kodZapr: str) -> None:
    #kod zahashowany i przetestowany pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do usunięcia użytego kodu zaproszeniowego "DELETE FROM Kody WHERE Kod="+kodZapr+";"
    return None

def wstawKod(login: str, token: str, kodZapr: str) -> None:
    #login, token i kod zahashowane i przetestowane pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do wstawienia nowego kodu zaproszeniowego "INSERT INTO Kody(Kod, Data) VALUES ("+kodZapr+", CURRENT_DATE());"
    dataAktywnosci(login,token)
    return None

def wstawUzytkownika(login: str, haslo: str, token: str, rola: str, nickPubliczny: str) -> None:
    #login, haslo i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nick przetestowany pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do wstawienia nowego użytkownika "INSERT INTO Uzytownicy(Login, Haslo, Token, Rola, NickPubliczny) VALUES ("+login+", "+haslo+", "+token+","+rola+","+nickPubliczny+");"
    dataAktywnosci(login,token)
    return None

# ! stworzenie bazy jest automatyczne, jeśli chcemy mieć wiele baz, stworzymy obiekt Projekt
def stworzBaze(nazwaProj: str) -> None:
    #nazwa projektu przetestowana pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do stworzenia wszystkich tabel z daną nazwą projektu (bazy)
    return None

# ? raczej nie będzie usuwania bazy bez usuwania całego projektu
def usunBaze(nazwaProj: str) -> None:
    #nazwa projektu przetestowana pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do usuwania bazy danych projektu "DROP DATABASE "+nazwaPRoj+";"
    return None

def czyBazaIstnieje(nazwaProj: str) -> bool:
    #nazwa projektu przetestowana pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do sprawdzenia istnienia bazy
    wynik: bool = False #mock; tu będzie zamiana otrzymaneg wyniku w prawda-fałsz
    return wynik

# * Baza będzie połączona poprzez samo stworzenie obiektu bazy na serwerze
def polaczZBaza(nazwaProj: str) -> None:
    #nazwa projektu przetestowana pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do połączenia z podaną bazą "CONNECT "+nazwaProj+";"
    return None

# * baza usuwa się po dropnięciu obiektu Database z pamięci (np. przez del, albo wyłączenie programu.)
def rozlaczZBaza() -> None:
    #TODO wywołanie prepared statement do rozłączenia z aktualnie połączoną bazą
    return None

def czyszczeniePolnocowe() -> None:
    #TODO wywołanie prepared statement do usunięcia z tabeli Kody starych kodów zaproszeniowych o datach o dwa dni starszych od obecnej
    #TODO wywołanie prepared statement do usunięcia z tabeli Uzytkownicy starych tokenów dla użytkowników o datach ostatniej aktywności o dwa dni starszych od obecnej
    
    return None

def czyJestPokoj(nazwaPokoju: str) -> bool:
    #nazwa pokoju przetestowana pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do sprawdzenia czy taki pokój istnieje "SELECT COUNT * FROM Pokoje WHERE Pokoj="+nazwaPokoju+";"
    wynik: bool = False #mock; tu będzie odebranie liczby i zmiana w prawda-fałsz
    
    return wynik

def stworzPokoj(login: str, token: str, nazwaPokoju: str) -> None:
    #login, token zahashowane i przetestowane pod względem bezpieczeństwa; nazwa pokoju przetestowana pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do wstawienia nowego pokoju "INSERT INTO Pokoje(Pokoj) VALUES ("+nazwaPokoju+");"      ID jest autoinkrementowane
    dataAktywnosci(login,token)
    return None

def usunPokoj(login: str, token: str, nazwaPokoju: str) -> None:
    #login, token zahashowane i przetestowane pod względem bezpieczeństwa; nazwa pokoju przetestowana pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do usuwania pokoju "DELETE FROM Pokoje WHERE Pokoj="+nazwaPokoju+";"      triggery usuwające z innych tabel dane związane z usuniętym pokojem
    dataAktywnosci(login,token)
    return None

def dodajDoPokoju(loginAdmina: str, tokenAdmina: str, nazwaPokoju: str, dodawanyLogin: str) -> None:
    #loginy i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju przetestowana pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do wstawienia nowego użytkownika do projektu "INSERT INTO Nalezenie(IDPokoju,IDUzytkownika) VALUES"...
    dataAktywnosci(loginAdmina,tokenAdmina)
    return None

def usunZPokoju(loginAdmina: str, tokenAdmina: str, nazwaPokoju: str, usuwanyLogin: str) -> None:
    #loginy i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju przetestowana pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do usunięcia użytkownika z projektu "DELETE FROM Nalezenie WHERE IDUzytkownika="...
    dataAktywnosci(loginAdmina,tokenAdmina)
    return None

def czyUzytkownikJestWPokoju(nazwaPokoju: str, login: str) -> bool:
    #login zahashowany oraz przetestowany pod względem bezpieczeństwa; nazwa pokoju przetestowana pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do sprawdzenia obecności użytkownika w pokoju "SELECT COUNT * FROM Nalezenie WHERE IDUzytkownika="..." AND IDPokoju="...
    wynik: bool = False #mock; tu będzie odebranie liczby i zmiana w prawda-fałsz
    
    return wynik

# todo: zaimplementować w bazie danych
def pokojeCzlonkowskie(login: str, token: str) -> typing.List[str]:
    #login zahashowany oraz przetestowany pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do pobrania listy pokojów, do których należy użytkownik WRAZ Z ICH KLUCZAMI KLUCZAMI PUBLICZNYMI I PRYWATNYMI ZASZYFROWANYMI JEGO PUBLICZNYM
    wynik: typing.List[str] = [""] #mock; tu będzie odebranie wyniku i zmiana w listę stringów
    dataAktywnosci(login, token)
    
    return wynik

# todo: zaimplementować w bazie danych
def dodajTaski(login: str, token: str, nazwaPokoju: str, listaTaskow: typing.List[o.Task]) -> None:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju i nazwy tasków przetestowane pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do wstawienia nowych tasków do pokoju (bez informacji o taskach incydentnych); jeśli jakiś istnieje, usuń go i zastąp nowym - TRANSKACYJNIE
    dataAktywnosci(login,token)
    return None

# todo: zaimplementować w bazie danych
def usunTaski(login: str, token: str, nazwaPokoju: str, listaTaskow: typing.List[o.Task]) -> None:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju i nazwy tasków przetestowane pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do usunięcia tasków z pokoju; jeśli jakiś nie istnieje, nic nie rób; po każdym usunięciu, usuń triggerem wszystkie zależności od niego - TRANSKACYJNIE
    dataAktywnosci(login,token)
    return None

# todo: zaimplementować w bazie danych
def zauktualizujWlasnosciTaskow(login: str, token: str, nazwaPokoju: str, listaTaskow: typing.List[o.Task]) -> None:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju i nazwy tasków przetestowane pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do zaktualizowania tasków (nazwy, dat, incydencji, koordynatów) z pokoju; jeśli jakiś nie istnieje (lub incydentny nie istnieje), nic nie rób - TRANSKACYJNIE
    dataAktywnosci(login,token)
    return None

# todo: zaimplementować w bazie danych
def ukonczTask(login: str, token: str, nazwaPokoju: str, idTaska: int) -> bool:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju przetestowana pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do sprawdzenia czy jakiś task nie blokuje zaznaczenia tego taska (wymagany, ale nieukończony)
    czyMozna: bool = False #mock, tu będzie rezultat otrzymany z operacji powyżej
    
    if(czyMozna):
        None #TODO wywołanie prepared statement do zaznaczenia taska o podanym ID jako ukończony
    dataAktywnosci(login,token)
    return czyMozna

# todo: zaimplementować w bazie danych
def odznaczTaskJakoNieukonczony(login: str, token: str, nazwaPokoju: str, idTaska: int) -> bool:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju przetestowana pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do sprawdzenia czy jakiś task nie blokuje odznaczenia tego taska (wymaga go i jest ukończony)
    czyMozna: bool = False #mock, tu będzie rezultat otrzymany z operacji powyżej
    
    if(czyMozna):
        None #TODO wywołanie prepared statement do odznaczenia taska o podanym ID jako nieukończony
    dataAktywnosci(login,token)
    return czyMozna

# todo: zaimplementować w bazie danych
def listaTaskow(login: str, token: str, nazwaPokoju: str) -> typing.List[str]:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju przetestowana pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do pobrania danych tasków z pokoju
    lista: typing.List[str] = [""] #mock, tu będzie przekształcenie rezultatu operacji powyżej
    
    dataAktywnosci(login,token)
    return lista

# todo: zaimplementować w bazie danych
def pobierzChat(login: str, token: str, nazwaPokoju: str) -> typing.List[str]:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju przetestowana pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do pobrania 100 ostatnich wiadomości z chatu pokoju
    lista: typing.List[str] = [""] #mock, tu będzie przekształcenie rezultatu operacji powyżej
    
    dataAktywnosci(login,token)
    return lista

# todo: zaimplementować w bazie danych
def aktualizacjaChatu(login: str, token: str, nazwaPokoju: str, autorOstatnioPosiadanej: str, dataOstatnioPosiadanej: int) -> typing.List[str]:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju i autor ostatniej wiadomości przetestowane pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do pobrania wszystkich wiadomości z chatu pokoju od ostatnio posiadanej
    lista: typing.List[str] = [""] #mock, tu będzie przekształcenie rezultatu operacji powyżej
    
    dataAktywnosci(login,token)
    return lista

# todo: zaimplementować w bazie danych
def dodajWiadomosc(login: str, token: str, nazwaPokoju: str, wiadomosc: str, data: int) -> None:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju przetestowana pod względem bezpieczeństwa; treść wiadomości z zabezpieczonymi cudzysłowami
    
    #TODO wywołanie prepared statement do dodania nowej wiadomości wiadomości do chatu pokoju
    
    dataAktywnosci(login,token)
    return None

# todo: zaimplementować w bazie danych
def czyWpisIstnieje(nazwaPokoju: str, wpis: o.WpisKalendarza) -> bool:
    #nazwa pokoju przetestowana pod względem bezpieczeństwa; treść wpisu z zabezpieczonymi cudzysłowami
    
    #TODO wywołanie prepared statement do sprawdzenia obecności wpisu w kalendarzu pokoju "SELECT COUNT * FROM Kalendarze WHERE IDPokoju="..." AND Tresc="..." AND Data="...
    wynik: bool = False #mock; tu będzie odebranie liczby i zmiana w prawda-fałsz
    
    return wynik

# todo: zaimplementować w bazie danych
def dodajWpisDoKalendarza(login: str, token: str, nazwaPokoju: str, wpis: o.WpisKalendarza) -> None:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju przetestowana pod względem bezpieczeństwa; treść wpisu z zabezpieczonymi cudzysłowami
    
    #TODO wywołanie prepared statement do wstawienia nowego wpisu do kalendarza pokoju
    dataAktywnosci(login,token)
    return None

# todo: zaimplementować w bazie danych
def usunWpisZKalendarza(login: str, token: str, nazwaPokoju: str, wpis: o.WpisKalendarza) -> None:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju przetestowana pod względem bezpieczeństwa; treść wpisu z zabezpieczonymi cudzysłowami
    
    #TODO wywołanie prepared statement do usunięcia wpisu z kalendarza pokoju
    dataAktywnosci(login,token)
    return None

# todo: zaimplementować w bazie danych
def modyfikujWpisKalendarza(login: str, token: str, nazwaPokoju: str, wpis: o.WpisKalendarza, noweDane: o.WpisKalendarza) -> None:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju przetestowana pod względem bezpieczeństwa; treści wpisów z zabezpieczonymi cudzysłowami
    
    #TODO wywołanie prepared statement do modyfikacji wpisu z kalendarza pokoju
    dataAktywnosci(login,token)
    return None

# todo: zaimplementować w bazie danych
def pobierzKalendarz(login: str, token: str, nazwaPokoju: str) -> typing.List[str]:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju przetestowana pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do pobrania wpisów z kalendarza pokoju
    lista: typing.List[str] = [""] #mock, tu będzie przekształcenie rezultatu operacji powyżej
    
    dataAktywnosci(login,token)
    return lista

# todo: zaimplementować w bazie danych
def czyPlikIstnieje(nazwaPokoju: str, nazwaPliku: str) -> bool:
    #nazwy pokoju i pliku przetestowane pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do sprawdzenia obecności pliku o podanej nazwie w pokoju "SELECT COUNT * FROM Pliki WHERE IDPokoju="..." AND NazwaPliku="...""
    wynik: bool = False #mock; tu będzie odebranie liczby i zmiana w prawda-fałsz
    
    return wynik

# todo: zaimplementować w bazie danych
def dodajPlik(login: str, token: str, nazwaPokoju: str, nazwaPliku: str, zawartoscPliku: bytes) -> None:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwy pokoju i pliku przetestowane pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do dodania nowego pliku dla pokoju
    
    dataAktywnosci(login,token)
    return None

# todo: zaimplementować w bazie danych
def usunPlik(login: str, token: str, nazwaPokoju: str, nazwaPliku: str) -> None:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwy pokoju i pliku przetestowane pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do usunięcia pliku z pokoju
    
    dataAktywnosci(login,token)
    return None

# todo: zaimplementować w bazie danych
def pobierzPlik(login: str, token: str, nazwaPokoju: str, nazwaPliku: str) -> bytes:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwy pokoju i pliku przetestowane pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do pobrania pliku o wskazanej nazwie
    wynik: bytes = None #mock; tu będzie odebranie rezultatu
    
    dataAktywnosci(login,token)
    return wynik

# todo: zaimplementować w bazie danych
def listaPlikow(login: str, token: str, nazwaPokoju: str) -> typing.List[str]:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju przetestowana pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do pobrania listy nazw i autorów plików
    wynik: typing.List[str] = [""] #mock; tu będzie odebranie rezultatu
    
    dataAktywnosci(login,token)
    return wynik

# todo: zaimplementować w bazie danych
def autorPliku(nazwaPokoju: str, nazwaPliku: str, dana: str = "nick") -> str:
    #nazwy pokoju i pliku przetestowane pod względem bezpieczeństwa
    if(dana=="nick"):
         #TODO wywołanie prepared statement do pobrania nicku publicznego autora pliku
         wynik="" #mock; tu będzie odebranie rezultatu
    elif(dana=="login"):
         #TODO wywołanie prepared statement do pobrania zahashowanego loginu autora pliku
         wynik="" #mock; tu będzie odebranie rezultatu
    else:
        wynik=""
        
    return wynik

# todo: zaimplementować w bazie danych
def czyKluczIstnieje(kluczPub: str) -> bool:
    #klucz przetestowany pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do sprawdzenia czy podany klucz już istnieje
    wynik: bool = False #mock; tu będzie odebranie rezultatu i zmiana w prawda-fałsz
    
    return wynik

# todo: zaimplementować w bazie danych
def ustawKlucz(login: str, token: str, kluczPub: str) -> None:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; klucz przetestowany pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do ustawienia klucza publicznego dla danego użytkownika
    
    return None

# todo: zaimplementować w bazie danych
def dodajKluczPokoju(loginAdmina: str, tokenAdmina: str, nazwaPokoju: str, kluczPubPokoju: str, kluczPrivPokoju: str, loginPosiadaczaKlucza: str):
    #loginy i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju i klucze przetestowane pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do wstawienia kluczy (IDPokoju, kluczPub, kluczPriv, IDUzytkownika)
    dataAktywnosci(loginAdmina,tokenAdmina)
    
    return None

# todo: zaimplementować w bazie danych
def czyKluczPokojuJuzIstnieje(kluczePubPokoju: str, kluczPrivPokoju: str, loginWlasciciela: str) -> bool:
    #login zahashowany oraz przetestowany pod względem bezpieczeństwa; klucze przetestowane pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do testu istnienia pary kluczy (kluczPub, kluczPriv, IDUzytkownika)
    wynik: bool = False #mock; tu będzie zamiana rezultatu w prawda-fałsz
    
    return wynik

# todo: zaimplementować w bazie danych
def czyZweryfikowany(login: str) -> bool:
    #login zahashowany oraz przetestowany pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do odebrania roli użytkownika "SELECT Rola FROM Uzytkownicy WHERE Login="+login+";"
    rola: str = ""  #mock; tu będzie zamina rezultatu w string
    
    return (not (rola=="Niezweryfikowany"))

# todo: zaimplementować w bazie danych
def usunKluczeDlaUzytkownika(loginAdmina: str, tokenAdmina: str, nazwaPokoju: str, loginPosiadaczaKlucza: str):
    #loginy i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju przetestowana pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do usunięcia kluczy (IDPokoju, IDUzytkownika)
    dataAktywnosci(loginAdmina,tokenAdmina)
    
    return None

# todo: zaimplementować w bazie danych
def kluczUzytkownika(loginAdmina: str, tokenAdmina: str, loginPosiadaczaKlucza: str) -> str:
    #loginy i token zahashowane oraz przetestowane pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do odebrania klucza użytkownika "SELECT KluczPub FROM Uzytkownicy WHERE Login="+loginPosiadaczaKlucza+";"
    wynik: str = "" #mock; tu będzie odebranie wyniku
    dataAktywnosci(loginAdmina,tokenAdmina)
    
    return wynik

# todo: zaimplementować w bazie danych
def loginUzytkownika(nick: str) -> str:
    #nick przetestowany pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do odebrania loginu użytkownika "SELECT Login FROM Uzytkownicy WHERE NickPubliczny="+nick+";"
    wynik: str = "" #mock; tu będzie odebranie wyniku
    
    return wynik

# todo: zaimplementować w bazie danych
def ustawRole(loginAdmina: str, tokenAdmina: str, loginZmienianego: str, nowaRola: str) -> None:
    #loginy i token zahashowane oraz przetestowane pod względem bezpieczeństwa; rola przetestowana pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do zmiany roli użytkownika
    dataAktywnosci(loginAdmina,tokenAdmina)
    
    return None

# todo: zaimplementować w bazie danych
def listaNiezweryfikowanych(login: str, token: str) -> typing.List[str]:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do odebrania listy niezweryfikowanych użytkowików "SELECT NickPubliczny FROM Uzytkownicy WHERE Rola=\"Niezweryfikowany\";"
    lista: typing.List[str] = [""] #mock; tu będzie odebranie wyniku i zmiana go w listę stringów
    dataAktywnosci(login,token)
    
    return lista