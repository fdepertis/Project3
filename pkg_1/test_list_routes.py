from Project3.pkg_1.timetable_1 import Timetable
from Project3.pkg_1.list_routes_2 import list_routes, _list_routes_aux
import datetime

timetable = Timetable()
a = timetable.insert_airport("A")
b = timetable.insert_airport("B", datetime.timedelta(hours=1))
c = timetable.insert_airport("C")
d = timetable.insert_airport("D")
e = timetable.insert_airport("E")
f = timetable.insert_airport("F")

timetable.insert_flight(a, b, datetime.datetime(2018, 12, 22, 8, 0, 0), datetime.datetime(2018, 12, 22, 8, 15, 0), 9)
timetable.insert_flight(a, b, datetime.datetime(2018, 12, 22, 8, 0, 0), datetime.datetime(2018, 12, 22, 8, 20, 0), 9)
timetable.insert_flight(a, c, datetime.datetime(2018, 12, 22, 8, 0, 0), datetime.datetime(2018, 12, 22, 9, 0, 0), 9)
timetable.insert_flight(a, c, datetime.datetime(2018, 12, 22, 11, 0, 0), datetime.datetime(2018, 12, 22, 12, 0, 0), 9)
timetable.insert_flight(b, d, datetime.datetime(2018, 12, 22, 8, 15, 0), datetime.datetime(2018, 12, 22, 9, 0, 0), 9)
timetable.insert_flight(b, e, datetime.datetime(2018, 12, 22, 8, 15, 0), datetime.datetime(2018, 12, 22, 9, 0, 0), 9)
timetable.insert_flight(b, e, datetime.datetime(2018, 12, 22, 8, 20, 0), datetime.datetime(2018, 12, 22, 9, 0, 0), 9)
timetable.insert_flight(e, f, datetime.datetime(2018, 12, 22, 9, 0, 0), datetime.datetime(2018, 12, 22, 10, 0, 0), 9)
timetable.insert_flight(c, f, datetime.datetime(2018, 12, 22, 9, 0, 0), datetime.datetime(2018, 12, 22, 10, 0, 0), 9)
timetable.insert_flight(c, f, datetime.datetime(2018, 12, 22, 14, 0, 0), datetime.datetime(2018, 12, 22, 15, 0, 0), 9)

for i in list_routes(timetable, a, f, datetime.datetime(2018, 12, 22, 7, 0, 0), datetime.timedelta(hours=10)):
    print("[")
    for j in i:
        print(j)
    print("]")
