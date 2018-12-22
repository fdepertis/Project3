"""
Progettare una funzione find_route() che, preso in input l’orario della compagnia,
gli areoporti a e b, ed un orario di partenza t, trova la rotta che permette di arrivare
da a a b nel minor tempo possibile, partendo ad un orario non precedente a t. (Come
per l’esercizio precedente, bisogna tener conto del tempo minimo di coincidenza di
ogni scalo).
"""

from ..timetable import Timetable
import datetime

def find_route(timetable, a, b, t):
    if type(timetable) is not Timetable:
        raise TypeError("timetable must be Timetable typed.")
    if type(a) is not type(b) is not Timetable.Airport:
        raise TypeError("a and b must be Timetable.Airport typed.")
    if type(t) is not datetime.datetime:
        raise TypeError("t must be datetime.datetime typed.")
    else:
        discovered = {}
        for airport in timetable.airports():
            discovered[airport] = []
    pass