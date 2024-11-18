import hashlib as hash
import typing
import ManagerKodow as Kody
#import KomunikacjaZBaza as Bazy
import MockTestowyKomunikacjiZBaza as Bazy


def stworzProjekt(nazwaProjektu: str, login: str, haslo: str) -> str: #token sesji
    #login i hasło już zahashowane
    
    Bazy.stworzBaze(nazwaProjektu)
    
    token: str = Kody.wygenerujKod()
    hashTok: str = hash.sha3_512(token)
    Bazy.wstawUzytkownika(login,haslo,hashTok,"Właściciel zespołu")
    
    Bazy.stworzPokoj(login,hashTok,nazwaProjektu)                #automatycznie stwórz pokój główny o nazwie takiej samej jak nazwa projektu
    Bazy.dodajDoPokoju(login,hashTok,nazwaProjektu,login)        #dodaj siebie (właściciela) do pokoju głównego
        
    return token




def dodajZaproszenie(login: str, token: str, kodZaproszeniowy: str) -> typing.Tuple[bool, bool]: #[czy są uprawnienia, czy się udało]
    #kod zaproszeniowy już zahashowany
    hashLog: str = hash.sha3_512(login)
    hashTok: str = hash.sha3_512(token)
    
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
    hashLog: str = hash.sha3_512(login)
    hashTok: str = hash.sha3_512(token)
    
    wynik: int = Bazy.iloscUzytkownikow(login=hashLog, token=hashTok, rola="Właściciel zespołu")
    
    if(wynik!=1):
        return False
        
    else:
        Bazy.rozlaczZBaza()
        Bazy.usunBaze(nazwaProjektu)
        return True