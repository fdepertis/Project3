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
        discovered_airports = dict()            #dictionary used to map airports (keys) with routes (values)
        discovered_flights = set()              #set used to check if a flight is already taken
        for airport in timetable.airports():
            discovered_airports[airport] = []   #set an empty list for every airport in discovered_airports
        _find_route_aux(timetable, a, b, t, discovered_airports, discovered_flights)    #recursive function
        return discovered_airports[b]           #return best route for b


def _find_route_aux(timetable, a, b, t, discovered_airports, discovered_flights):
    if a == b:
        return                                          #if it has arrived in b, it returns
    else:
        for f in timetable.incident_flights(a):         #for each incident outgoing flight of a
            if f not in discovered_flights:             #if this flight has not taken yet
                discovered_flights.add(f)               #take it
                if f.l() > t + f.s().c():               #check if you can take the flight
                    w = f.opposite(a)
                    #if is the first time you find this airport, tell it a new flight to reach it.
                    if len(discovered_airports[w]) == 0:
                        discovered_airports[w].append(f)
                    #else, if you found a faster sequence of flights to reach it, update its routes
                    elif discovered_airports[w][len(discovered_airports)-1].a() > f.a():
                        discovered_airports[w].clear()
                        discovered_airports[w] = discovered_airports[a]
                        discovered_airports[w].append(f)
                    #run again this function with same timetable, opposite airport, b, arrival time of this flight, ...
                    _find_route_aux(timetable, w, b, f.a(), discovered_airports, discovered_flights)

