import typing
import Obiekty as o


def czyLoginIstnieje(login: str) -> bool:
    #login zahashowany oraz przetestowany pod względem bezpieczeństwa
    #TODO wywołanie prepared statement do sprawdzenia czy taki login już istnieje "SELECT COUNT * FROM Uzytkownicy WHERE Login="+login+";"
    print("Sprawdzenie istnienia loginu: "+login+"\n")
    wynik: bool = True #mock; tu będzie odebranie liczby i zmiana w prawda-fałsz
    
    return wynik


def probaLogowania(login: str, haslo: str) -> bool:
    #login i hasło zahashowane oraz przetestowane pod względem bezpieczeństwa
    #TODO wywołanie prepared statement do próby logowania "SELECT COUNT * FROM Uzytkownicy WHERE Login="+login+" AND Haslo="+haslo+";"
    print("Sprawdzenie istnienia użytkownika:\nLogin = "+login+"\nhasło = "+haslo+"\n")
    wynik: bool = True #mock; tu będzie odebranie liczby i zmiana w prawda-fałsz
    
    return wynik


def autoryzacjaTokenem(login: str, token: str) -> bool:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa
    #TODO wywołanie prepared statement do próby autoryzacji sesji "SELECT COUNT * FROM Uzytkownicy WHERE Login="+login+" AND Token="+token+";"
    print("Sprawdzenie istnienia użytkownika:\nLogin = "+login+"\ntoken = "+token+"\n")
    wynik: bool = True #mock; tu będzie odebranie liczby i zmiana w prawda-fałsz
    
    return wynik


def czyNickIstnieje(nickPubliczny: str) -> bool:
    #nick przetstowany pod względem bezpieczeństwa
    #TODO wywołanie prepared statement do sprawdzenia czy taki nick już istnieje "SELECT COUNT * FROM Uzytkownicy WHERE NickPubliczny="+nickPubliczny+";"
    print("Sprawdzenie istnienia nicku: "+nickPubliczny+"\n")
    wynik: bool = True #mock; tu będzie odebranie liczby i zmiana w prawda-fałsz
    
    return wynik


def rolaUzytkownika(login: str, token: str) -> str:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa
    print("Sprawdzanie roli użytkownika dla:\nlogin = "+login+"\ntoken = "+token+"\n")
    #TODO wywołanie prepared statement do odebrania roli użytkownika "SELECT Rola FROM Uzytkownicy WHERE Login="+login+" AND Token="+token+";"
    rola: str = "Właściciel"  #mock; tu będzie zamina rezultatu w string
    return rola


def czyJestKod(kodZapr: str) -> bool:
    #kod zahashowany i przetestowany pod względem bezpieczeństwa
    print("Sprawdzanie obecności kodu zaproszeniowego: "+kodZapr+"\n")
    #TODO wywołanie prepared statement do sprawdzenia czy taki kod zaproszeniowy istnieje "SELECT COUNT * FROM Kody WHERE Kod="+kodZapr+";"
    wynik: bool = False #mock; tu będzie odebranie liczby i zmiana w prawda-fałsz
    
    return wynik


def dataAktywnosci(login: str, token: str) -> None:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa
    print("Aktualizacja daty aktywności użytkownika:\nlogin = "+login+"\ntoken = "+token+"\n")
    #TODO wywołanie prepared statement do aktualizacji daty aktywności użytkownika "UPDATE Uzytownicy SET Data=CURRENT_DATE() WHERE Login="+login+" AND Token="token+";"
    return None


def ustawToken(login: str, haslo: str, token: str) -> None:
    #login, haslo i token zahashowane oraz przetestowane pod względem bezpieczeństwa
    print("Ustawienie użytkownikowi:\nlogin = "+login+"\nhasło = "+haslo+"\ntokenu: "+token+"\n")
    #TODO wywołanie prepared statement do wstawienia tokenu dla użytkownika "UPDATE Uzytownicy SET Token="+token+" WHERE Login="+login+" AND Haslo="haslo+";"
    dataAktywnosci(login,token)
    return None


def usunKod(kodZapr: str) -> None:
    #kod zahashowany i przetestowany pod względem bezpieczeństwa
    print("Usunięcie kodu zaproszeniowego: "+kodZapr+"\n")
    #TODO wywołanie prepared statement do usunięcia użytego kodu zaproszeniowego "DELETE FROM Kody WHERE Kod="+kodZapr+";"
    return None


def wstawKod(login: str, token: str, kodZapr: str) -> None:
    #login, token i kod zahashowane i przetestowane pod względem bezpieczeństwa
    print("Wstawienie kodu zaproszeniowego: "+kodZapr+"\n")
    #TODO wywołanie prepared statement do wstawienia nowego kodu zaproszeniowego "INSERT INTO Kody(Kod, Data) VALUES ("+kodZapr+", CURRENT_DATE());"
    dataAktywnosci(login,token)
    return None


def wstawUzytkownika(login: str, haslo: str, token: str, rola: str, nickPubliczny: str) -> None:
    #login, haslo i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nick przetestowany pod względem bezpieczeństwa
    print("Wstawienie użytkownika: \nlogin = "+login+"\nhasło = "+haslo+"\ntoken = "+token+"\nrola = "+rola+"\nnick = "+nickPubliczny+"\n")
    #TODO wywołanie prepared statement do wstawienia nowego użytkownika "INSERT INTO Uzytownicy(Login, Haslo, Token, Rola, NickPubliczny) VALUES ("+login+", "+haslo+", "+token+","+rola+","+nickPubliczny+");"
    dataAktywnosci(login,token)
    return None


def stworzBaze(nazwaProj: str) -> None:
    #nazwa projektu przetestowana pod względem bezpieczeństwa
    print("Stworzenie bazy projektu o nazwie "+nazwaProj+"\n")
    #TODO wywołanie prepared statement do stworzenia wszystkich tabel z daną nazwą projektu (bazy)
    return None


def usunBaze(nazwaProj: str) -> None:
    #nazwa projektu przetestowana pod względem bezpieczeństwa
    print("Usunięcie bazy projektu o nazwie "+nazwaProj+"\n")
    #TODO wywołanie prepared statement do usuwania bazy danych projektu "DROP DATABASE "+nazwaPRoj+";"
    return None


def czyBazaIstnieje(nazwaProj: str) -> bool:
    #nazwa projektu przetestowana pod względem bezpieczeństwa
    print("Sprawdzenie istnienia bazy projektu o nazwie "+nazwaProj+"\n")
    #TODO wywołanie prepared statement do sprawdzenia istnienia bazy
    wynik: bool = True #mock; tu będzie zamiana otrzymaneg wyniku w prawda-fałsz
    return wynik


def polaczZBaza(nazwaProj: str) -> None:
    #nazwa projektu przetestowana pod względem bezpieczeństwa
    print("Łączenie z bazą projektu o nazwie "+nazwaProj+"\n")
    #TODO wywołanie prepared statement do połączenia z podaną bazą "CONNECT "+nazwaProj+";"
    return None


def rozlaczZBaza() -> None:
    print("Rozłączenie z bazą projektu\n")
    #TODO wywołanie prepared statement do rozłączenia z aktualnie połączoną bazą
    return None


def czyszczeniePolnocowe() -> None:
    #TODO wywołanie prepared statement do usunięcia z tabeli Kody starych kodów zaproszeniowych o datach o dwa dni starszych od obecnej
    #TODO wywołanie prepared statement do usunięcia z tabeli Uzytkownicy starych tokenów dla użytkowników o datach ostatniej aktywności o dwa dni starszych od obecnej
    
    return None


def czyJestPokoj(nazwaPokoju: str) -> bool:
    #nazwa pokoju przetestowana pod względem bezpieczeństwa
    print("Sprawdzenie istnienia pokoju o nazwie "+nazwaPokoju+"\n")
    #TODO wywołanie prepared statement do sprawdzenia czy taki pokój istnieje "SELECT COUNT * FROM Pokoje WHERE Pokoj="+nazwaPokoju+";"
    wynik: bool = True #mock; tu będzie odebranie liczby i zmiana w prawda-fałsz
    
    return wynik


def stworzPokoj(login: str, token: str, nazwaPokoju: str) -> None:
    #login, token zahashowane i przetestowane pod względem bezpieczeństwa; nazwa pokoju przetestowana pod względem bezpieczeństwa
    print("Stworzenie pokoju o nazwie "+nazwaPokoju+"\nPrzez użytkownika:\nlogin = "+login+"\ntoken = "+token+"\n")
    #TODO wywołanie prepared statement do wstawienia nowego pokoju "INSERT INTO Pokoje(Pokoj) VALUES ("+nazwaPokoju+");"      ID jest autoinkrementowane
    dataAktywnosci(login,token)
    return None


def usunPokoj(login: str, token: str, nazwaPokoju: str) -> None:
    #login, token zahashowane i przetestowane pod względem bezpieczeństwa; nazwa pokoju przetestowana pod względem bezpieczeństwa
    print("Usunięcie pokoju o nazwie "+nazwaPokoju+"\nPrzez użytkownika:\nlogin = "+login+"\ntoken = "+token+"\n")
    #TODO wywołanie prepared statement do usuwania pokoju "DELETE FROM Pokoje WHERE Pokoj="+nazwaPokoju+";"      triggery usuwające z innych tabel dane związane z usuniętym pokojem
    dataAktywnosci(login,token)
    return None


def dodajDoPokoju(loginAdmina: str, tokenAdmina: str, nazwaPokoju: str, dodawanyLogin: str) -> None:
    #loginy i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju przetestowana pod względem bezpieczeństwa
    print("Dodanie do pokoju o nazwie "+nazwaPokoju+"\nUżytkownika:\nlogin = "+dodawanyLogin+"\nPrzez:\nlogin = "+loginAdmina+"\ntoken = "+tokenAdmina+"\n")
    #TODO wywołanie prepared statement do wstawienia nowego użytkownika do projektu "INSERT INTO Nalezenie(IDPokoju,IDUzytkownika) VALUES"...
    dataAktywnosci(loginAdmina,tokenAdmina)
    return None


def usunZPokoju(loginAdmina: str, tokenAdmina: str, nazwaPokoju: str, usuwanyLogin: str) -> None:
    #loginy i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju przetestowana pod względem bezpieczeństwa
    print("Usuwanie z pokoju o nazwie "+nazwaPokoju+"\nUżytkownika:\nlogin = "+usuwanyLogin+"\nPrzez:\nlogin = "+loginAdmina+"\ntoken = "+tokenAdmina+"\n")
    #TODO wywołanie prepared statement do usunięcia użytkownika z projektu "DELETE FROM Nalezenie WHERE IDUzytkownika="...
    dataAktywnosci(loginAdmina,tokenAdmina)
    return None


def czyUzytkownikJestWPokoju(nazwaPokoju: str, login: str) -> bool:
    #login zahashowany oraz przetestowany pod względem bezpieczeństwa; nazwa pokoju przetestowana pod względem bezpieczeństwa
    print("Sprawdzanie należenia do pokoju o nazwie "+nazwaPokoju+"\nUżytkownika:\nlogin = "+login+"\n")
    #TODO wywołanie prepared statement do sprawdzenia obecności użytkownika w pokoju "SELECT COUNT * FROM Nalezenie WHERE IDUzytkownika="..." AND IDPokoju="...
    wynik: bool = True #mock; tu będzie odebranie liczby i zmiana w prawda-fałsz
    
    return wynik


def pokojeCzlonkowskie(login: str, token: str) -> typing.List[str]:
    #login zahashowany oraz przetestowany pod względem bezpieczeństwa
    print("Sprawdzanie pokojów członkowskich użytkownika:\nlogin = "+login+"\ntoken = "+token+"\n")
    #TODO wywołanie prepared statement do, w których pokojach jest użytkownik "SELECT DISTINCT Pokoj FROM (Pokoje JOIN...) WHERE Login="+login+";"
    wynik: typing.List[str] = ["pokoj1, pokoj2, pokoj3, X, main"] #mock; tu będzie odebranie wyniku i zmiana w listę stringów
    dataAktywnosci(login,token)
    
    return wynik


def dodajTaski(login: str, token: str, nazwaPokoju: str, listaTaskow: typing.List[o.Task]) -> None:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju i nazwy tasków przetestowane pod względem bezpieczeństwa
    print("Dodanie przez użytkownika: \nlogin = "+login+"\ntoken = "+token+"\nDo pokoju: "+nazwaPokoju+"\nNowych tasków:\n")
    for task in listaTaskow:
        print(str(task.id)+"\t"+task.nazwa+"\t"+str(task.dzien)+"."+str(task.miesiac)+"."+str(task.rok)+"\t["+str(task.x)+"; "+str(task.y)+"]\t",end="")
        print(task.wymaganeTaski)
    print("")
    #TODO wywołanie prepared statement do wstawienia nowych tasków do pokoju (bez informacji o taskach incydentnych); jeśli jakiś istnieje, usuń go i zastąp nowym - TRANSKACYJNIE
    dataAktywnosci(login,token)
    return None


def usunTaski(login: str, token: str, nazwaPokoju: str, listaTaskow: typing.List[o.Task]) -> None:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju i nazwy tasków przetestowane pod względem bezpieczeństwa
    print("Usunięcie przez użytkownika: \nlogin = "+login+"\ntoken = "+token+"\nZ pokoju: "+nazwaPokoju+"\nTasków:\n")
    for task in listaTaskow:
        print(str(task.id)+"\t"+task.nazwa+"\t"+str(task.dzien)+"."+str(task.miesiac)+"."+str(task.rok)+"\t["+str(task.x)+"; "+str(task.y)+"]\t",end="")
        print(task.wymaganeTaski)
    print("")
    #TODO wywołanie prepared statement do usunięcia tasków z pokoju; jeśli jakiś nie istnieje, nic nie rób; po każdym usunięciu, usuń triggerem wszystkie zależności od niego - TRANSKACYJNIE
    dataAktywnosci(login,token)
    return None


def zauktualizujWlasnosciTaskow(login: str, token: str, nazwaPokoju: str, listaTaskow: typing.List[o.Task]) -> None:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju i nazwy tasków przetestowane pod względem bezpieczeństwa
    print("Zaktualizowanie przez użytkownika: \nlogin = "+login+"\ntoken = "+token+"\nW pokoju: "+nazwaPokoju+"\nTasków:\n")
    for task in listaTaskow:
        print(str(task.id)+"\t"+task.nazwa+"\t"+str(task.dzien)+"."+str(task.miesiac)+"."+str(task.rok)+"\t["+str(task.x)+"; "+str(task.y)+"]\t",end="")
        print(task.wymaganeTaski)
    print("")
    #TODO wywołanie prepared statement do zaktualizowania tasków (nazwy, dat, incydencji, koordynatów) z pokoju; jeśli jakiś nie istnieje (lub incydentny nie istnieje), nic nie rób - TRANSKACYJNIE
    dataAktywnosci(login,token)
    return None


def ukonczTask(login: str, token: str, nazwaPokoju: str, idTaska: int) -> bool:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju przetestowana pod względem bezpieczeństwa
    print("Próba zaznaczenia przez użytkownika:\nlogin = "+login+"\ntoken = "+token+"\nW pokoju: "+nazwaPokoju+"\nTaska o ID = "+str(idTaska)+" jako ukończony")
    #TODO wywołanie prepared statement do sprawdzenia czy jakiś task nie blokuje zaznaczenia tego taska (wymagany, ale nieukończony)
    czyMozna: bool = True #mock, tu będzie rezultat otrzymany z operacji powyżej
    
    if(czyMozna):
        print("Sukces")
        None #TODO wywołanie prepared statement do zaznaczenia taska o podanym ID jako ukończony
    dataAktywnosci(login,token)
    print("")
    return czyMozna


def odznaczTaskJakoNieukonczony(login: str, token: str, nazwaPokoju: str, idTaska: int) -> bool:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju przetestowana pod względem bezpieczeństwa
    print("Próba odznaczenia przez użytkownika:\nlogin = "+login+"\ntoken = "+token+"\nW pokoju: "+nazwaPokoju+"\nTaska o ID = "+str(idTaska)+" jako nieukończony")
    #TODO wywołanie prepared statement do sprawdzenia czy jakiś task nie blokuje odznaczenia tego taska (wymaga go i jest ukończony)
    czyMozna: bool = True #mock, tu będzie rezultat otrzymany z operacji powyżej
    
    if(czyMozna):
        print("Sukces")
        None #TODO wywołanie prepared statement do odznaczenia taska o podanym ID jako nieukończony
    dataAktywnosci(login,token)
    print("")
    return czyMozna


def listaTaskow(login: str, token: str, nazwaPokoju: str) -> typing.List[str]:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju przetestowana pod względem bezpieczeństwa
    print("Pobranie przez użytkownika:\nlogin = "+login+"\ntoken = "+token+"\nTasków z pokoju: "+nazwaPokoju+"\n")
    #TODO wywołanie prepared statement do pobrania danych tasków z pokoju
    lista: typing.List[str] = ["1; nazwaTaska1; 12, 2, 2025; true; 100.06, 157.0; 2, 3, 5","2; nazwaTaska2; 1, 1, 2025; true; 120.06, 17.0; 3","3; nazwaTaska3; 10, 1, 2025; true; 20.06, 1007.47; 4, 5","5; nazwaTaska5; 1, 12, 2024; true; 426.66, 711.711; ","7; nazwaTaska7; 1, 12, 2026; false; 469.66, 71.711; 8","8; nazwaTaska8; 14, 7, 2026; false; 568.66, 711.711; 1, 2, 3, 4, 5"] #mock, tu będzie przekształcenie rezultatu operacji powyżej
    
    dataAktywnosci(login,token)
    return lista


def pobierzChat(login: str, token: str, nazwaPokoju: str) -> typing.List[str]:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju przetestowana pod względem bezpieczeństwa
    print("Pobranie przez użytkownika:\nlogin = "+login+"\ntoken = "+token+"\nChatu pokoju: "+nazwaPokoju+"\n")
    #TODO wywołanie prepared statement do pobrania 100 ostatnich wiadomości z chatu pokoju
    lista: typing.List[str] = ["Wiadomość 1.","Uzytkownik1","123456789","Wiadomość 2.","Uzytkownik2","123456790","Wiadomość 3.","Uzytkownik3","123456791","Wiadomość 4.","Uzytkownik4","123456792"] #mock, tu będzie przekształcenie rezultatu operacji powyżej
    
    dataAktywnosci(login,token)
    return lista


def aktualizacjaChatu(login: str, token: str, nazwaPokoju: str, autorOstatnioPosiadanej: str, dataOstatnioPosiadanej: int) -> typing.List[str]:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju i autor ostatniej wiadomości przetestowane pod względem bezpieczeństwa
    print("Pobranie przez użytkownika:\nlogin = "+login+"\ntoken = "+token+"\nAktualizacji chatu pokoju: "+nazwaPokoju+"\nOd wiadomości użytkownika: "+autorOstatnioPosiadanej+"\nz daty o kodzie: "+str(dataOstatnioPosiadanej)+"\n")
    #TODO wywołanie prepared statement do pobrania wszystkich wiadomości z chatu pokoju od ostatnio posiadanej
    lista: typing.List[str] = ["Wiadomość 3.","Uzytkownik3","123456791","Wiadomość 4.","Uzytkownik4","123456792","Wiadomość'admina","Uzytkownik711","123456795"] #mock, tu będzie przekształcenie rezultatu operacji powyżej
    
    dataAktywnosci(login,token)
    return lista


def dodajWiadomosc(login: str, token: str, nazwaPokoju: str, wiadomosc: str, data: int) -> None:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju przetestowana pod względem bezpieczeństwa; treść wiadomości z zabezpieczonymi cudzysłowami
    print("Wysłanie przez użytkownika:\nlogin = "+login+"\ntoken = "+token+"\nNa chat pokoju: "+nazwaPokoju+"\nWiadomości: "+wiadomosc+"\nZ kodem daty: "+str(data)+"\n")
    #TODO wywołanie prepared statement do dodania nowej wiadomości wiadomości do chatu pokoju
    
    dataAktywnosci(login,token)
    return None


def czyWpisIstnieje(nazwaPokoju: str, wpis: o.WpisKalendarza) -> bool:
    #nazwa pokoju przetestowana pod względem bezpieczeństwa; treść wpisu z zabezpieczonymi cudzysłowami
    print("Sprawdzenie istnienia w kalendarzu pokoju: "+nazwaPokoju+"\nWpisu o nazwie "+wpis.nazwa+"\nI dacie: "+str(wpis.dzien)+"."+str(wpis.miesiac)+"."+str(wpis.rok)+"\n")
    #TODO wywołanie prepared statement do sprawdzenia obecności wpisu w kalendarzu pokoju "SELECT COUNT * FROM Kalendarze WHERE IDPokoju="..." AND Tresc="..." AND Data="...
    wynik: bool = True #mock; tu będzie odebranie liczby i zmiana w prawda-fałsz
    
    return wynik


def dodajWpisDoKalendarza(login: str, token: str, nazwaPokoju: str, wpis: o.WpisKalendarza) -> None:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju przetestowana pod względem bezpieczeństwa; treść wpisu z zabezpieczonymi cudzysłowami
    print("Dodanie przez użytkownika:\nlogin = "+login+"\ntoken = "+token+"\nDo kalendarza pokoju: "+nazwaPokoju+"\nWpisu o nazwie "+wpis.nazwa+"\nI dacie: "+str(wpis.dzien)+"."+str(wpis.miesiac)+"."+str(wpis.rok)+"\n")
    #TODO wywołanie prepared statement do wstawienia nowego wpisu do kalendarza pokoju
    dataAktywnosci(login,token)
    return None


def usunWpisZKalendarza(login: str, token: str, nazwaPokoju: str, wpis: o.WpisKalendarza) -> None:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju przetestowana pod względem bezpieczeństwa; treść wpisu z zabezpieczonymi cudzysłowami
    print("Usunięcie przez użytkownika:\nlogin = "+login+"\ntoken = "+token+"\nZ kalendarza pokoju: "+nazwaPokoju+"\nWpisu o nazwie "+wpis.nazwa+"\nI dacie: "+str(wpis.dzien)+"."+str(wpis.miesiac)+"."+str(wpis.rok)+"\n")
    #TODO wywołanie prepared statement do usunięcia wpisu z kalendarza pokoju
    dataAktywnosci(login,token)
    return None


def modyfikujWpisKalendarza(login: str, token: str, nazwaPokoju: str, wpis: o.WpisKalendarza, noweDane: o.WpisKalendarza) -> None:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju przetestowana pod względem bezpieczeństwa; treści wpisów z zabezpieczonymi cudzysłowami
    print("Zmiana przez użytkownika:\nlogin = "+login+"\ntoken = "+token+"\nW kalendarzu pokoju: "+nazwaPokoju+"\nWpisu o nazwie "+wpis.nazwa+"\nI dacie: "+str(wpis.dzien)+"."+str(wpis.miesiac)+"."+str(wpis.rok)+"\nNa wpis o nazwie "+noweDane.nazwa+"\nI dacie: "+str(noweDane.dzien)+"."+str(noweDane.miesiac)+"."+str(noweDane.rok)+"\n")
    #TODO wywołanie prepared statement do modyfikacji wpisu z kalendarza pokoju
    dataAktywnosci(login,token)
    return None


def pobierzKalendarz(login: str, token: str, nazwaPokoju: str) -> typing.List[str]:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju przetestowana pod względem bezpieczeństwa
    print("Pobranie przez użytkownika:\nlogin = "+login+"\ntoken = "+token+"\nKalendarza pokoju: "+nazwaPokoju+"\n")
    #TODO wywołanie prepared statement do pobrania wpisów z kalendarza pokoju
    lista: typing.List[str] = ["Spotkanie 1.","1, 3, 2025","Spotkanie 2.","12, 4, 2025","Inne wydarzenie","1, 1, 2026"] #mock, tu będzie przekształcenie rezultatu operacji powyżej
    
    dataAktywnosci(login,token)
    return lista


def czyPlikIstnieje(nazwaPokoju: str, nazwaPliku: str) -> bool:
    #nazwy pokoju i pliku przetestowane pod względem bezpieczeństwa
    print("Sprawdzenie istnienia w pokoju: "+nazwaPokoju+"\nPliku o nazwie "+nazwaPliku+"\n")
    #TODO wywołanie prepared statement do sprawdzenia obecności pliku o podanej nazwie w pokoju "SELECT COUNT * FROM Pliki WHERE IDPokoju="..." AND NazwaPliku="...""
    wynik: bool = True #mock; tu będzie odebranie liczby i zmiana w prawda-fałsz
    
    return wynik


def dodajPlik(login: str, token: str, nazwaPokoju: str, nazwaPliku: str, zawartoscPliku: bytes) -> None:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwy pokoju i pliku przetestowane pod względem bezpieczeństwa
    print("Dodanie przez użytkownika:\nlogin = "+login+"\ntoken = "+token+"\nDo pokoju: "+nazwaPokoju+"\nPliku o nazwie "+nazwaPliku+"\nI treści: "+zawartoscPliku.decode()+"\n")
    #TODO wywołanie prepared statement do dodania nowego pliku dla pokoju
    
    dataAktywnosci(login,token)
    return None


def usunPlik(login: str, token: str, nazwaPokoju: str, nazwaPliku: str) -> None:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwy pokoju i pliku przetestowane pod względem bezpieczeństwa
    print("Usunięcie przez użytkownika:\nlogin = "+login+"\ntoken = "+token+"\nZ pokoju: "+nazwaPokoju+"\nPliku o nazwie "+nazwaPliku+"\n")
    #TODO wywołanie prepared statement do usunięcia pliku z pokoju
    
    dataAktywnosci(login,token)
    return None


def pobierzPlik(login: str, token: str, nazwaPokoju: str, nazwaPliku: str) -> bytes:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwy pokoju i pliku przetestowane pod względem bezpieczeństwa
    print("Pobranie przez użytkownika:\nlogin = "+login+"\ntoken = "+token+"\nZ pokoju: "+nazwaPokoju+"\nPliku o nazwie "+nazwaPliku+"\n")
    #TODO wywołanie prepared statement do pobrania pliku o wskazanej nazwie
    wynik: bytes = ("Bardzo bardzo istotna zawartość\ntego pliku").encode() #mock; tu będzie odebranie rezultatu
    
    dataAktywnosci(login,token)
    return wynik


def listaPlikow(login: str, token: str, nazwaPokoju: str) -> typing.List[str]:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju przetestowana pod względem bezpieczeństwa
    print("Pobranie przez użytkownika:\nlogin = "+login+"\ntoken = "+token+"\nListy plików pokoju: "+nazwaPokoju+"\n")
    #TODO wywołanie prepared statement do pobrania listy nazw i autorów plików
    wynik: typing.List[str] = [""] #mock; tu będzie odebranie rezultatu
    
    dataAktywnosci(login,token)
    return wynik


def autorPliku(nazwaPokoju: str, nazwaPliku: str, dana: str = "nick") -> str:
    #nazwy pokoju i pliku przetestowane pod względem bezpieczeństwa
    if(dana=="nick"):
        print("Pobranie nicku autora pliku: "+nazwaPliku+"\nZ pokoju: "+nazwaPokoju+"\n")
        #TODO wywołanie prepared statement do pobrania nicku publicznego autora pliku
        wynik="nick1234" #mock; tu będzie odebranie rezultatu
    elif(dana=="login"):
        print("Pobranie loginu autora pliku: "+nazwaPliku+"\nZ pokoju: "+nazwaPokoju+"\n")
        #TODO wywołanie prepared statement do pobrania zahashowanego loginu autora pliku
        wynik="login1234" #mock; tu będzie odebranie rezultatu
    else:
        print("Nieznana dana autora pliku")
        wynik=""
        
    return wynik


def czyKluczIstnieje(kluczPub: str) -> bool:
    #klucz przetestowany pod względem bezpieczeństwa
    print("Sprawdzenie istnienia klucza: "+kluczPub+"\n")
    #TODO wywołanie prepared statement do sprawdzenia czy podany klucz już istnieje
    wynik: bool = False #mock; tu będzie odebranie rezultatu i zmiana w prawda-fałsz
    
    return wynik


def ustawKlucz(login: str, token: str, kluczPub: str) -> None:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa; klucz przetestowany pod względem bezpieczeństwa
    print("Ustawienie użytkownikowi:\nlogin = "+login+"\ntoken = "+token+"\nKlucza publicznego: "+kluczPub+"\n")
    #TODO wywołanie prepared statement do ustawienia klucza publicznego dla danego użytkownika
    
    return None


def dodajKluczPokoju(loginAdmina: str, tokenAdmina: str, nazwaPokoju: str, kluczPubPokoju: str, kluczPrivPokoju: str, loginPosiadaczaKlucza: str):
    #loginy i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju i klucze przetestowane pod względem bezpieczeństwa
    print("Dodanie przez admina:\nlogin = "+loginAdmina+"\ntoken = "+tokenAdmina+"\Kluczy: "+kluczPubPokoju+"\n"+kluczPrivPokoju+"\nPokoju: "+nazwaPokoju+"\nDla użytkownika: "+loginPosiadaczaKlucza+"\n")
    #TODO wywołanie prepared statement do wstawienia kluczy (IDPokoju, kluczPub, kluczPriv, IDUzytkownika)
    dataAktywnosci(loginAdmina,tokenAdmina)
    
    return None


def czyKluczPokojuJuzIstnieje(kluczePubPokoju: str, kluczPrivPokoju: str, loginWlasciciela: str) -> bool:
    #login zahashowany oraz przetestowany pod względem bezpieczeństwa; klucze przetestowane pod względem bezpieczeństwa
    print("Sprawdzenie istnienia kluczy:\n"+kluczePubPokoju+"\n"+kluczPrivPokoju+"\nDla właściciela projektu: "+loginWlasciciela+"\n")
    #TODO wywołanie prepared statement do testu istnienia pary kluczy (kluczPub, kluczPriv, IDUzytkownika)
    wynik: bool = False #mock; tu będzie zamiana rezultatu w prawda-fałsz
    
    return wynik


def czyZweryfikowany(login: str) -> bool:
    #login zahashowany oraz przetestowany pod względem bezpieczeństwa
    print("Sprawdzenie stanu weryfikacji użytkownika:\nlogin = "+login+"\n")
    #TODO wywołanie prepared statement do odebrania roli użytkownika "SELECT Rola FROM Uzytkownicy WHERE Login="+login+";"
    rola: str = ""  #mock; tu będzie zamina rezultatu w string
    
    return (not (rola=="Niezweryfikowany"))


def usunKluczeDlaUzytkownika(loginAdmina: str, tokenAdmina: str, nazwaPokoju: str, loginPosiadaczaKlucza: str):
    #loginy i token zahashowane oraz przetestowane pod względem bezpieczeństwa; nazwa pokoju przetestowana pod względem bezpieczeństwa
    print("Usunięcie przez admina:\nlogin = "+loginAdmina+"\ntoken = "+tokenAdmina+"\nKlucza użytkownika: "+loginPosiadaczaKlucza+"\nDo pokoju: "+nazwaPokoju+"\n")
    #TODO wywołanie prepared statement do usunięcia kluczy (IDPokoju, IDUzytkownika)
    dataAktywnosci(loginAdmina,tokenAdmina)
    
    return None


def kluczUzytkownika(loginAdmina: str, tokenAdmina: str, loginPosiadaczaKlucza: str) -> str:
    #loginy i token zahashowane oraz przetestowane pod względem bezpieczeństwa
    print("Pobranie przez admina:\nlogin = "+loginAdmina+"\ntoken = "+tokenAdmina+"\nKlucza publicznego użytkownika: "+loginPosiadaczaKlucza+"\n")
    #TODO wywołanie prepared statement do odebrania klucza użytkownika "SELECT KluczPub FROM Uzytkownicy WHERE Login="+loginPosiadaczaKlucza+";"
    wynik: str = "klucz12345666666" #mock; tu będzie odebranie wyniku
    dataAktywnosci(loginAdmina,tokenAdmina)
    
    return wynik


def loginUzytkownika(nick: str) -> str:
    #nick przetestowany pod względem bezpieczeństwa
    print("Pobranie loginu użytkownika o nicku: "+nick+"\n")
    #TODO wywołanie prepared statement do odebrania loginu użytkownika "SELECT Login FROM Uzytkownicy WHERE NickPubliczny="+nick+";"
    wynik: str = "loginUwU" #mock; tu będzie odebranie wyniku
    
    return wynik


def ustawRole(loginAdmina: str, tokenAdmina: str, loginZmienianego: str, nowaRola: str) -> None:
    #loginy i token zahashowane oraz przetestowane pod względem bezpieczeństwa; rola przetestowana pod względem bezpieczeństwa
    print("Ustawienie przez admina:\nlogin = "+loginAdmina+"\ntoken = "+tokenAdmina+"\nRoli: "+nowaRola+"\nUżytkownikowi o loginie: "+loginZmienianego+"\n")
    #TODO wywołanie prepared statement do zmiany roli użytkownika
    dataAktywnosci(loginAdmina,tokenAdmina)
    
    return None

def listaNiezweryfikowanych(login: str, token: str) -> typing.List[str]:
    #login i token zahashowane oraz przetestowane pod względem bezpieczeństwa
    print("Pobranie przez admina:\nlogin = "+login+"\ntoken = "+token+"\nListy niezweryfikowanych użytkowników\n")
    #TODO wywołanie prepared statement do odebrania listy niezweryfikowanych użytkowików "SELECT NickPubliczny FROM Uzytkownicy WHERE Rola=\"Niezweryfikowany\";"
    lista: typing.List[str] = ["nickNiezw1","NickNiezw2","NickNiezw3"] #mock; tu będzie odebranie wyniku i zmiana go w listę stringów
    dataAktywnosci(login,token)
    
    return lista