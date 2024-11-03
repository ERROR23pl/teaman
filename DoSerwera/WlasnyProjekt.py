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