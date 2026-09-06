import pandas as pd
from preparation_donnees import charger_et_preparer


#On genere qlq donnees pour tester 
#teste des tickets en retard
def test_ticket_en_retard():
    donnees = pd.DataFrame({
        "ticket_id": ["T001", "T002"],
        "titre": ["Test 1", "Test 2"],
        "statut": ["à faire", "termine"],
        "priorite": ["moyenne", "faible"],
        "responsable": ["Alice", "Karim"],
        "date_creation": ["2026-01-01", "2026-01-01"],
        "date_limite": ["2020-01-01", "2020-01-01"],  # both are in the past
        "type": ["tâche", "tâche"]
    })


    donnees.to_csv("temp_test.csv", index= False)
    resultat = charger_et_preparer("temp_test.csv")

    
    assert resultat.loc[0, "en_retard"] == True
    assert resultat.loc[1, "en_retard"] == False

    print(repr(resultat.loc[1, "statut"]))

#test des tickets bloques
def test_ticket_bloque():
    donnees = pd.DataFrame({
        "ticket_id": ["T001", "T002"],
        "titre": ["Test 1", "Test 2"],
        "statut": ["bloque", "A faire"],
        "priorite": ["moyenne", "moyenne"],
        "responsable": ["Alice", "Karim"],
        "date_creation": ["2026-01-01", "2026-01-01"],
        "date_limite": ["2026-12-01", "2026-12-01"],
        "type": ["tache", "tache"]
    })



    donnees.to_csv("temp_test.csv", index=False)
    resultat = charger_et_preparer("temp_test.csv")

    assert (resultat.loc[0, "statut"] == "bloque") == True
    assert (resultat.loc[1, "statut"] == "bloque") == False

#test des tickets sans responsable
def test_ticket_sans_responsable():
    donnees = pd.DataFrame({
        "ticket_id": ["T001", "T002"],
        "titre": ["Test 1", "Test 2"],
        "statut": ["A faire", "A faire"],
        "priorite": ["moyenne", "moyenne"],
        "responsable": [None, "Alice"],
        "date_creation": ["2026-01-01", "2026-01-01"],
        "date_limite": ["2026-12-01", "2026-12-01"],
        "type": ["tache", "tache"]
    })

    donnees.to_csv("temp_test.csv", index=False)
    resultat = charger_et_preparer("temp_test.csv")

    assert resultat.loc[0, "sans_responsable"] == True
    assert resultat.loc[1, "sans_responsable"] == False


#test de tickets critiques
def test_ticket_critique():
    donnees = pd.DataFrame({
        "ticket_id": ["T001", "T002"],
        "titre": ["Test 1", "Test 2"],
        "statut": ["A faire", "A faire"],
        "priorite": ["critique", "faible"],
        "responsable": ["Alice", "Karim"],
        "date_creation": ["2026-01-01", "2026-01-01"],
        "date_limite": ["2026-12-01", "2026-12-01"],
        "type": ["tache", "tache"]
    })

    donnees.to_csv("temp_test.csv", index=False)
    resultat = charger_et_preparer("temp_test.csv")

    assert resultat.loc[0, "critique"] == True
    assert resultat.loc[1, "critique"] == False


