import socket
import typing
import hashlib as hash
import ManagerHasel as Hasla
import ManagerKodow as Kody
import ManagerNazw as Nazwy
import AnalizyOdpowiedzi as Analizy



def probaRejestracji(adresSerwera: typing.Tuple[str,int], projekt: str, kodZapr: str, login: str, haslo: str, powtHaslo: str) -> typing.Tuple[str, str]:    #w przypadku sukcesu zwraca token sesji oraz (dla celów wizualnych) rolę w projekcie
    if (projekt=="" or login=="" or haslo==""):
        raise NameError("PustePole")
    if(haslo!=powtHaslo):
        raise NameError("RozneHasla")
    if (not Nazwy.przetestujNazwe(projekt)):
        raise NameError("ZlaNazwaProjektu")
    if (not Nazwy.przetestujNazwe(login)):
        raise NameError("ZlyLogin")
    if(not Kody.przetestujKod(kodZapr)):
        raise NameError("ZlyKod")
    if (not Hasla.czyBrakZabronionychZnakow(haslo)):
        raise NameError("ZlyZnakWHasle")
    if (not Hasla.poprawnoscHasla(haslo)):
        raise NameError("ZleHaslo")
    
    try:
        serwer: socket.socket = socket.create_connection(adresSerwera)
        
        #poinformuj, że akcją jest tworzenie projektu
        
        serwer.sendall(projekt)                                                             #TODO póżniej zmienić w rzeczywistą wersję
        czyProjektIstnieje: bool = Analizy.analizaTrueFalse(serwer.recv(4096))              #TODO póżniej zmienić w rzeczywistą wersję
        
        if(czyProjektIstnieje):
            raise NameError("__ProjIstnieje")
        
        serwer.sendall(hash.sha3_512(login),hash.sha3_512(haslo))                           #TODO póżniej zmienić w rzeczywistą i dodatkowo zaszyfrowaną wersję
        odpowiedz: bytes = serwer.recv(4096)
        rezultat: typing.Tuple = Analizy.analizaBoolStr(odpowiedz)
        
        serwer.close()
        return rezultat[1], "Właściciel zespołu"
    
    except NameError as error:
        if(str(error)[:2]=="__"):
            raise NameError(str(error)[2:])
        else:
            raise NameError("BladPolZSerwerem")