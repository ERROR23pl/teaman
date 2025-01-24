import hashlib as hash
import typing
import Obiekty as o
import KomunikacjaZBaza as Bazy
import Database.SQLLite as Baza


def obslugaTaskow(baza: Baza.SQLLiteDB, login: str, token: str, nazwaPokoju: str, dodawaneTaski: typing.List[o.Task], usuwaneTaski: typing.List[o.Task], zmienianeTaski: typing.List[o.Task]) -> typing.Tuple[bool, typing.List[str]]: #[sukces operacji, [""]]
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
        Bazy.dodajTaski(baza,login,nazwaPokoju,dodawaneTaski)                #dodaje bez informacji o wierzchołkach incydentnych; jeśli task o jakimś ID istniał, jest nadpisywany
        Bazy.usunTaski(baza,login,nazwaPokoju,usuwaneTaski)
        Bazy.zauktualizujWlasnosciTaskow(baza,login,nazwaPokoju,dodawaneTaski+zmienianeTaski)       #operacje niemożliwe są pomijane
        
        return True, [""]



def oznaczJakoWykonany(baza: Baza.SQLLiteDB, login: str, token: str, nazwaPokoju: str, idTaska: int) -> typing.Tuple[bool, typing.List[str]]: #[sukces operacji, [""]]
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
            czyMozna: bool = Bazy.ukonczTask(baza,login,nazwaPokoju,idTaska)
            
            if(czyMozna):
                return True, [""]
            
            else:
                return False, ["Inne taski uniemożliwiają wykonanie operacji"]



def oznaczJakoNiewykonany(baza: Baza.SQLLiteDB, login: str, token: str, nazwaPokoju: str, idTaska: int) -> typing.Tuple[bool, typing.List[str]]: #[sukces operacji, [""]]
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
            czyMozna: bool = Bazy.odznaczTaskJakoNieukonczony(baza,login,nazwaPokoju,idTaska)
            
            if(czyMozna):
                return True, [""]
            
            else:
                return False, ["Inne taski uniemożliwiają wykonanie operacji"]



def pobierzTaski(baza: Baza.SQLLiteDB, login: str, token: str, nazwaPokoju: str) -> typing.Tuple[bool, typing.List[str]]: #[sukces operacji, lista tasków pokoju w formie listy stringów]
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
            lista: typing.List[str] = Bazy.listaTaskow(baza,login,nazwaPokoju)
            return True, lista