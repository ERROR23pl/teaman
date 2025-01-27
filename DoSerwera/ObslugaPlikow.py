import typing
import Obiekty as o
import SQLLite as Baza
import ManagerPlikowKomunikacyjnych as Pliki
import UdostepnianiePlikow as udPlikow

def obsluzDodawaniePliku(zapytanie: typing.List, nazwaProjektu: o.nazwa, czyProjektIstnieje: bool):
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
        nazwaPokoju: o.nazwa = o.nazwa(str(zapytanie[4]))
            
    except:
        return Pliki.stworzPlikZOdpowiedzia(False,["Nazwa pokoju nie spełnia założeń"])   #niepoprawna nazwa pokoju
            
    try:
        nazwaPliku: o.nazwaPliku = o.nazwaPliku(str(zapytanie[5]))
        zawartoscPliku: bytes = (str(zapytanie[6])).encode()
            
    except:
        return Pliki.stworzPlikZOdpowiedzia(False,["Nazwa pliku nie spełnia założeń"])   #niepoprawna nazwa pliku
            
    rezultat: typing.Tuple[bool,typing.List[str]] = udPlikow.dodajPlik(baza,login.wart,token.wart,nazwaPokoju.wart,nazwaPliku.wart,zawartoscPliku)

    return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])


def obsluzUsuwaniePliku(zapytanie: typing.List, nazwaProjektu: o.nazwa, czyProjektIstnieje: bool):
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
        nazwaPokoju: o.nazwa = o.nazwa(str(zapytanie[4]))
            
    except:
        return Pliki.stworzPlikZOdpowiedzia(False,["Nazwa pokoju nie spełnia założeń"])   #niepoprawna nazwa pokoju
            
    idPliku: int = int(zapytanie[5])
            
    rezultat: typing.Tuple[bool,typing.List[str]] = udPlikow.usunPlik(baza,login.wart,token.wart,nazwaPokoju.wart,idPliku)

    return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])



def obsluzPobraniePliku(zapytanie: typing.List, nazwaProjektu: o.nazwa, czyProjektIstnieje: bool):
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
        nazwaPokoju: o.nazwa = o.nazwa(str(zapytanie[4]))
            
    except:
        return Pliki.stworzPlikZOdpowiedzia(False,["Nazwa pokoju nie spełnia założeń"])   #niepoprawna nazwa pokoju
            
    idPliku: int = int(zapytanie[5])
            
    rezultat: typing.Tuple[bool,typing.List[str]] = udPlikow.pobierzPlik(baza,login.wart,token.wart,nazwaPokoju.wart,idPliku)

    return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])


def obsluzPobranieListyPlikow(zapytanie: typing.List, nazwaProjektu: o.nazwa, czyProjektIstnieje: bool):
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
        nazwaPokoju: o.nazwa = o.nazwa(str(zapytanie[4]))
            
    except:
        return Pliki.stworzPlikZOdpowiedzia(False,["Nazwa pokoju nie spełnia założeń"])   #niepoprawna nazwa pokoju
            
    rezultat: typing.Tuple[bool,typing.List[str]] = udPlikow.pobierzListePlikow(baza,login.wart,token.wart,nazwaPokoju.wart)

    return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])