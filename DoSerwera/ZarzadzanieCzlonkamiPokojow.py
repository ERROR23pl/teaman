import typing
import hashlib as hash
import KomunikacjaZBaza as Bazy
    
    
def dodajDoPokoju(login: str, token: str, nazwaPokoju: str, dodawanaOsoba: str) -> typing.Tuple[bool, bool, bool]: #[czy są uprawnienia, czy pokój istniał, czy się udało]
    hashLog: str = hash.sha3_512(login)
    hashTok: str = hash.sha3_512(token)
    
    wynik: int = Bazy.iloscUzytkownikow(login=hashLog, token=hashTok, rola="Właściciel zespołu")
    
    if(wynik!=1):
        return False, False, False
        
    czyPokojIstnieje: bool = Bazy.czyJestPokoj(nazwaPokoju)
    
    if(not czyPokojIstnieje):
        return True, False, False
    
    else:
        hashDod: str = hash.sha3_512(dodawanaOsoba)
        czyMoznaDodac: bool = ((Bazy.iloscUzytkownikow(login=hashLog)>0) and (not Bazy.czyUzytkownikJestWPokoju(nazwaPokoju,hashDod)))   #TODO  #użytkownik istnieje w projekcie, ale nie ma go w pokoju

        if(not czyMoznaDodac):
            return True,True,False
        else:        
            Bazy.dodajDoPokoju(nazwaPokoju,hashDod) 
            return True, True, True



def usunZPokoju(login: str, token: str, nazwaPokoju: str, usuwanaOsoba: str) -> typing.Tuple[bool, bool]: #[czy są uprawnienia, czy pokój istniał i się udało]
    hashLog: str = hash.sha3_512(login)
    hashTok: str = hash.sha3_512(token)
    
    wynik: int = Bazy.iloscUzytkownikow(login=hashLog, token=hashTok, rola="Właściciel zespołu")
    
    if(wynik!=1):
        return False, False
        
    czyPokojIstnieje: bool = Bazy.czyJestPokoj(nazwaPokoju)
    
    if(not czyPokojIstnieje):
        return True, False
    
    else:
        hashUs: str = hash.sha3_512(usuwanaOsoba)
        
        Bazy.usunZPokoju(nazwaPokoju,hashUs)    #TODO   #nawet, gdyby takiej osoby nie było, to i tak efekt usunięcia jest ten sam, więc nie jest testowane 
        return True, True