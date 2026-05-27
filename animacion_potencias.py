import streamlit as st
import random

def modulo_potencias_basicas():
    st.title("📦 El Almacén de las Cajas Infinitas")
    
    st.markdown("""
    ### 📝 El Mito del Multiplicador
    ¡Cuidado! El exponente **no multiplica** a la base. Es una instrucción de repetición.
    * **Base:** El número protagonista.
    * **Exponente:** El contador de veces que el protagonista se multiplica por sí mismo.
    """)
    
    if 'pregunta_pot' not in st.session_state:
        st.session_state.pregunta_pot = random.choice([
            {"q": "4^3", "op": ["4 * 3 = 12", "4 * 4 * 4 = 64"], "a": "4 * 4 * 4 = 64"},
            {"q": "5^2", "op": ["5 * 2 = 10", "5 * 5 = 25"], "a": "5 * 5 = 25"},
            {"q": "2^4", "op": ["2 * 4 = 8", "2 * 2 * 2 * 2 = 16"], "a": "2 * 2 * 2 * 2 = 16"}
        ])
    
    p = st.session_state.pregunta_pot
    st.write(f"### ¿Cuál es el desarrollo correcto de **{p['q']}**?")
    
    res = st.radio("Elige la opción correcta:", p['op'], index=None)
    
    if st.button("Revisar respuesta"):
        if res == p['a']:
            st.success("¡Exacto! El número se multiplica por sí mismo, no por el exponente.")
            st.balloons()
        else:
            st.error("¡Cuidado, es una trampa clásica! El exponente nos dice cuántas veces multiplicar la base por sí misma.")
            
    if st.button("🔄 Nuevo Reto"):
        st.session_state.pop('pregunta_pot', None)
        st.rerun()