import hashlib as hash
import typing
import Obiekty as o
import KomunikacjaZBaza as Bazy
import SQLLite as Baza



def dodajDoKalendarza(baza: Baza.SQLLiteDB, login: str, token: str, nazwaPokoju: str, wpis: o.WpisKalendarza) -> typing.Tuple[bool,typing.List[str]]: #[sukces operacji, [""]]
    hashLog: str = hash.sha3_512(login.encode()).hexdigest()
    hashTok: str = hash.sha3_512(token.encode()).hexdigest()
    
    if(not Bazy.autoryzacjaTokenem(baza,hashLog,hashTok)):
        return False, ["Niepoprawne dane"]
    
    if(Bazy.rolaUzytkownika(baza,hashLog)!="Admin"):
        return False, ["Brak uprawnień"]
        
    czyPokojIstnieje: bool = Bazy.czyJestPokoj(baza,nazwaPokoju)
    
    if(not czyPokojIstnieje):
        return False, ["Pokój nie istnieje"]
    
    else:
        czyNalezyDoPokoju: bool = Bazy.czyUzytkownikJestWPokoju(baza,nazwaPokoju,hashLog)
        if(not czyNalezyDoPokoju):
            return False, ["Użytkownik nie należy do pokoju"]
        
        else:
            if(not (Bazy.czyWpisIstnieje(baza,nazwaPokoju,wpis))):
                Bazy.dodajWpisDoKalendarza(baza,hashLog,nazwaPokoju,wpis)
                return True, [""]
            
            else:
                return False, ["Wpis już istnieje"]



def usunZKalendarza(baza: Baza.SQLLiteDB, login: str, token: str, nazwaPokoju: str, wpis: o.WpisKalendarza) -> typing.Tuple[bool,typing.List[str]]: #[sukces operacji, [""]]
    hashLog: str = hash.sha3_512(login.encode()).hexdigest()
    hashTok: str = hash.sha3_512(token.encode()).hexdigest()
    
    if(not Bazy.autoryzacjaTokenem(baza,hashLog,hashTok)):
        return False, ["Niepoprawne dane"]
    
    if(Bazy.rolaUzytkownika(baza,hashLog)!="Admin"):
        return False, ["Brak uprawnień"]
        
    czyPokojIstnieje: bool = Bazy.czyJestPokoj(baza,nazwaPokoju)
    
    if(not czyPokojIstnieje):
        return False, ["Pokój nie istnieje"]
    
    else:
        czyNalezyDoPokoju: bool = Bazy.czyUzytkownikJestWPokoju(baza,nazwaPokoju,hashLog)
        if(not czyNalezyDoPokoju):
            return False, ["Użytkownik nie należy do pokoju"]
        
        else:
            Bazy.usunWpisZKalendarza(baza,hashLog,nazwaPokoju,wpis)       #nawet, jeśli wpis nie nie istniał, to usunięcie zostaje uznane za udane
            return True, [""]



def modyfikujWpisKalendarza(baza: Baza.SQLLiteDB, login: str, token: str, nazwaPokoju: str, wpis: o.WpisKalendarza, noweDane: o.WpisKalendarza) -> typing.Tuple[bool,typing.List[str]]: #[sukces operacji, [""]]
    hashLog: str = hash.sha3_512(login.encode()).hexdigest()
    hashTok: str = hash.sha3_512(token.encode()).hexdigest()
    
    if(not Bazy.autoryzacjaTokenem(baza,hashLog,hashTok)):
        return False, ["Niepoprawne dane"]
    
    if(Bazy.rolaUzytkownika(baza,hashLog)!="Admin"):
        return False, ["Brak uprawnień"]
        
    czyPokojIstnieje: bool = Bazy.czyJestPokoj(baza,nazwaPokoju)
    
    if(not czyPokojIstnieje):
        return False, ["Pokój nie istnieje"]
    
    else:
        czyNalezyDoPokoju: bool = Bazy.czyUzytkownikJestWPokoju(baza,nazwaPokoju,hashLog)
        if(not czyNalezyDoPokoju):
            return False, ["Użytkownik nie należy do pokoju"]
        
        else:
            if(not Bazy.czyWpisIstnieje(baza,nazwaPokoju,wpis)):
                return False, ["Wpis nie istnieje"]
            
            elif(Bazy.czyWpisIstnieje(baza,nazwaPokoju,noweDane)):
                return False, ["Nowy wpis już istnieje"]
            
            else:
                Bazy.modyfikujWpisKalendarza(baza,hashLog,nazwaPokoju,wpis,noweDane)
                return True, [""]



def pobierzKalendarz(baza: Baza.SQLLiteDB, login: str, token: str, nazwaPokoju: str) -> typing.Tuple[bool,typing.List[str]]: #[sukces operacji, kalendarz pokoju w formie listy stringów]
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
            lista: typing.List[str] = Bazy.pobierzKalendarz(baza,hashLog,nazwaPokoju)
            return True, lista