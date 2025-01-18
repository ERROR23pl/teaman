import hashlib as hash
import typing
import Obiekty as o
#import KomunikacjaZBaza as Bazy
import MockTestowyKomunikacjiZBaza as Bazy



def dodajDoKalendarza(login: str, token: str, nazwaPokoju: str, wpis: o.WpisKalendarza) -> typing.Tuple[bool,typing.List[str]]: #[sukces operacji, [""]]
    hashLog: str = hash.sha3_512(login.encode()).hexdigest()
    hashTok: str = hash.sha3_512(token.encode()).hexdigest()
    
    if(not Bazy.autoryzacjaTokenem(hashLog,hashTok)):
        return False, ["Niepoprawne dane"]
    
    if(Bazy.rolaUzytkownika(hashLog,hashTok)!="Admin"):
        return False, ["Brak uprawnień"]
        
    czyPokojIstnieje: bool = Bazy.czyJestPokoj(nazwaPokoju)
    
    if(not czyPokojIstnieje):
        return False, ["Pokój nie istnieje"]
    
    else:
        czyNalezyDoPokoju: bool = Bazy.czyUzytkownikJestWPokoju(nazwaPokoju,hashLog)
        if(not czyNalezyDoPokoju):
            return False, ["Użytkownik nie należy do pokoju"]
        
        else:
            if(not (Bazy.czyWpisIstnieje(nazwaPokoju,wpis))):
                Bazy.dodajWpisDoKalendarza(login,token,nazwaPokoju,wpis)
                return True, [""]
            
            else:
                return False, ["Wpis już istnieje"]



def usunZKalendarza(login: str, token: str, nazwaPokoju: str, wpis: o.WpisKalendarza) -> typing.Tuple[bool,typing.List[str]]: #[sukces operacji, [""]]
    hashLog: str = hash.sha3_512(login.encode()).hexdigest()
    hashTok: str = hash.sha3_512(token.encode()).hexdigest()
    
    if(not Bazy.autoryzacjaTokenem(hashLog,hashTok)):
        return False, ["Niepoprawne dane"]
    
    if(Bazy.rolaUzytkownika(hashLog,hashTok)!="Admin"):
        return False, ["Brak uprawnień"]
        
    czyPokojIstnieje: bool = Bazy.czyJestPokoj(nazwaPokoju)
    
    if(not czyPokojIstnieje):
        return False, ["Pokój nie istnieje"]
    
    else:
        czyNalezyDoPokoju: bool = Bazy.czyUzytkownikJestWPokoju(nazwaPokoju,hashLog)
        if(not czyNalezyDoPokoju):
            return False, ["Użytkownik nie należy do pokoju"]
        
        else:
            Bazy.usunWpisZKalendarza(login,token,nazwaPokoju,wpis)       #nawet, jeśli wpis nie nie istniał, to usunięcie zostaje uznane za udane
            return True, [""]



def modyfikujWpisKalendarza(login: str, token: str, nazwaPokoju: str, wpis: o.WpisKalendarza, noweDane: o.WpisKalendarza) -> typing.Tuple[bool,typing.List[str]]: #[sukces operacji, [""]]
    hashLog: str = hash.sha3_512(login.encode()).hexdigest()
    hashTok: str = hash.sha3_512(token.encode()).hexdigest()
    
    if(not Bazy.autoryzacjaTokenem(hashLog,hashTok)):
        return False, ["Niepoprawne dane"]
    
    if(Bazy.rolaUzytkownika(hashLog,hashTok)!="Admin"):
        return False, ["Brak uprawnień"]
        
    czyPokojIstnieje: bool = Bazy.czyJestPokoj(nazwaPokoju)
    
    if(not czyPokojIstnieje):
        return False, ["Pokój nie istnieje"]
    
    else:
        czyNalezyDoPokoju: bool = Bazy.czyUzytkownikJestWPokoju(nazwaPokoju,hashLog)
        if(not czyNalezyDoPokoju):
            return False, ["Użytkownik nie należy do pokoju"]
        
        else:
            if(not Bazy.czyWpisIstnieje(nazwaPokoju,wpis)):
                return False, ["Wpis nie istnieje"]
            
            elif(Bazy.czyWpisIstnieje(nazwaPokoju,noweDane)):
                return False, ["Nowy wpis już istnieje"]
            
            else:
                Bazy.modyfikujWpisKalendarza(login,token,nazwaPokoju,wpis,noweDane)
                return True, [""]



def pobierzKalendarz(login: str, token: str, nazwaPokoju: str) -> typing.Tuple[bool,typing.List[str]]: #[sukces operacji, kalendarz pokoju w formie listy stringów]
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
            lista: typing.List[str] = Bazy.pobierzKalendarz(login,token,nazwaPokoju)
            return True, lista