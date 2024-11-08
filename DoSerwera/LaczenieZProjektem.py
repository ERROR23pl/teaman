import hashlib as hash
import typing
import ManagerKodow as Kody
import KomunikacjaZBaza as Bazy



def probaLogowania(login: str, haslo: str) -> typing.Tuple[bool,str,str]: #[poprawność danych, token sesji, rola]
    hashLog: str = hash.sha3_512(login)
    hashHas: str = hash.sha3_512(haslo)
    
    wynik: int = Bazy.iloscUzytkownikow(login=hashLog, haslo=hashHas)
    
    if(wynik!=1):
        return False, "", ""
    
    else:
        token: str = Kody.wygenerujKod()
        hashTok: str = hash.sha3_512(token)
        Bazy.ustawToken(hashLog,hashHas,hashTok)
        rola: str = Bazy.rolaUzytkownika(hashLog,hashTok)
        
        return True, token, rola



def probaRejestracji(kodZaproszeniowy: str, hashLog: str, hashHas: str) -> typing.Tuple[bool,bool,str]: #[poprawność kodu, sukces rejestracji, token sesji]
    #login i hasło już zahashowane
    hashKod: str = hash.sha3_512(kodZaproszeniowy)
    
    czyKodIstnieje: bool = Bazy.czyJestKod(hashKod)
    
    if(not czyKodIstnieje):
        return False, False, ""
    
    wynik: int = Bazy.iloscUzytkownikow(login=hashLog)
    
    if(wynik!=0):
        return True, False, ""
    
    else:
        token: str = Kody.wygenerujKod()
        hashTok: str = hash.sha3_512(token)
        Bazy.wstawUzytkownika(hashLog,hashHas,hashTok,"Członek zespołu")
        Bazy.usunKod(hashKod)
        
        return True, True, token