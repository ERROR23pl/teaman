import typing
import json
import WydobywanieTaskow as Taski

def analizaPliku(otrzymanyPlik) -> typing.List:
    dekoder = json.JSONDecoder()
    dane : dict = dekoder.decode(otrzymanyPlik)
    
    if(str(dane['operacja'])!="modyfikacja taskow"):
        wartosci: typing.List = dane.values()
        return wartosci
    
    else:
        wartosci: typing.List = []
        dodawaneTaski: typing.List[typing.Tuple[int,str,typing.Tuple[int,int,int],typing.Tuple[float,float],typing.List[int]]] = []
        usuwaneTaski: typing.List[typing.Tuple[int,str,typing.Tuple[int,int,int],typing.Tuple[float,float],typing.List[int]]] = []
        zmienianeTaski: typing.List[typing.Tuple[int,str,typing.Tuple[int,int,int],typing.Tuple[float,float],typing.List[int]]] = []
        
        for wpis in dane:
            if("DodawanyTask" in str(wpis)):
                task = Taski.task(dane[wpis])
                dodawaneTaski.append(task)
            elif("UsuwanyTask" in str(wpis)):
                task = Taski.task(dane[wpis])
                usuwaneTaski.append(task)
            elif("ModyfikowanyTask" in str(wpis)):
                task = Taski.task(dane[wpis])
                zmienianeTaski.append(task)
            else:
                wartosci.append(dane[wpis])
        
        return wartosci+dodawaneTaski+usuwaneTaski+zmienianeTaski
            


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