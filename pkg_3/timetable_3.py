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

Timetable implemented as Edge List, where there is an Airport List and Flight List.
Flight list is ordered on decreasing Available Seats of Flights.
"""

import datetime


class Timetable:
    class Airport:
        __slots__ = '_name', '_coincidence_time'

        def __init__(self, name, coincidence_time=datetime.timedelta(0)):
            if type(coincidence_time) is not datetime.timedelta:
                raise TypeError("Coincidence Time must be datetime.timedelta typed.")
            self._name = name
            self._coincidence_time = coincidence_time

        def name(self):
            return self._name

        def c(self):
            return self._coincidence_time

        def __hash__(self):
            return hash((self.name(), self.c()))

        def __str__(self):
            return "Airport: " + str(self._name) + "\nCoincidence Time: " + str(self._coincidence_time)

        def __eq__(self, other):
            return self._name == other._name and self._coincidence_time == other._coincidence_time

    class Flight:
        __slots__ = '_origin', '_destination', '_departure_time', '_arrival_time', '_available_seats', '_diesel'

        def __init__(self, origin, destination, departure_time, arrival_time, available_seats):
            if type(origin) is not type(destination) is not Timetable.Airport:
                raise TypeError("Origin and Destination must be Timetable.Airport typed.")
            elif type(departure_time) is not type(arrival_time) is not datetime.datetime:
                raise TypeError("Departure and Arival Times must be datetime.datetime typed.")
            elif type(available_seats) is not int or available_seats < 1:
                raise TypeError("Available Seats must be positive integer.")
            elif arrival_time <= departure_time:
                raise ValueError("Arrival time must be greater than departure time.")
            else:
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

        def flight_time_in_minutes(self):
            delta = self.a() - self.l()
            return delta.total_seconds()/60

        def __hash__(self):
            return hash((self.s(), self.d(), self.l(), self.a(), self. p()))

        def __str__(self):
            return "Flight from: " + str(self.s().name()) + ", to: " + str(self.d().name()) + "\nDeparture: " + str(self.l()) + ", Arrival: " + str(self.a()) + ", Available Seats: " + str(self.p())

        def __eq__(self, other):
            return self.s() == other.s() and self.d() == other.d() and self.l() == other.l() and self.a() == other.a()

    def __init__(self):
        self._airports = []
        self._flights = []

    def _validate_airport(self, a):
        """Verify that a is an Airport of this timetable."""
        if not isinstance(a, self.Airport):
            raise TypeError('Airport expected')
        elif a not in self._airports:
            raise ValueError('This airport does not belong to this timetable.')

    def airport_count(self):
        return len(self._airports)

    def airports(self):
        for a in self._airports:
            yield a

    def flight_count(self):
        return len(self._flights)

    def flights(self):
        for f in self._flights:
            yield f

    def get_direct_flights(self, origin, destination):
        self._validate_airport(origin)
        self._validate_airport(destination)
        for f in self._flights:
            if f.s() is origin and f.d() is destination:
                yield f

    def degree(self, a, outgoing=True):
        self._validate_airport(a)
        result = 0
        if outgoing:
            for f in self._flights:
                if f.s() is a:
                    result += 1
        else:
            for f in self._flights:
                if f.d() is a:
                    result += 1
        return result

    def incident_flights(self, a, outgoing=True):
        self._validate_airport(a)
        if outgoing:
            for f in self._flights:
                if f.s() is a:
                    yield f
        else:
            for f in self._flights:
                if f.d() is a:
                    yield f

    def incident_flights_reversed(self, a, outgoing=True):
        self._validate_airport(a)
        if outgoing:
            for i in range(1, len(self._flights)+1):
                if self._flights[-i].s() is a:
                    yield self._flights[-i]
        else:
            for i in range(1, len(self._flights)+1):
                if self._flights[-i].d() is a:
                    yield self._flights[-i]

    def insert_airport(self, name, coincidence_time=datetime.timedelta(0)):
        """Insert and return a new Vertex with element x."""
        a = self.Airport(name, coincidence_time)
        self._airports.append(a)
        return a

    def insert_flight(self, origin, destination, departure_time, arrival_time, available_seats):
        """Insert and return a new Edge from u to v with auxiliary element x.

        Raise a ValueError if u and v are not vertices of the graph.
        Raise a ValueError if u and v are already adjacent.
        """
        self._validate_airport(origin)
        self._validate_airport(destination)
        f = self.Flight(origin, destination, departure_time, arrival_time, available_seats)
        for flight in self.get_direct_flights(origin, destination):
            if f == flight:
                raise ValueError("There is already a flight with same origin, destination, departure and arrival times.")

        i = 0
        added = False
        while i < len(self._flights) and not added:
            if self._flights[i].p() < f.p():
                self._flights.insert(i, f)
                added = True
            i += 1
        if not added:
            self._flights.append(f)


if __name__ == '__main__':
    t = Timetable()
    nap = t.insert_airport("NAP", datetime.timedelta(minutes=30))
    mxp = t.insert_airport("MXP", datetime.timedelta(minutes=30))
    rom = t.insert_airport("FCO")

    t.insert_flight(nap, mxp, datetime.datetime(2018, 1, 1, 12, 0, 0), datetime.datetime(2018, 1, 1, 14, 0, 0), 500)
    t.insert_flight(nap, mxp, datetime.datetime(2018, 1, 1, 8, 0, 0), datetime.datetime(2018, 1, 1, 10, 0, 0), 200)
    t.insert_flight(nap, mxp, datetime.datetime(2018, 1, 1, 10, 0, 0), datetime.datetime(2018, 1, 1, 12, 0, 0), 300)
    t.insert_flight(nap, mxp, datetime.datetime(2018, 1, 1, 13, 0, 0), datetime.datetime(2018, 1, 1, 15, 0, 0), 600)
    t.insert_flight(nap, mxp, datetime.datetime(2018, 1, 1, 9, 0, 0), datetime.datetime(2018, 1, 1, 11, 0, 0), 400)
    t.insert_flight(nap, mxp, datetime.datetime(2018, 1, 1, 7, 0, 0), datetime.datetime(2018, 1, 1, 9, 0, 0), 100)

    print("Incident Flights: ")
    for f in t.incident_flights(nap):
        print(f)
    print("\nIncident Flights reversed: ")
    for f in t.incident_flights_reversed(nap):
        print(f)
    print("\nAirport Count: ", t.airport_count())
    print("\nAirports: ")
    for a in t.airports():
        print(a)
    print("\nFlight Count: ", t.flight_count())
    print("\nFlights: ")
    for f in t.flights():
        print(f)
    print("\nDegrees: ")
    print(t.degree(nap))
    print(t.degree(nap, False))
    print(t.degree(mxp))
    print(t.degree(mxp, False))
    print("\nDirect Flights: ")
    for f in t.get_direct_flights(nap, mxp):
        print(f)
        print(f.flight_time())