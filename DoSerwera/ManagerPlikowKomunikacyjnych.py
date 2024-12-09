import typing
import json

def analizaPliku(otrzymanyPlik) -> typing.List:
    dekoder = json.JSONDecoder()
    dane : dict = dekoder.decode(otrzymanyPlik)
    
    if(str(dane['operacja'])!="modyfikacja taskow"):
        wartosci: typing.List = []
        for wpis in dane:
            wartosci.append(dane[wpis])
        return wartosci
    
    else:
        wartosci: typing.List = []
        dodawaneTaski: typing.List[typing.Tuple[int,str,typing.Tuple[int,int,int],typing.Tuple[float,float],typing.List[int]]] = []
        usuwaneTaski: typing.List[typing.Tuple[int,str,typing.Tuple[int,int,int],typing.Tuple[float,float],typing.List[int]]] = []
        zmienianeTaski: typing.List[typing.Tuple[int,str,typing.Tuple[int,int,int],typing.Tuple[float,float],typing.List[int]]] = []
        
        for wpis in dane:
            if("DodawanyTask" in str(wpis)):
                dodawaneTaski.append(dane[wpis])
            elif("UsuwanyTask" in str(wpis)):
                usuwaneTaski.append(dane[wpis])
            elif("ModyfikowanyTask" in str(wpis)):
                zmienianeTaski.append(dane[wpis])
            else:
                wartosci.append(dane[wpis])
        
        wartosci.append(dodawaneTaski)
        wartosci.append(usuwaneTaski)
        wartosci.append(zmienianeTaski)
        return wartosci
            


def stworzPlikZOdpowiedzia(sukcesOperacji: bool, dane: typing.List[str]):
    slownik: dict = {}
    slownik['sukces'] = sukcesOperacji
    
    if(not sukcesOperacji):
        slownik['blad'] = dane[0]
    
    else:
        for i in range(len(dane)):
            slownik['dana'+str(i+1)] = dane[i]
    
    koder = json.JSONEncoder(ensure_ascii=False)
    return koder.encode(slownik)