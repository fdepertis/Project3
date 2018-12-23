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
        discovered = set()                                  #set used to check already taken airports
        routes = dict()                                     #dictionary used to map airports (keys) with routes (values)
        routes[a] = None
        for airport in timetable.airports():
            if not airport == a:
                routes[airport] = []                        #set an empty list for every airport in discovered_airports
        _find_route_aux(timetable, a, b, t, routes, discovered)                                     #recursive function
        return routes[b]                                                                       #return best route for b


def _find_route_aux(timetable, a, b, t, routes, discovered):
    if a == b:
        return                                                                      #if it has arrived in b, it returns
    else:
        for f in timetable.incident_flights_reversed(a):                        #for each incident outgoing flight of a
            if f.l() > t + f.s().c():                                                 #check if you can take the flight
                w = f.opposite(a)
                #if you want to go from a to a, the best way is to take no flights
                if routes[w] is None:
                    pass
                #if is the first time you find this airport, tell it a new flight to reach it
                elif len(routes[w]) == 0:
                    routes[w].append(f)
                #else, if you found a faster sequence of flights to reach it, update its routes
                elif routes[w][-1].a() > f.a():
                    routes[w].clear()
                    routes[w] = routes[a]
                    routes[w].append(f)
                #run again this function with same timetable, opposite airport, b, arrival time of this flight, ...
                if w not in discovered:
                    discovered.add(w)
                    _find_route_aux(timetable, w, b, f.a(), routes, discovered)
            else:
                break
