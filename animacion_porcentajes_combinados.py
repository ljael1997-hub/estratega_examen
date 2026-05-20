import streamlit as st
import random

def modulo_combinados_streamlit():
    st.title("🧩 Porcentajes Combinados (Estrategia Avanzada)")
    
    st.markdown("""
    ### 📝 Descompón el Problema
    Si en tu examen te piden un porcentaje "raro" como el **13%**, no te estreses. Desmóntalo usando los bloques que ya conoces:
    * 🧱 Un bloque de **10%**
    * 🧱 Tres bloques de **1%** ($1\% + 1\% + 1\% = 3\%$)
    
    ¡Sumas los resultados de tus bloques y listo, tienes la respuesta sin una sola multiplicación larga!
    """)
    
    if 'game_id_comb' not in st.session_state: 
        st.session_state.game_id_comb = 0
        
    if 'reto_comb' not in st.session_state:
        base_num = random.choice([200, 300, 500, 600, 800])
        porcentaje_pedid = random.choice([12, 15, 21, 31, 13])
        st.session_state.reto_comb = {
            "num": base_num,
            "porc": porcentaje_pedid,
            "solucion": int((base_num * porcentaje_pedid) / 100)
        }
        
    c = st.session_state.reto_comb
    gid = st.session_state.game_id_comb
    
    st.info(f"🎯 **Tu Reto Combinado: Calcula el {c['porc']}% de {c['num']}**")
    st.divider()
    
    # Guías interactivas según el porcentaje que toque
    p_diez = c['porc'] // 10
    p_uno = c['porc'] % 10
    
    st.write(f"💡 **Pista del estratega:** Para armar el {c['porc']}%, necesitas calcular el 10% y el 1% de {c['num']}:")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"• El **10%** de {c['num']} es: `{c['num']/10}`")
    with col2:
        st.write(f"• El **1%** de {c['num']} es: `{c['num']/100}`")
        
    st.write("")
    user_final = st.number_input(f"¿Cuál es el resultado final de {c['porc']}% de {c['num']}?", step=1, value=None, key=f"comb_f_{gid}")
    
    if st.button("🧩 Combinar Bloques"):
        if user_final == c['solucion']:
            st.balloons()
            st.success(f"¡ESPECTACULAR! Combinaste los bloques a la perfección. La respuesta es {c['solucion']}.")
        else:
            st.error(f"La combinación no dio la cantidad exacta. Intenta sumando {p_diez} veces el 10% y {p_uno} veces el 1%.")
            
    if st.button("🔄 Cambiar de Reto"):
        st.session_state.game_id_comb += 1
        del st.session_state.reto_comb
        st.rerun()