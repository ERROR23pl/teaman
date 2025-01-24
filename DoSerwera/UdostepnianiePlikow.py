import hashlib as hash
import typing
import KomunikacjaZBaza as Bazy
import Database.SQLLite as Baza


def dodajPlik(baza: Baza.SQLLiteDB, login: str, token: str, nazwaPokoju: str, nazwaPliku: str, zawartoscPliku: bytes) -> typing.Tuple[bool,typing.List[str]]: #[sukces operacji, [""]]
    hashLog: str = hash.sha3_512(login.encode()).hexdigest()
    hashTok: str = hash.sha3_512(token.encode()).hexdigest()
    
    if(not Bazy.autoryzacjaTokenem(baza,hashLog,hashTok)):
        return False, ["Niepoprawne dane"]
        
    czyPokojIstnieje: bool = Bazy.czyJestPokoj(baza,nazwaPokoju)
    
    if(not czyPokojIstnieje):
        return False, ["Pokój nie istnieje"]
    
    else:
        czyNalezyDoPokoju: bool = Bazy.czyUzytkownikJestWPokoju(baza,nazwaPokoju,hashLog)
        if(not czyNalezyDoPokoju):
            return False, ["Użytkownik nie należy do pokoju"]
        
        else:
            czyMozna: bool = not (Bazy.czyPlikIstnieje(baza,nazwaPokoju,nazwaPliku))
            if(czyMozna):
                Bazy.dodajPlik(baza,login,nazwaPokoju,nazwaPliku,zawartoscPliku)
                return True, [""]
            return False, ["Plik już istnieje"]



def usunPlik(baza: Baza.SQLLiteDB, login: str, token: str, nazwaPokoju: str, nazwaPliku: str) -> typing.Tuple[bool,typing.List[str]]: #[sukces operacji, [""]]
    hashLog: str = hash.sha3_512(login.encode()).hexdigest()
    hashTok: str = hash.sha3_512(token.encode()).hexdigest()
    
    if(not Bazy.autoryzacjaTokenem(baza,hashLog,hashTok)):
        return False, ["Niepoprawne dane"]
        
    czyPokojIstnieje: bool = Bazy.czyJestPokoj(baza,nazwaPokoju)
    
    if(not czyPokojIstnieje):
        return False, ["Pokój nie istnieje"]
    
    else:
        czyNalezyDoPokoju: bool = Bazy.czyUzytkownikJestWPokoju(baza,nazwaPokoju,hashLog)
        if(not czyNalezyDoPokoju):
            return False, ["Użytkownik nie należy do pokoju"]
        
        else:
            czyPlikJest: bool = Bazy.czyPlikIstnieje(baza,nazwaPokoju,nazwaPliku)
            if (not czyPlikJest):
                return True, [""]         #jeśli wpis nie nie istniał, to usunięcie zostaje uznane za udane

            if (Bazy.rolaUzytkownika(baza,hashLog)=="Admin" or Bazy.autorPliku(baza,nazwaPokoju,nazwaPliku,dana="login")==hashLog):
                Bazy.usunPlik(baza,login,nazwaPokoju,nazwaPliku)
                return True, [""]
            
            return False, ["Brak uprawnień"]



def pobierzPlik(baza: Baza.SQLLiteDB, login: str, token: str, nazwaPokoju: str, nazwaPliku: str) -> typing.Tuple[bool,typing.List[str]]: #[sukces operacji, [decode zawartości pliku]]
    hashLog: str = hash.sha3_512(login.encode()).hexdigest()
    hashTok: str = hash.sha3_512(token.encode()).hexdigest()
    
    if(not Bazy.autoryzacjaTokenem(baza,hashLog,hashTok)):
        return False, ["Niepoprawne dane"]
        
    czyPokojIstnieje: bool = Bazy.czyJestPokoj(baza,nazwaPokoju)
    
    if(not czyPokojIstnieje):
        return False, ["Pokój nie istnieje"]
    
    else:
        czyNalezyDoPokoju: bool = Bazy.czyUzytkownikJestWPokoju(baza,nazwaPokoju,hashLog)
        if(not czyNalezyDoPokoju):
            return False, ["Użytkownik nie należy do pokoju"]
        
        else:
            czyPlikJest: bool = Bazy.czyPlikIstnieje(baza,nazwaPokoju,nazwaPliku)
            if (not czyPlikJest):
                return False, ["Plik nie istnieje"]
            
            zawartosc: bytes = Bazy.pobierzPlik(baza,login,nazwaPokoju,nazwaPliku)
            strZawartosci: str = zawartosc.decode()
            return True, [strZawartosci]



def pobierzListePlikow(baza: Baza.SQLLiteDB, login: str, token: str, nazwaPokoju: str) -> typing.Tuple[bool,typing.List[str]]: #[sukces operacji, lista plików (nazwa, nick autora) w pokoju w formie listy stringów]
    hashLog: str = hash.sha3_512(login.encode()).hexdigest()
    hashTok: str = hash.sha3_512(token.encode()).hexdigest()
    
    if(not Bazy.autoryzacjaTokenem(baza,hashLog,hashTok)):
        return False, ["Niepoprawne dane"]
        
    czyPokojIstnieje: bool = Bazy.czyJestPokoj(baza,nazwaPokoju)
    
    if(not czyPokojIstnieje):
        return False, ["Pokój nie istnieje"]
    
    else:
        czyNalezyDoPokoju: bool = Bazy.czyUzytkownikJestWPokoju(baza,nazwaPokoju,hashLog)
        if(not czyNalezyDoPokoju):
            return False, ["Użytkownik nie należy do pokoju"]
        
        else:
            lista: typing.List[str] = Bazy.listaPlikow(baza,login,nazwaPokoju)
            return True, lista