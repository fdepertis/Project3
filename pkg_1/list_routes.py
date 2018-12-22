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

from ..timetable import Timetable
import datetime

def list_routes(t, a, b, actual_time, max_time):
    if type(t) is not Timetable:
        raise TypeError("t must be Timetable typed.")
    if type(a) is not type(b) is not Timetable.Airport:
        raise TypeError("a and b must be Timetable.Airport typed.")
    if type(actual_time) is not datetime.time:
        raise TypeError("actual_time must be datetime.time typed.")
    if type(max_time) is not datetime.timedelta:
        raise TypeError("max_time must be datetime.timedelta typed.")
    routes = dict()
    _list_routes_aux(t, a, b, actual_time, max_time, routes)
    return routes


def _list_routes_aux(t, a, b, actual_time, max_time, routes):
    if a == b:
        return
    else:
        for f in t.incident_edges(a):
            o = f.opposite(a)
            routes[o] = f
            if f.l() > actual_time + a.c() or f.a() < max_time:
                _list_routes_aux(t, o, b, o.a(), max_time, routes)
