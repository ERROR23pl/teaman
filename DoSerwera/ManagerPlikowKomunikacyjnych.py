import typing
import json

def analizaPliku(otrzymanyPlik) -> typing.List:
    #TODO tutaj w przyszłości będzie analiza informacji otrzymanych od klienta w żądaniu i zamiana w informacje dla serwera
    
    return ["operacja","nazwa serwera","dane"]


def stworzPlikZOdpowiedzia(sukcesOperacji: bool, dane: typing.List[str]):
    slownik: dict = {}
    slownik['sukces'] = sukcesOperacji
    
    if(not sukcesOperacji):
        slownik['blad'] = dane[0]
    
    else:
        slownik['dane'] = dane
    
    with open("odpowiedz.json",'w') as plikZOdp:
        json.dump(slownik,plikZOdp)
    
    return plikZOdp