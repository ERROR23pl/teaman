import typing
import Logowanie as Log
import Rejestrowanie as Rej
import TworzenieProjektu as TworzProj
import ZarzadzanieZespolem as ZarzZesp
import WysylanieDoGUI as WysylGUI


adresSerwera: typing.Tuple = ["localhost",8000]     #w przyszłości będzie zmienione na adres
token: str                                          #tu po zalogowaniu będzie zapisywany token sesji
nazwaUzytkownika: str                               #tu po zalogowaniu będzie zapisywana nazwa użytkownika
nazwaProjektu: str                                  #tu po zalogowaniu będzie zapisywana nazwa projektu, do którego się podłączono
GUI: None                                           #GUI interaktywne


    