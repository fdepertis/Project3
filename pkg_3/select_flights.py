"""
Un volo consuma 60kg di gasolio per ogni ora di volo e prima del decollo la
compagnia deve acquistare dal gesture dell’areoporto il gasolio necessario per il
volo. Si assuma che ogni kg di gasolio costa 1€ e che la compagnia ha a disposizione
un budget complessivo uguale a B per pagare il gasolio e che questo budget non
consente di coprire tutti i voli previsti nell’orario. Gli amministratori della
compagnia devono decidere quali voli far partire e quali cancellare. Progettare una
funzione select_flights() che, preso in input l’orario della compagnia ed il budget B,
seleziona quali voli far decollare in modo da massimizzare il numero complessivo di
posti disponibili. Inoltre, la funzione deve restituire per ogni areoporto a quanti
soldi devono essere assegnati al responsabile dello scalo per pagare il gasolio
necessario per tutti i voli in partenza da a.

Analizzare la complessità di tempo di ciascuna delle tre funzioni proposte in
funzione di n ed m.
"""

tmp=[]
max_seat={}
list_flights={}
money={}
max_seat["max"]=0
tmp.append(max_seat)
tmp.append(list_flights)
tmp.append(money)

def knapsackRec(timetable, i, c, DP):
    global tmp
    if c < 0:
        return 0
    elif i == 0 or c == 0:
        return 0
    else:
        if DP[i][c] < 0:

            nottaken = knapsackRec(timetable, i-1, c, DP)
            taken = knapsackRec(timetable, i-1, c-int(timetable.get_flights()[i-1].price()), DP) + timetable.get_flights()[i-1].p()

            if max(taken,nottaken)>tmp[0]["max"]:

                if tmp[0]["max"] == 0 and DP[i-1][c-int(timetable.get_flights()[i-1].price())]==-1:
                    tmp[0]["max"] = max(taken,nottaken)
                    try:
                        tmp[1][timetable.get_flights()[i-1]]
                    except:
                        tmp[1][timetable.get_flights()[i-1]]=1
                        try:
                            tmp[2][timetable.get_flights()[i-1].s()] += timetable.get_flights()[i-1].price()
                        except:
                            tmp[2][timetable.get_flights()[i-1].s()] = timetable.get_flights()[i-1].price()



                if DP[i-1][c-int(timetable.get_flights()[i-1].price())]!=-1:
                    tmp[0]["max"] = max(taken,nottaken)
                    try:
                        tmp[1][timetable.get_flights()[i-1]]
                    except:
                        tmp[1][timetable.get_flights()[i-1]]=1
                        try:
                            tmp[2][timetable.get_flights()[i-1].s()] += timetable.get_flights()[i-1].price()
                        except:
                            tmp[2][timetable.get_flights()[i-1].s()] = timetable.get_flights()[i-1].price()

            DP[i][c] = max(nottaken, taken)

        return DP[i][c]

def select_flights(timetable,B):#O(m*B)

    global tmp

    n = len(timetable.get_flights())
    DP = [[-1]*(B+1) for i in range(n+1)]

    a=knapsackRec(timetable,n,B,DP)
    if a == 0:
        return None
    else:
        return (tmp[1].keys(),tmp[2])



