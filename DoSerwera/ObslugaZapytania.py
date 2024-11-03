import ManagerPlikowKomunikacyjnych as Pliki
import ManagerHasel as Hasla
import ManagerKodow as Kody
import ManagerNazw as Nazwy
import LaczenieZProjektem as LogIRej
import WlasnyProjekt as WlProj
import typing

def ObsluzZapytanie(plikKomunikacyjny):
    zapytanie: typing.List = Pliki.analizaPliku(plikKomunikacyjny)
    operacja: str = zapytanie[0]
    nazwaProjektu: str = zapytanie[1]
    
    if(not Nazwy.przetestujNazwe(nazwaProjektu)):
        return Pliki.stworzPlikZOdpowiedzia()   #niepoprawna nazwa projektu
    
    
    if(operacja=="logowanie"):
        czyProjektIstnieje: bool = True
        #TODO wywołanie prepared statement sprawdzającego czy jest baza danych takiego projektu i, jeśli tak łącząca się z nią; 
        #jeśli nie ma, ustawia czyProjektIstnieje=False
        
        if(not czyProjektIstnieje):
            return Pliki.stworzPlikZOdpowiedzia()   #niepoprawna nazwa projektu
        
        login: str = zapytanie[2]
        haslo: str = zapytanie[3]
        
        if((not Nazwy.przetestujNazwe(login)) or (not Hasla.poprawnoscHasla(haslo))):
            return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True)   #niepoprawne dane
        
        rezultat: typing.Tuple[bool,str,str] = LogIRej.probaLogowania(login,haslo)
        
        return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True, poprawnoscDanych=rezultat[0], sukcesOperacji=rezultat[0], dane=[rezultat[1],rezultat[2]])

    
    elif(operacja=="rejestracja"):
        czyProjektIstnieje: bool = True
        #TODO wywołanie prepared statement sprawdzającego czy jest baza danych takiego projektu i, jeśli tak łącząca się z nią; 
        #jeśli nie ma, ustawia czyProjektIstnieje=False
        
        if(not czyProjektIstnieje):
            return Pliki.stworzPlikZOdpowiedzia()   #niepoprawna nazwa projektu
        
        kodZapr: str = zapytanie[2]
        login: str = zapytanie[3]
        haslo: str = zapytanie[4]
        
        if((not Kody.przetestujKod(kodZapr))  or (not Nazwy.przetestujNazwe(login)) or (not Hasla.poprawnoscHasla(haslo))):
            return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True)   #niepoprawne dane
        
        rezultat: typing.Tuple[bool,bool,str] = LogIRej.probaRejestracji(kodZapr,login,haslo)
        
        return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True, poprawnoscDanych=rezultat[0], sukcesOperacji=rezultat[1], dane=[rezultat[2]])

    
    elif(operacja=="tworzenie projektu"):
        czyMoznaStworzycProj: bool = True
        #TODO wywołanie prepared statement sprawdzającego czy jest baza danych takiego projektu; 
        #jeśli jest, ustawia czyMoznaStworzycProj=False
        
        if(not czyMoznaStworzycProj):
            return Pliki.stworzPlikZOdpowiedzia()   #niepoprawna nazwa projektu
        
        login: str = zapytanie[2]
        haslo: str = zapytanie[3]
        
        if((not Nazwy.przetestujNazwe(login)) or (not Hasla.poprawnoscHasla(haslo))):
            return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True)   #niepoprawne dane
        
        rezultat: str = WlProj.stworzProjekt(nazwaProjektu,login,haslo)
        
        return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True, poprawnoscDanych=True, sukcesOperacji=True, dane=[rezultat])

    
    elif(operacja=="zapraszanie"):
        czyProjektIstnieje: bool = True
        #TODO wywołanie prepared statement sprawdzającego czy jest baza danych takiego projektu i, jeśli tak łącząca się z nią; 
        #jeśli nie ma, ustawia czyProjektIstnieje=False
        
        if(not czyProjektIstnieje):
            return Pliki.stworzPlikZOdpowiedzia()   #niepoprawna nazwa projektu
        
        login: str = zapytanie[2]
        token: str = zapytanie[3]
        kodZapr: str = zapytanie[4]
        
        if((not Nazwy.przetestujNazwe(login)) or (not Kody.przetestujKod(token))):
            return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True)   #niepoprawne dane
        
        if((not Kody.przetestujKod(kodZapr))):
            return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True, poprawnoscDanych=True)   #niepoprawny kod - prośba o nowy
        
        rezultat: typing.Tuple[bool,bool] = WlProj.dodajZaproszenie(login,token,kodZapr)
        
        return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True, poprawnoscDanych=rezultat[0], sukcesOperacji=rezultat[1], dane=[""])
    
    
    elif(operacja=="usuwanie projektu"):
        czyProjektIstnieje: bool = True
        #TODO wywołanie prepared statement sprawdzającego czy jest baza danych takiego projektu i, jeśli tak łącząca się z nią; 
        #jeśli nie ma, ustawia czyProjektIstnieje=False
        
        if(not czyProjektIstnieje):
            return Pliki.stworzPlikZOdpowiedzia()   #niepoprawna nazwa projektu
        
        login: str = zapytanie[2]
        token: str = zapytanie[3]
        
        if((not Nazwy.przetestujNazwe(login)) or (not Kody.przetestujKod(token))):
            return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True)   #niepoprawne dane
        
        rezultat: bool = WlProj.usunProjekt(login,token)
        
        return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True, poprawnoscDanych=rezultat, sukcesOperacji=rezultat, dane=[""])
    
    
    #tu w przyszłości dalsze operacje
    
    else:              #nieznana operacja
        return Pliki.stworzPlikZOdpowiedzia()