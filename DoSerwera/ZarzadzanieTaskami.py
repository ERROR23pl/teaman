import hashlib as hash
import typing
#import KomunikacjaZBaza as Bazy
import MockTestowyKomunikacjiZBaza as Bazy


#budowa taska: typing.Tuple[int,str,typing.Tuple[int,int,int],typing.Tuple[float,float],typing.List[int]] -> [id, nazwa, [data wymaganego końca: dzień,miesiąc,rok], [koordynaty wizualne: x,y], [lista id tasków, od których zależny]]


def obslugaTaskow(login: str, token: str, nazwaPokoju: str, listaTaskow: typing.List[typing.List[typing.Tuple[int,str,typing.Tuple[int,int,int],typing.Tuple[float,float],typing.List[int]]]]) -> typing.Tuple[bool, typing.List[str]]: #[sukces operacji, [""]]
    hashLog: str = hash.sha3_512(login.encode()).hexdigest()
    hashTok: str = hash.sha3_512(token.encode()).hexdigest()
    
    wynik: int = Bazy.iloscUzytkownikow(login=hashLog, token=hashTok)
    
    if(wynik!=1):
        return False, ["Niepoprawne dane"]
    
    if(Bazy.rolaUzytkownika(hashLog,hashTok)!="Właściciel zespołu"):
        return False, ["Brak uprawnień"]
        
    czyPokojIstnieje: bool = Bazy.czyJestPokoj(nazwaPokoju)
    
    if(not czyPokojIstnieje):
        return False, ["Pokój nie istnieje"]
    
    else:
        #listaTaskow=[taski dodane, taski usunięte, taski zmodyfikowane]
        Bazy.dodajTaski(login,token,nazwaPokoju,listaTaskow[0])                #dodaje bez informacji o wierzchołkach incydentnych; jeśli task o jakimś ID istniał, jest nadpisywany
        Bazy.usunTaski(login,token,nazwaPokoju,listaTaskow[1])
        Bazy.zauktualizujWlasnosciTaskow(login,token,nazwaPokoju,listaTaskow[0]+listaTaskow[2])       #operacje niemożliwe są pomijane
        
        return True, [""]



def oznaczJakoWykonany(login: str, token: str, nazwaPokoju: str, idTaska: int) -> typing.Tuple[bool, typing.List[str]]: #[sukces operacji, [""]]
    hashLog: str = hash.sha3_512(login.encode()).hexdigest()
    hashTok: str = hash.sha3_512(token.encode()).hexdigest()
    
    wynik: int = Bazy.iloscUzytkownikow(login=hashLog, token=hashTok)
    
    if(wynik!=1):
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
    
    wynik: int = Bazy.iloscUzytkownikow(login=hashLog, token=hashTok)
    
    if(wynik!=1):
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
    
    wynik: int = Bazy.iloscUzytkownikow(login=hashLog, token=hashTok)
    
    if(wynik!=1):
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