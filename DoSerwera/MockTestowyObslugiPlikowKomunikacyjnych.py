import typing
import json

def analizaPliku(otrzymanyPlik) -> typing.List:
    #TODO tutaj w przyszłości będzie analiza informacji otrzymanych od klienta w żądaniu i zamiana w informacje dla serwera
    
    #return ["operacja","nazwa serwera","dane"]
    return otrzymanyPlik


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