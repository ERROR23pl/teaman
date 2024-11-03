import hashlib as hash
import ManagerKodow as Kody


def stworzProjekt(login: str, haslo: str) -> str: #token sesji
    #login i hasło już zahashowane
    
    #TODO wywołanie prepared statement do stworzenia wszystkich tabel
    
    token: str = Kody.wygenerujKod()
    hashTok: str = hash.sha3_512(token)
    #TODO wywołanie prepared statement do wstawienia nowego użytkownika "INSERT INTO Uzytownicy(Login, Haslo, Token, Rola) VALUES ("+login+", "+haslo+", "+hashTok+", 'Właściciel zespołu');"
        
    return token




def dodajZaproszenie():
    None
    



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