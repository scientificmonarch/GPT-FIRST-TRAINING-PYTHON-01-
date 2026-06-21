import streamlit as st
import random

# 1. Le design de la page
st.title("🎈 Mon super jeu de Devinette !")
st.write("J'ai choisi un nombre entre 1 et 100. À toi de jouer !")

# 2. La boîte à souvenirs (pour ne pas oublier le nombre secret à chaque clic)
if "nombre_secret" not in st.session_state:
    st.session_state.nombre_secret = random.randint(1, 100)
    st.session_state.essais = 0

# 3. La zone pour jouer 
# une jolie boîte avec des boutons + et - pour choisir le nombre
proposition = st.number_input("Ta propostion :", min_value=1, max_value=100, step=1)

#Le bouton pour valider
if st.button("Vérifier mon nombre"):
    st.session_state.essais +=1

    # 4. Les indices
    if proposition < st.session_state.nombre_secret:
        st.warning("c'est plus haut ! ⬆️")
    elif proposition > st.session_state.nombre_secret:
        st.warning("C'est plus bas ! ⬆️")
    else:
        st.success(f"Bravo ! 🎉 tu as trouvé en {st.session_state.essais} essais !")
        st.balloons() # L'animation de victoire ! 
