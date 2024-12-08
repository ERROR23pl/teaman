import hashlib as hash
import typing
#import KomunikacjaZBaza as Bazy
import MockTestowyKomunikacjiZBaza as Bazy


def pobierzChat(login: str, token: str, nazwaPokoju: str) -> typing.Tuple[bool,typing.List[str]]: #[sukces operacji, 100 ostatnich wiadomości z chatu pokoju w formie listy stringów]
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
            lista: typing.List[str] = Bazy.pobierzChat(login,token,nazwaPokoju)
            return True, lista
        


def zaktualizujChat(login: str, token: str, nazwaPokoju: str, ostatniaPosiadana: typing.Tuple[str, int]) -> typing.Tuple[bool,typing.List[str]]: #[sukces operacji, wszystkie wiadomości od ostatnio posiadanej z chatu pokoju w formie listy stringów]
    #ostatniaPosiadana = [wysyłający,data]
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
            lista: typing.List[str] = Bazy.aktualizacjaChatu(login,token,nazwaPokoju,ostatniaPosiadana[0],ostatniaPosiadana[1])
            return True, lista



def wyslijWiadomosc(login: str, token: str, nazwaPokoju: str, ostatniaPosiadana: typing.Tuple[str, int], nowaWiadomosc: typing.Tuple[str, int]) -> typing.Tuple[bool,typing.List[str]]: #[sukces operacji, wszystkie wiadomości od ostatnio posiadanej z chatu pokoju w formie listy stringów]
    #nowaWiadomosc = [treść,data] (wysyłający jest znany, bo login)
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
            Bazy.dodajWiadomosc(login,token,nazwaPokoju,nowaWiadomosc[0],nowaWiadomosc[1])
            lista: typing.List[str] = Bazy.aktualizacjaChatu(login,token,nazwaPokoju,ostatniaPosiadana[0],ostatniaPosiadana[1])
            return True, lista