import csv
import random
from datetime import date, timedelta
import os

status = ["A faire", "En cours", "bloque", "termine"]
#None est pour tester le cas des tickets sans responsable
priorites = ["faible", "moyenne", "elevee", "critique"]
responsables = ["Mouad", "Douae", "Fatime", "Eman", None]
type_ticket = ["Tache", "bug", "amelioration"]

tickets = []
aujourd_hui = date.today() 
for i in range (1,41) :
    ticket_id = f"T{i:03d}"
    titre = f"Ticket exemple {i}"
    statut = random.choice(status)
    priorite = random.choice(priorites)
    responsable = random.choice(responsables)
    type_t = random.choice(type_ticket)


    date_creation = aujourd_hui - timedelta(days=random.randint(5, 60))
    date_limite = date_creation + timedelta(days=random.randint(3, 30))

    if i <= 5 : #les 5 1e tickets sont en retard par defaut
        date_limite = aujourd_hui - timedelta(days = 10)
        statut = random.choice(["A faire", "En cours", "bloque"])
        #print(ticket_id, date_creation, date_limite)

    elif i <= 10 : #Tickets garantis d'etre bloques
        statut = 'bloque'

    elif i <= 15: #Tickets garantis d'etre sans responsable 
        responsable = None


    tickets.append({
        "ticket_id" : ticket_id,
        "titre" : titre,
        "statut" : statut,
        "priorite" : priorite,
        "responsable" : responsable if responsable else "",
        "date_creation" : date_creation.isoformat(), 
        "date_limite" : date_limite.isoformat(),
        "type_t" : type_t

    })

with open("tickets_demo.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=tickets[0].keys())
    writer.writeheader()
    writer.writerows(tickets)


print(status)



    

#On genere des tickets avec des titres, responsables et dates aleatoires
print(os.getcwd())

if i <= 5:
    print(ticket_id, date_creation, date_limite)