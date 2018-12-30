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
import datetime
from Project3.timetable import Timetable

counter = 0
def list_routes(timetable, a, b, t, T):

    if t + T <= list(timetable.incident_flights(a))[0].l():
        return None
    else:
        return list(dfs_paths(timetable, a, b, t, T, a))




def dfs_paths(timetable, start, goal, t, T, current, path_flights = None):
    global counter

    if path_flights is None:
        path_flights = []

    if current == goal:
        if path_flights[0].l() >= t and path_flights[len(path_flights)-1].l() <= t + T:
            yield path_flights

    for next in timetable[current] - set(path_flights):#O(deg v )

        if next.s() != start and path_flights[len(path_flights)-1].a() + next.s().c() > next.l():
            print("ECCO IL VOLO CON CUI SEI ARRIVATO NEL TUO ULTIMO AEREOPORTO")
            print(path_flights[len(path_flights)-1])
            print("ECCO IL VOLO CHE NON PUOI PRENDERE")
            print(next)
            print("NON LO PUOI PRENDERE PERCHE'")
            print(str(path_flights[len(path_flights)-1].a()) + " + " + str(next.s().c()) + " > " +  str(next.l()))
            print("NON CE LA FAI A PRENDERE LA COINCIDENZA")
            print("")

        if (next.s() != start and path_flights[len(path_flights)-1].a() + next.s().c() > next.l()):
            continue

        if next.l() < t + T:
            counter += 1
            yield from dfs_paths(timetable, start, goal, t, T, next.opposite(current), path_flights + [next])


if __name__ == '__main__':

    timetable = Timetable()
    a = timetable.insert_airport("A")
    b = timetable.insert_airport("B")
    c = timetable.insert_airport("C")
    d = timetable.insert_airport("D")
    e = timetable.insert_airport("E")
    f = timetable.insert_airport("F")

    timetable.insert_flight(a,b,datetime.datetime(2018,12,22,8,0,0),datetime.datetime(2018,12,22,8,15,0),9)
    timetable.insert_flight(a,b,datetime.datetime(2018,12,22,8,0,0),datetime.datetime(2018,12,22,8,20,0),9)
    timetable.insert_flight(a,c,datetime.datetime(2018,12,22,8,0,0),datetime.datetime(2018,12,22,9,0,0),9)
    timetable.insert_flight(a,c,datetime.datetime(2018,12,22,8,0,0),datetime.datetime(2018,12,22,8,9,0),9)
    timetable.insert_flight(a,c,datetime.datetime(2018,12,22,11,0,0),datetime.datetime(2018,12,22,12,0,0),9)
    timetable.insert_flight(c,b,datetime.datetime(2018,12,22,8,10,0),datetime.datetime(2018,12,22,8,20,0),9)
    timetable.insert_flight(b,d,datetime.datetime(2018,12,22,8,15,0),datetime.datetime(2018,12,22,9,0,0),9)
    timetable.insert_flight(b,e,datetime.datetime(2018,12,22,8,15,0),datetime.datetime(2018,12,22,9,0,0),9)
    timetable.insert_flight(b,e,datetime.datetime(2018,12,22,8,20,0),datetime.datetime(2018,12,22,9,0,0),9)
    timetable.insert_flight(e,f,datetime.datetime(2018,12,22,9,0,0),datetime.datetime(2018,12,22,10,0,0),9)
    timetable.insert_flight(c,f,datetime.datetime(2018,12,22,9,0,0),datetime.datetime(2018,12,22,10,0,0),9)
    timetable.insert_flight(c,f,datetime.datetime(2018,12,22,9,0,0),datetime.datetime(2018,12,22,10,0,0),9)

    for i in list_routes(timetable,a,f,datetime.datetime(2018,12,22,7,0,0),datetime.timedelta(hours=3)):
        print("[ ")
        for k in i:
            print(str(k) + " ,")
        print(" ]")
    print(counter)

