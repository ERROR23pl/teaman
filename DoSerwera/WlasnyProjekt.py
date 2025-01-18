import hashlib as hash
import typing
import ManagerKodow as Kody
import ManagerKluczy as Klucze
#import KomunikacjaZBaza as Bazy
import MockTestowyKomunikacjiZBaza as Bazy


def stworzProjekt(nazwaProjektu: str, login: str, haslo: str, nick: str, kluczPub: str) -> typing.Tuple[bool,typing.List[str]]: #[sukces operacji, [token sesji]]
    #login i hasło już zahashowane
    
    Bazy.stworzBaze(nazwaProjektu)
    Bazy.polaczZBaza(nazwaProjektu)
    
    token: str = Kody.wygenerujKod()
    hashTok: str = hash.sha3_512(token.encode()).hexdigest()
    Bazy.wstawUzytkownika(login,haslo,hashTok,"Admin",nick)
    Bazy.ustawKlucz(login,hashTok,kluczPub)
    
    kluczePokoju: typing.Tuple[str,str] = Klucze.generujKluczePokoju()
    kluczePokoju[0] = Klucze.zaszyfruj(kluczPub,kluczePokoju[0])
    kluczePokoju[1] = Klucze.zaszyfruj(kluczPub,kluczePokoju[1])
    
    Bazy.stworzPokoj(login,hashTok,nazwaProjektu)                #automatycznie stwórz pokój główny o nazwie takiej samej jak nazwa projektu
    Bazy.dodajDoPokoju(login,hashTok,nazwaProjektu,login)        #dodaj siebie (właściciela) do pokoju głównego
    Bazy.dodajKluczPokoju(login,hashTok,nazwaProjektu,kluczePokoju[0],kluczePokoju[1],login)    #dodanie do tabeli kluczy, wygenerowanych kluczy pokoju głównego zaszyfrowanych kluczm publicznym właściciela
        
    return True, [token]




def dodajZaproszenie(login: str, token: str, kodZaproszeniowy: str) -> typing.Tuple[bool,typing.List[str]]: #[sukces operacji, [""]]
    #kod zaproszeniowy już zahashowany
    hashLog: str = hash.sha3_512(login.encode()).hexdigest()
    hashTok: str = hash.sha3_512(token.encode()).hexdigest()
    
    if(not Bazy.autoryzacjaTokenem(hashLog,hashTok)):
        return False, ["Niepoprawne dane"]
    
    if(Bazy.rolaUzytkownika(hashLog,hashTok)!="Admin"):
        return False, ["Brak uprawnień"]
        
    czyKodJuzJest: bool = Bazy.czyJestKod(kodZaproszeniowy)
    
    if(czyKodJuzJest):
        return False,["Wyślij nowy kod"]
    
    else:
        Bazy.wstawKod(hashLog,hashTok,kodZaproszeniowy)
        return True, [""]




def usunProjekt(nazwaProjektu: str, login: str, token: str) -> typing.Tuple[bool,typing.List[str]]: #[sukces operacji, [""]]
    hashLog: str = hash.sha3_512(login.encode()).hexdigest()
    hashTok: str = hash.sha3_512(token.encode()).hexdigest()
    
    if(not Bazy.autoryzacjaTokenem(hashLog,hashTok)):
        return False, ["Niepoprawne dane"]
    
    if(Bazy.rolaUzytkownika(hashLog,hashTok)!="Admin"):
        return False, ["Brak uprawnień"]
        
    else:
        Bazy.rozlaczZBaza()
        Bazy.usunBaze(nazwaProjektu)
        return True, [""]


 

def pobierzKluczPublicznyUzytkownika(login: str, token: str, nickUzytkownika: str) -> typing.Tuple[bool,typing.List[str]]: #[sukces operacji, [klucz]]
    hashLog: str = hash.sha3_512(login.encode()).hexdigest()
    hashTok: str = hash.sha3_512(token.encode()).hexdigest()
    
    if(not Bazy.autoryzacjaTokenem(hashLog,hashTok)):
        return False, ["Niepoprawne dane"]
    
    if(Bazy.rolaUzytkownika(hashLog,hashTok)!="Admin"):
        return False, ["Brak uprawnień"]
    
    if(not Bazy.czyNickIstnieje(nickUzytkownika)):
        return False, ["Drugi użytkownik nie istnieje"]
    
    else:
        loginUzytkownika: str = Bazy.loginUzytkownika(nickUzytkownika)
        klucz: str = Bazy.kluczUzytkownika(hashLog,hashTok,loginUzytkownika)
        return True, [klucz]