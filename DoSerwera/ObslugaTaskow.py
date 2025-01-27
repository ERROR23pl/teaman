import typing
import Obiekty as o
import SQLLite as Baza
import ManagerPlikowKomunikacyjnych as Pliki
import ZarzadzanieTaskami as Taski

def obsluzModTaskow(zapytanie: typing.List, nazwaProjektu: o.nazwa, czyProjektIstnieje: bool):
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
            
    dodawaneTaski: typing.List[o.Task] = zapytanie[5]
    usuwaneTaski: typing.List[o.Task] = zapytanie[6]
    modyfikowaneTaski: typing.List[o.Task] = zapytanie[7]                    
            
    rezultat: typing.Tuple[bool,typing.List[str]] = Taski.obslugaTaskow(baza,login.wart,token.wart,nazwaPokoju.wart,dodawaneTaski,usuwaneTaski,modyfikowaneTaski)

    if(rezultat[0]):
        nowaListaTaskow: typing.List[str] = (Taski.pobierzTaski(baza,login.wart,token.wart,nazwaPokoju.wart))[1]
        return Pliki.stworzPlikZOdpowiedzia(rezultat[0],nowaListaTaskow)
    else:
        return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])



def obsluzPobranieListyTaskow(zapytanie: typing.List, nazwaProjektu: o.nazwa, czyProjektIstnieje: bool):
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
            
    rezultat: typing.Tuple[bool,typing.List[str]] = Taski.pobierzTaski(baza,login.wart,token.wart,nazwaPokoju.wart)

    return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])



def obsluzZaznaczenieTaska(zapytanie: typing.List, nazwaProjektu: o.nazwa, czyProjektIstnieje: bool):
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
            
    idTaska: int = int(zapytanie[5])   
            
    rezultat: typing.Tuple[bool,typing.List[str]] = Taski.oznaczJakoWykonany(baza,login.wart,token.wart,nazwaPokoju.wart,idTaska)

    if(rezultat[0]):
        nowaListaTaskow: typing.List[str] = (Taski.pobierzTaski(baza,login.wart,token.wart,nazwaPokoju.wart))[1]
        return Pliki.stworzPlikZOdpowiedzia(rezultat[0],nowaListaTaskow)
    else:
        return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])
    
    
    
def obsluzOdznaczenieTaska(zapytanie: typing.List, nazwaProjektu: o.nazwa, czyProjektIstnieje: bool):
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
            
    idTaska: int = int(zapytanie[5])
            
    rezultat: typing.Tuple[bool,typing.List[str]] = Taski.oznaczJakoNiewykonany(baza,login.wart,token.wart,nazwaPokoju.wart,idTaska)

    if(rezultat[0]):
        nowaListaTaskow: typing.List[str] = (Taski.pobierzTaski(baza,login.wart,token.wart,nazwaPokoju.wart))[1]
        return Pliki.stworzPlikZOdpowiedzia(rezultat[0],nowaListaTaskow)
    else:
        return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])