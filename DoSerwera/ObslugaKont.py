import typing
import hashlib as hash
import Obiekty as o
import SQLLite as Baza
import ManagerPlikowKomunikacyjnych as Pliki
import LaczenieZProjektem as LogIRej
import WlasnyProjekt as WlProj

def obsluzLogowanie(zapytanie: typing.List, nazwaProjektu: o.nazwa, czyProjektIstnieje: bool):
    if(czyProjektIstnieje):
        baza = Baza.SQLLiteDB("./Bazy/"+nazwaProjektu.wart+".db")
    else:
        return Pliki.stworzPlikZOdpowiedzia(False,["Projekt nie istnieje"])   #niepoprawna nazwa projektu
            
    try:
        login: o.nazwa = o.nazwa(str(zapytanie[2]))
        haslo: o.haslo = o.haslo(str(zapytanie[3]))
            
    except:
        return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane
            
    rezultat: typing.Tuple[bool,typing.List[str]] = LogIRej.probaLogowania(baza,login.wart,haslo.wart)

    return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])



def obsluzRejestracje(zapytanie: typing.List, nazwaProjektu: o.nazwa, czyProjektIstnieje: bool):
    if(czyProjektIstnieje):
        baza = Baza.SQLLiteDB("./Bazy/"+nazwaProjektu.wart+".db")
    else:
        return Pliki.stworzPlikZOdpowiedzia(False,["Projekt nie istnieje"])   #niepoprawna nazwa projektu
            
    try:
        kodZapr: o.kod = o.kod(str(zapytanie[2]))
        login: o.nazwa = o.nazwa(str(zapytanie[3]))
        haslo: o.haslo = o.haslo(str(zapytanie[4]))
        nick: o.nazwa = o.nazwa(str(zapytanie[5]))
            
    except:
        return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane
            
    if(login.wart==nick.wart):
        return Pliki.stworzPlikZOdpowiedzia(False,["Nick taki jak login"])   #niepoprawne dane - nazwa publiczna nie może być taka jak login
    
    hasLog: str = hash.sha3_512(login.wart.encode()).hexdigest()
    hasHas: str = hash.sha3_512(haslo.wart.encode()).hexdigest()
    rezultat: typing.Tuple[bool,typing.List[str]] = LogIRej.probaRejestracji(baza,kodZapr.wart,hasLog,hasHas,nick.wart)

    return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])



def obsluzTworzenieProjektu(zapytanie: typing.List, nazwaProjektu: o.nazwa, czyProjektIstnieje: bool):
    if(czyProjektIstnieje):
        return Pliki.stworzPlikZOdpowiedzia(False,["Projekt istnieje"])   #nie można stworzyć projektu, bo już istnieje
            
    try:
        login: o.nazwa = o.nazwa(str(zapytanie[2]))
        haslo: o.haslo = o.haslo(str(zapytanie[3]))
        nick: o.nazwa = o.nazwa(str(zapytanie[4]))
        kluczPub: o.klucz = o.klucz(str(zapytanie[5]))
            
    except:
        return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane
            
    if(login.wart==nick.wart):
        return Pliki.stworzPlikZOdpowiedzia(False,["Nick taki jak login"])   #niepoprawne dane - nazwa publiczna nie może być taka jak login
    
    hasLog: str = hash.sha3_512(login.wart.encode()).hexdigest()
    hasHas: str = hash.sha3_512(haslo.wart.encode()).hexdigest()
    baza = Baza.SQLLiteDB("./Bazy/"+nazwaProjektu.wart+".db")
    rezultat: typing.Tuple[bool,typing.List[str]] = WlProj.stworzProjekt(baza,nazwaProjektu.wart,hasLog,hasHas,nick.wart,kluczPub.wart)

    return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])



def obsluzZapraszanie(zapytanie: typing.List, nazwaProjektu: o.nazwa, czyProjektIstnieje: bool):
    if(czyProjektIstnieje):
        baza = Baza.SQLLiteDB("./Bazy/"+nazwaProjektu.wart+".db")
    else:
        return Pliki.stworzPlikZOdpowiedzia(False,["Projekt nie istnieje"])   #niepoprawna nazwa projektu
            
    try:
        login: o.nazwa = o.nazwa(str(zapytanie[2]))
        token: o.kod = o.kod(str(zapytanie[3]))
            
    except:
        return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane
            
    try:
        kodZapr: o.kod = o.kod(str(zapytanie[4]))
            
    except:
        return Pliki.stworzPlikZOdpowiedzia(False,["Wyślij nowy kod"])   #niepoprawny kod - prośba o nowy
    
    hasKod: str = hash.sha3_512(kodZapr.wart.encode()).hexdigest()     
    rezultat: typing.Tuple[bool,typing.List[str]] = WlProj.dodajZaproszenie(baza,login.wart,token.wart,hasKod)

    return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])



def obsluzUsuwanieProjektu(zapytanie: typing.List, nazwaProjektu: o.nazwa, czyProjektIstnieje: bool):
    if(czyProjektIstnieje):
        baza = Baza.SQLLiteDB("./Bazy/"+nazwaProjektu.wart+".db")
    else:
        return Pliki.stworzPlikZOdpowiedzia(False,["Projekt nie istnieje"])   #niepoprawna nazwa projektu
            
    try:
        login: o.nazwa = o.nazwa(str(zapytanie[2]))
        token: o.kod = o.kod(str(zapytanie[3]))
            
    except:
        return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane
            
    rezultat: typing.Tuple[bool,typing.List[str]] = WlProj.usunProjekt(baza,nazwaProjektu.wart,login.wart,token.wart)
            
    return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])