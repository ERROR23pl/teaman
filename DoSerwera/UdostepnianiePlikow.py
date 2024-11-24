import hashlib as hash
import typing
#import KomunikacjaZBaza as Bazy
import MockTestowyKomunikacjiZBaza as Bazy


def dodajPlik(login: str, token: str, nazwaPokoju: str, nazwaPliku: str, zawartoscPliku: bytes) -> typing.Tuple[bool, bool, bool]: #[czy poprawne dane, czy pokój istniał i się do niego należy, czy plik o takiej nazwie już nie istniał w pokoju]
    hashLog: str = hash.sha3_512(login.encode()).hexdigest()
    hashTok: str = hash.sha3_512(token.encode()).hexdigest()
    
    wynik: int = Bazy.iloscUzytkownikow(login=hashLog, token=hashTok)
    
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
            czyMozna: bool = not (Bazy.czyPlikIstnieje(nazwaPokoju,nazwaPliku))   #TODO
            if(czyMozna):
                Bazy.dodajPlik(login,token,nazwaPokoju,nazwaPliku,zawartoscPliku)                #TODO
            return True, True, czyMozna



def usunPlik(login: str, token: str, nazwaPokoju: str, nazwaPliku: str, zawartoscPliku: bytes) -> typing.Tuple[bool, bool, bool]: #[czy poprawne dane, czy pokój istniał i się do niego należy, czy miało się uprawnienia do usunięcia tego danego pliku (lub plik nie istniał, więc usunięcie udane z założenia)]
    hashLog: str = hash.sha3_512(login.encode()).hexdigest()
    hashTok: str = hash.sha3_512(token.encode()).hexdigest()
    
    wynik: int = Bazy.iloscUzytkownikow(login=hashLog, token=hashTok)
    
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
            czyPlikJest: bool = Bazy.czPlikIstnieje(nazwaPokoju,nazwaPliku)
            if (not czyPlikJest):
                return True, True, True         #jeśli wpis nie nie istniał, to usunięcie zostaje uznane za udane

            if (Bazy.iloscUzytkownikow(login=hashLog,token=hashTok,rola="Właściciel zespołu")==1 or Bazy.autorPliku(nazwaPokoju,nazwaPliku)==hashLog):  #TODO
                Bazy.usunPlik(nazwaPokoju,nazwaPliku)       #TODO
                return True, True, True
            
            return True, True, False




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