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
        discovered_airports = dict()
        discovered_flights = set()
        for airport in timetable.airports():
            discovered_airports[airport] = []
        _find_route_aux(timetable, a, b, t, discovered_airports, discovered_flights)
        return discovered_airports[b]



def _find_route_aux(timetable, a, b, t, discovered_airports, discovered_flights):
    if a == b:
        return
    else:
        for f in timetable.incident_flights(a):
            if f not in discovered_flights:
                discovered_flights.add(f)
                if f.l() > t + f.s().c():               #check if you can take the flight
                    w = f.opposite(a)
                    if len(discovered_airports[w]) == 0:
                        discovered_airports[w].append(f)
                    elif discovered_airports[w][len(discovered_airports)-1].a() > f.a():
                        discovered_airports[w].clear()
                        discovered_airports[w] = discovered_airports[a]
                        discovered_airports[w].append(f)

