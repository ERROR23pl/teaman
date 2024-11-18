import hashlib as hash
import typing
#import KomunikacjaZBaza as Bazy
import MockTestowyKomunikacjiZBaza as Bazy


def pobierzChat(login: str, token: str, nazwaPokoju: str) -> typing.Tuple[bool, bool, typing.List[str]]: #[czy poprawne dane, czy pokój istniał i się do niego należy, 100 ostatnich wiadomości z chatu pokoju w formie listy stringów]
    hashLog: str = hash.sha3_512(login)
    hashTok: str = hash.sha3_512(token)
    
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
            lista: typing.List[str] = Bazy.pobierzChat(login,token,nazwaPokoju)
            return True, True, lista
        


def zaktualizujChat(login: str, token: str, nazwaPokoju: str, ostatniaPosiadana: typing.Tuple[str, int]) -> typing.Tuple[bool, bool, typing.List[str]]: #[czy poprawne dane, czy pokój istniał i się do niego należy, wszystkie wiadomości od ostatnio posiadanej z chatu pokoju w formie listy stringów]
    #ostatniaPosiadana = [wysyłający,data]
    hashLog: str = hash.sha3_512(login)
    hashTok: str = hash.sha3_512(token)
    
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
            lista: typing.List[str] = Bazy.aktualizacjaChatu(login,token,nazwaPokoju,ostatniaPosiadana[0],ostatniaPosiadana[1])
            return True, True, lista



def wyslijWiadomosc(login: str, token: str, nazwaPokoju: str, ostatniaPosiadana: typing.Tuple[str, int], nowaWiadomosc: typing.Tuple[str, int]) -> typing.Tuple[bool, bool, typing.List[str]]: #[czy poprawne dane, czy pokój istniał i się do niego należy, wszystkie wiadomości od ostatnio posiadanej z chatu pokoju w formie listy stringów]
    #nowaWiadomosc = [treść,data] (wysyłający jest znany, bo login)
    hashLog: str = hash.sha3_512(login)
    hashTok: str = hash.sha3_512(token)
    
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
            Bazy.dodajWiadomosc(login,token,nazwaPokoju,nowaWiadomosc[0],nowaWiadomosc[1])                      #TODO
            lista: typing.List[str] = Bazy.aktualizacjaChatu(login,token,nazwaPokoju,ostatniaPosiadana[0],ostatniaPosiadana[1])
            return True, True, lista