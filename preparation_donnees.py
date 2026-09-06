import pandas as pd
from datetime import date






def niveau_gravite(jours_retard, en_retard) :
    if not en_retard :
        return "aucun"
    elif jours_retard <= 3 :
        return "faible"
    elif jours_retard <= 10 :
        return "moyen"
    else :
        return "élevé"


def charger_et_preparer(chemin_csv) :


    df = pd.read_csv(chemin_csv)

    colonnes_attendues = ["ticket_id", "titre", "statut", "priorite", "responsable", "date_creation", "date_limite", "type_t"]
    colonnes_manquantes = [col for col in colonnes_attendues if col not in df.columns]
    
    if colonnes_manquantes:
        raise ValueError(f"Colonnes manquantes dans le fichier CSV : {colonnes_manquantes}")

    df["date_creation"] = pd.to_datetime(df["date_creation"])
    df["date_limite"] = pd.to_datetime(df["date_limite"])




    aujourd_hui = pd.Timestamp(date.today())



    df["en_retard"] = (df["date_limite"] < aujourd_hui) & (df["statut"] != "termine")
    df["sans_responsable"] = df["responsable"].isna()
    df["critique"] = df["priorite"] == "critique"
    df["jours_retard"] = (aujourd_hui - df["date_limite"]).dt.days



    




    return df
