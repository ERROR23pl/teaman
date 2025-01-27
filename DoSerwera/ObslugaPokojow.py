import typing
import Obiekty as o
import SQLLite as Baza
import ManagerPlikowKomunikacyjnych as Pliki
import ZarzadzaniePokojami as Pokoje
import ZarzadzanieCzlonkamiPokojow as CzlPokojow

def obsluzTworzeniePokoju(zapytanie: typing.List, nazwaProjektu: o.nazwa, czyProjektIstnieje: bool):
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
            
    rezultat: typing.Tuple[bool,typing.List[str]] = Pokoje.stworzPokoj(baza,login.wart,token.wart,nazwaPokoju.wart)

    return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])


def obsluzUsuwaniePokoju(zapytanie: typing.List, nazwaProjektu: o.nazwa, czyProjektIstnieje: bool):
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
            
    if(nazwaProjektu.wart==nazwaPokoju.wart):
        return Pliki.stworzPlikZOdpowiedzia(False, dane=["Nie można usunąć pokoju głównego"])
            
    rezultat: typing.Tuple[bool,typing.List[str]] = Pokoje.usunPokoj(baza,login.wart,token.wart,nazwaPokoju.wart)

    return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])


def obsluzDodawanieDoPokoju(zapytanie: typing.List, nazwaProjektu: o.nazwa, czyProjektIstnieje: bool):
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
        dodawanyUzytkownik: o.nazwa = o.nazwa(str(zapytanie[5]))
            
    except:
        return Pliki.stworzPlikZOdpowiedzia(False,["Nick drugiego użytkownika nie spełnia założeń"])   #niepoprawny nick dodawanego użytkownika
            
    kluczePokojuZaszyfrowaneKluczemDodawanego: typing.Tuple[str,str] = [str(zapytanie[6]),str(zapytanie[7])]
            
    rezultat: typing.Tuple[bool,typing.List[str]] = CzlPokojow.dodajDoPokoju(baza,login.wart,token.wart,nazwaPokoju.wart,dodawanyUzytkownik.wart,kluczePokojuZaszyfrowaneKluczemDodawanego)

    return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])


def obsluzUsuwanieZPokoju(zapytanie: typing.List, nazwaProjektu: o.nazwa, czyProjektIstnieje: bool):
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
        usuwanyUzytkownik: o.nazwa = o.nazwa(str(zapytanie[5]))
            
    except:
        return Pliki.stworzPlikZOdpowiedzia(False,["Nick drugiego użytkownika nie spełnia założeń"])   #niepoprawny nick usuwanego użytkownika
            
    rezultat: typing.Tuple[bool,typing.List[str]] = CzlPokojow.usunZPokoju(baza,login.wart,token.wart,nazwaPokoju.wart,usuwanyUzytkownik.wart)

    return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])



def obsluzPobieranieListyPokojow(zapytanie: typing.List, nazwaProjektu: o.nazwa, czyProjektIstnieje: bool):
    if(czyProjektIstnieje):
        baza = Baza.SQLLiteDB("./Bazy/"+nazwaProjektu.wart+".db")
    else:
        return Pliki.stworzPlikZOdpowiedzia(False,["Projekt nie istnieje"])   #niepoprawna nazwa projektu
            
    try:
        login: o.nazwa = o.nazwa(str(zapytanie[2]))
        token: o.kod = o.kod(str(zapytanie[3]))
            
    except:
        return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane

            
    rezultat: typing.Tuple[bool,typing.List[str]] = Pokoje.listaPokojow(baza,login.wart,token.wart)

    return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])