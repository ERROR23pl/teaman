import hashlib as hash
import typing
import Obiekty as o
import KomunikacjaZBaza as Bazy
import SQLLite as Baza


def pobierzChat(baza: Baza.SQLLiteDB, login: str, token: str, nazwaPokoju: str) -> typing.Tuple[bool,typing.List[str]]: #[sukces operacji, 100 ostatnich wiadomości z chatu pokoju w formie listy stringów]
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
            lista: typing.List[str] = Bazy.pobierzChat(baza,hashLog,nazwaPokoju)
            return True, lista
        


def zaktualizujChat(baza: Baza.SQLLiteDB, login: str, token: str, nazwaPokoju: str, ostatniaPosiadana: o.Wiadomosc) -> typing.Tuple[bool,typing.List[str]]: #[sukces operacji, wszystkie wiadomości od ostatnio posiadanej z chatu pokoju w formie listy stringów]
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
            lista: typing.List[str] = Bazy.aktualizacjaChatu(baza,hashLog,nazwaPokoju,ostatniaPosiadana.autor,ostatniaPosiadana.data)
            return True, lista



def wyslijWiadomosc(baza: Baza.SQLLiteDB, login: str, token: str, nazwaPokoju: str, ostatniaPosiadana: o.Wiadomosc, nowaWiadomosc: o.Wiadomosc) -> typing.Tuple[bool,typing.List[str]]: #[sukces operacji, wszystkie wiadomości od ostatnio posiadanej z chatu pokoju w formie listy stringów]
    #nowaWiadomosc = [treść,data] (wysyłający jest znany, bo login)
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
            Bazy.dodajWiadomosc(baza,hashLog,nazwaPokoju,nowaWiadomosc.tresc)
            if(ostatniaPosiadana.data==0 and ostatniaPosiadana.autor==""):
                Bazy.pobierzChat(baza,hashLog,nazwaPokoju)
            else:
                lista: typing.List[str] = Bazy.aktualizacjaChatu(baza,hashLog,nazwaPokoju,ostatniaPosiadana.autor,ostatniaPosiadana.data)
            return True, lista