import hashlib as hash
import typing
import ManagerKodow as Kody
import KomunikacjaZBaza as Bazy
import Database.SQLLite as Baza



def probaLogowania(baza: Baza.SQLLiteDB, login: str, haslo: str) -> typing.Tuple[bool,typing.List[str]]: #[sukces operacji, [token sesji, rola]]
    hashLog: str = hash.sha3_512(login.encode()).hexdigest()
    hashHas: str = hash.sha3_512(haslo.encode()).hexdigest()
    
    if(not Bazy.probaLogowania(baza,hashLog,hashHas)):
        return False, ["Niepoprawne dane"]
    
    else:
        token: str = Kody.wygenerujKod()
        hashTok: str = hash.sha3_512(token.encode()).hexdigest()
        Bazy.ustawToken(baza,hashLog,hashTok)
        rola: str = Bazy.rolaUzytkownika(baza,hashLog)
        
        return True, [token, rola]



def probaRejestracji(baza: Baza.SQLLiteDB, kodZaproszeniowy: str, hashLog: str, hashHas: str, nick: str) -> typing.Tuple[bool,typing.List[str]]: #[sukces operacji, [token sesji]]
    #login i hasło już zahashowane
    hashKod: str = hash.sha3_512(kodZaproszeniowy.encode()).hexdigest()
    
    czyKodIstnieje: bool = Bazy.czyJestKod(baza,hashKod)
    
    if(not czyKodIstnieje):
        return False, ["Niepoprawny kod"]
        
    if(Bazy.czyLoginIstnieje(baza,hashLog) or Bazy.czyNickIstnieje(baza,nick)):
        return False, ["Dane już zajęte"]
    
    else:
        token: str = Kody.wygenerujKod()
        hashTok: str = hash.sha3_512(token.encode()).hexdigest()
        Bazy.wstawUzytkownika(baza,hashLog,hashHas,hashTok,"Niezweryfikowany",nick)
        Bazy.usunKod(baza,hashKod)
        
        return True, [token]



def probaUstawieniaKluczaPublicznego(baza: Baza.SQLLiteDB, login: str, token: str, kluczPub: str) -> typing.Tuple[bool,typing.List[str]]:        #[sukces operacji, [""]]
    hashLog: str = hash.sha3_512(login.encode()).hexdigest()
    hashTok: str = hash.sha3_512(token.encode()).hexdigest()
        
    if(not Bazy.autoryzacjaTokenem(baza,hashLog,hashTok)):
        return False, ["Niepoprawne dane"]
    
    czyTakiKluczIstnieje: bool = Bazy.czyKluczIstnieje(baza,kluczPub)
    
    if(czyTakiKluczIstnieje):
        return False, ["Wyślij nowy klucz"]
    
    else:
        Bazy.ustawKlucz(baza,hashLog,kluczPub)
        return True, [""]