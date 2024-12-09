import typing
import json
import WydobywanieTaskow as Taski

def analizaPliku(otrzymanyPlik) -> typing.List:
    with open(otrzymanyPlik,'r',encoding="utf-8") as plik:
        dane : dict = json.load(plik)
    
    if(str(dane['operacja'])!="modyfikacja taskow"):
        wartosci: typing.List = dane.values()
        return wartosci
    
    else:
        wartosci: typing.List = []
        dodawaneTaski: typing.List[typing.Tuple[int,str,typing.Tuple[int,int,int],typing.Tuple[float,float],typing.List[int]]] = []
        usuwaneTaski: typing.List[typing.Tuple[int,str,typing.Tuple[int,int,int],typing.Tuple[float,float],typing.List[int]]] = []
        zmienianeTaski: typing.List[typing.Tuple[int,str,typing.Tuple[int,int,int],typing.Tuple[float,float],typing.List[int]]] = []
        
        for wpis in dane:
            if("DodawanyTask" in str(wpis.key)):
                task = Taski.task(wpis.value)
                dodawaneTaski.append(task)
            elif("UsuwanyTask" in str(wpis.key)):
                task = Taski.task(wpis.value)
                usuwaneTaski.append(task)
            elif("ModyfikowanyTask" in str(wpis.key)):
                task = Taski.task(wpis.value)
                zmienianeTaski.append(task)
            else:
                wartosci.append(wpis.value)
        
        return wartosci+dodawaneTaski+usuwaneTaski+zmienianeTaski
            


def stworzPlikZOdpowiedzia(sukcesOperacji: bool, dane: typing.List[str]):
    slownik: dict = {}
    slownik['sukces'] = sukcesOperacji
    
    if(not sukcesOperacji):
        slownik['blad'] = dane[0]
    
    else:
        for i in range(len(dane)):
            slownik['dana'+str(i+1)] = dane[i]
    
    with open("odpowiedz.json",'w',encoding="utf-8") as plikZOdp:
        json.dump(slownik,plikZOdp)
    
    return plikZOdp