import typing
import Obiekty as o
import SQLLite as Baza
import ManagerPlikowKomunikacyjnych as Pliki
import ZarzadzanieChatami as Chaty

def obsluzPobranieChatu(zapytanie: typing.List, nazwaProjektu: o.nazwa, czyProjektIstnieje: bool):
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
            
    rezultat: typing.Tuple[bool,typing.List[str]] = Chaty.pobierzChat(baza,login.wart,token.wart,nazwaPokoju.wart)

    return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])



def obsluzAktChatu(zapytanie: typing.List, nazwaProjektu: o.nazwa, czyProjektIstnieje: bool):
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
            
    ostatniaPosiadana: o.Wiadomosc = o.Wiadomosc(zapytanie[5])
            
    rezultat: typing.Tuple[bool,typing.List[str]] = Chaty.zaktualizujChat(baza,login.wart,token.wart,nazwaPokoju.wart,ostatniaPosiadana)
    
    return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])



def obsluzWyslanieWiadomosci(zapytanie: typing.List, nazwaProjektu: o.nazwa, czyProjektIstnieje: bool):
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
            
    ostatniaPosiadana: o.Wiadomosc = o.Wiadomosc(zapytanie[5]) 
    wiadomosc: o.Wiadomosc = o.Wiadomosc(0,trescWiadomosci=str(zapytanie[6]))
    rezultat: typing.Tuple[bool,typing.List[str]] = Chaty.wyslijWiadomosc(baza,login.wart,token.wart,nazwaPokoju.wart,ostatniaPosiadana,wiadomosc)

    return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])