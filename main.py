import streamlit as st
import pandas as pd

st.markdown("# Bienvenue sur ton dashboard statsfoot")

data = {}

col1, col2 = st.columns(2)

with col1:

    player_name = st.text_input("Nom Joueur")

    if player_name:
        data["Nom"] = player_name
    else:
        data["Nom"] = "Null"

with col2:

    strong_foot = st.selectbox("Pieds fort", ["Droit", "Gauche"])

    if strong_foot:
        data["Pieds fort"] = strong_foot

col1, col2 = st.columns(2)

with col1:
    field_place = st.selectbox("Place sur le terrain", ["Attaquant", "Aillier", "Defenseur"])

    if field_place:
        data["Poste"] = field_place

with col2:

    confidence = st.selectbox("Montre de la confiance en soi", ["Très fort", "Fort", "Moyen"])

    if confidence:
        data["Confiance en soi"] = confidence


col1, col2 = st.columns(2, gap="small")

with col1:
    if st.button("Sauvegarder dans la DB", type="primary"):
        st.success("Joueur sauvegardé")

df = pd.DataFrame(data, index=[1]).T
df.columns = ["Val"]

csv = df.to_csv().encode('utf-8')

with col2:
    st.download_button(label="Télécharger la fiche", data=csv, file_name=f"{player_name}.csv", mime='text/csv')
