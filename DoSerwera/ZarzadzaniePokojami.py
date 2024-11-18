import typing
import hashlib as hash
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
        Bazy.dodajDoPokoju(hashLog,hashTok,nazwaPokoju,hashLog)        #dodaj siebie (właściciela) do pokoju
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



def listaPokojow(login: str, token: str) -> typing.Tuple[bool, typing.List[str]]: #[czy poprawne dane, [lista pokojów, do których się należy]]
    hashLog: str = hash.sha3_512(login.encode()).hexdigest()
    hashTok: str = hash.sha3_512(token.encode()).hexdigest()
    
    wynik: int = Bazy.iloscUzytkownikow(login=hashLog, token=hashTok)
    
    if(wynik!=1):
        return False, [""]
    
    else:
        lista: typing.List[str] = Bazy.pokojeCzlonkowskie(hashLog,hashTok)
        return True, lista