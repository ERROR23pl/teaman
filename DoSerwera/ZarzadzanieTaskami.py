import hashlib as hash
import typing
import Obiekty as o
#import KomunikacjaZBaza as Bazy
import MockTestowyKomunikacjiZBaza as Bazy


def obslugaTaskow(login: str, token: str, nazwaPokoju: str, dodawaneTaski: typing.List[o.Task], usuwaneTaski: typing.List[o.Task], zmienianeTaski: typing.List[o.Task]) -> typing.Tuple[bool, typing.List[str]]: #[sukces operacji, [""]]
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
        Bazy.dodajTaski(login,token,nazwaPokoju,dodawaneTaski)                #dodaje bez informacji o wierzchołkach incydentnych; jeśli task o jakimś ID istniał, jest nadpisywany
        Bazy.usunTaski(login,token,nazwaPokoju,usuwaneTaski)
        Bazy.zauktualizujWlasnosciTaskow(login,token,nazwaPokoju,dodawaneTaski+zmienianeTaski)       #operacje niemożliwe są pomijane
        
        return True, [""]



def oznaczJakoWykonany(login: str, token: str, nazwaPokoju: str, idTaska: int) -> typing.Tuple[bool, typing.List[str]]: #[sukces operacji, [""]]
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
            czyMozna: bool = Bazy.ukonczTask(login,token,nazwaPokoju,idTaska)
            
            if(czyMozna):
                return True, [""]
            
            else:
                return False, ["Inne taski uniemożliwiają wykonanie operacji"]



def oznaczJakoNiewykonany(login: str, token: str, nazwaPokoju: str, idTaska: int) -> typing.Tuple[bool, typing.List[str]]: #[sukces operacji, [""]]
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
            czyMozna: bool = Bazy.odznaczTaskJakoNieukonczony(login,token,nazwaPokoju,idTaska)
            
            if(czyMozna):
                return True, [""]
            
            else:
                return False, ["Inne taski uniemożliwiają wykonanie operacji"]



def pobierzTaski(login: str, token: str, nazwaPokoju: str) -> typing.Tuple[bool, typing.List[str]]: #[sukces operacji, lista tasków pokoju w formie listy stringów]
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
            lista: typing.List[str] = Bazy.listaTaskow(login,token,nazwaPokoju)
            return True, lista