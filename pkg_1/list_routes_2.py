"""
Progettare una funzione list_routes() che, preso in input l’orario della compagnia,
gli areoporti a e b, un orario di partenza t ed un intervallo di tempo T, restituisce
tutte le rotte che consentono di andare da a a b con un durata complessiva del
viaggio non superiore a T e con orario di partenza successivo a t. Una rotta è
costituita da una sequenza di voli e la sua durata è data dalla somma delle durate di
tutti i voli più i tempi di attesa negli scali per le coincidenze. Ad ogni scalo bisogna
considerare che non è possibile effettuare una coincidenza se tra l’orario di
atterraggio di un volo ed il tempo di decollo del volo successivo intercorre un tempo
inferiore a c(a).
"""

from Project3.pkg_1.timetable_1 import Timetable
import datetime


def list_routes(timetable, a, b, t, T):
    if type(timetable) is not Timetable:
        raise TypeError("timetable must be Timetable typed.")
    if type(a) is not type(b) is not Timetable.Airport:
        raise TypeError("a and b must be Timetable.Airport typed.")
    if type(t) is not datetime.datetime:
        raise TypeError("t must be datetime.datetime typed.")
    if type(T) is not datetime.timedelta:
        raise TypeError("T must be datetime.timedelta typed.")
    else:
        routes = dict()
        discovered = set()

        for airport in timetable.airports():
            routes[airport] = []
        _list_routes_aux(timetable, a, b, t, t+T, routes, discovered)

        return routes[b]


def _list_routes_aux(timetable, a, b, t, max_arrival_time, routes, discovered):
    if a is b:
        return
    else:
        for f in timetable.incident_flights_reversed(a):
            if f.l() >= t + f.s().c():
                # if departure time is greater than actual time + coincidence time
                if f.a() <= max_arrival_time and f not in discovered:
                    # if arrival time is smaller than max arrival time and flight has not been discovered yet

                    discovered.add(f)                                                           # mark it as discovered
                    w = f.opposite(a)                                                           # take opposite airport

                    if len(routes[a]) == 0:
                        routes[w].append([])
                        routes[w][-1].append(f)
                    # this condition is needed for airports adjacent to 'a', because 'a' has an empty route

                    else:
                        for i in range(len(routes[a])):
                            routes[w].append([])
                            routes[w][-1] += routes[a][i]
                            routes[w][-1].append(f)
                    # in every case, you tell to an airport that can be reached
                    # using the same path of the previous, then adding 'f'

                    _list_routes_aux(timetable, w, b, f.a(), max_arrival_time, routes, discovered)
                    # at the end, it launch recursion on same timetable, opposite airport, same destination,
                    # arrival time of taken flight, same max arrival time and same dict and set
            else:
                break
