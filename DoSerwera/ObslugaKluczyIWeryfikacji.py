import typing
import Obiekty as o
import SQLLite as Baza
import ManagerPlikowKomunikacyjnych as Pliki
import LaczenieZProjektem as LogIRej
import WlasnyProjekt as WlProj
import WeryfikacjaIRole as Wer

def obsluzUstawianieKlucza(zapytanie: typing.List, nazwaProjektu: o.nazwa, czyProjektIstnieje: bool):
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
        kluczPub: o.klucz = o.klucz(str(zapytanie[4]))
            
    except:
        return Pliki.stworzPlikZOdpowiedzia(False,["Wyślij nowy klucz"])   #niepoprawny klucz - prośba o nowy
            
    rezultat: typing.Tuple[bool,typing.List[str]] = LogIRej.probaUstawieniaKluczaPublicznego(baza,login.wart,token.wart,kluczPub.wart)

    return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])


def obsluzPobieranieCzyjegosKlucza(zapytanie: typing.List, nazwaProjektu: o.nazwa, czyProjektIstnieje: bool):
    if(czyProjektIstnieje):
        baza = Baza.SQLLiteDB("./Bazy/"+nazwaProjektu.wart+".db")
    else:
        return Pliki.stworzPlikZOdpowiedzia(False,["Projekt nie istnieje"])   #niepoprawna nazwa projektu
            
    try:
        login: o.nazwa = o.nazwa(str(zapytanie[2]))
        token: o.kod = o.kod(str(zapytanie[3]))
        nickUzytkownika: o.nazwa = o.nazwa(str(zapytanie[4]))
            
    except:
        return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane
            
    rezultat: typing.Tuple[bool,typing.List[str]] = WlProj.pobierzKluczPublicznyUzytkownika(baza,login.wart,token.wart,nickUzytkownika.wart)

    return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])


def obsluzPobieranieListyNiezweryfikowanych(zapytanie: typing.List, nazwaProjektu: o.nazwa, czyProjektIstnieje: bool):
    if(czyProjektIstnieje):
        baza = Baza.SQLLiteDB("./Bazy/"+nazwaProjektu.wart+".db")
    else:
        return Pliki.stworzPlikZOdpowiedzia(False,["Projekt nie istnieje"])   #niepoprawna nazwa projektu
            
    try:
        login: o.nazwa = o.nazwa(str(zapytanie[2]))
        token: o.kod = o.kod(str(zapytanie[3]))
            
    except:
        return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane

            
    rezultat: typing.Tuple[bool,typing.List[str]] = Wer.listaNiezweryfikowanych(baza,login.wart,token.wart)

    return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])


def obsluzZmianeRoli(zapytanie: typing.List, nazwaProjektu: o.nazwa, czyProjektIstnieje: bool):
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
        nickUzytkownika: o.nazwa = o.nazwa(str(zapytanie[4]))
            
    except:
        return Pliki.stworzPlikZOdpowiedzia(False,["Nick drugiego użytkownika nie spełnia założeń"])   #niepoprawny nick celu
            
    try:
        nowaRola: o.rola = o.rola(str(zapytanie[5]))
            
    except:
        return Pliki.stworzPlikZOdpowiedzia(False,["Nowa rola nie spełnia założeń"])   #niepoprawna rola
            
    rezultat: typing.Tuple[bool,typing.List[str]] = Wer.ustawRole(baza,login.wart,token.wart,nickUzytkownika.wart,nowaRola.wart)

    return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])



def obsluzWeryfikacje(zapytanie: typing.List, nazwaProjektu: o.nazwa, czyProjektIstnieje: bool):
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
        nickUzytkownika: o.nazwa = o.nazwa(str(zapytanie[4]))
            
    except:
        return Pliki.stworzPlikZOdpowiedzia(False,["Nick drugiego użytkownika nie spełnia założeń"])   #niepoprawny nick celu
            
    try:
        nowaRola: o.rola = o.rola(str(zapytanie[5]))
            
    except:
        return Pliki.stworzPlikZOdpowiedzia(False,["Nowa rola nie spełnia założeń"])   #niepoprawna rola
            
    kluczePokojuGl: typing.Tuple[str,str] = [str(zapytanie[6]), str(zapytanie[7])]
            
    rezultat: typing.Tuple[bool,typing.List[str]] = Wer.zweryfikuj(baza,login.wart,token.wart,nickUzytkownika.wart,nowaRola.wart,nazwaProjektu.wart,kluczePokojuGl)

    return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])