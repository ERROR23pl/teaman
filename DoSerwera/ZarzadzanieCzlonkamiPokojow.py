import typing
import hashlib as hash
#import KomunikacjaZBaza as Bazy
import MockTestowyKomunikacjiZBaza as Bazy
    
    
def dodajDoPokoju(login: str, token: str, nazwaPokoju: str, dodawanaOsoba: str, kluczePokoju: typing.Tuple[str,str]) -> typing.Tuple[bool, bool, bool]: #[czy są uprawnienia, czy pokój istniał, czy się udało]
    hashLog: str = hash.sha3_512(login.encode()).hexdigest()
    hashTok: str = hash.sha3_512(token.encode()).hexdigest()
    
    wynik: int = Bazy.iloscUzytkownikow(login=hashLog, token=hashTok, rola="Właściciel zespołu")
    
    if(wynik!=1):
        return False, False, False
        
    czyPokojIstnieje: bool = Bazy.czyJestPokoj(nazwaPokoju)
    
    if(not czyPokojIstnieje):
        return True, False, False
    
    else:
        czyUzytkownikWProjekcie: bool = (Bazy.iloscUzytkownikow(nickPubliczny=dodawanaOsoba))
        if(not czyUzytkownikWProjekcie):
            return True,True,False
        
        loginDodawanego: str = Bazy.loginUzytkownika(dodawanaOsoba) #hash loginu dodawanego użytkownika
        czyMoznaDodac: bool = ((not Bazy.czyUzytkownikJestWPokoju(nazwaPokoju,loginDodawanego)) and Bazy.czyZweryfikowany(loginDodawanego))  #użytkownik istnieje w projekcie i jest zweryfikowany, ale nie ma go w pokoju

        if(not czyMoznaDodac):
            return True,True,False
        else:        
            Bazy.dodajDoPokoju(hashLog,hashTok,nazwaPokoju,loginDodawanego)
            Bazy.dodajKluczPokoju(login,hashTok,nazwaPokoju,kluczePokoju[0],kluczePokoju[1],loginDodawanego)    #dodanie do tabeli kluczy, wygenerowanych kluczy pokoju głównego zaszyfrowanych kluczm publicznym dodawanego użytkownika
            return True, True, True



def usunZPokoju(login: str, token: str, nazwaPokoju: str, usuwanaOsoba: str) -> typing.Tuple[bool, bool]: #[czy są uprawnienia, czy pokój istniał i się udało]
    hashLog: str = hash.sha3_512(login.encode()).hexdigest()
    hashTok: str = hash.sha3_512(token.encode()).hexdigest()
    
    wynik: int = Bazy.iloscUzytkownikow(login=hashLog, token=hashTok, rola="Właściciel zespołu")
    
    if(wynik!=1):
        return False, False
        
    czyPokojIstnieje: bool = Bazy.czyJestPokoj(nazwaPokoju)
    
    if(not czyPokojIstnieje):
        return True, False
    
    else:
        czyUzytkownikWProjekcie: bool = (Bazy.iloscUzytkownikow(nickPubliczny=usuwanaOsoba))
        if(not czyUzytkownikWProjekcie):
            return True,True
        
        loginUsuwanego: str = Bazy.loginUzytkownika(usuwanaOsoba) #hash loginu usuwanego użytkownika
        
        Bazy.usunZPokoju(hashLog,hashTok,nazwaPokoju,loginUsuwanego)   #nawet, gdyby takiej osoby nie było, to i tak efekt usunięcia jest ten sam, więc nie jest testowane 
        Bazy.usunKluczeDlaUzytkownika(hashLog,hashTok,nazwaPokoju,loginUsuwanego)   #usunięcie kluczy serwera zaszyfrowanych kluczem publicznym usuniętego użytkownika
        return True, True