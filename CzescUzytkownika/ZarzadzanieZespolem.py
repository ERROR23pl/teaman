import socket
import typing
import ManagerKodow as Kody
import ManagerNazw as Nazwy
import AnalizyOdpowiedzi as Analizy


def probaZaproszenia(adresSerwera: typing.Tuple[str,int], projekt: str, login: str, tokenSesji: str) -> str:    #w przypadku sukcesu zwraca kod zaproszeniowy
    if (projekt==""):
        raise NameError("NiepolZProj")
    if(tokenSesji==""):
        raise NameError("BrakTokenu")
    if (not Nazwy.przetestujNazwe(projekt)):
        raise NameError("ZlaNazwaProjektu")
    if (not Nazwy.przetestujNazwe(login)):
        raise NameError("ZlyLogin")
    if(not Kody.przetestujKod(tokenSesji)):
        raise NameError("ZlyToken")
    
    try:
        serwer: socket.socket = socket.create_connection(adresSerwera)
        
        #poinformuj, że akcją jest zapraszanie do projektu
        
        serwer.sendall(projekt)                                                     #TODO póżniej zmienić w rzeczywistą wersję
        czyProjektIstnieje: bool = Analizy.analizaTrueFalse(serwer.recv(4096))      #TODO póżniej zmienić w rzeczywistą wersję
        
        if(not czyProjektIstnieje):
            raise NameError("__ProjNieIstnieje")
        
        serwer.sendall(login,tokenSesji)                                            #TODO póżniej zmienić w rzeczywistą i zaszyfrowaną wersję
        czyTokenPopr: bool = Analizy.analizaTrueFalse(serwer.recv(4096))            #TODO póżniej zmienić w rzeczywistą wersję
        
        if(not czyTokenPopr):
            raise NameError("__TokenNiepopr")
        
        kodZapr: str = Kody.wygenerujKod()
        serwer.sendall(kodZapr)                                                     #TODO póżniej zmienić w rzeczywistą i zaszyfrowaną wersję
        czySukces: bool = Analizy.analizaTrueFalse(serwer.recv(4096))
        while (not czySukces):
            kodZapr = Kody.wygenerujKod()
            serwer.sendall(kodZapr)                                                 #TODO póżniej zmienić w rzeczywistą i zaszyfrowaną wersję
            czySukces = Analizy.analizaTrueFalse(serwer.recv(4096))
        
        serwer.close()
        return kodZapr
    
    except NameError as error:
        if(str(error)[:2]=="__"):
            raise NameError(str(error)[2:])
        else:
            raise NameError("BladPolZSerwerem")



def probaUsunieciaProjektu(adresSerwera: typing.Tuple[str,int], projekt: str, login: str, tokenSesji: str) -> bool:    #w przypadku sukcesu zwraca True
    if (projekt==""):
        raise NameError("NiepolZProj")
    if(tokenSesji==""):
        raise NameError("BrakTokenu")
    if (not Nazwy.przetestujNazwe(projekt)):
        raise NameError("ZlaNazwaProjektu")
    if (not Nazwy.przetestujNazwe(login)):
        raise NameError("ZlyLogin")
    if(not Kody.przetestujKod(tokenSesji)):
        raise NameError("ZlyToken")
    
    try:
        serwer: socket.socket = socket.create_connection(adresSerwera)
        
        #poinformuj, że akcją jest usuwanie projektu
        
        serwer.sendall(projekt)                                                     #TODO póżniej zmienić w rzeczywistą wersję
        czyProjektIstnieje: bool = Analizy.analizaTrueFalse(serwer.recv(4096))      #TODO póżniej zmienić w rzeczywistą wersję
        
        if(not czyProjektIstnieje):
            raise NameError("__ProjNieIstnieje")
        
        serwer.sendall(login,tokenSesji)                                            #TODO póżniej zmienić w rzeczywistą i zaszyfrowaną wersję
        czyTokenPopr: bool = Analizy.analizaTrueFalse(serwer.recv(4096))            #TODO póżniej zmienić w rzeczywistą wersję
        
        if(not czyTokenPopr):
            raise NameError("__TokenNiepopr")

        else:
            serwer.close()
            return True
    
    except NameError as error:
        if(str(error)[:2]=="__"):
            raise NameError(str(error)[2:])
        else:
            raise NameError("BladPolZSerwerem")