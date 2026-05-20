import streamlit as st
import random
import math

def modulo_forja_streamlit():
    st.title("⚒️ La Forja de Números (Leyes de Construcción)")
    
    st.markdown("""
    ### 🧱 Los Dos Lados del Espejo
    Para dominar los exámenes necesitas dos habilidades: **Construir** pisos usando potencias y **Desmantelar** cuartos usando raíces cuadradas.
    """)
    
    if 'game_id_forja' not in st.session_state: 
        st.session_state.game_id_forja = 0
        
    if 'reto_forja' not in st.session_state:
        # Generamos dos números diferentes para que los juegos no se copien las respuestas
        lado_pot = random.choice([2, 3, 4, 5, 6])
        lado_raiz = random.choice([2, 3, 4, 5, 6])
        while lado_raiz == lado_pot:  # Asegura que sean distintos
            lado_raiz = random.choice([2, 3, 4, 5, 6])
            
        st.session_state.reto_forja = {
            "b_pot": lado_pot,
            "c_pot": lado_pot ** 2,
            "b_raiz": lado_raiz,
            "c_raiz": lado_raiz ** 2
        }
        
    r = st.session_state.reto_forja
    gid = st.session_state.game_id_forja
    
    # =========================================================================
    # ⚔️ ZONA 1: LA FORJA DE POTENCIAS (CONSTRUIR)
    # =========================================================================
    st.header("⏬ 1. La Forja de Potencias (Multiplicar)")
    st.write(f"Diseña un cuarto cuadrado que mida **{r['b_pot']}** bloques de largo por **{r['b_pot']}** de ancho. ¿Cuántos bloques usarás en total para rellenar el piso (**{r['b_pot']}²**)?")
    
    # Generación del HTML para el Plano de Potencia
    cuadritos_pot = ""
    for fila in range(r['b_pot']):
        for col in range(r['b_pot']):
            if fila == r['b_pot'] - 1 and col == 0: color = "background: linear-gradient(135deg, #f472b6, #3b82f6);"
            elif fila == r['b_pot'] - 1: color = "background-color: #3b82f6;"  # Base Azul
            elif col == 0: color = "background-color: #f472b6;"  # Altura Rosa
            else: color = "background-color: #f59e0b;"  # Relleno Ámbar
            cuadritos_pot += f'<div style="{color} border: 1px solid #1e293b; border-radius: 4px; aspect-ratio: 1/1;"></div>'

    html_potencia = f"""
    <div style="background-color: #1e293b; padding: 12px; border-radius: 12px; border: 2px solid #3b82f6; max-width: 340px; margin: 0 auto; font-family: sans-serif;">
        <div style="color: #60a5fa; font-weight: bold; font-size: 12px; text-align: center; margin-bottom: 10px;">🔨 CONSTRUYENDO: Plano de {r['b_pot']} × {r['b_pot']}</div>
        <div style="display: grid; grid-template-columns: repeat({r['b_pot']}, 1fr); gap: 4px; background: #0f172a; padding: 8px; border-radius: 6px; max-width: 180px; margin: 0 auto;">
            {cuadritos_pot}
        </div>
    </div>
    """
    st.components.v1.html(html_potencia, height=250)
    
    user_pot = st.number_input("Total de bloques para construir el piso:", step=1, key=f"f_p_{gid}", value=None)
    
    st.divider()
    
    # =========================================================================
    # 🔍 ZONA 2: LA CUEVA DE LAS RAÍCES (DESMANTELAR)
    # =========================================================================
    st.header("⏫ 2. La Cueva de las Raíces (Desarmar)")
    st.write(f"Entraste a una habitación oculta que ya está pavimentada con **{r['c_raiz']}** bloques en total. Para abrir la salida, necesitas calcular cuánto mide una sola de sus paredes (**√{r['c_raiz']}**).")
    
    # Generación del HTML para el Plano de Raíz (Efecto misterioso/cerrado todo en morado/ámbar)
    cuadritos_raiz = ""
    for fila in range(r['b_raiz']):
        for col in range(r['b_raiz']):
            # Dibujamos las paredes exteriores que debe adivinar en un tono lila/roto, y el centro misterioso
            if fila == r['b_raiz'] - 1 or col == 0:
                color = "background-color: #a855f7;"  # Muros a descubrir (Morado)
            else:
                color = "background-color: #475569;"  # Bloques encerrados
            cuadritos_raiz += f'<div style="{color} border: 1px solid #1e293b; border-radius: 4px; aspect-ratio: 1/1;"></div>'

    html_raiz = f"""
    <div style="background-color: #1e293b; padding: 12px; border-radius: 12px; border: 2px solid #a855f7; max-width: 340px; margin: 0 auto; font-family: sans-serif;">
        <div style="color: #c084fc; font-weight: bold; font-size: 12px; text-align: center; margin-bottom: 10px;">🔍 CUARTO CERRADO: {r['c_raiz']} bloques adentro</div>
        <div style="display: grid; grid-template-columns: repeat({r['b_raiz']}, 1fr); gap: 4px; background: #0f172a; padding: 8px; border-radius: 6px; max-width: 180px; margin: 0 auto;">
            {cuadritos_raiz}
        </div>
    </div>
    """
    st.components.v1.html(html_raiz, height=250)
    st.info(f"🤔 *Pregunta de la Cueva:* ¿Qué longitud de pared multiplicada **por sí misma** genera los {r['c_raiz']} bloques?")
    
    user_raiz = st.number_input("Medida secreta de la pared:", step=1, key=f"f_r_{gid}", value=None)
    
    # =========================================================================
    # 🏟️ EVALUACIÓN DEL MÓDULO
    # =========================================================================
    st.write("")
    if st.button("⚒️ Sellar Registros en la Forja"):
        if user_pot == r['c_pot'] and user_raiz == r['b_raiz']:
            st.balloons()
            st.success(f"¡PERFECTO MAESTRO! Sabes construir con potencias ({r['b_pot']}² = {r['c_pot']}) y sabes abrir cerraduras con raíces (√{r['c_raiz']} = {r['b_raiz']}).")
        else:
            st.error("Uno de los dos planos no está bien calculado. Revisa tus multiplicaciones mentales.")
            
    if st.button("🔄 Generar Nuevos Planos"):
        st.session_state.game_id_forja += 1
        del st.session_state.reto_forja
        st.rerun()