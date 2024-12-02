import hashlib as hash
import typing
import ManagerKodow as Kody
import ManagerKluczy as Klucze
#import KomunikacjaZBaza as Bazy
import MockTestowyKomunikacjiZBaza as Bazy


def stworzProjekt(nazwaProjektu: str, login: str, haslo: str, nick: str, kluczPub: str) -> str: #token sesji
    #login i hasło już zahashowane
    
    Bazy.stworzBaze(nazwaProjektu)
    Bazy.polaczZBaza(nazwaProjektu)
    
    token: str = Kody.wygenerujKod()
    hashTok: str = hash.sha3_512(token.encode()).hexdigest()
    Bazy.wstawUzytkownika(login,haslo,hashTok,"Właściciel zespołu",nick)
    Bazy.ustawKlucz(login,hashTok,kluczPub)
    
    kluczePokoju: typing.Tuple[str,str] = Klucze.generujKluczePokoju()
    kluczePokoju[0] = Klucze.zaszyfruj(kluczPub,kluczePokoju[0])
    kluczePokoju[1] = Klucze.zaszyfruj(kluczPub,kluczePokoju[1])
    
    Bazy.stworzPokoj(login,hashTok,nazwaProjektu)                #automatycznie stwórz pokój główny o nazwie takiej samej jak nazwa projektu
    Bazy.dodajDoPokoju(login,hashTok,nazwaProjektu,login)        #dodaj siebie (właściciela) do pokoju głównego
    Bazy.dodajKluczPokoju(login,hashTok,nazwaProjektu,kluczePokoju[0],kluczePokoju[1],login)    #dodanie do tabeli kluczy, wygenerowanych kluczy pokoju głównego zaszyfrowanych kluczm publicznym właściciela
        
    return token




def dodajZaproszenie(login: str, token: str, kodZaproszeniowy: str) -> typing.Tuple[bool, bool]: #[czy są uprawnienia, czy się udało]
    #kod zaproszeniowy już zahashowany
    hashLog: str = hash.sha3_512(login.encode()).hexdigest()
    hashTok: str = hash.sha3_512(token.encode()).hexdigest()
    
    wynik: int = Bazy.iloscUzytkownikow(login=hashLog, token=hashTok, rola="Właściciel zespołu")
    
    if(wynik!=1):
        return False, False
        
    czyKodJuzJest: bool = Bazy.czyJestKod(kodZaproszeniowy)
    
    if(czyKodJuzJest):
        return True, False
    
    else:
        Bazy.wstawKod(hashLog,hashTok,kodZaproszeniowy)
        return True, True




def usunProjekt(nazwaProjektu: str, login: str, token: str) -> bool: #czy się udało
    hashLog: str = hash.sha3_512(login.encode()).hexdigest()
    hashTok: str = hash.sha3_512(token.encode()).hexdigest()
    
    wynik: int = Bazy.iloscUzytkownikow(login=hashLog, token=hashTok, rola="Właściciel zespołu")
    
    if(wynik!=1):
        return False
        
    else:
        Bazy.rozlaczZBaza()
        Bazy.usunBaze(nazwaProjektu)
        return True


 

def pobierzKluczPublicznyUzytkownika(login: str, token: str, nickUzytkownika: str) -> typing.Tuple[bool,bool,str]: #[czy były uprawnienia, czy użytkownik istnieje, klucz]
    hashLog: str = hash.sha3_512(login.encode()).hexdigest()
    hashTok: str = hash.sha3_512(token.encode()).hexdigest()
    
    wynik: int = Bazy.iloscUzytkownikow(login=hashLog, token=hashTok, rola="Właściciel zespołu")
    
    if(wynik!=1):
        return False, False, ""
    
    wynik = Bazy.iloscUzytkownikow(nickPubliczny=nickUzytkownika)
    
    if(wynik!=1):
        return True, False, ""
    
    else:
        return True, True, Bazy.kluczUzytkownika(hashLog,hashTok,nickUzytkownika)