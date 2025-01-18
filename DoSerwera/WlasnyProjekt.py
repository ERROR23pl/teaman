import hashlib as hash
import typing
import ManagerKodow as Kody
import ManagerKluczy as Klucze
import KomunikacjaZBaza as Bazy
import sys
sys.path.insert(1, '../Database')
import SQLLite as Baza


def stworzProjekt(baza: Baza.SQLLiteDB, nazwaProjektu: str, login: str, haslo: str, nick: str, kluczPub: str) -> typing.Tuple[bool,typing.List[str]]: #[sukces operacji, [token sesji]]
    #login i hasło już zahashowane
    
    token: str = Kody.wygenerujKod()
    hashTok: str = hash.sha3_512(token.encode()).hexdigest()
    Bazy.wstawUzytkownika(baza,login,haslo,hashTok,"Admin",nick)
    Bazy.ustawKlucz(baza,login,hashTok,kluczPub)
    
    kluczePokoju: typing.Tuple[str,str] = Klucze.generujKluczePokoju()
    kluczePokoju[0] = Klucze.zaszyfruj(kluczPub,kluczePokoju[0])
    kluczePokoju[1] = Klucze.zaszyfruj(kluczPub,kluczePokoju[1])
    
    Bazy.stworzPokoj(baza,login,hashTok,nazwaProjektu)                #automatycznie stwórz pokój główny o nazwie takiej samej jak nazwa projektu
    Bazy.dodajDoPokoju(baza,login,hashTok,nazwaProjektu,login)        #dodaj siebie (właściciela) do pokoju głównego
    Bazy.dodajKluczPokoju(baza,login,hashTok,nazwaProjektu,kluczePokoju[0],kluczePokoju[1],login)    #dodanie do tabeli kluczy, wygenerowanych kluczy pokoju głównego zaszyfrowanych kluczm publicznym właściciela
        
    return True, [token]




def dodajZaproszenie(baza: Baza.SQLLiteDB, login: str, token: str, kodZaproszeniowy: str) -> typing.Tuple[bool,typing.List[str]]: #[sukces operacji, [""]]
    #kod zaproszeniowy już zahashowany
    hashLog: str = hash.sha3_512(login.encode()).hexdigest()
    hashTok: str = hash.sha3_512(token.encode()).hexdigest()
    
    if(not Bazy.autoryzacjaTokenem(baza,hashLog,hashTok)):
        return False, ["Niepoprawne dane"]
    
    if(Bazy.rolaUzytkownika(baza,hashLog,hashTok)!="Admin"):
        return False, ["Brak uprawnień"]
        
    czyKodJuzJest: bool = Bazy.czyJestKod(baza,kodZaproszeniowy)
    
    if(czyKodJuzJest):
        return False,["Wyślij nowy kod"]
    
    else:
        Bazy.wstawKod(baza,hashLog,hashTok,kodZaproszeniowy)
        return True, [""]




def usunProjekt(baza: Baza.SQLLiteDB, nazwaProjektu: str, login: str, token: str) -> typing.Tuple[bool,typing.List[str]]: #[sukces operacji, [""]]
    hashLog: str = hash.sha3_512(login.encode()).hexdigest()
    hashTok: str = hash.sha3_512(token.encode()).hexdigest()
    
    if(not Bazy.autoryzacjaTokenem(baza,hashLog,hashTok)):
        return False, ["Niepoprawne dane"]
    
    if(Bazy.rolaUzytkownika(baza,hashLog,hashTok)!="Admin"):
        return False, ["Brak uprawnień"]
        
    else:
        Bazy.usunBaze(baza,nazwaProjektu)
        return True, [""]


 

def pobierzKluczPublicznyUzytkownika(baza: Baza.SQLLiteDB, login: str, token: str, nickUzytkownika: str) -> typing.Tuple[bool,typing.List[str]]: #[sukces operacji, [klucz]]
    hashLog: str = hash.sha3_512(login.encode()).hexdigest()
    hashTok: str = hash.sha3_512(token.encode()).hexdigest()
    
    if(not Bazy.autoryzacjaTokenem(baza,hashLog,hashTok)):
        return False, ["Niepoprawne dane"]
    
    if(Bazy.rolaUzytkownika(baza,hashLog,hashTok)!="Admin"):
        return False, ["Brak uprawnień"]
    
    if(not Bazy.czyNickIstnieje(baza,nickUzytkownika)):
        return False, ["Drugi użytkownik nie istnieje"]
    
    else:
        loginUzytkownika: str = Bazy.loginUzytkownika(baza,nickUzytkownika)
        klucz: str = Bazy.kluczUzytkownika(baza,hashLog,hashTok,loginUzytkownika)
        return True, [klucz]