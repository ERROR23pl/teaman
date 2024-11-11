import ManagerPlikowKomunikacyjnych as Pliki
import ManagerHasel as Hasla
import ManagerKodow as Kody
import ManagerNazw as Nazwy
import LaczenieZProjektem as LogIRej
import WlasnyProjekt as WlProj
import KomunikacjaZBaza as Bazy
import ZarzadzaniePokojami as Pokoje
import ZarzadzanieCzlonkamiPokojow as CzlPokojow
import typing


#TODO plik w rozwoju; po zakończeniu, przerzucić case'y do osobnych plików, a tut tylko wywołania

def ObsluzZapytanie(plikKomunikacyjny):
    zapytanie: typing.List = Pliki.analizaPliku(plikKomunikacyjny)
    operacja: str = zapytanie[0]
    nazwaProjektu: str = zapytanie[1]
    
    if(not Nazwy.przetestujNazwe(nazwaProjektu)):
        return Pliki.stworzPlikZOdpowiedzia()   #niepoprawna nazwa projektu
    
    
    if(operacja=="logowanie"):
        czyProjektIstnieje: bool = Bazy.czyBazaIstnieje(nazwaProjektu)
        
        if(czyProjektIstnieje):
            Bazy.polaczZBaza(nazwaProjektu)
        else:
            return Pliki.stworzPlikZOdpowiedzia()   #niepoprawna nazwa projektu
        
        login: str = zapytanie[2]
        haslo: str = zapytanie[3]
        
        if((not Nazwy.przetestujNazwe(login)) or (not Hasla.poprawnoscHasla(haslo))):
            return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True)   #niepoprawne dane
        
        rezultat: typing.Tuple[bool,str,str] = LogIRej.probaLogowania(login,haslo)
        
        Bazy.rozlaczZBaza()
        return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True, poprawnoscDanych=rezultat[0], sukcesOperacji=rezultat[0], dane=[rezultat[1],rezultat[2]])

    
    elif(operacja=="rejestracja"):
        czyProjektIstnieje: bool = Bazy.czyBazaIstnieje(nazwaProjektu)
        
        if(czyProjektIstnieje):
            Bazy.polaczZBaza(nazwaProjektu)
        else:
            return Pliki.stworzPlikZOdpowiedzia()   #niepoprawna nazwa projektu
        
        kodZapr: str = zapytanie[2]
        login: str = zapytanie[3]
        haslo: str = zapytanie[4]
        
        if((not Kody.przetestujKod(kodZapr))  or (not Nazwy.przetestujNazwe(login)) or (not Hasla.poprawnoscHasla(haslo))):
            return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True)   #niepoprawne dane
        
        rezultat: typing.Tuple[bool,bool,str] = LogIRej.probaRejestracji(kodZapr,login,haslo)
        
        Bazy.rozlaczZBaza()
        return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True, poprawnoscDanych=rezultat[0], sukcesOperacji=rezultat[1], dane=[rezultat[2]])

    
    elif(operacja=="tworzenie projektu"):
        czyProjektIstnieje: bool = Bazy.czyBazaIstnieje(nazwaProjektu)
        
        if(czyProjektIstnieje):
            return Pliki.stworzPlikZOdpowiedzia()   #nie można stworzyć projektu, bo już istnieje
        
        login: str = zapytanie[2]
        haslo: str = zapytanie[3]
        
        if((not Nazwy.przetestujNazwe(login)) or (not Hasla.poprawnoscHasla(haslo))):
            return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True)   #niepoprawne dane
        
        rezultat: str = WlProj.stworzProjekt(nazwaProjektu,login,haslo)
        
        Bazy.rozlaczZBaza()
        return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True, poprawnoscDanych=True, sukcesOperacji=True, dane=[rezultat])

    
    elif(operacja=="zapraszanie"):
        czyProjektIstnieje: bool = Bazy.czyBazaIstnieje(nazwaProjektu)
        
        if(czyProjektIstnieje):
            Bazy.polaczZBaza(nazwaProjektu)
        else:
            return Pliki.stworzPlikZOdpowiedzia()   #niepoprawna nazwa projektu
        
        login: str = zapytanie[2]
        token: str = zapytanie[3]
        kodZapr: str = zapytanie[4]
        
        if((not Nazwy.przetestujNazwe(login)) or (not Kody.przetestujKod(token))):
            return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True)   #niepoprawne dane
        
        if((not Kody.przetestujKod(kodZapr))):
            return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True, poprawnoscDanych=True)   #niepoprawny kod - prośba o nowy
        
        rezultat: typing.Tuple[bool,bool] = WlProj.dodajZaproszenie(login,token,kodZapr)
        
        Bazy.rozlaczZBaza()
        return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True, poprawnoscDanych=rezultat[0], sukcesOperacji=rezultat[1], dane=[""])
    
    
    elif(operacja=="usuwanie projektu"):
        czyProjektIstnieje: bool = Bazy.czyBazaIstnieje(nazwaProjektu)
        
        if(czyProjektIstnieje):
            Bazy.polaczZBaza(nazwaProjektu)
        else:
            return Pliki.stworzPlikZOdpowiedzia()   #niepoprawna nazwa projektu
        
        login: str = zapytanie[2]
        token: str = zapytanie[3]
        
        if((not Nazwy.przetestujNazwe(login)) or (not Kody.przetestujKod(token))):
            return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True)   #niepoprawne dane
        
        rezultat: bool = WlProj.usunProjekt(login,token)
        
        return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True, poprawnoscDanych=rezultat, sukcesOperacji=rezultat, dane=[""])
    
    
    elif(operacja=="tworzenie pokoju"):
        czyProjektIstnieje: bool = Bazy.czyBazaIstnieje(nazwaProjektu)
        
        if(czyProjektIstnieje):
            Bazy.polaczZBaza(nazwaProjektu)
        else:
            return Pliki.stworzPlikZOdpowiedzia()   #niepoprawna nazwa projektu
        
        login: str = zapytanie[2]
        token: str = zapytanie[3]
        nazwaPokoju: str = zapytanie[4]
        
        if((not Nazwy.przetestujNazwe(login)) or (not Kody.przetestujKod(token))):
            return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True)   #niepoprawne dane
        
        if((not Nazwy.przetestujNazwe(nazwaPokoju))):
            return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True, poprawnoscDanych=True)   #niepoprawna nazwa pokoju
        
        rezultat: typing.Tuple[bool,bool] = Pokoje.stworzPokoj(login,token,nazwaPokoju)
        
        Bazy.rozlaczZBaza()
        return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True, poprawnoscDanych=rezultat[0], sukcesOperacji=rezultat[1], dane=[""])
    
    
    elif(operacja=="usuwanie pokoju"):
        czyProjektIstnieje: bool = Bazy.czyBazaIstnieje(nazwaProjektu)
        
        if(czyProjektIstnieje):
            Bazy.polaczZBaza(nazwaProjektu)
        else:
            return Pliki.stworzPlikZOdpowiedzia()   #niepoprawna nazwa projektu
        
        login: str = zapytanie[2]
        token: str = zapytanie[3]
        nazwaPokoju: str = zapytanie[4]
        
        if((not Nazwy.przetestujNazwe(login)) or (not Kody.przetestujKod(token))):
            return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True)   #niepoprawne dane
        
        if((not Nazwy.przetestujNazwe(nazwaPokoju))):
            return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True, poprawnoscDanych=True)   #niepoprawna nazwa pokoju
        
        rezultat: typing.Tuple[bool,bool] = Pokoje.stworzPokoj(login,token,nazwaPokoju)
        
        Bazy.rozlaczZBaza()
        return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True, poprawnoscDanych=rezultat[0], sukcesOperacji=rezultat[1], dane=[""])
    
    
    elif(operacja=="dodawanie do pokoju"):
        czyProjektIstnieje: bool = Bazy.czyBazaIstnieje(nazwaProjektu)
        
        if(czyProjektIstnieje):
            Bazy.polaczZBaza(nazwaProjektu)
        else:
            return Pliki.stworzPlikZOdpowiedzia()   #niepoprawna nazwa projektu
        
        login: str = zapytanie[2]
        token: str = zapytanie[3]
        nazwaPokoju: str = zapytanie[4]
        dodawanyUzytkownik: str = zapytanie[5]
        
        if((not Nazwy.przetestujNazwe(login)) or (not Kody.przetestujKod(token))):
            return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True)   #niepoprawne dane
        
        if((not Nazwy.przetestujNazwe(nazwaPokoju)) or (not Nazwy.przetestujNazwe(dodawanyUzytkownik))):
            return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True, poprawnoscDanych=True)   #niepoprawna nazwa pokoju lub login dodawanego użytkownika
        
        rezultat: typing.Tuple[bool,bool,bool] = CzlPokojow.dodajDoPokoju(login,token,nazwaPokoju,dodawanyUzytkownik)
        
        Bazy.rozlaczZBaza()
        return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True, poprawnoscDanych=rezultat[0], sukcesOperacji=(rezultat[1] and rezultat[2]), dane=[""])
    
    
    elif(operacja=="usuwanie z pokoju"):
        czyProjektIstnieje: bool = Bazy.czyBazaIstnieje(nazwaProjektu)
        
        if(czyProjektIstnieje):
            Bazy.polaczZBaza(nazwaProjektu)
        else:
            return Pliki.stworzPlikZOdpowiedzia()   #niepoprawna nazwa projektu
        
        login: str = zapytanie[2]
        token: str = zapytanie[3]
        nazwaPokoju: str = zapytanie[4]
        usuwanyUzytkownik: str = zapytanie[5]
        
        if((not Nazwy.przetestujNazwe(login)) or (not Kody.przetestujKod(token))):
            return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True)   #niepoprawne dane
        
        if((not Nazwy.przetestujNazwe(nazwaPokoju)) or (not Nazwy.przetestujNazwe(usuwanyUzytkownik))):
            return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True, poprawnoscDanych=True)   #niepoprawna nazwa pokoju lub login usuwanego użytkownika
        
        rezultat: typing.Tuple[bool,bool] = CzlPokojow.usunZPokoju(login,token,nazwaPokoju,usuwanyUzytkownik)
        
        Bazy.rozlaczZBaza()
        return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True, poprawnoscDanych=rezultat[0], sukcesOperacji=rezultat[1], dane=[""])
    
    
    #tu w przyszłości dalsze operacje
    
    else:              #nieznana operacja
        return Pliki.stworzPlikZOdpowiedzia()