import typing
import hashlib as hash
import ManagerKluczy as Klucze
#import KomunikacjaZBaza as Bazy
import MockTestowyKomunikacjiZBaza as Bazy


def stworzPokoj(login: str, token: str, nazwaPokoju: str) -> typing.Tuple[bool, bool]: #[czy są uprawnienia, czy nazwa była unikalna dla projektu]
    hashLog: str = hash.sha3_512(login.encode()).hexdigest()
    hashTok: str = hash.sha3_512(token.encode()).hexdigest()
    
    wynik: int = Bazy.iloscUzytkownikow(login=hashLog, token=hashTok, rola="Właściciel zespołu")
    
    if(wynik!=1):
        return False, False
        
    czyPokojJuzJest: bool = Bazy.czyJestPokoj(nazwaPokoju)
    
    if(czyPokojJuzJest):
        return True, False
    
    else:
        Bazy.stworzPokoj(hashLog,hashTok,nazwaPokoju)
        kluczPubAdmina: str = Bazy.pobierzKluczUzytkownika(login,token)
        czyTakiKluczPokojuJuzIstnieje: bool = True
        
        while(czyTakiKluczPokojuJuzIstnieje):
            kluczePokoju: typing.Tuple[str,str] = Klucze.generujKluczePokoju()
            kluczePokoju[0] = Klucze.zaszyfruj(kluczPubAdmina,kluczePokoju[0])
            kluczePokoju[1] = Klucze.zaszyfruj(kluczPubAdmina,kluczePokoju[1])
            czyTakiKluczPokojuJuzIstnieje = Bazy.czyKluczPokojuJuzIstnieje(kluczePokoju[0],kluczePokoju[1],login)   #dwa pokoje nie mogą mieć tej samej pary kluczy (a każdy pokój ma w bazie swoje klucze zaszyfrowane przez właściciela)
        
        Bazy.dodajDoPokoju(hashLog,hashTok,nazwaPokoju,hashLog)        #dodaj siebie (właściciela) do pokoju
        Bazy.dodajKluczPokoju(login,hashTok,nazwaPokoju,kluczePokoju[0],kluczePokoju[1],login)    #dodanie do tabeli kluczy, wygenerowanych kluczy pokoju głównego zaszyfrowanych kluczm publicznym właściciela
        return True, True



def usunPokoj(login: str, token: str, nazwaPokoju: str) -> bool: #[czy były uprawnienia]
    hashLog: str = hash.sha3_512(login.encode()).hexdigest()
    hashTok: str = hash.sha3_512(token.encode()).hexdigest()
    
    wynik: int = Bazy.iloscUzytkownikow(login=hashLog, token=hashTok, rola="Właściciel zespołu")
    
    if(wynik!=1):
        return False
        
    czyPokojIstnieje: bool = Bazy.czyJestPokoj(nazwaPokoju)
    
    if(czyPokojIstnieje):                               #jeśli nie istniał, to usuwanie uznane za udane
        Bazy.usunPokoj(hashLog,hashTok,nazwaPokoju)
        
    return True



def listaPokojow(login: str, token: str) -> typing.Tuple[bool, typing.List[str]]: #[czy poprawne dane, [lista pokojów, do których się należy, postaci: nazwa, klucz pubiczny pokoju zaszyfrowany naszym kluczem publicznym, klucz rywatny pokoju zaszyfrowany naszym kluczem publicznym]]
    hashLog: str = hash.sha3_512(login.encode()).hexdigest()
    hashTok: str = hash.sha3_512(token.encode()).hexdigest()
    
    wynik: int = Bazy.iloscUzytkownikow(login=hashLog, token=hashTok)
    
    if(wynik!=1):
        return False, [""]
    
    else:
        lista: typing.List[str] = Bazy.pokojeCzlonkowskie(hashLog,hashTok)
        return True, lista