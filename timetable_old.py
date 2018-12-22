"""
Una nuova compagnia di trasporto aereo ha costruito il proprio orario e sta progettando
una serie di servizi da fornire ai propri clienti per progettare i loro viaggi. L’orario della
compagnia è dato da:
- Una lista A di n aeroporti in cui la compagnia fa scalo; per ogni aeroporto a
    lviene fornita l’indicazione del tempo minimo di coincidenza c(a), che è il tempo
    minimo necessario in quell’aeroporto per prendere una coincidenza;
- Un insieme F di m voli, dove per ogni volo f viene indicato:
    - l’areoporto di partenza s(f)
    - l’areoporto di arrivo d(f)
    - l’orario di partenza l(f)
    - l’orario di arrivo a(f)
    - il numero di posti disponibili sul volo p(f)
"""
import datetime


class Timetable:
    class Airport:
        __slots__ = '_name', '_coincidence_time'

        def __init__(self, name, coincidence_time=datetime.timedelta(0)):
            if type(coincidence_time) is not datetime:
                raise TypeError("Coincidence Time must be datetime.timedelta typed.")
            self._name = name
            self._coincidence_time = coincidence_time

        def name(self):
            return self._name

        def c(self):
            return self._coincidence_time

        def __hash__(self):
            return hash((self._name, self._coincidence_time))

        def __str__(self):
            return "Airport: " + str(self._name) + "\nCoincidence Time: " + str(self._coincidence_time)

    class Flight:
        __slots__ = '_origin', '_destination', '_departure_time', '_arrival_time', '_available_seats'

        def __init__(self, origin, destination, departure_time, arrival_time, available_seats):
            if type(origin) is not type(destination) is not Timetable.Airport:
                raise TypeError("Origin and Destination must be Timetable.Airport typed.")
            if type(departure_time) is not type(arrival_time) is not datetime.datetime:
                raise TypeError("Departure and Arival Times must be datetime.datetime typed.")
            if type(available_seats) is not int or arrival_time < 1:
                raise TypeError("Available Seats must be positive integer.")
            if arrival_time <= departure_time:
                raise ValueError("Arrival time must be greater than departure time.")
            self._origin = origin
            self._destination = destination
            self._departure_time = departure_time
            self._arrival_time = arrival_time
            self._available_seats = available_seats

        def opposite(self, a):
            """Return the vertex that is opposite v on this edge."""
            if not isinstance(a, Timetable.Airport):
                raise TypeError('A must be an Airport')
            elif a is self._origin:
                return self._destination
            elif a is self._destination:
                return self._origin
            else:
                raise ValueError('A not incident to Flight')

        def s(self):
            return self._origin

        def d(self):
            return self._destination

        def l(self):
            return self._departure_time

        def a(self):
            return self._arrival_time

        def p(self):
            return self._available_seats

        def flight_time(self):
            return self._arrival_time - self._departure_time

        def __hash__(self):
            return hash(self._origin, self._destination, self._departure_time, self._arrival_time, self._available_seats)

        def __str__(self):
            return "Flight from: " + str(self.s().name()) + ", to:" + str(self.d().name()) + "\nDeparture: " + str(self.l()) + ", Arrival: " + str(self.a()) + ", Available Seats: " + str(self.p())

    def __init__(self):
        self._outgoing = {}
        self._incoming = {}

    def _validate_airport(self, a):
        """Verify that a is an Airport of this timetable."""
        if not isinstance(a, self.Airport):
            raise TypeError('Airport expected')
        elif a not in self._outgoing:
            raise ValueError('Vertex does not belong to this graph.')

    def airport_count(self):
        return len(self._outgoing)

    def airports(self):
        return self._outgoing.keys()

    def flight_count(self):
        return sum(self._outgoing[a] for a in self._outgoing)

    def flights(self):
        result = set()
        for secondary_map in self._outgoing.values():
            result.update(secondary_map.keys())
        return result

    def get_direct_flights(self, origin, destination):
        result = set()
        for f,a in self._outgoing[origin]:
            if a == destination:
                result.update(f)
        return result

    def degree(self, a, outgoing=True):
        self._validate_airport(a)
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[a])

    def incident_flights(self, a, outgoing=True):
        self._validate_airport(a)
        adj = self._outgoing if outgoing else self._incoming
        for f in adj[a].keys():
            yield f

    def ordered_incident_flights(self, a, outgoing=True):
        flights = list(self.incident_flights(a, outgoing))
        """Ordinamento dei voli in base a non so cosa"""
        return flights

    def insert_airport(self, name, coincidence_time):
        """Insert and return a new Vertex with element x."""
        a = self.Airport(name, coincidence_time)
        self._outgoing[a] = {}
        self._incoming[a] = {}        # need distinct map for incoming edges
        return a

    def insert_flight(self, origin, destination, departure_time, arrival_time, available_seats):
        """Insert and return a new Edge from u to v with auxiliary element x.

        Raise a ValueError if u and v are not vertices of the graph.
        Raise a ValueError if u and v are already adjacent.
        """
        self._validate_airport(origin)
        self._validate_airport(destination)
        f = self.Flight(origin, destination, departure_time, arrival_time, available_seats)
        self._outgoing[origin][f] = destination
        self._incoming[destination][f] = origin
