import socket
import typing
import ManagerHasel as Hasla
import ManagerKodow as Kody
import ManagerNazw as Nazwy


def analizaOdpowiedzi(odpowiedz: bytes) -> typing.Tuple[bool, str, str]:                    #TODO
    #zmiana odpowiedzi serwera w [False,"",""] lub [True, odszyfrowany token sesji, rola]
    return [False,"",""]    #tymczasowo


def probaLogowania(adresSerwera: typing.Tuple[str,int], projekt: str, login: str, haslo: str) -> typing.Tuple[str, str]:
    if (projekt=="" or login=="" or haslo==""):
        raise NameError("PustePole")
    if (not Nazwy.przetestujNazwe(projekt)):
        raise NameError("ZlaNazwaProjektu")
    if (not Nazwy.przetestujNazwe(login)):
        raise NameError("ZlyLogin")
    if (not Hasla.czyBrakZabronionychZnakow(haslo)):
        raise NameError("ZlyZnakWHasle")
    
    try:
        serwer: socket.socket = socket.create_connection(adresSerwera)
        serwer.sendall(projekt)                                             #TODO póżniej zmienić w rzeczywistą wersję
        czyProjektIstnieje: bool = bool(serwer.recv(4096))                  #TODO póżniej zmienić w rzeczywistą wersję
        
        if(not czyProjektIstnieje):
            raise NameError("__ProjNieIstnieje")
        
        serwer.sendall(login,haslo)                                         #TODO póżniej zmienić w rzeczywistą i zaszyfrowaną wersję
        odpowiedz: bytes = serwer.recv(4096)
        rezultat: typing.Tuple = analizaOdpowiedzi(odpowiedz)
        
        if(not rezultat[0]):
            raise NameError("__NieudaneLogowanie")
        else:
            serwer.close
            return rezultat[1], rezultat[2]
    
    except NameError as error:
        if(str(error)[:2]=="__"):
            raise NameError(str(error)[2:])
        else:
            raise NameError("BladPolZSerwerem")