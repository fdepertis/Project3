from ..timetable import Timetable
import datetime
from .list_routes import list_routes

t = Timetable()
t.insert_vertex("MXP", datetime.timedelta(minutes=10))
t.insert_vertex("TRN", datetime.timedelta(minutes=10))
t.insert_vertex("FCO", datetime.timedelta(minutes=15))
t.insert_vertex("NAP", datetime.timedelta(minutes=20))
t.insert_vertex("BRI", datetime.timedelta(minutes=25))
t.insert_vertex("PMO", datetime.timedelta(minutes=30))
t.insert_vertex("CTA", datetime.timedelta(minutes=30))
t.insert_vertex("CAG", datetime.timedelta(minutes=35))
