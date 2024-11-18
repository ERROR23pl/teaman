#import ManagerPlikowKomunikacyjnych as Pliki
import MockTestowyObslugiPlikowKomunikacyjnych as Pliki
import ManagerHasel as Hasla
import ManagerKodow as Kody
import ManagerNazw as Nazwy
import LaczenieZProjektem as LogIRej
import WlasnyProjekt as WlProj
#import KomunikacjaZBaza as Bazy
import MockTestowyKomunikacjiZBaza as Bazy
import ZarzadzaniePokojami as Pokoje
import ZarzadzanieCzlonkamiPokojow as CzlPokojow
import ZarzadzanieTaskami as Taski
import ZarzadzanieChatami as Chaty
import ZarzadzanieKalendarzem as Kalendarz
import typing


#TODO plik w rozwoju; po zakończeniu, przerzucić case'y do osobnych plików, a tu tylko wywołania

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
        
        rezultat: typing.Tuple[bool,bool,str] = LogIRej.probaRejestracji(nazwaProjektu,kodZapr,login,haslo)
        
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
        return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True, poprawnoscDanych=rezultat[0], sukcesOperacji=rezultat[1])
    
    
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
        
        rezultat: bool = WlProj.usunProjekt(nazwaProjektu,login,token)
        
        return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True, poprawnoscDanych=rezultat, sukcesOperacji=rezultat)
    
    
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
        return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True, poprawnoscDanych=rezultat[0], sukcesOperacji=rezultat[1])
    
    
    elif(operacja=="usuwanie pokoju"):
        czyProjektIstnieje: bool = Bazy.czyBazaIstnieje(nazwaProjektu)
        
        if(czyProjektIstnieje):
            Bazy.polaczZBaza(nazwaProjektu)
        else:
            return Pliki.stworzPlikZOdpowiedzia()   #niepoprawna nazwa projektu
        
        login: str = zapytanie[2]
        token: str = zapytanie[3]
        nazwaPokoju: str = zapytanie[4]
        
        if(nazwaProjektu==nazwaPokoju):
            return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True, dane=["Nie można usunąć pokoju głównego"])
        
        if((not Nazwy.przetestujNazwe(login)) or (not Kody.przetestujKod(token))):
            return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True)   #niepoprawne dane
        
        if((not Nazwy.przetestujNazwe(nazwaPokoju))):
            return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True, poprawnoscDanych=True)   #niepoprawna nazwa pokoju
        
        rezultat: bool = Pokoje.usunPokoj(login,token,nazwaPokoju)
        
        Bazy.rozlaczZBaza()
        return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True, poprawnoscDanych=rezultat, sukcesOperacji=rezultat)
    
    
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
        return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True, poprawnoscDanych=rezultat[0], sukcesOperacji=(rezultat[1] and rezultat[2]))
    
    
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
        return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True, poprawnoscDanych=rezultat[0], sukcesOperacji=rezultat[1])
    
    
    elif(operacja=="lista pokojow"):
        czyProjektIstnieje: bool = Bazy.czyBazaIstnieje(nazwaProjektu)
        
        if(czyProjektIstnieje):
            Bazy.polaczZBaza(nazwaProjektu)
        else:
            return Pliki.stworzPlikZOdpowiedzia()   #niepoprawna nazwa projektu
        
        login: str = zapytanie[2]
        token: str = zapytanie[3]
        
        if((not Nazwy.przetestujNazwe(login)) or (not Kody.przetestujKod(token))):
            return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True)   #niepoprawne dane

        
        rezultat: typing.Tuple[bool, typing.List[str]] = Pokoje.listaPokojow(login,token)
        
        Bazy.rozlaczZBaza()
        return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True, poprawnoscDanych=rezultat[0], sukcesOperacji=rezultat[0], dane=rezultat[1])
    
    
    
    elif(operacja=="modyfikacja taskow"):
        czyProjektIstnieje: bool = Bazy.czyBazaIstnieje(nazwaProjektu)
        
        if(czyProjektIstnieje):
            Bazy.polaczZBaza(nazwaProjektu)
        else:
            return Pliki.stworzPlikZOdpowiedzia()   #niepoprawna nazwa projektu
        
        login: str = zapytanie[2]
        token: str = zapytanie[3]
        nazwaPokoju: str = zapytanie[4]
        dodawaneTaski: typing.List[typing.Tuple[int,str,typing.Tuple[int,int,int],typing.Tuple[float,float],typing.List[int]]] = zapytanie[5]
        usuwaneTaski: typing.List[typing.Tuple[int,str,typing.Tuple[int,int,int],typing.Tuple[float,float],typing.List[int]]] = zapytanie[6]
        modyfikowaneTaski: typing.List[typing.Tuple[int,str,typing.Tuple[int,int,int],typing.Tuple[float,float],typing.List[int]]] = zapytanie[7]
        
        
        if((not Nazwy.przetestujNazwe(login)) or (not Kody.przetestujKod(token))):
            return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True)   #niepoprawne dane
        
        if(not Nazwy.przetestujNazwe(nazwaPokoju)):
            return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True, poprawnoscDanych=True)   #niepoprawna nazwa pokoju
        
        i: int = 0
        while(i<len(dodawaneTaski)):
            if(Nazwy.przetestujNazwe(dodawaneTaski[i][1])):
                i+=1
            else:
                if(i<len(dodawaneTaski)):
                    dodawaneTaski=dodawaneTaski[:i]+dodawaneTaski[i+1:]
                else:
                    dodawaneTaski=dodawaneTaski[:i]

        i=0
        while(i<len(usuwaneTaski)):
            if(Nazwy.przetestujNazwe(usuwaneTaski[i][1])):
                i+=1
            else:
                if(i<len(usuwaneTaski)):
                    usuwaneTaski=usuwaneTaski[:i]+usuwaneTaski[i+1:]
                else:
                    usuwaneTaski=usuwaneTaski[:i]
        
        i=0
        while(i<len(modyfikowaneTaski)):
            if(Nazwy.przetestujNazwe(modyfikowaneTaski[i][1])):
                i+=1
            else:
                if(i<len(modyfikowaneTaski)):
                    modyfikowaneTaski=modyfikowaneTaski[:i]+modyfikowaneTaski[i+1:]
                else:
                    modyfikowaneTaski=modyfikowaneTaski[:i]
                
        
        rezultat: typing.Tuple[bool,bool] = Taski.obslugaTaskow(login,token,nazwaPokoju,[dodawaneTaski,usuwaneTaski,modyfikowaneTaski])
        nowaListaTaskow: typing.List[str] = (Taski.pobierzTaski(login,token,nazwaPokoju))[2]
        
        Bazy.rozlaczZBaza()
        return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True, poprawnoscDanych=rezultat[0], sukcesOperacji=rezultat[1], dane=nowaListaTaskow)
    
    
    
    elif(operacja=="pobierz taski"):
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
        
        if(not Nazwy.przetestujNazwe(nazwaPokoju)):
            return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True, poprawnoscDanych=True)   #niepoprawna nazwa pokoju    
        
        rezultat: typing.Tuple[bool,bool,typing.List[str]] = Taski.pobierzTaski(login,token,nazwaPokoju)
        
        Bazy.rozlaczZBaza()
        return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True, poprawnoscDanych=rezultat[0], sukcesOperacji=rezultat[1], dane=rezultat[2])
    
    
    
    elif(operacja=="zaznacz task"):
        czyProjektIstnieje: bool = Bazy.czyBazaIstnieje(nazwaProjektu)
        
        if(czyProjektIstnieje):
            Bazy.polaczZBaza(nazwaProjektu)
        else:
            return Pliki.stworzPlikZOdpowiedzia()   #niepoprawna nazwa projektu
        
        login: str = zapytanie[2]
        token: str = zapytanie[3]
        nazwaPokoju: str = zapytanie[4]
        idTaska: int = zapytanie[5]
        
        if((not Nazwy.przetestujNazwe(login)) or (not Kody.przetestujKod(token))):
            return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True)   #niepoprawne dane
        
        if(not Nazwy.przetestujNazwe(nazwaPokoju)):
            return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True, poprawnoscDanych=True)   #niepoprawna nazwa pokoju    
        
        rezultat: typing.Tuple[bool,bool,bool] = Taski.oznaczJakoWykonany(login,token,nazwaPokoju,idTaska)
        nowaListaTaskow: typing.List[str] = (Taski.pobierzTaski(login,token,nazwaPokoju))[2]
        
        Bazy.rozlaczZBaza()
        return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True, poprawnoscDanych=rezultat[0], sukcesOperacji=(rezultat[1] and rezultat[2]), dane=nowaListaTaskow)
    
    
    
    elif(operacja=="odznacz task"):
        czyProjektIstnieje: bool = Bazy.czyBazaIstnieje(nazwaProjektu)
        
        if(czyProjektIstnieje):
            Bazy.polaczZBaza(nazwaProjektu)
        else:
            return Pliki.stworzPlikZOdpowiedzia()   #niepoprawna nazwa projektu
        
        login: str = zapytanie[2]
        token: str = zapytanie[3]
        nazwaPokoju: str = zapytanie[4]
        idTaska: int = zapytanie[5]
        
        if((not Nazwy.przetestujNazwe(login)) or (not Kody.przetestujKod(token))):
            return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True)   #niepoprawne dane
        
        if(not Nazwy.przetestujNazwe(nazwaPokoju)):
            return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True, poprawnoscDanych=True)   #niepoprawna nazwa pokoju    
        
        rezultat: typing.Tuple[bool,bool,bool] = Taski.oznaczJakoNiewykonany(login,token,nazwaPokoju,idTaska)
        nowaListaTaskow: typing.List[str] = (Taski.pobierzTaski(login,token,nazwaPokoju))[2]
        
        Bazy.rozlaczZBaza()
        return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True, poprawnoscDanych=rezultat[0], sukcesOperacji=(rezultat[1] and rezultat[2]), dane=nowaListaTaskow)
    
    
    elif(operacja=="pobierz chat"):
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
        
        if(not Nazwy.przetestujNazwe(nazwaPokoju)):
            return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True, poprawnoscDanych=True)   #niepoprawna nazwa pokoju    
        
        rezultat: typing.Tuple[bool,bool,typing.List[str]] = Chaty.pobierzChat(login,token,nazwaPokoju)
        
        Bazy.rozlaczZBaza()
        return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True, poprawnoscDanych=rezultat[0], sukcesOperacji=rezultat[1], dane=rezultat[2])
    
    
    elif(operacja=="zaktualizuj chat"):
        czyProjektIstnieje: bool = Bazy.czyBazaIstnieje(nazwaProjektu)
        
        if(czyProjektIstnieje):
            Bazy.polaczZBaza(nazwaProjektu)
        else:
            return Pliki.stworzPlikZOdpowiedzia()   #niepoprawna nazwa projektu
        
        login: str = zapytanie[2]
        token: str = zapytanie[3]
        nazwaPokoju: str = zapytanie[4]  
        ostatniaPosiadana: typing.Tuple[str,int] = [zapytanie[5],zapytanie[6]]
        
        if((not Nazwy.przetestujNazwe(login)) or (not Kody.przetestujKod(token))):
            return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True)   #niepoprawne dane
        
        if((not Nazwy.przetestujNazwe(nazwaPokoju)) or (not Nazwy.przetestujNazwe(zapytanie[5]))):
            return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True, poprawnoscDanych=True)   #niepoprawna nazwa pokoju    
        
        rezultat: typing.Tuple[bool,bool,typing.List[str]] = Chaty.zaktualizujChat(login,token,nazwaPokoju,ostatniaPosiadana)
        
        Bazy.rozlaczZBaza()
        return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True, poprawnoscDanych=rezultat[0], sukcesOperacji=rezultat[1], dane=rezultat[2])
    
    
    elif(operacja=="wyslij wiadomosc"):
        czyProjektIstnieje: bool = Bazy.czyBazaIstnieje(nazwaProjektu)
        
        if(czyProjektIstnieje):
            Bazy.polaczZBaza(nazwaProjektu)
        else:
            return Pliki.stworzPlikZOdpowiedzia()   #niepoprawna nazwa projektu
        
        login: str = zapytanie[2]
        token: str = zapytanie[3]
        nazwaPokoju: str = zapytanie[4]  
        ostatniaPosiadana: typing.Tuple[str,int] = [zapytanie[5],zapytanie[6]]
        wiadomosc: typing.Tuple[str,int] = [zapytanie[7],zapytanie[8]]
        
        if((not Nazwy.przetestujNazwe(login)) or (not Kody.przetestujKod(token))):
            return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True)   #niepoprawne dane
        
        if((not Nazwy.przetestujNazwe(nazwaPokoju)) or (not Nazwy.przetestujNazwe(zapytanie[5]))):
            return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True, poprawnoscDanych=True)   #niepoprawna nazwa pokoju    
        
        wiadomosc[0]=Nazwy.zabezpieczCudzyslowy(wiadomosc[0])
        rezultat: typing.Tuple[bool,bool,typing.List[str]] = Chaty.wyslijWiadomosc(login,token,nazwaPokoju,ostatniaPosiadana,wiadomosc)
        
        Bazy.rozlaczZBaza()
        return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True, poprawnoscDanych=rezultat[0], sukcesOperacji=rezultat[1], dane=rezultat[2])
    
    
    elif(operacja=="pobierz kalendarz"):
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
        
        if(not Nazwy.przetestujNazwe(nazwaPokoju)):
            return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True, poprawnoscDanych=True)   #niepoprawna nazwa pokoju    
        
        rezultat: typing.Tuple[bool,bool,typing.List[str]] = Kalendarz.pobierzKalendarz(login,token,nazwaPokoju)
        
        Bazy.rozlaczZBaza()
        return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True, poprawnoscDanych=rezultat[0], sukcesOperacji=rezultat[1], dane=rezultat[2])
    
    
    elif(operacja=="dodawanie wpisu kalendarza"):
        czyProjektIstnieje: bool = Bazy.czyBazaIstnieje(nazwaProjektu)
        
        if(czyProjektIstnieje):
            Bazy.polaczZBaza(nazwaProjektu)
        else:
            return Pliki.stworzPlikZOdpowiedzia()   #niepoprawna nazwa projektu
        
        login: str = zapytanie[2]
        token: str = zapytanie[3]
        nazwaPokoju: str = zapytanie[4]
        wpis: typing.Tuple[str,typing.Tuple[int,int,int]] = [zapytanie[5],zapytanie[6]]
        
        if((not Nazwy.przetestujNazwe(login)) or (not Kody.przetestujKod(token))):
            return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True)   #niepoprawne dane
        
        if((not Nazwy.przetestujNazwe(nazwaPokoju)) or (not Nazwy.przetestujNazwe(dodawanyUzytkownik))):
            return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True, poprawnoscDanych=True)   #niepoprawna nazwa pokoju lub login dodawanego użytkownika
        
        wpis[0]=Nazwy.zabezpieczCudzyslowy(wpis[0])
        rezultat: typing.Tuple[bool,bool,bool] = Kalendarz.dodajDoKalendarza(login,token,nazwaPokoju,wpis)
        
        Bazy.rozlaczZBaza()
        return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True, poprawnoscDanych=rezultat[0], sukcesOperacji=(rezultat[1] and rezultat[2]))
    
    
    elif(operacja=="usuwanie wpisu kalendarza"):
        czyProjektIstnieje: bool = Bazy.czyBazaIstnieje(nazwaProjektu)
        
        if(czyProjektIstnieje):
            Bazy.polaczZBaza(nazwaProjektu)
        else:
            return Pliki.stworzPlikZOdpowiedzia()   #niepoprawna nazwa projektu
        
        login: str = zapytanie[2]
        token: str = zapytanie[3]
        nazwaPokoju: str = zapytanie[4]
        wpis: typing.Tuple[str,typing.Tuple[int,int,int]] = [zapytanie[5],zapytanie[6]]
        
        if((not Nazwy.przetestujNazwe(login)) or (not Kody.przetestujKod(token))):
            return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True)   #niepoprawne dane
        
        if((not Nazwy.przetestujNazwe(nazwaPokoju)) or (not Nazwy.przetestujNazwe(dodawanyUzytkownik))):
            return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True, poprawnoscDanych=True)   #niepoprawna nazwa pokoju lub login dodawanego użytkownika
        
        wpis[0]=Nazwy.zabezpieczCudzyslowy(wpis[0])
        rezultat: typing.Tuple[bool,bool] = Kalendarz.usunZKalendarza(login,token,nazwaPokoju,wpis)
        
        Bazy.rozlaczZBaza()
        return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True, poprawnoscDanych=rezultat[0], sukcesOperacji=rezultat[1])
    
    
    elif(operacja=="modyfikacja wpisu kalendarza"):
        czyProjektIstnieje: bool = Bazy.czyBazaIstnieje(nazwaProjektu)
        
        if(czyProjektIstnieje):
            Bazy.polaczZBaza(nazwaProjektu)
        else:
            return Pliki.stworzPlikZOdpowiedzia()   #niepoprawna nazwa projektu
        
        login: str = zapytanie[2]
        token: str = zapytanie[3]
        nazwaPokoju: str = zapytanie[4]
        wpis: typing.Tuple[str,typing.Tuple[int,int,int]] = [zapytanie[5],zapytanie[6]]
        noweDane: typing.Tuple[str,typing.Tuple[int,int,int]] = [zapytanie[7],zapytanie[8]]
        
        if((not Nazwy.przetestujNazwe(login)) or (not Kody.przetestujKod(token))):
            return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True)   #niepoprawne dane
        
        if((not Nazwy.przetestujNazwe(nazwaPokoju)) or (not Nazwy.przetestujNazwe(dodawanyUzytkownik))):
            return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True, poprawnoscDanych=True)   #niepoprawna nazwa pokoju lub login dodawanego użytkownika
        
        wpis[0]=Nazwy.zabezpieczCudzyslowy(wpis[0])
        noweDane[0]=Nazwy.zabezpieczCudzyslowy(noweDane[0])
        rezultat: typing.Tuple[bool,bool,bool] = Kalendarz.modyfikujWpisKalendarza(login,token,nazwaPokoju,wpis,noweDane)
        
        Bazy.rozlaczZBaza()
        return Pliki.stworzPlikZOdpowiedzia(poprawnyProjekt=True, poprawnoscDanych=rezultat[0], sukcesOperacji=(rezultat[1] and rezultat[2]))
    
    
    #tu w przyszłości dalsze operacje
    
    else:              #nieznana operacja
        return Pliki.stworzPlikZOdpowiedzia()