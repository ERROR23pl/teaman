import hashlib as hash
import typing
import ManagerKodow as Kody


def probaLogowania(login: str, haslo: str) -> typing.Tuple[bool,str,str]: #[poprawność danych, token sesji, rola]
    hashLog: str = hash.sha3_512(login)
    hashHas: str = hash.sha3_512(haslo)
    
    #TODO wywołanie prepared statement do próby logowania "SELECT COUNT * FROM Uzytkownicy WHERE Login="+hashLog+" AND Haslo="+hashHas+";"
    wynik: int = 0 #mock; tu będzie odebranie liczby
    
    if(wynik!=1):
        return False, "", ""
    
    else:
        token: str = Kody.wygenerujKod()
        hashTok: str = hash.sha3_512(token)
        #TODO wywołanie prepared statement do wstawienia tokenu dla użytkownika "UPDATE Uzytownicy SET Token="+hashTok+" WHERE Login="+hashLog+" AND Haslo="hashHas+";"
        rola: str = "" #TODO wywołanie prepared statement do odebrania roli użytkownika "SELECT Rola FROM Uzytkownicy WHERE Login="+hashLog+" AND Haslo="+hashHas+";"
        
        return True, token, rola



def probaRejestracji(kodZaproszeniowy: str, login: str, haslo: str) -> typing.Tuple[bool,bool,str]: #[poprawność kodu, sukces rejestracji, token sesji]
    #login i hasło już zahashowane
    hashKod: str = hash.sha3_512(kodZaproszeniowy)
    
    #TODO wywołanie prepared statement do sprawdzenia czy taki kod zaproszeniowy istnieje "SELECT COUNT * FROM Kody WHERE Kod="+hashKod+";"
    wynik: int = 0 #mock; tu będzie odebranie liczby
    
    if(wynik!=1):
        return False, False, ""
    
    #TODO wywołanie prepared statement do próby rejestracji - sprawdzenia czy taki login już istnieje "SELECT COUNT * FROM Uzytkownicy WHERE Login="+login+";"
    wynik: int = 0 #mock; tu będzie odebranie liczby
    
    if(wynik!=0):
        return True, False, ""
    
    else:
        token: str = Kody.wygenerujKod()
        hashTok: str = hash.sha3_512(token)
        #TODO wywołanie prepared statement do wstawienia nowego użytkownika "INSERT INTO Uzytownicy(Login, Haslo, Token, Rola) VALUES ("+login+", "+haslo+", "+hashTok+", 'Członek zespołu');"
        #TODO wywołanie prepared statement do usunięcia użytego kodu zaproszeniowego "DELETE FROM Kody WHERE Kod="+hashKod+";"
        
        return True, True, token