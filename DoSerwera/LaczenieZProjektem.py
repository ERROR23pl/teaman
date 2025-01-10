import hashlib as hash
import typing
import ManagerKodow as Kody
#import KomunikacjaZBaza as Bazy
import MockTestowyKomunikacjiZBaza as Bazy



def probaLogowania(login: str, haslo: str) -> typing.Tuple[bool,typing.List[str]]: #[sukces operacji, [token sesji, rola]]
    hashLog: str = hash.sha3_512(login.encode()).hexdigest()
    hashHas: str = hash.sha3_512(haslo.encode()).hexdigest()
    
    if(not Bazy.probaLogowania(hashLog,hashHas)):
        return False, ["Niepoprawne dane"]
    
    else:
        token: str = Kody.wygenerujKod()
        hashTok: str = hash.sha3_512(token.encode()).hexdigest()
        Bazy.ustawToken(hashLog,hashHas,hashTok)
        rola: str = Bazy.rolaUzytkownika(hashLog,hashTok)
        
        return True, [token, rola]



def probaRejestracji(nazwaProjektu: str, kodZaproszeniowy: str, hashLog: str, hashHas: str, nick: str) -> typing.Tuple[bool,typing.List[str]]: #[sukces operacji, [token sesji]]
    #login i hasło już zahashowane
    hashKod: str = hash.sha3_512(kodZaproszeniowy.encode()).hexdigest()
    
    czyKodIstnieje: bool = Bazy.czyJestKod(hashKod)
    
    if(not czyKodIstnieje):
        return False, ["Niepoprawny kod"]
        
    if(Bazy.czyLoginIstnieje(hashLog) or Bazy.czyNickIstnieje(nick)):
        return False, ["Dane już zajęte"]
    
    else:
        token: str = Kody.wygenerujKod()
        hashTok: str = hash.sha3_512(token.encode()).hexdigest()
        Bazy.wstawUzytkownika(hashLog,hashHas,hashTok,"Niezweryfikowany",nick)
        Bazy.usunKod(hashKod)
        
        return True, [token]



def probaUstawieniaKluczaPublicznego(login: str, token: str, kluczPub: str) -> typing.Tuple[bool,typing.List[str]]:        #[sukces operacji, [""]]
    hashLog: str = hash.sha3_512(login.encode()).hexdigest()
    hashTok: str = hash.sha3_512(token.encode()).hexdigest()
        
    if(not Bazy.autoryzacjaTokenem(hashLog,hashTok)):
        return False, ["Niepoprawne dane"]
    
    czyTakiKluczIstnieje: bool = Bazy.czyKluczIstnieje(kluczPub)
    
    if(czyTakiKluczIstnieje):
        return False, ["Wyślij nowy klucz"]
    
    else:
        Bazy.ustawKlucz(hashLog,hashTok,kluczPub)
        return True, [""]