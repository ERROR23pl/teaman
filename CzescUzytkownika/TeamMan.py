import socket
import typing
import ManagerHasel as Hasla
import ManagerKodow as Kody
import ManagerNazw as Nazwy
import Logowanie

adresSerwera: typing.Tuple = ["localhost",8000]     #w przyszłości będzie zmienione na adres
token: str                                          #tu po zalogowaniu będzie zapisywany token sesji
nazwaUzytkownika: str                               #tu po zalogowaniu będzie zapisywana nazwa użytkownika
nazwaProjektu: str                                  #tu po zalogowaniu będzie zapisywana nazwa projektu, do którego się podłączono
GUI: None                                           #GUI interaktywne


    