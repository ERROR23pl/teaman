import typing
import hashlib as hash
#import KomunikacjaZBaza as Bazy
import MockTestowyKomunikacjiZBaza as Bazy
    
    
def dodajDoPokoju(login: str, token: str, nazwaPokoju: str, dodawanaOsoba: str, kluczePokoju: typing.Tuple[str,str]) -> typing.Tuple[bool,typing.List[str]]: #[sukces operacji, [""]]
    hashLog: str = hash.sha3_512(login.encode()).hexdigest()
    hashTok: str = hash.sha3_512(token.encode()).hexdigest()
    
    wynik: int = Bazy.iloscUzytkownikow(login=hashLog, token=hashTok)
    
    if(wynik!=1):
        return False, ["Niepoprawne dane"]
    
    if(Bazy.rolaUzytkownika(hashLog,hashTok)!="Właściciel zespołu"):
        return False, ["Brak uprawnień"]
        
    czyPokojIstnieje: bool = Bazy.czyJestPokoj(nazwaPokoju)
    
    if(not czyPokojIstnieje):
        return False, ["Pokój nie istnieje"]
    
    else:
        czyUzytkownikWProjekcie: bool = (Bazy.iloscUzytkownikow(nickPubliczny=dodawanaOsoba))
        if(not czyUzytkownikWProjekcie):
            return False, ["Drugi użytkownik nie istnieje"]
        
        loginDodawanego: str = Bazy.loginUzytkownika(dodawanaOsoba) #hash loginu dodawanego użytkownika

        if(Bazy.czyUzytkownikJestWPokoju(nazwaPokoju,loginDodawanego)):         #użytkownik już jest w pokoju
            return False, ["Drugi użytkownik już należy do pokoju"]
        
        elif(not Bazy.czyZweryfikowany(loginDodawanego)):                       #użytkownik niezweryfikowany - nie można go nigdzie dodać przed weryfikacją
            return False, ["Drugi użytkownik niezweryfikowany"]

        else:        
            Bazy.dodajDoPokoju(hashLog,hashTok,nazwaPokoju,loginDodawanego)
            Bazy.dodajKluczPokoju(login,hashTok,nazwaPokoju,kluczePokoju[0],kluczePokoju[1],loginDodawanego)    #dodanie do tabeli kluczy, wygenerowanych kluczy pokoju głównego zaszyfrowanych kluczm publicznym dodawanego użytkownika
            return True, [""]



def usunZPokoju(login: str, token: str, nazwaPokoju: str, usuwanaOsoba: str) -> typing.Tuple[bool,typing.List[str]]: #[sukces operacji, [""]]
    hashLog: str = hash.sha3_512(login.encode()).hexdigest()
    hashTok: str = hash.sha3_512(token.encode()).hexdigest()
    
    wynik: int = Bazy.iloscUzytkownikow(login=hashLog, token=hashTok)
    
    if(wynik!=1):
        return False, ["Niepoprawne dane"]
    
    if(Bazy.rolaUzytkownika(hashLog,hashTok)!="Właściciel zespołu"):
        return False, ["Brak uprawnień"]
        
    czyPokojIstnieje: bool = Bazy.czyJestPokoj(nazwaPokoju)
    
    if(not czyPokojIstnieje):
        return False, ["Pokój nie istnieje"]
    
    else:
        czyUzytkownikWProjekcie: bool = (Bazy.iloscUzytkownikow(nickPubliczny=usuwanaOsoba))
        if(not czyUzytkownikWProjekcie):
            return True, [""]               #usuwany użytkownik nie jest w projekcie - usunięcie z pokoju uważane za udane
        
        loginUsuwanego: str = Bazy.loginUzytkownika(usuwanaOsoba) #hash loginu usuwanego użytkownika
        
        Bazy.usunZPokoju(hashLog,hashTok,nazwaPokoju,loginUsuwanego)   #nawet, gdyby takiej osoby nie było, to i tak efekt usunięcia jest ten sam, więc nie jest testowane 
        Bazy.usunKluczeDlaUzytkownika(hashLog,hashTok,nazwaPokoju,loginUsuwanego)   #usunięcie kluczy serwera zaszyfrowanych kluczem publicznym usuniętego użytkownika
        return True, [""]