import hashlib as hash
import typing
import ManagerKodow as Kody


def stworzProjekt(login: str, haslo: str) -> str: #token sesji
    #login i hasło już zahashowane
    
    #TODO wywołanie prepared statement do stworzenia wszystkich tabel
    
    token: str = Kody.wygenerujKod()
    hashTok: str = hash.sha3_512(token)
    #TODO wywołanie prepared statement do wstawienia nowego użytkownika "INSERT INTO Uzytownicy(Login, Haslo, Token, Rola) VALUES ("+login+", "+haslo+", "+hashTok+", 'Właściciel zespołu');"
        
    return token




def dodajZaproszenie(login: str, token: str, kodZaproszeniowy: str) -> typing.Tuple[bool, bool]: #[czy są uprawnienia, czy się udało]
    #kod zaproszeniowy już zahashowany
    hashLog: str = hash.sha3_512(login)
    hashTok: str = hash.sha3_512(token)
    
    #TODO wywołanie prepared statement do testu poprawności sesji oraz uprawnień "SELECT COUNT * FROM Uzytkownicy WHERE Login="+hashLog+" AND Token="+hashTok+" AND Rola='Właściciel zespolu';"
    wynik: int = 0 #mock; tu będzie odebranie liczby
    
    if(wynik!=1):
        return False, False
        
    #TODO wywołanie prepared statement do sprawdzenia czy taki kod nie jest już w bazie "SELECT COUNT * FROM Kody WHERE Kod="+kodZaproszeniowy+";"
    wynik: int = 0 #mock; tu będzie odebranie liczby
    
    if(wynik!=0):
        return True, False
    
    else:
        #TODO wywołanie prepared statement do wstawienia nowego kodu zaproszeniowego "INSERT INTO Kody(Kod, Data) VALUES ("+kodZaproszeniowy+", CURRENT_DATE());"
        return True, True



def usunProjekt(login: str, token: str) -> bool: #czy się udało
    hashLog: str = hash.sha3_512(login)
    hashTok: str = hash.sha3_512(token)
    
    #TODO wywołanie prepared statement do testu poprawności sesji oraz uprawnień "SELECT COUNT * FROM Uzytkownicy WHERE Login="+hashLog+" AND Token="+hashTok+" AND Rola='Właściciel zespolu';"
    wynik: int = 0 #mock; tu będzie odebranie liczby
    
    if(wynik!=1):
        return False
        
    else:
        #TODO wywołanie prepared statement do usuwania bazy danych projektu
        return True