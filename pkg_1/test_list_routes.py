import datetime
from Project3.pkg_1.timetable_1 import Timetable
from Project3.pkg_1.list_routes import list_routes

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