import typing


def iloscUzytkownikow(login: str, haslo: str = "", token: str = "", rola: str = "") -> int:
    #login, haslo i token zahashowane oraz przetestowane pod względem bezpieczeństwa
    ilosc: int
    
    if(haslo=="" and token=="" and rola==""):
        #TODO wywołanie prepared statement do sprawdzenia czy taki login już istnieje "SELECT COUNT * FROM Uzytkownicy WHERE Login="+login+";"
        ilosc = 0 #mock; tu będzie zmiana wyniku w liczbę int
    
    elif(haslo!="" and token=="" and rola==""):
        #TODO wywołanie prepared statement do próby logowania "SELECT COUNT * FROM Uzytkownicy WHERE Login="+login+" AND Haslo="+haslo+";"
        ilosc = 0 #mock; tu będzie zmiana wyniku w liczbę int
    
    elif(haslo=="" and token!="" and rola==""):
        #TODO wywołanie prepared statement do testu poprawności sesji"SELECT COUNT * FROM Uzytkownicy WHERE Login="+login+" AND Token="+token+";"
        ilosc = 0 #mock; tu będzie zmiana wyniku w liczbę int
    
    elif(haslo=="" and token!="" and rola!=""):
        #TODO wywołanie prepared statement do testu poprawności sesji oraz uprawnień "SELECT COUNT * FROM Uzytkownicy WHERE Login="+login+" AND Token="+token+" AND Rola="+rola+";"
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


def wstawUzytkownika(login: str, haslo: str, token: str, rola: str) -> None:
    #login, haslo i token zahashowane oraz przetestowane pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do wstawienia nowego użytkownika "INSERT INTO Uzytownicy(Login, Haslo, Token, Rola) VALUES ("+login+", "+haslo+", "+token+","+rola+");"
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


def usunZPokoju(loginAdmina: str, tokenAdmina: str, nazwaPokoju: str, dodawanyLogin: str) -> None:
    #loginy i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju przetestowana pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do usunięcia użytkownika z projektu "DELETE FROM Nalezenie WHERE IDUzytkownika="...
    dataAktywnosci(loginAdmina,tokenAdmina)
    return None


def czyUzytkownikJestWPokoju(nazwaPokoju: str, login: str) -> bool:
    #login zahashowany oraz przetestowany pod względem bezpieczeństwa; nazwa pokoju przetestowana pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do sprawdzenia obecności użytkownika w projekcie "SELECT COUNT * FROM Nalezenie WHERE IDUzytkownika="..." AND IDProjektu="...
    wynik: bool = False #mock; tu będzie odebranie liczby i zmiana w prawda-fałsz
    
    return wynik


def pokojeCzlonkowskie(login: str, token: str) -> typing.List[str]:
    #login zahashowany oraz przetestowany pod względem bezpieczeństwa
    
    #TODO wywołanie prepared statement do, w których projektach jest użytkownik "SELECT DISTINCT Projekt FROM (Projekty JOIN...) WHERE Login="+login+";"
    wynik: typing.List[str] = [""] #mock; tu będzie odebranie wyniku i zmiana w listę stringów
    dataAktywnosci(login,token)
    
    return wynik