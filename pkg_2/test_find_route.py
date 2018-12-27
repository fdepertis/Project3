from Project3.timetable import Timetable
from Project3.pkg_2.find_route import find_route
import datetime


timetable = Timetable()

pmo = timetable.insert_airport("PMO", datetime.timedelta(minutes=30))
cag = timetable.insert_airport("CAG", datetime.timedelta(minutes=30))
nap = timetable.insert_airport("NAP", datetime.timedelta(minutes=30))
bri = timetable.insert_airport("BRI", datetime.timedelta(minutes=30))
fco = timetable.insert_airport("FCO", datetime.timedelta(minutes=30))
flr = timetable.insert_airport("FLR", datetime.timedelta(minutes=30))
trn = timetable.insert_airport("TRN", datetime.timedelta(minutes=30))
mxp = timetable.insert_airport("MXP", datetime.timedelta(minutes=30))

for i in range(8, 16):
    #Voli da Palermo
    timetable.insert_flight(pmo, nap, datetime.datetime(2019, 1, 1, i, 0, 0), datetime.datetime(2019, 1, 1, i+2, 0, 0), 200)
    timetable.insert_flight(pmo, fco, datetime.datetime(2019, 1, 1, i, 0, 0), datetime.datetime(2019, 1, 1, i+2, 0, 0), 200)
    timetable.insert_flight(pmo, bri, datetime.datetime(2019, 1, 1, i, 0, 0), datetime.datetime(2019, 1, 1, i+2, 0, 0), 200)
    #Voli da Cagliari
    timetable.insert_flight(cag, nap, datetime.datetime(2019, 1, 1, i, 0, 0), datetime.datetime(2019, 1, 1, i+2, 0, 0), 200)
    timetable.insert_flight(cag, fco, datetime.datetime(2019, 1, 1, i, 0, 0), datetime.datetime(2019, 1, 1, i+2, 0, 0), 200)
    #Voli da Napoli
    timetable.insert_flight(nap, fco, datetime.datetime(2019, 1, 1, i, 0, 0), datetime.datetime(2019, 1, 1, i+2, 0, 0), 200)
    timetable.insert_flight(nap, cag, datetime.datetime(2019, 1, 1, i, 0, 0), datetime.datetime(2019, 1, 1, i+2, 0, 0), 200)
    timetable.insert_flight(nap, pmo, datetime.datetime(2019, 1, 1, i, 0, 0), datetime.datetime(2019, 1, 1, i+2, 0, 0), 200)
    #Voli da Bari:
    timetable.insert_flight(bri, pmo, datetime.datetime(2019, 1, 1, i, 0, 0), datetime.datetime(2019, 1, 1, i+2, 0, 0), 200)
    #Voli da Roma
    timetable.insert_flight(fco, cag, datetime.datetime(2019, 1, 1, i, 0, 0), datetime.datetime(2019, 1, 1, i+2, 0, 0), 200)
    timetable.insert_flight(fco, nap, datetime.datetime(2019, 1, 1, i, 0, 0), datetime.datetime(2019, 1, 1, i+2, 0, 0), 200)
    timetable.insert_flight(fco, pmo, datetime.datetime(2019, 1, 1, i, 0, 0), datetime.datetime(2019, 1, 1, i+2, 0, 0), 200)
    timetable.insert_flight(fco, flr, datetime.datetime(2019, 1, 1, i, 0, 0), datetime.datetime(2019, 1, 1, i+2, 0, 0), 200)
    #Voli da Firenze
    timetable.insert_flight(flr, fco, datetime.datetime(2019, 1, 1, i, 0, 0), datetime.datetime(2019, 1, 1, i+2, 0, 0), 200)
    timetable.insert_flight(flr, trn, datetime.datetime(2019, 1, 1, i, 0, 0), datetime.datetime(2019, 1, 1, i+2, 0, 0), 200)
    timetable.insert_flight(flr, mxp, datetime.datetime(2019, 1, 1, i, 0, 0), datetime.datetime(2019, 1, 1, i+2, 0, 0), 200)
    #Voli da Torino
    timetable.insert_flight(trn, flr, datetime.datetime(2019, 1, 1, i, 0, 0), datetime.datetime(2019, 1, 1, i+2, 0, 0), 200)
    timetable.insert_flight(trn, mxp, datetime.datetime(2019, 1, 1, i, 0, 0), datetime.datetime(2019, 1, 1, i+2, 0, 0), 200)
    #Voli da Milano
    timetable.insert_flight(mxp, trn, datetime.datetime(2019, 1, 1, i, 0, 0), datetime.datetime(2019, 1, 1, i+2, 0, 0), 200)
    timetable.insert_flight(mxp, flr, datetime.datetime(2019, 1, 1, i, 0, 0), datetime.datetime(2019, 1, 1, i+2, 0, 0), 200)

for f in find_route(timetable, nap, mxp, datetime.datetime(2019, 1, 1, 8, 0, 0)):
    print(f)
