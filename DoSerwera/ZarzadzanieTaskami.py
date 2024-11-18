import hashlib as hash
import typing
#import KomunikacjaZBaza as Bazy
import MockTestowyKomunikacjiZBaza as Bazy


#budowa taska: typing.Tuple[int,str,typing.Tuple[int,int,int],typing.Tuple[float,float],typing.List[int]] -> [id, nazwa, [data wymaganego końca: dzień,miesiąc,rok], [koordynaty wizualne: x,y], [lista id tasków, od których zależny]]


def obslugaTaskow(login: str, token: str, nazwaPokoju: str, listaTaskow: typing.List[typing.List[typing.Tuple[int,str,typing.Tuple[int,int,int],typing.Tuple[float,float],typing.List[int]]]]) -> typing.Tuple[bool, bool]: #[czy są uprawnienia, czy pokój istniał i się udało]
    hashLog: str = hash.sha3_512(login.encode()).hexdigest()
    hashTok: str = hash.sha3_512(token.encode()).hexdigest()
    
    wynik: int = Bazy.iloscUzytkownikow(login=hashLog, token=hashTok, rola="Właściciel zespołu")
    
    if(wynik!=1):
        return False, False
        
    czyPokojIstnieje: bool = Bazy.czyJestPokoj(nazwaPokoju)
    
    if(not czyPokojIstnieje):
        return True, False
    
    else:
        #listaTaskow=[taski dodane, taski usunięte, taski zmodyfikowane]
        Bazy.dodajTaski(login,token,nazwaPokoju,listaTaskow[0])                #dodaje bez informacji o wierzchołkach incydentnych; jeśli task o jakimś ID istniał, jest nadpisywany
        Bazy.usunTaski(login,token,nazwaPokoju,listaTaskow[1])
        Bazy.zauktualizujWlasnosciTaskow(login,token,nazwaPokoju,listaTaskow[0]+listaTaskow[2])       #operacje niemożliwe są pomijane
        
        return True, True



def oznaczJakoWykonany(login: str, token: str, nazwaPokoju: str, idTaska: int) -> typing.Tuple[bool, bool, bool]: #[czy poprawne dane, czy pokój istniał i się do niego należy, czy inne taski nie blokują]
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
            czyMozna: bool = Bazy.ukonczTask(login,token,nazwaPokoju,idTaska)
            return True, True, czyMozna



def oznaczJakoNiewykonany(login: str, token: str, nazwaPokoju: str, idTaska: int) -> typing.Tuple[bool, bool, bool]: #[czy poprawne dane, czy pokój istniał i się do niego należy, czy inne taski nie blokują]
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
            czyMozna: bool = Bazy.odznaczTaskJakoNieukonczony(login,token,nazwaPokoju,idTaska)
            return True, True, czyMozna



def pobierzTaski(login: str, token: str, nazwaPokoju: str) -> typing.Tuple[bool, bool, typing.List[str]]: #[czy poprawne dane, czy pokój istniał i się do niego należy, lista tasków pokoju w formie listy stringów]
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
            lista: typing.List[str] = Bazy.listaTaskow(login,token,nazwaPokoju)
            return True, True, lista