import typing
import hashlib as hash
import ManagerKluczy as Klucze
#import KomunikacjaZBaza as Bazy
import MockTestowyKomunikacjiZBaza as Bazy


def stworzPokoj(login: str, token: str, nazwaPokoju: str) -> typing.Tuple[bool,typing.List[str]]: #[sukces operacji, [""]]
    hashLog: str = hash.sha3_512(login.encode()).hexdigest()
    hashTok: str = hash.sha3_512(token.encode()).hexdigest()
    
    wynik: int = Bazy.iloscUzytkownikow(login=hashLog, token=hashTok)
    
    if(wynik!=1):
        return False, ["Niepoprawne dane"]
    
    if(Bazy.rolaUzytkownika(hashLog,hashTok)!="Właściciel"):
        return False, ["Brak uprawnień"]
        
    czyPokojJuzJest: bool = Bazy.czyJestPokoj(nazwaPokoju)
    
    if(czyPokojJuzJest):
        return False, ["Pokój już istnieje"]
    
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
        return True, [""]



def usunPokoj(login: str, token: str, nazwaPokoju: str) -> typing.Tuple[bool,typing.List[str]]: #[sukces operacji, [""]]
    hashLog: str = hash.sha3_512(login.encode()).hexdigest()
    hashTok: str = hash.sha3_512(token.encode()).hexdigest()
    
    wynik: int = Bazy.iloscUzytkownikow(login=hashLog, token=hashTok)
    
    if(wynik!=1):
        return False, ["Niepoprawne dane"]
    
    if(Bazy.rolaUzytkownika(hashLog,hashTok)!="Właściciel"):
        return False, ["Brak uprawnień"]
        
    czyPokojIstnieje: bool = Bazy.czyJestPokoj(nazwaPokoju)
    
    if(czyPokojIstnieje):                               #jeśli nie istniał, to usuwanie uznane za udane
        Bazy.usunPokoj(hashLog,hashTok,nazwaPokoju)
        
    return True, [""]



def listaPokojow(login: str, token: str) -> typing.Tuple[bool, typing.List[str]]: #[sukces operacji, [lista pokojów, do których się należy, postaci: nazwa, klucz pubiczny pokoju zaszyfrowany naszym kluczem publicznym, klucz rywatny pokoju zaszyfrowany naszym kluczem publicznym]]
    hashLog: str = hash.sha3_512(login.encode()).hexdigest()
    hashTok: str = hash.sha3_512(token.encode()).hexdigest()
    
    wynik: int = Bazy.iloscUzytkownikow(login=hashLog, token=hashTok)
    
    if(wynik!=1):
        return False, ["Niepoprawne dane"]
    
    else:
        lista: typing.List[str] = Bazy.pokojeCzlonkowskie(hashLog,hashTok)
        return True, lista