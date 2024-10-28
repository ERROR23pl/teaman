import socket
import typing
import hashlib as hash
import ManagerHasel as Hasla
import ManagerKodow as Kody
import ManagerNazw as Nazwy


def analizaTrueFalse(odpowiedz: bytes) -> bool:         #TODO
    #zmiana odpowiedzi serwera w False lub True
    return True    #tymczasowo


def analizaOdpowiedzi(odpowiedz: bytes) -> typing.Tuple[bool, str]:                    #TODO
    #zmiana odpowiedzi serwera w [False,""] lub [True, odszyfrowany token sesji]
    return [False,""]    #tymczasowo


def probaZaproszenia(adresSerwera: typing.Tuple[str,int], projekt: str, login: str, tokenSesji: str) -> str:    #w przypadku sukcesu zwraca kod zaproszeniowy
    if (projekt==""):
        raise NameError("NiepolZProj")
    if(tokenSesji==""):
        raise NameError("BrakTokenu")
    if (not Nazwy.przetestujNazwe(projekt)):
        raise NameError("ZlaNazwaProjektu")
    
    if(not Kody.przetestujKod(tokenSesji)):
        raise NameError("ZlyToken")
    
    try:
        serwer: socket.socket = socket.create_connection(adresSerwera)
        serwer.sendall(projekt)                                             #TODO póżniej zmienić w rzeczywistą wersję
        czyProjektIstnieje: bool = analizaTrueFalse(serwer.recv(4096))      #TODO póżniej zmienić w rzeczywistą wersję
        
        if(not czyProjektIstnieje):
            raise NameError("__ProjNieIstnieje")
        
        serwer.sendall(tokenSesji)                                          #TODO póżniej zmienić w rzeczywistą i zaszyfrowaną wersję
        czyTokenPopr: bool = bool(serwer.recv(4096))                          #TODO póżniej zmienić w rzeczywistą wersję
        
        if(not czyKodPopr):
            raise NameError("__KodNieIstnieje")
        
        serwer.sendall(hash.sha3_512(login),hash.sha3_512(haslo))           #TODO póżniej zmienić w rzeczywistą i dodatkowo zaszyfrowaną wersję
        odpowiedz: bytes = serwer.recv(4096)
        rezultat: typing.Tuple = analizaOdpowiedzi(odpowiedz)
        
        if(not rezultat[0]):
            raise NameError("__LoginIstnieje")
        else:
            serwer.close
            return rezultat[1], "Członek zespołu"
    
    except NameError as error:
        if(str(error)[:2]=="__"):
            raise NameError(str(error)[2:])
        else:
            raise NameError("BladPolZSerwerem")