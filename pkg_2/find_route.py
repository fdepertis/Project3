"""
Progettare una funzione find_route() che, preso in input l’orario della compagnia,
gli areoporti a e b, ed un orario di partenza t, trova la rotta che permette di arrivare
da a a b nel minor tempo possibile, partendo ad un orario non precedente a t. (Come
per l’esercizio precedente, bisogna tener conto del tempo minimo di coincidenza di
ogni scalo).
"""

from Project3.timetable import Timetable
from Project3.TdP_collections.priority_queue.adaptable_heap_priority_queue import AdaptableHeapPriorityQueue
import datetime


def find_route(timetable, a, b, t):
    if type(timetable) is not Timetable:
        raise TypeError("timetable must be Timetable typed.")
    if type(a) is not type(b) is not Timetable.Airport:
        raise TypeError("a and b must be Timetable.Airport typed.")
    if type(t) is not datetime.datetime:
        raise TypeError("t must be datetime.datetime typed.")
    else:
        d = dict()              #used to map airports with arrival times
        q = dict()              #same of d, but this is used as queue
        routes = dict()         #used to map airports with routes
        cloud = set()           #used to set an airport as discovered

        for airport in timetable.airports():
            if airport is a:
                d[airport] = t
                q[airport] = t
            else:
                d[airport] = datetime.datetime(5000, 1, 1, 0, 0, 0)
                q[airport] = datetime.datetime(5000, 1, 1, 0, 0, 0)
            routes[airport] = []

        while len(q) > 0:
            airport = min(q, key=q.get)
            cloud.add(airport)
            del q[airport]
            for f in timetable.incident_flights_reversed(airport):
                if f.l() > d[airport] + f.s().c():
                    w = f.opposite(airport)
                    if w not in cloud:
                        if len(routes[w]) == 0 or routes[w][-1].a() > f.a():
                            routes[w].clear()
                            for flight in routes[airport]:
                                routes[w].append(flight)
                            routes[w].append(f)
                            d[w] = f.a()
                            if w in q:
                                q[w] = f.a()
                else:
                    break
        return routes[b]
