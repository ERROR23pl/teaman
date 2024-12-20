import hashlib as hash
import typing
#import KomunikacjaZBaza as Bazy
import MockTestowyKomunikacjiZBaza as Bazy

def zweryfikuj(login: str, token: str, nickWeryfikowanego: str, nowaRola: str, nazwaProjektu: str, kluczePokojuGlownegoZaszyfrowaneKluczemWeryfikowanego: typing.Tuple[str,str]) -> typing.Tuple[bool,typing.List[str]]:   #[sukces operacji, [""]]
    hashLog: str = hash.sha3_512(login.encode()).hexdigest()
    hashTok: str = hash.sha3_512(token.encode()).hexdigest()
    
    wynik: int = Bazy.iloscUzytkownikow(login=hashLog, token=hashTok)
    
    if(wynik!=1):
        return False, ["Niepoprawne dane"]
    
    if(Bazy.rolaUzytkownika(hashLog,hashTok)!="Właściciel"):
        return False, ["Brak uprawnień"]
    
    if(nowaRola=="Właściciel" or nowaRola=="Niezweryfikowany"):
        return False, ["Nie można ustawić roli "+nowaRola]
    
    if(Bazy.iloscUzytkownikow(nickPubliczny=nickWeryfikowanego)!=1):
        return False, ["Drugi użytkownik nie istnieje"]
    
    loginWeryfikowanego: str = Bazy.loginUzytkownika(nickWeryfikowanego)
    if(Bazy.czyZweryfikowany(loginWeryfikowanego)):
        return False, ["Drugi użytkownik już zweryfikowany"]
    
    else:
        Bazy.ustawRole(hashLog,hashTok,loginWeryfikowanego,nowaRola)
        Bazy.dodajDoPokoju(hashLog,hashTok,nazwaProjektu,loginWeryfikowanego)        #dodaj zweryfikowanego użytkownika do pokoju głównego
        Bazy.dodajKluczPokoju(login,hashTok,nazwaProjektu,kluczePokojuGlownegoZaszyfrowaneKluczemWeryfikowanego[0],kluczePokojuGlownegoZaszyfrowaneKluczemWeryfikowanego[1],loginWeryfikowanego)    #dodanie do tabeli kluczy, wygenerowanych kluczy pokoju głównego zaszyfrowanych kluczm publicznym zweryfikowanego użytkownika
        return True, [""]


def listaNiezweryfikowanych(login: str, token: str) -> typing.Tuple[bool,typing.List[str]]: #[sukces operacji, lista nicków niezweryfikowanych użytkowników]
    hashLog: str = hash.sha3_512(login.encode()).hexdigest()
    hashTok: str = hash.sha3_512(token.encode()).hexdigest()
    
    wynik: int = Bazy.iloscUzytkownikow(login=hashLog, token=hashTok)
    
    if(wynik!=1):
        return False, ["Niepoprawne dane"]
    
    if(Bazy.rolaUzytkownika(hashLog,hashTok)!="Właściciel"):
        return False, ["Brak uprawnień"]
    
    lista = Bazy.listaNiezweryfikowanych(hashLog,hashTok)
    return True, lista


def ustawRole(login: str, token: str, nick: str, nowaRola: str) -> typing.Tuple[bool,typing.List[str]]: #[sukces operacji, [""]]
    hashLog: str = hash.sha3_512(login.encode()).hexdigest()
    hashTok: str = hash.sha3_512(token.encode()).hexdigest()
    
    wynik: int = Bazy.iloscUzytkownikow(login=hashLog, token=hashTok)
    
    if(wynik!=1):
        return False, ["Niepoprawne dane"]
    
    if(Bazy.rolaUzytkownika(hashLog,hashTok)!="Właściciel"):
        return False, ["Brak uprawnień"]
    
    if(nowaRola=="Właściciel" or nowaRola=="Niezweryfikowany"):
        return False, ["Nie można ustawić roli "+nowaRola]
    
    if(Bazy.iloscUzytkownikow(nickPubliczny=nick)!=1):
        return False, ["Drugi użytkownik nie istnieje"]
    
    loginEdytowanego: str = Bazy.loginUzytkownika(nick)
    if(not Bazy.czyZweryfikowany(loginEdytowanego)):
        return False, ["Drugi użytkownik niezweryfikowany"]
    
    else:
        Bazy.ustawRole(hashLog,hashTok,loginEdytowanego,nowaRola)
        return True, [""]