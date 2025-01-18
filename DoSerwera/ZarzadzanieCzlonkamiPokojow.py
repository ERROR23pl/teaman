import typing
import hashlib as hash
import KomunikacjaZBaza as Bazy
import sys
sys.path.insert(1, '../Database')
import SQLLite as Baza
    
    
def dodajDoPokoju(baza: Baza.SQLLiteDB, login: str, token: str, nazwaPokoju: str, dodawanaOsoba: str, kluczePokoju: typing.Tuple[str,str]) -> typing.Tuple[bool,typing.List[str]]: #[sukces operacji, [""]]
    hashLog: str = hash.sha3_512(login.encode()).hexdigest()
    hashTok: str = hash.sha3_512(token.encode()).hexdigest()
    
    if(not Bazy.autoryzacjaTokenem(baza,hashLog,hashTok)):
        return False, ["Niepoprawne dane"]
    
    if(Bazy.rolaUzytkownika(baza,hashLog,hashTok)!="Admin"):
        return False, ["Brak uprawnień"]
        
    czyPokojIstnieje: bool = Bazy.czyJestPokoj(baza,nazwaPokoju)
    
    if(not czyPokojIstnieje):
        return False, ["Pokój nie istnieje"]
    
    else:
        if(not Bazy.czyNickIstnieje(baza,dodawanaOsoba)):
            return False, ["Drugi użytkownik nie istnieje"]
        
        loginDodawanego: str = Bazy.loginUzytkownika(baza,dodawanaOsoba) #hash loginu dodawanego użytkownika

        if(Bazy.czyUzytkownikJestWPokoju(baza,nazwaPokoju,loginDodawanego)):         #użytkownik już jest w pokoju
            return False, ["Drugi użytkownik już należy do pokoju"]
        
        elif(not Bazy.czyZweryfikowany(baza,loginDodawanego)):                       #użytkownik niezweryfikowany - nie można go nigdzie dodać przed weryfikacją
            return False, ["Drugi użytkownik niezweryfikowany"]

        else:        
            Bazy.dodajDoPokoju(baza,hashLog,hashTok,nazwaPokoju,loginDodawanego)
            Bazy.dodajKluczPokoju(baza,login,hashTok,nazwaPokoju,kluczePokoju[0],kluczePokoju[1],loginDodawanego)    #dodanie do tabeli kluczy, wygenerowanych kluczy pokoju głównego zaszyfrowanych kluczm publicznym dodawanego użytkownika
            return True, [""]



def usunZPokoju(baza: Baza.SQLLiteDB, login: str, token: str, nazwaPokoju: str, usuwanaOsoba: str) -> typing.Tuple[bool,typing.List[str]]: #[sukces operacji, [""]]
    hashLog: str = hash.sha3_512(login.encode()).hexdigest()
    hashTok: str = hash.sha3_512(token.encode()).hexdigest()
    
    if(not Bazy.autoryzacjaTokenem(baza,hashLog,hashTok)):
        return False, ["Niepoprawne dane"]
    
    if(Bazy.rolaUzytkownika(baza,hashLog,hashTok)!="Admin"):
        return False, ["Brak uprawnień"]
        
    czyPokojIstnieje: bool = Bazy.czyJestPokoj(baza,nazwaPokoju)
    
    if(not czyPokojIstnieje):
        return False, ["Pokój nie istnieje"]
    
    else:
        if(not Bazy.czyNickIstnieje(baza,usuwanaOsoba)):
            return True, [""]               #usuwany użytkownik nie jest w projekcie - usunięcie z pokoju uważane za udane
        
        loginUsuwanego: str = Bazy.loginUzytkownika(baza,usuwanaOsoba) #hash loginu usuwanego użytkownika
        if(loginUsuwanego==hashLog):
            return False, ["Nie można usunąć właściciela projektu z pokoju"]
        
        Bazy.usunZPokoju(baza,hashLog,hashTok,nazwaPokoju,loginUsuwanego)   #nawet, gdyby takiej osoby nie było, to i tak efekt usunięcia jest ten sam, więc nie jest testowane 
        Bazy.usunKluczeDlaUzytkownika(baza,hashLog,hashTok,nazwaPokoju,loginUsuwanego)   #usunięcie kluczy serwera zaszyfrowanych kluczem publicznym usuniętego użytkownika
        return True, [""]