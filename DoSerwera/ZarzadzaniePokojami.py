import typing
import hashlib as hash
import ManagerKluczy as Klucze
import KomunikacjaZBaza as Bazy
import sys
sys.path.insert(1, '../Database')
import SQLLite as Baza


def stworzPokoj(baza: Baza.SQLLiteDB, login: str, token: str, nazwaPokoju: str) -> typing.Tuple[bool,typing.List[str]]: #[sukces operacji, [""]]
    hashLog: str = hash.sha3_512(login.encode()).hexdigest()
    hashTok: str = hash.sha3_512(token.encode()).hexdigest()
    
    if(not Bazy.autoryzacjaTokenem(baza,hashLog,hashTok)):
        return False, ["Niepoprawne dane"]
    
    if(Bazy.rolaUzytkownika(baza,hashLog,hashTok)!="Admin"):
        return False, ["Brak uprawnień"]
        
    czyPokojJuzJest: bool = Bazy.czyJestPokoj(baza,nazwaPokoju)
    
    if(czyPokojJuzJest):
        return False, ["Pokój już istnieje"]
    
    else:
        Bazy.stworzPokoj(baza,hashLog,hashTok,nazwaPokoju)
        kluczPubAdmina: str = Bazy.kluczUzytkownika(baza,login,token,login)
        czyTakiKluczPokojuJuzIstnieje: bool = True
        
        while(czyTakiKluczPokojuJuzIstnieje):
            kluczePokoju: typing.Tuple[str,str] = Klucze.generujKluczePokoju()
            kluczePokoju[0] = Klucze.zaszyfruj(kluczPubAdmina,kluczePokoju[0])
            kluczePokoju[1] = Klucze.zaszyfruj(kluczPubAdmina,kluczePokoju[1])
            czyTakiKluczPokojuJuzIstnieje = Bazy.czyKluczPokojuJuzIstnieje(baza,kluczePokoju[0],kluczePokoju[1],login)   #dwa pokoje nie mogą mieć tej samej pary kluczy (a każdy pokój ma w bazie swoje klucze zaszyfrowane przez właściciela)
        
        Bazy.dodajDoPokoju(baza,hashLog,hashTok,nazwaPokoju,hashLog)        #dodaj siebie (właściciela) do pokoju
        Bazy.dodajKluczPokoju(baza,login,hashTok,nazwaPokoju,kluczePokoju[0],kluczePokoju[1],login)    #dodanie do tabeli kluczy, wygenerowanych kluczy pokoju głównego zaszyfrowanych kluczm publicznym właściciela
        return True, [""]



def usunPokoj(baza: Baza.SQLLiteDB, login: str, token: str, nazwaPokoju: str) -> typing.Tuple[bool,typing.List[str]]: #[sukces operacji, [""]]
    hashLog: str = hash.sha3_512(login.encode()).hexdigest()
    hashTok: str = hash.sha3_512(token.encode()).hexdigest()
    
    if(not Bazy.autoryzacjaTokenem(baza,hashLog,hashTok)):
        return False, ["Niepoprawne dane"]
    
    if(Bazy.rolaUzytkownika(baza,hashLog,hashTok)!="Admin"):
        return False, ["Brak uprawnień"]
        
    czyPokojIstnieje: bool = Bazy.czyJestPokoj(baza,nazwaPokoju)
    
    if(czyPokojIstnieje):                               #jeśli nie istniał, to usuwanie uznane za udane
        Bazy.usunPokoj(baza,hashLog,hashTok,nazwaPokoju)
        
    return True, [""]



def listaPokojow(baza: Baza.SQLLiteDB, login: str, token: str) -> typing.Tuple[bool, typing.List[str]]: #[sukces operacji, [lista pokojów, do których się należy, postaci: [nazwa, klucz pubiczny pokoju zaszyfrowany naszym kluczem publicznym, klucz prywatny pokoju zaszyfrowany naszym kluczem publicznym]]]
    hashLog: str = hash.sha3_512(login.encode()).hexdigest()
    hashTok: str = hash.sha3_512(token.encode()).hexdigest()
    
    if(not Bazy.autoryzacjaTokenem(baza,hashLog,hashTok)):
        return False, ["Niepoprawne dane"]
    
    else:
        lista: typing.List[str] = Bazy.pokojeCzlonkowskie(baza,hashLog,hashTok)
        return True, lista