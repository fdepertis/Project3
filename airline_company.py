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

class airline_company(Graph):

    class airport(Graph.Vertex):

        __slots__ = '_coincidence_time'

        def __init__(self,airport,coincidence = None):
            if type(airport) is not type(str):
                raise TypeError("No obj str in input")
            if type(coincidence) is not type(datetime):
                raise TypeError("No obj datetime.time in input")
            super().__init__(airport)
            self._coincidence_time = coincidence

        def element(self):
            return self._element

        def _is_airport_layover(self):
            return self._coincidence_time is None

        def c(self):
            return self._coincidence_time

        def __eq__(self, other):
            return self._airport is other._airport and self._coincidence_time is other._coincidence_time

    class flight(Graph.Edge):
        class _flight_element():
            __slots__ = '_departure_time', '_arrival_time', '_available_seats'

            def __init__(self, l, a , p):
                if type(l) is not type(datetime) or type(a) is type(datetime):
                    raise TypeError("No obj datetime.time in input")
                if type(p) is not type(int):
                    raise TypeError("No obj int in input")
                if l>a:
                    if l==a:
                        raise ValueError("departure time and arrival time are equal")
                    else:
                        raise ValueError("departure time is greater then arrival time. It is impossible!")
                self._departure_time = l    #orario di partenza
                self._arrival_time = a      #orario di arrivo
                self._available_seats = p   # posti disponibili

            def __eq__(self, other):
                return self._departure_time is other._departure_time and self._arrival_time is other._arrival_time

        def s(self):
            """

            :return: arline_company.airport
            """
            return self._origin

        def d(self):
            """

            :return: airline_company.airport
            """
            return self._destination

        def l(self):
            """

            :return: datetime.datetime
            """
            return self._element._departure_time

        def a(self):
            """

            :return: datetime.datetime
            """
            return self._element._arrival_time

        def p(self):
            """

            :return: int
            """
            return self._element._available_seats

        def _flight_time(self):
            """
            :return: datetime.timedelta
            """
            return self.a()-self.l()

        def __eq__(self, other):
            return self._origin is other._origin and self._destination is other._destination and self._element == other._element


    def __init__(self, directed=True):
        super().__init__(directed)
        #Il grafo si suppone sia diretto in quando ogni arco identificato da un volo ha un aereoporto da cui partire e un aereoporto a cui arrivare


