import hashlib as hash
import typing
import KomunikacjaZBaza as Bazy
import sys
sys.path.insert(1, '../Database')
import SQLLite as Baza


def zweryfikuj(baza: Baza.SQLLiteDB, login: str, token: str, nickWeryfikowanego: str, nowaRola: str, nazwaProjektu: str, kluczePokojuGlownegoZaszyfrowaneKluczemWeryfikowanego: typing.Tuple[str,str]) -> typing.Tuple[bool,typing.List[str]]:   #[sukces operacji, [""]]
    hashLog: str = hash.sha3_512(login.encode()).hexdigest()
    hashTok: str = hash.sha3_512(token.encode()).hexdigest()
    
    if(not Bazy.autoryzacjaTokenem(baza,hashLog,hashTok)):
        return False, ["Niepoprawne dane"]
    
    if(Bazy.rolaUzytkownika(baza,hashLog,hashTok)!="Admin"):
        return False, ["Brak uprawnień"]
    
    if(nowaRola=="Admin" or nowaRola=="Niezweryfikowany"):
        return False, ["Nie można ustawić takiej roli"]
    
    if(not Bazy.czyNickIstnieje(baza,nickWeryfikowanego)):
        return False, ["Drugi użytkownik nie istnieje"]
    
    loginWeryfikowanego: str = Bazy.loginUzytkownika(baza,nickWeryfikowanego)
    if(Bazy.czyZweryfikowany(baza,loginWeryfikowanego)):
        return False, ["Drugi użytkownik już zweryfikowany"]
    
    else:
        Bazy.ustawRole(baza,hashLog,hashTok,loginWeryfikowanego,nowaRola)
        Bazy.dodajDoPokoju(baza,hashLog,hashTok,nazwaProjektu,loginWeryfikowanego)        #dodaj zweryfikowanego użytkownika do pokoju głównego
        Bazy.dodajKluczPokoju(baza,login,hashTok,nazwaProjektu,kluczePokojuGlownegoZaszyfrowaneKluczemWeryfikowanego[0],kluczePokojuGlownegoZaszyfrowaneKluczemWeryfikowanego[1],loginWeryfikowanego)    #dodanie do tabeli kluczy, wygenerowanych kluczy pokoju głównego zaszyfrowanych kluczm publicznym zweryfikowanego użytkownika
        return True, [""]


def listaNiezweryfikowanych(baza: Baza.SQLLiteDB, login: str, token: str) -> typing.Tuple[bool,typing.List[str]]: #[sukces operacji, lista nicków niezweryfikowanych użytkowników]
    hashLog: str = hash.sha3_512(login.encode()).hexdigest()
    hashTok: str = hash.sha3_512(token.encode()).hexdigest()
    
    if(not Bazy.autoryzacjaTokenem(baza,hashLog,hashTok)):
        return False, ["Niepoprawne dane"]
    
    if(Bazy.rolaUzytkownika(baza,hashLog,hashTok)!="Admin"):
        return False, ["Brak uprawnień"]
    
    lista = Bazy.listaNiezweryfikowanych(baza,hashLog,hashTok)
    return True, lista


def ustawRole(baza: Baza.SQLLiteDB, login: str, token: str, nick: str, nowaRola: str) -> typing.Tuple[bool,typing.List[str]]: #[sukces operacji, [""]]
    hashLog: str = hash.sha3_512(login.encode()).hexdigest()
    hashTok: str = hash.sha3_512(token.encode()).hexdigest()
    
    if(not Bazy.autoryzacjaTokenem(baza,hashLog,hashTok)):
        return False, ["Niepoprawne dane"]
    
    if(Bazy.rolaUzytkownika(baza,hashLog,hashTok)!="Admin"):
        return False, ["Brak uprawnień"]
    
    if(nowaRola=="Admin" or nowaRola=="Niezweryfikowany"):
        return False, ["Nie można ustawić takiej roli"]
    
    if(not Bazy.czyNickIstnieje(baza,nick)):
        return False, ["Drugi użytkownik nie istnieje"]
    
    loginEdytowanego: str = Bazy.loginUzytkownika(baza,nick)
    if(not Bazy.czyZweryfikowany(baza,loginEdytowanego)):
        return False, ["Drugi użytkownik niezweryfikowany"]
    
    if(loginEdytowanego==hashLog):
        return False,["Nie można zmienić roli właściciela"]
    
    else:
        Bazy.ustawRole(baza,hashLog,hashTok,loginEdytowanego,nowaRola)
        return True, [""]