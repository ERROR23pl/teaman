import typing

def analizaPliku(otrzymanyPlik) -> typing.List:
    #TODO tutaj w przyszłości będzie analiza informacji otrzymanych od klienta w żądaniu i zamiana w informacje dla serwera
    
    #return ["operacja","nazwa serwera","dane"]
    return otrzymanyPlik


def stworzPlikZOdpowiedzia(poprawnyProjekt: bool = False, poprawnoscDanych: bool = False, sukcesOperacji: bool = False, dane: typing.List = [""]):
    #TODO tutaj w przyszłości będzie tworzony na podstawie wprowadzonych danych plik odpowiedzi do klienta
    
    return poprawnyProjekt,poprawnoscDanych,sukcesOperacji,dane