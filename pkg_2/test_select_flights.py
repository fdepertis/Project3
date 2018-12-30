from Project3.pkg_3.select_flights import select_flights
from Project3.pkg_3.timetable_3 import Timetable
import datetime

timetable = Timetable()
a = timetable.insert_airport("A")
b = timetable.insert_airport("B")
c = timetable.insert_airport("C")
d = timetable.insert_airport("D")
e = timetable.insert_airport("E")
f = timetable.insert_airport("F")

timetable.insert_flight(a,b,datetime.datetime(2018,12,22,8,0,0),datetime.datetime(2018,12,22,8,15,0),5)
timetable.insert_flight(a,b,datetime.datetime(2018,12,22,8,0,0),datetime.datetime(2018,12,22,8,20,0),2)

timetable.insert_flight(a,c,datetime.datetime(2018,12,22,8,0,0),datetime.datetime(2018,12,22,9,0,0),94)
timetable.insert_flight(a,c,datetime.datetime(2018,12,22,8,0,0),datetime.datetime(2018,12,22,8,9,0),95)

timetable.insert_flight(a,c,datetime.datetime(2018,12,22,11,0,0),datetime.datetime(2018,12,22,12,0,0),69)
timetable.insert_flight(c,b,datetime.datetime(2018,12,22,8,10,0),datetime.datetime(2018,12,22,8,20,0),95)
""""
timetable.insert_flight(b,d,datetime.datetime(2018,12,22,8,15,0),datetime.datetime(2018,12,22,9,0,0),93)
timetable.insert_flight(b,e,datetime.datetime(2018,12,22,8,15,0),datetime.datetime(2018,12,22,9,0,0),94)
timetable.insert_flight(b,e,datetime.datetime(2018,12,22,8,20,0),datetime.datetime(2018,12,22,9,0,0),943)
timetable.insert_flight(e,f,datetime.datetime(2018,12,22,9,0,0),datetime.datetime(2018,12,22,10,0,0),9566)
timetable.insert_flight(c,f,datetime.datetime(2018,12,22,9,0,0),datetime.datetime(2018,12,22,10,0,0),9643)
timetable.insert_flight(c,f,datetime.datetime(2018,12,22,9,0,0),datetime.datetime(2018,12,22,11,0,0),93)
"""
B=60
print("Trovare tutti i voli della compangia per cui si possa massimizzare\nil numero di di passeggeri in transito rientrando in un budget di",B)

flights,money= select_flights(timetable,B)
print("\nVoli selezionati")
for i in flights:
    print(i)
print("\nBudget assegnati ai vari aereoporti")
for i in money.keys():
    print(i)
    print("Buget: " + str(money[i]) + " $")
