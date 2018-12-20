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
from TdP_collections.graphs.graph import Graph
import datetime

class Timetable(Graph):
    class Airport(Graph.Vertex):
        __slots__ = '_coincidence_time'

        def __init__(self, name, coincidence_time = datetime.timedelta(0)):
            if type(coincidence_time) is not datetime:
                raise TypeError("Coincidence Time must be datetime.timedelta typed.")
            super().__init__(name)
            self._coincidence_time = coincidence_time

        def __hash__(self):         # will allow vertex to be a map/set key
            return hash((self._element, self._coincidence_time))

        def c(self):
            return self._coincidence_time

        def __str__(self):
            return "Airport: ", str(self.element(), "\nCoincidence Time:", str(self._coincidence_time)

    class Flight(Graph.Edge):

        def __init__(self, origin, destination, departure_time, arrival_time, available_seats):
            if type(origin) is not type(destination) is not Timetable.Airport:
                raise TypeError("Origin and Destination must be Timetable.Airport typed.")
            if type(departure_time) is not type(arrival_time) is not datetime.time:
                raise TypeError("Departure and Arival Times must be datetime.time typed.")
            if type(available_seats) is not int or arrival_time < 1:
                raise TypeError("Available Seats must be positive integer.")
            self._origin = origin
            self._destination = destination
            self._element = (departure_time, arrival_time, available_seats)

        def opposite(self, a):
            """Return the vertex that is opposite v on this edge."""
            if not isinstance(a, Timetable.Airport):
                raise TypeError('A must be an Airport')
            if a is self._origin:
                return self._destination
            elif a is self._destination:
                return self._origin
            else:
                raise ValueError('A not incident to Flight')

        def __hash__(self):         # will allow edge to be a map/set key
            return hash((self._origin, self._destination, self._element.departure_time, self._element.arrival_time, self._element.available_seats))

        def s(self):
            return self._origin

        def d(self):
            return self._destination

        def l(self):
            return self._element.departure_time

        def a(self):
            return self._element.arrival_time

        def p(self):
            return self._element.available_seats

        def flight_time(self):
            return self._element.arrival_time - self._element.departure_time

    def __init__(self):
        super().__init__(True)

    def _validate_vertex(self, a):
        """Verify that v is an Airport of this timetable."""
        if not isinstance(a, self.Airport):
            raise TypeError('Airport expected')
        elif a not in self._outgoing:
            raise ValueError('Vertex does not belong to this graph.')

    def insert_vertex(self, name, coincidence_time):
        """Insert and return a new Vertex with element x."""
        a = self.Airport(name, coincidence_time)
        self._outgoing[a] = {}
        self._incoming[a] = {}        # need distinct map for incoming edges
        return a

    def insert_edge(self, origin, destination, departure_time, arrival_time, available_seats):
        """Insert and return a new Edge from u to v with auxiliary element x.

        Raise a ValueError if u and v are not vertices of the graph.
        Raise a ValueError if u and v are already adjacent.
        """
        self._validate_vertex(origin)
        self._validate_vertex(destination)
        f = self.Flight(origin, destination, departure_time, arrival_time, available_seats)
        self._outgoing[origin][destination] = f
        self._incoming[destination][origin] = f