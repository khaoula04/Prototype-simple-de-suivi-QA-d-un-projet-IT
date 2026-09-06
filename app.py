import streamlit as st 
import pandas as pd
from preparation_donnees import charger_et_preparer
import plotly.express as px



st.title("Suivi QA d'un Projet IT")

df = charger_et_preparer("tickets_demo.csv")


#Tests de robustesse 
#df = charger_et_preparer("test_vide.csv")              #fichier CSV vide
#df = charger_et_preparer("test_date_manquante.csv")    #Date manquante 
#df = charger_et_preparer("test_colonne_manquante.csv") #colonne manquante 




st.write("Aperçu des tickets : ")
st.dataframe(df)

total_tickets = len(df)
tickets_termines = len(df[df["statut"] == "termine"])
tickets_bloques = len(df[df["statut"] == "bloque"])
tickets_en_retard = df["en_retard"].sum()
tickets_sans_resp = df["sans_responsable"].sum()

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Total tickets", total_tickets)
col2.metric("Terminés", tickets_termines)
col3.metric("Bloqués", tickets_bloques)
col4.metric("En retard", tickets_en_retard)
col5.metric("Sans responsable", tickets_sans_resp)



#Les filtres dans la barre laterale
st.sidebar.header("Filtres")

statuts_choisis = st.sidebar.multiselect(
    "Statut",
    options = df["statut"].unique(),
    default = df["statut"].unique()
)

priorites_choisies = st.sidebar.multiselect(
    "Priorité", 
    options=df["priorite"].unique(), 
    default=df["priorite"].unique()
)

responsables_choisis = st.sidebar.multiselect(
    "Responsable",
    options= df["responsable"].dropna().unique(),
    default = df["responsable"].dropna().unique()
)


df_filtre = df[
    (df["statut"].isin(statuts_choisis)) & 
    (df["priorite"].isin(priorites_choisies)) &
    (df["responsable"].isin(responsables_choisis) | df["responsable"].isna())
]

#tableau filtre
st.write(f"{len(df_filtre)} tickets affiche(s) sur {total_tickets}")
st.dataframe(df_filtre)




#graphiques plotly
col_gauche, col_droite = st.columns(2)

with col_gauche:
    fig_statut = px.bar(
        df_filtre["statut"].value_counts().reset_index(),
        x="statut", y="count",
        title="Tickets par statut"
    )
    st.plotly_chart(fig_statut)

with col_droite:
    fig_priorite = px.bar(
        df_filtre["priorite"].value_counts().reset_index(),
        x="priorite", y="count",
        title="Tickets par priorité"
    )
    st.plotly_chart(fig_priorite)


#Alertes
st.subheader("Alertes principales")

alertes = df_filtre[
    df_filtre["en_retard"] | df_filtre["critique"] | df_filtre["sans_responsable"] | (df_filtre["statut"] == "bloque")

]


if len(alertes) == 0:
    st.success("Aucune alerte détectée sur les tickets filtrés.")


else :
    st.warning(f"{len(alertes)} ticket(s) necessitent une attention particuliere")
    st.dataframe(alertes[["ticket_id", "titre", "statut", "priorite", "responsable", "en_retard", "critique", "sans_responsable"]])




#Synthese
st.subheader("Synthese :")

synthese = f"""

**Total tickets analyses : {len(df_filtre)}**



**Points d'attention :**


- {df_filtre["en_retard"].sum()} : nombre des tickets en retard
- {df_filtre["critique"].sum()} : nombre des tickets critiques
- {df_filtre['sans_responsable'].sum()} : nombre de tickets sans responsable
- {(df_filtre["statut"]== "bloque").sum()} : nombre de tickets bloqué(s) 

"""

st.markdown(synthese)

