import typing


def iloscUzytkownikow(login: str, haslo: str = "", token: str = "", rola: str = "", nickPubliczny: str = "") -> int:
    #login, haslo i token zahashowane oraz przetestowane pod względem bezpieczeństwa
    ilosc: int
    
    if(haslo=="" and token=="" and rola=="" and nickPubliczny==""):
        #TODO wywołanie prepared statement do sprawdzenia czy taki login już istnieje "SELECT COUNT * FROM Uzytkownicy WHERE Login="+login+";"
        ilosc = 0 #mock; tu będzie zmiana wyniku w liczbę int
    
    elif(haslo!="" and token=="" and rola=="" and nickPubliczny==""):
        #TODO wywołanie prepared statement do próby logowania "SELECT COUNT * FROM Uzytkownicy WHERE Login="+login+" AND Haslo="+haslo+";"
        ilosc = 0 #mock; tu będzie zmiana wyniku w liczbę int
    
    elif(haslo=="" and token!="" and rola=="" and nickPubliczny==""):
        #TODO wywołanie prepared statement do testu poprawności sesji"SELECT COUNT * FROM Uzytkownicy WHERE Login="+login+" AND Token="+token+";"
        ilosc = 0 #mock; tu będzie zmiana wyniku w liczbę int
    
    elif(haslo=="" and token!="" and rola!="" and nickPubliczny==""):
        #TODO wywołanie prepared statement do testu poprawności sesji oraz uprawnień "SELECT COUNT * FROM Uzytkownicy WHERE Login="+login+" AND Token="+token+" AND Rola="+rola+";"
        ilosc = 0 #mock; tu będzie zmiana wyniku w liczbę int
    
    elif(login=="" and haslo=="" and token=="" and rola=="" and nickPubliczny!=""):
        #TODO wywołanie prepared statement do sprawdzenia czy taki nick już istnieje "SELECT COUNT * FROM Uzytkownicy WHERE NickPubliczny="+nickPubliczny+";"
        ilosc = 0 #mock; tu będzie zmiana wyniku w liczbę int
    
    else:           #nieznana opcja
        ilosc = -1  #wynik zawsze niespełniający warunków
    
    return ilosc


def rolaUzytkownika(login: str, token: str) -> str:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do odebrania roli użytkownika "SELECT Rola FROM Uzytkownicy WHERE Login="+login+" AND Token="+token+";"
    rola: str = ""  #mock; tu będzie zamina rezultatu w string
    return rola


def czyJestKod(kodZapr: str) -> bool:
    #kod zahashowany i przetestowany pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do sprawdzenia czy taki kod zaproszeniowy istnieje "SELECT COUNT * FROM Kody WHERE Kod="+kodZapr+";"
    wynik: bool = False #mock; tu będzie odebranie liczby i zmiana w prawda-fałsz
    
    return wynik


def dataAktywnosci(login: str, token: str) -> None:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa
    #TODO wywołanie prepared statement do aktualizacji daty aktywności użytkownika "UPDATE Uzytownicy SET Data=CURRENT_DATE() WHERE Login="+login+" AND Token="token+";"
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


def stworzBaze(nazwaProj: str) -> None:
    #nazwa projektu przetestowana pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do stworzenia wszystkich tabel z daną nazwą projektu (bazy)
    return None


def usunBaze(nazwaProj: str) -> None:
    #nazwa projektu przetestowana pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do usuwania bazy danych projektu "DROP DATABASE "+nazwaPRoj+";"
    return None


def czyBazaIstnieje(nazwaProj: str) -> bool:
    #nazwa projektu przetestowana pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do sprawdzenia istnienia bazy
    wynik: bool = False #mock; tu będzie zamiana otrzymaneg wyniku w prawda-fałsz
    return wynik


def polaczZBaza(nazwaProj: str) -> None:
    #nazwa projektu przetestowana pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do połączenia z podaną bazą "CONNECT "+nazwaProj+";"
    return None


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


def pokojeCzlonkowskie(login: str, token: str) -> typing.List[str]:
    #login zahashowany oraz przetestowany pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do pobrania listy pokojów, do których należy użytkownik WRAZ Z ICH KLUCZAMI KLUCZAMI PUBLICZNYMI I PRYWATNYMI ZASZYFROWANYMI JEGO PUBLICZNYM
    wynik: typing.List[str] = [""] #mock; tu będzie odebranie wyniku i zmiana w listę stringów
    dataAktywnosci(login,token)
    
    return wynik


def dodajTaski(login: str, token: str, nazwaPokoju: str, listaTaskow: typing.List[typing.Tuple[int,str,typing.Tuple[int,int,int],typing.Tuple[float,float],typing.List[int]]]) -> None:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju i nazwy tasków przetestowane pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do wstawienia nowych tasków do pokoju (bez informacji o taskach incydentnych); jeśli jakiś istnieje, usuń go i zastąp nowym - TRANSKACYJNIE
    dataAktywnosci(login,token)
    return None


def usunTaski(login: str, token: str, nazwaPokoju: str, listaTaskow: typing.List[typing.Tuple[int,str,typing.Tuple[int,int,int],typing.Tuple[float,float],typing.List[int]]]) -> None:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju i nazwy tasków przetestowane pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do usunięcia tasków z pokoju; jeśli jakiś nie istnieje, nic nie rób; po każdym usunięciu, usuń triggerem wszystkie zależności od niego - TRANSKACYJNIE
    dataAktywnosci(login,token)
    return None


def zauktualizujWlasnosciTaskow(login: str, token: str, nazwaPokoju: str, listaTaskow: typing.List[typing.Tuple[int,str,typing.Tuple[int,int,int],typing.Tuple[float,float],typing.List[int]]]) -> None:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju i nazwy tasków przetestowane pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do zaktualizowania tasków (nazwy, dat, incydencji, koordynatów) z pokoju; jeśli jakiś nie istnieje (lub incydentny nie istnieje), nic nie rób - TRANSKACYJNIE
    dataAktywnosci(login,token)
    return None


def ukonczTask(login: str, token: str, nazwaPokoju: str, idTaska: int) -> bool:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju przetestowana pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do sprawdzenia czy jakiś task nie blokuje zaznaczenia tego taska (wymagany, ale nieukończony)
    czyMozna: bool = False #mock, tu będzie rezultat otrzymany z operacji powyżej
    
    if(czyMozna):
        None #TODO wywołanie prepared statement do zaznaczenia taska o podanym ID jako ukończony
    dataAktywnosci(login,token)
    return czyMozna


def odznaczTaskJakoNieukonczony(login: str, token: str, nazwaPokoju: str, idTaska: int) -> bool:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju przetestowana pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do sprawdzenia czy jakiś task nie blokuje odznaczenia tego taska (wymaga go i jest ukończony)
    czyMozna: bool = False #mock, tu będzie rezultat otrzymany z operacji powyżej
    
    if(czyMozna):
        None #TODO wywołanie prepared statement do odznaczenia taska o podanym ID jako nieukończony
    dataAktywnosci(login,token)
    return czyMozna


def listaTaskow(login: str, token: str, nazwaPokoju: str) -> typing.List[str]:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju przetestowana pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do pobrania danych tasków z pokoju
    lista: typing.List[str] = [""] #mock, tu będzie przekształcenie rezultatu operacji powyżej
    
    dataAktywnosci(login,token)
    return lista


def pobierzChat(login: str, token: str, nazwaPokoju: str) -> typing.List[str]:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju przetestowana pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do pobrania 100 ostatnich wiadomości z chatu pokoju
    lista: typing.List[str] = [""] #mock, tu będzie przekształcenie rezultatu operacji powyżej
    
    dataAktywnosci(login,token)
    return lista


def aktualizacjaChatu(login: str, token: str, nazwaPokoju: str, autorOstatnioPosiadanej: str, dataOstatnioPosiadanej: int) -> typing.List[str]:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju i autor ostatniej wiadomości przetestowane pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do pobrania wszystkich wiadomości z chatu pokoju od ostatnio posiadanej
    lista: typing.List[str] = [""] #mock, tu będzie przekształcenie rezultatu operacji powyżej
    
    dataAktywnosci(login,token)
    return lista


def dodajWiadomosc(login: str, token: str, nazwaPokoju: str, wiadomosc: str, data: int) -> None:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju przetestowana pod względem bezpieczeństwa; treść wiadomości z zabezpieczonymi cudzysłowami
    
    #TODO wywołanie prepared statement do dodania nowej wiadomości wiadomości do chatu pokoju
    
    dataAktywnosci(login,token)
    return None


def czyWpisIstnieje(nazwaPokoju: str, wpis: typing.Tuple[str,typing.Tuple[int,int,int]]) -> bool:
    #nazwa pokoju przetestowana pod względem bezpieczeństwa; treść wpisu z zabezpieczonymi cudzysłowami
    
    #TODO wywołanie prepared statement do sprawdzenia obecności wpisu w kalendarzu pokoju "SELECT COUNT * FROM Kalendarze WHERE IDPokoju="..." AND Tresc="..." AND Data="...
    wynik: bool = False #mock; tu będzie odebranie liczby i zmiana w prawda-fałsz
    
    return wynik


def dodajWpisDoKalendarza(login: str, token: str, nazwaPokoju: str, wpis: typing.Tuple[str,typing.Tuple[int,int,int]]) -> None:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju przetestowana pod względem bezpieczeństwa; treść wpisu z zabezpieczonymi cudzysłowami
    
    #TODO wywołanie prepared statement do wstawienia nowego wpisu do kalendarza pokoju
    dataAktywnosci(login,token)
    return None


def usunWpisZKalendarza(login: str, token: str, nazwaPokoju: str, wpis: typing.Tuple[str,typing.Tuple[int,int,int]]) -> None:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju przetestowana pod względem bezpieczeństwa; treść wpisu z zabezpieczonymi cudzysłowami
    
    #TODO wywołanie prepared statement do usunięcia wpisu z kalendarza pokoju
    dataAktywnosci(login,token)
    return None


def modyfikujWpisKalendarza(login: str, token: str, nazwaPokoju: str, wpis: typing.Tuple[str,typing.Tuple[int,int,int]], noweDane: typing.Tuple[str,typing.Tuple[int,int,int]]) -> None:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju przetestowana pod względem bezpieczeństwa; treści wpisów z zabezpieczonymi cudzysłowami
    
    #TODO wywołanie prepared statement do modyfikacji wpisu z kalendarza pokoju
    dataAktywnosci(login,token)
    return None


def pobierzKalendarz(login: str, token: str, nazwaPokoju: str) -> typing.List[str]:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju przetestowana pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do pobrania wpisów z kalendarza pokoju
    lista: typing.List[str] = [""] #mock, tu będzie przekształcenie rezultatu operacji powyżej
    
    dataAktywnosci(login,token)
    return lista


def czyPlikIstnieje(nazwaPokoju: str, nazwaPliku: str) -> bool:
    #nazwy pokoju i pliku przetestowane pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do sprawdzenia obecności pliku o podanej nazwie w pokoju "SELECT COUNT * FROM Pliki WHERE IDPokoju="..." AND NazwaPliku="...""
    wynik: bool = False #mock; tu będzie odebranie liczby i zmiana w prawda-fałsz
    
    return wynik


def dodajPlik(login: str, token: str, nazwaPokoju: str, nazwaPliku: str, zawartoscPliku: bytes) -> None:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwy pokoju i pliku przetestowane pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do dodania nowego pliku dla pokoju
    
    dataAktywnosci(login,token)
    return None


def usunPlik(login: str, token: str, nazwaPokoju: str, nazwaPliku: str) -> None:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwy pokoju i pliku przetestowane pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do usunięcia pliku z pokoju
    
    dataAktywnosci(login,token)
    return None


def pobierzPlik(login: str, token: str, nazwaPokoju: str, nazwaPliku: str) -> bytes:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwy pokoju i pliku przetestowane pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do pobrania pliku o wskazanej nazwie
    wynik: bytes = None #mock; tu będzie odebranie rezultatu
    
    dataAktywnosci(login,token)
    return wynik


def listaPlikow(login: str, token: str, nazwaPokoju: str) -> typing.List[str]:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju przetestowana pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do pobrania listy nazw i autorów plików
    wynik: typing.List[str] = [""] #mock; tu będzie odebranie rezultatu
    
    dataAktywnosci(login,token)
    return wynik


def czyKluczIstnieje(kluczPub: str) -> bool:
    #klucz przetestowany pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do sprawdzenia czy podany klucz już istnieje
    wynik: bool = False #mock; tu będzie odebranie rezultatu i zmiana w prawda-fałsz
    
    return wynik


def ustawKlucz(login: str, token: str, kluczPub: str) -> None:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; klucz przetestowany pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do ustawienia klucza publicznego dla danego użytkownika
    
    return None


def dodajKluczPokoju(loginAdmina: str, tokenAdmina: str, nazwaPokoju: str, kluczPubPokoju: str, kluczPrivPokoju: str, loginPosiadaczaKlucza: str):
    #loginy i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju i klucze przetestowane pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do wstawienia kluczy (IDPokoju, kluczPub, kluczPriv, IDUzytkownika)
    dataAktywnosci(loginAdmina,tokenAdmina)
    
    return None


def czyKluczPokojuJuzIstnieje(kluczePubPokoju: str, kluczPrivPokoju: str, loginWlasciciela: str) -> bool:
    #login zahashowany oraz przetestowany pod względem bezpieczeństwa; klucze przetestowane pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do testu istnienia pary kluczy (kluczPub, kluczPriv, IDUzytkownika)
    wynik: bool = False #mock; tu będzie zamiana rezultatu w prawda-fałsz
    
    return wynik


def czyZweryfikowany(login: str) -> bool:
    #login zahashowany oraz przetestowany pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do odebrania roli użytkownika "SELECT Rola FROM Uzytkownicy WHERE Login="+login+";"
    rola: str = ""  #mock; tu będzie zamina rezultatu w string
    
    return (not (rola=="Niezweryfikowany"))


def usunKluczeDlaUzytkownika(loginAdmina: str, tokenAdmina: str, nazwaPokoju: str, loginPosiadaczaKlucza: str):
    #loginy i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju przetestowana pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do usunięcia kluczy (IDPokoju, IDUzytkownika)
    dataAktywnosci(loginAdmina,tokenAdmina)
    
    return None


def kluczUzytkownika(loginAdmina: str, tokenAdmina: str, nickPosiadaczaKlucza: str) -> str:
    #loginy i token zahashowane oraz przetestowane pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do odebrania klucza użytkownika "SELECT KluczPub FROM Uzytkownicy WHERE NickPubliczny="+nickPosiadaczaKlucza+";"
    wynik: str = "" #mock; tu będzie odebranie wyniku
    dataAktywnosci(loginAdmina,tokenAdmina)
    
    return wynik