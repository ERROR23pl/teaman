import hashlib as hash
import typing
#import KomunikacjaZBaza as Bazy
import MockTestowyKomunikacjiZBaza as Bazy


def dodajPlik(login: str, token: str, nazwaPokoju: str, nazwaPliku: str, zawartoscPliku: bytes) -> typing.Tuple[bool,typing.List[str]]: #[sukces operacji, [""]]
    hashLog: str = hash.sha3_512(login.encode()).hexdigest()
    hashTok: str = hash.sha3_512(token.encode()).hexdigest()
    
    if(not Bazy.autoryzacjaTokenem(hashLog,hashTok)):
        return False, ["Niepoprawne dane"]
        
    czyPokojIstnieje: bool = Bazy.czyJestPokoj(nazwaPokoju)
    
    if(not czyPokojIstnieje):
        return False, ["Pokój nie istnieje"]
    
    else:
        czyNalezyDoPokoju: bool = Bazy.czyUzytkownikJestWPokoju(nazwaPokoju,hashLog)
        if(not czyNalezyDoPokoju):
            return False, ["Użytkownik nie należy do pokoju"]
        
        else:
            czyMozna: bool = not (Bazy.czyPlikIstnieje(nazwaPokoju,nazwaPliku))
            if(czyMozna):
                Bazy.dodajPlik(login,token,nazwaPokoju,nazwaPliku,zawartoscPliku)
                return True, [""]
            return False, ["Plik już istnieje"]



def usunPlik(login: str, token: str, nazwaPokoju: str, nazwaPliku: str) -> typing.Tuple[bool,typing.List[str]]: #[sukces operacji, [""]]
    hashLog: str = hash.sha3_512(login.encode()).hexdigest()
    hashTok: str = hash.sha3_512(token.encode()).hexdigest()
    
    if(not Bazy.autoryzacjaTokenem(hashLog,hashTok)):
        return False, ["Niepoprawne dane"]
        
    czyPokojIstnieje: bool = Bazy.czyJestPokoj(nazwaPokoju)
    
    if(not czyPokojIstnieje):
        return False, ["Pokój nie istnieje"]
    
    else:
        czyNalezyDoPokoju: bool = Bazy.czyUzytkownikJestWPokoju(nazwaPokoju,hashLog)
        if(not czyNalezyDoPokoju):
            return False, ["Użytkownik nie należy do pokoju"]
        
        else:
            czyPlikJest: bool = Bazy.czyPlikIstnieje(nazwaPokoju,nazwaPliku)
            if (not czyPlikJest):
                return True, [""]         #jeśli wpis nie nie istniał, to usunięcie zostaje uznane za udane

            if (Bazy.rolaUzytkownika(login=hashLog,token=hashTok)=="Właściciel zespołu" or Bazy.autorPliku(nazwaPokoju,nazwaPliku,dana="login")==hashLog):
                Bazy.usunPlik(login,token,nazwaPokoju,nazwaPliku)
                return True, [""]
            
            return False, ["Brak uprawnień"]



def pobierzPlik(login: str, token: str, nazwaPokoju: str, nazwaPliku: str) -> typing.Tuple[bool,typing.List[str]]: #[sukces operacji, [decode zawartości pliku]]
    hashLog: str = hash.sha3_512(login.encode()).hexdigest()
    hashTok: str = hash.sha3_512(token.encode()).hexdigest()
    
    if(not Bazy.autoryzacjaTokenem(hashLog,hashTok)):
        return False, ["Niepoprawne dane"]
        
    czyPokojIstnieje: bool = Bazy.czyJestPokoj(nazwaPokoju)
    
    if(not czyPokojIstnieje):
        return False, ["Pokój nie istnieje"]
    
    else:
        czyNalezyDoPokoju: bool = Bazy.czyUzytkownikJestWPokoju(nazwaPokoju,hashLog)
        if(not czyNalezyDoPokoju):
            return False, ["Użytkownik nie należy do pokoju"]
        
        else:
            czyPlikJest: bool = Bazy.czyPlikIstnieje(nazwaPokoju,nazwaPliku)
            if (not czyPlikJest):
                return False, ["Plik nie istnieje"]
            
            zawartosc: bytes = Bazy.pobierzPlik(login,token,nazwaPokoju,nazwaPliku)
            strZawartosci: str = zawartosc.decode()
            return True, [strZawartosci]



def pobierzListePlikow(login: str, token: str, nazwaPokoju: str) -> typing.Tuple[bool,typing.List[str]]: #[sukces operacji, lista plików (nazwa, nick autora) w pokoju w formie listy stringów]
    hashLog: str = hash.sha3_512(login.encode()).hexdigest()
    hashTok: str = hash.sha3_512(token.encode()).hexdigest()
    
    if(not Bazy.autoryzacjaTokenem(hashLog,hashTok)):
        return False, ["Niepoprawne dane"]
        
    czyPokojIstnieje: bool = Bazy.czyJestPokoj(nazwaPokoju)
    
    if(not czyPokojIstnieje):
        return False, ["Pokój nie istnieje"]
    
    else:
        czyNalezyDoPokoju: bool = Bazy.czyUzytkownikJestWPokoju(nazwaPokoju,hashLog)
        if(not czyNalezyDoPokoju):
            return False, ["Użytkownik nie należy do pokoju"]
        
        else:
            lista: typing.List[str] = Bazy.listaPlikow(login,token,nazwaPokoju)
            return True, lista