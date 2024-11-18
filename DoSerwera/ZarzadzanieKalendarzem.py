import hashlib as hash
import typing
#import KomunikacjaZBaza as Bazy
import MockTestowyKomunikacjiZBaza as Bazy


#budowa wpisu: typing.Tuple[str,typing.Tuple[int,int,int]] -> [nazwa/opis, [data: dzień,miesiąc,rok]]


def dodajDoKalendarza(login: str, token: str, nazwaPokoju: str, wpis: typing.Tuple[str,typing.Tuple[int,int,int]]) -> typing.Tuple[bool, bool, bool]: #[czy poprawne dane i ma się uprawnienia, czy pokój istniał i się do niego należy, czy nie był kopią już istniejącego]
    hashLog: str = hash.sha3_512(login.encode()).hexdigest()
    hashTok: str = hash.sha3_512(token.encode()).hexdigest()
    
    wynik: int = Bazy.iloscUzytkownikow(login=hashLog, token=hashTok, rola="Właściciel zespołu")
    
    if(wynik!=1):
        return False, False, False
        
    czyPokojIstnieje: bool = Bazy.czyJestPokoj(nazwaPokoju)
    
    if(not czyPokojIstnieje):
        return True, False, False
    
    else:
        czyNalezyDoPokoju: bool = Bazy.czyUzytkownikJestWPokoju(nazwaPokoju,hashLog)
        if(not czyNalezyDoPokoju):
            return True, False, False
        
        else:
            czyMozna: bool = not (Bazy.czyWpisIstnieje(nazwaPokoju,wpis))
            if(czyMozna):
                Bazy.dodajWpisDoKalendarza(login,token,nazwaPokoju,wpis)
            return True, True, czyMozna



def usunZKalendarza(login: str, token: str, nazwaPokoju: str, wpis: typing.Tuple[str,typing.Tuple[int,int,int]]) -> typing.Tuple[bool, bool]: #[czy poprawne dane i ma się uprawnienia, czy pokój istniał i się do niego należy]
    hashLog: str = hash.sha3_512(login.encode()).hexdigest()
    hashTok: str = hash.sha3_512(token.encode()).hexdigest()
    
    wynik: int = Bazy.iloscUzytkownikow(login=hashLog, token=hashTok, rola="Właściciel zespołu")
    
    if(wynik!=1):
        return False, False
        
    czyPokojIstnieje: bool = Bazy.czyJestPokoj(nazwaPokoju)
    
    if(not czyPokojIstnieje):
        return True, False
    
    else:
        czyNalezyDoPokoju: bool = Bazy.czyUzytkownikJestWPokoju(nazwaPokoju,hashLog)
        if(not czyNalezyDoPokoju):
            return True, False
        
        else:
            Bazy.usunWpisZKalendarza(login,token,nazwaPokoju,wpis)       #nawet, jeśli wpis nie nie istniał, to usunięcie zostaje uznane za udane
            return True, True



def modyfikujWpisKalendarza(login: str, token: str, nazwaPokoju: str, wpis: typing.Tuple[str,typing.Tuple[int,int,int]], noweDane: typing.Tuple[str,typing.Tuple[int,int,int]]) -> typing.Tuple[bool, bool, bool]: #[czy poprawne dane i ma się uprawnienia, czy pokój istniał i się do niego należy, czy wpis istniał i czy nowa wersja nie byłaby kopią już istniejącego]
    hashLog: str = hash.sha3_512(login.encode()).hexdigest()
    hashTok: str = hash.sha3_512(token.encode()).hexdigest()
    
    wynik: int = Bazy.iloscUzytkownikow(login=hashLog, token=hashTok, rola="Właściciel zespołu")
    
    if(wynik!=1):
        return False, False, False
        
    czyPokojIstnieje: bool = Bazy.czyJestPokoj(nazwaPokoju)
    
    if(not czyPokojIstnieje):
        return True, False, False
    
    else:
        czyNalezyDoPokoju: bool = Bazy.czyUzytkownikJestWPokoju(nazwaPokoju,hashLog)
        if(not czyNalezyDoPokoju):
            return True, False, False
        
        else:
            czyMozna: bool = Bazy.czyWpisIstnieje(nazwaPokoju,wpis) and (not Bazy.czyWpisIstnieje(nazwaPokoju,noweDane))
            if(czyMozna):
                Bazy.modyfikujWpisKalendarza(login,token,nazwaPokoju,wpis,noweDane)
            return True, True, czyMozna



def pobierzKalendarz(login: str, token: str, nazwaPokoju: str) -> typing.Tuple[bool, bool, typing.List[str]]: #[czy poprawne dane, czy pokój istniał i się do niego należy, kalendarz pokoju w formie listy stringów]
    hashLog: str = hash.sha3_512(login.encode()).hexdigest()
    hashTok: str = hash.sha3_512(token.encode()).hexdigest()
    
    wynik: int = Bazy.iloscUzytkownikow(login=hashLog, token=hashTok)
    
    if(wynik!=1):
        return False, False, [""]
        
    czyPokojIstnieje: bool = Bazy.czyJestPokoj(nazwaPokoju)
    
    if(not czyPokojIstnieje):
        return True, False, [""]
    
    else:
        czyNalezyDoPokoju: bool = Bazy.czyUzytkownikJestWPokoju(nazwaPokoju,hashLog)
        if(not czyNalezyDoPokoju):
            return True, False, [""]
        
        else:
            lista: typing.List[str] = Bazy.pobierzKalendarz(login,token,nazwaPokoju)
            return True, True, lista