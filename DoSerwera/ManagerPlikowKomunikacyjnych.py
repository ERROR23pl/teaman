import typing
import json
import Obiekty as o

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
        dodawaneTaski: typing.List[o.Task] = []
        usuwaneTaski: typing.List[o.Task] = []
        zmienianeTaski: typing.List[o.Task] = []
        
        for wpis in dane:
            if("DodawanyTask" in str(wpis)):
                try:
                    nowyTask: o.Task = o.Task(dane[wpis][0],dane[wpis][1],dane[wpis][2],dane[wpis][3],dane[wpis][4],dane[wpis][5])
                    dodawaneTaski.append(nowyTask)
                except:
                    None
            elif("UsuwanyTask" in str(wpis)):
                try:
                    nowyTask: o.Task = o.Task(dane[wpis][0],dane[wpis][1],dane[wpis][2],dane[wpis][3],dane[wpis][4],dane[wpis][5])
                    usuwaneTaski.append(nowyTask)
                except:
                    None
            elif("ModyfikowanyTask" in str(wpis)):
                try:
                    nowyTask: o.Task = o.Task(dane[wpis][0],dane[wpis][1],dane[wpis][2],dane[wpis][3],dane[wpis][4],dane[wpis][5])
                    zmienianeTaski.append(nowyTask)
                except:
                    None
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