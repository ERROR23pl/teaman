import socket
import typing
import ManagerHasel as Hasla
import ManagerKodow as Kody
import ManagerNazw as Nazwy
import Logowanie

adresSerwera: typing.Tuple = ["localhost",8000]    #w przyszłości będzie zmienione na adres
token: str                              #tu po zalogowaniu będzie zapisywany token sesji
nazwaUzytkownika: str                   #tu po zalogowaniu będzie zapisywana nazwa użytkownika
nazwaProjektu: str                      #tu po zalogowaniu będzie zapisywana nazwa projektu, do którego się podłączono


def wyslijBladDoGUI(blad: NameError):
    kodBledu: str = str(blad)
    komunikat: str
    
    if(kodBledu=="PustePole"):
        komunikat="Żadne pole nie może być puste!"
    elif(kodBledu=="ZlaNazwaProjektu"):
        komunikat="Podana nazwa projektu nie jest poprawna - nazwa musi mieć minimum dziesięć znaków i może składać się tylko z liter, cyfr oraz znaku '_'!"
