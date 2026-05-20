import streamlit as st
import random

def modulo_porcentajes_streamlit():
    st.title("✨ La Magia del Punto (Porcentajes Rápido)")
    
    st.markdown("""
    ### 📝 El Truco Secreto del Examen
    Hacer la regla de tres para los porcentajes te quita mucho tiempo. En su lugar, usa **la magia de mover el punto decimal**:
    * 🎯 **Para sacar el 10%:** Imagina que el número tiene un punto al final y muévelo **1 lugar a la izquierda** (es lo mismo que dividir entre 10).
    * 🎯 **Para sacar el 1%:** Agarra el punto final y muévelo **2 lugares a la izquierda** (es lo mismo que dividir entre 100).
    """)
    
    if 'game_id_porc' not in st.session_state: 
        st.session_state.game_id_porc = 0
        
    if 'reto_porc' not in st.session_state:
        numero = random.choice([120, 250, 400, 850, 1500, 340, 60, 900])
        st.session_state.reto_porc = {
            "numero": numero,
            "diez_porc": numero / 10,
            "uno_porc": numero / 100
        }
        
    ret = st.session_state.reto_porc
    gid = st.session_state.game_id_porc
    
    st.info(f"🔮 **Tu número mágico de esta misión es: {ret['numero']}**")
    st.divider()
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📍 El truco del 10%")
        st.write(f"Mueve el punto 1 lugar a la izquierda en `{ret['numero']}`")
        user_10 = st.number_input("¿Cuánto es el 10%?", step=0.1, key=f"p10_{gid}", value=None)
        
    with col2:
        st.subheader("📍 El truco del 1%")
        st.write(f"Mueve el punto 2 lugares a la izquierda en `{ret['numero']}`")
        user_1 = st.number_input("¿Cuánto es el 1%?", step=0.01, key=f"p1_{gid}", value=None)
        
    html_punto = f"""
    <div style="background-color: #1e293b; padding: 15px; border-radius: 12px; text-align: center; font-family: monospace; color: white; max-width: 320px; margin: 15px auto; border: 1px dashed #475569;">
        <div style="font-size: 14px; color: #94a3b8; margin-bottom: 8px;">📍 Mapa del punto invisible:</div>
        <div style="font-size: 24px; font-weight: bold; letter-spacing: 2px;">
            <span style="color: #60a5fa;">← 1%</span> [{ret['numero']}] <span style="color: #f59e0b;">10% ←</span>
        </div>
    </div>
    """
    st.components.v1.html(html_punto, height=90)

    if st.button("🔮 Invocar la Magia del Punto"):
        if user_10 == ret['diez_porc'] and user_1 == ret['uno_porc']:
            st.balloons()
            st.success(f"¡LOGRADO! El 10% es {ret['diez_porc']} y el 1% es {ret['uno_porc']}.")
        else:
            st.error("Los trucos del punto no coinciden. Recuerda: para el 10% saltas 1 lugar, para el 1% saltas 2 lugares.")

    if st.button("🔄 Probar con otro Número"):
        st.session_state.game_id_porc += 1
        del st.session_state.reto_porc
        st.rerun()