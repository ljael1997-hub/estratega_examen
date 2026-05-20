import streamlit as st
import random

def modulo_forja_streamlit():
    st.title("⚒️ La Forja de Números (Leyes de Construcción)")
    
    st.markdown("""
    ### 🧱 Los Dos Lados del Espejo
    Para dominar los exámenes necesitas dos habilidades: **Construir** pisos usando potencias y **Desmantelar** cuartos usando raíces cuadradas.
    """)
    
    if 'game_id_forja' not in st.session_state: 
        st.session_state.game_id_forja = 0
        
    if 'reto_forja' not in st.session_state:
        lado_pot = random.choice([2, 3, 4, 5, 6])
        lado_raiz = random.choice([2, 3, 4, 5, 6])
        while lado_raiz == lado_pot:  
            lado_raiz = random.choice([2, 3, 4, 5, 6])
            
        st.session_state.reto_forja = {
            "b_pot": lado_pot,
            "c_pot": lado_pot ** 2,
            "b_raiz": lado_raiz,
            "c_raiz": lado_raiz ** 2
        }
        
    r = st.session_state.reto_forja
    gid = st.session_state.game_id_forja
    
    st.divider()
    
    # =========================================================================
    # ⚔️ ZONA 1: LA FORJA DE POTENCIAS (CONSTRUIR)
    # =========================================================================
    st.header("⏬ 1. La Forja de Potencias (Multiplicar)")
    st.write(f"Diseña un cuarto cuadrado que mida **{r['b_pot']}** bloques de largo por **{r['b_pot']}** de ancho. ¿Cuántos bloques usarás en total para rellenar el piso?")
    
    cuadritos_pot = ""
    for fila in range(r['b_pot']):
        for col in range(r['b_pot']):
            if fila == r['b_pot'] - 1 and col == 0: color = "background: linear-gradient(135deg, #f472b6, #3b82f6);"
            elif fila == r['b_pot'] - 1: color = "background-color: #3b82f6;"  
            elif col == 0: color = "background-color: #f472b6;"  
            else: color = "background-color: #f59e0b;"  
            cuadritos_pot += f'<div style="{color} border: 1px solid #1e293b; border-radius: 4px; aspect-ratio: 1/1;"></div>'

    operacion_eje_pot = f"{r['b_pot']} × {r['b_pot']}"

    html_potencia = f"""
    <div style="
        background-color: #1e293b; 
        padding: 15px 15px 25px 15px; 
        border-radius: 12px; 
        border: 2px solid #3b82f6; 
        max-width: 360px; 
        margin: 0 auto; 
        font-family: 'Segoe UI', sans-serif; 
        box-sizing: border-box;
    ">
        <div style="color: #60a5fa; font-weight: bold; font-size: 13px; text-align: center; margin-bottom: 20px; background: rgba(0,0,0,0.2); padding: 5px; border-radius: 4px;">
            🔨 CONSTRUYENDO: Plano Base
        </div>
        
        <div style="display: flex; align-items: center; justify-content: center; position: relative; padding-left: 35px; padding-bottom: 35px; box-sizing: border-box;">
            
            <div style="
                position: absolute;
                left: -10px;
                top: calc(50% - 17px);
                transform: rotate(-90deg);
                color: #f472b6;
                font-weight: bold;
                font-size: 13px;
                white-space: nowrap;
            ">
                ← Ancho: {operacion_eje_pot} →
            </div>
            
            <div style="
                background: #0f172a; 
                padding: 8px; 
                border-radius: 6px; 
                display: grid; 
                grid-template-columns: repeat({r['b_pot']}, 1fr); 
                gap: 4px; 
                width: 100%;
                max-width: 180px;
                box-sizing: border-box;
            ">
                {cuadritos_pot}
            </div>
            
            <div style="
                position: absolute;
                bottom: -5px;
                left: 35px;
                right: 0;
                text-align: center;
                color: #60a5fa;
                font-weight: bold;
                font-size: 13px;
                white-space: nowrap;
            ">
                ← Largo: {operacion_eje_pot} →
            </div>
        </div>
    </div>
    """
    st.components.v1.html(html_potencia, height=310)
    
    # BANNER ROJO INTERACTIVE
    st.markdown("""
        <div style="background-color: rgba(220, 53, 69, 0.1); padding: 10px; border-radius: 6px; border-left: 5px solid #dc3545; margin: 15px 0 10px 0;">
            <span style="color: #ff6b6b; font-weight: bold; font-size: 15px; letter-spacing: 0.5px;">🚨 RESUELVE LO SIGUIENTE:</span>
        </div>
    """, unsafe_allow_html=True)
    st.code(f"Misión de Examen: {r['b_pot']}²", language="text")
    
    user_pot = st.number_input("Total de bloques para construir el piso:", step=1, key=f"f_p_{gid}", value=None, placeholder="Multiplica largo por ancho")
    
    st.divider()
    
    # =========================================================================
    # 🔍 ZONA 2: LA CUEVA DE LAS RAÍCES (DESMANTELAR)
    # =========================================================================
    st.header("⏫ 2. La Cueva de las Raíces (Desarmar)")
    st.write(f"Entraste a una habitación oculta pavimentada con **{r['c_raiz']}** bloques en total. Calcula cuánto mide una sola de sus paredes para abrir la cerradura.")
    
    cuadritos_raiz = ""
    for fila in range(r['b_raiz']):
        for col in range(r['b_raiz']):
            if fila == r['b_raiz'] - 1 and col == 0: color = "background: linear-gradient(135deg, #a855f7, #c084fc);"
            elif fila == r['b_raiz'] - 1: color = "background-color: #a855f7;"  
            elif col == 0: color = "background-color: #a855f7;"  
            else: color = "background-color: #475569;"  
            cuadritos_raiz += f'<div style="{color} border: 1px solid #1e293b; border-radius: 4px; aspect-ratio: 1/1;"></div>'

    html_raiz = f"""
    <div style="
        background-color: #1e293b; 
        padding: 15px; 
        border-radius: 12px; 
        border: 2px solid #a855f7; 
        max-width: 360px; 
        margin: 0 auto; 
        font-family: 'Segoe UI', sans-serif; 
        box-sizing: border-box;
    ">
        <div style="color: #c084fc; font-weight: bold; font-size: 13px; text-align: center; margin-bottom: 20px; background: rgba(0,0,0,0.2); padding: 5px; border-radius: 4px;">
            🔍 CUARTO CERRADO: {r['c_raiz']} bloques totales
        </div>
        
        <div style="display: flex; align-items: center; justify-content: center; position: relative; padding-left: 35px; padding-bottom: 35px; box-sizing: border-box;">
            
            <div style="
                position: absolute;
                left: -10px;
                top: calc(50% - 17px);
                transform: rotate(-90deg);
                color: #c084fc;
                font-weight: bold;
                font-size: 13px;
                white-space: nowrap;
            ">
                ← Pared: ❓ →
            </div>
            
            <div style="
                display: grid; 
                grid-template-columns: repeat({r['b_raiz']}, 1fr); 
                gap: 4px; 
                background: #0f172a; 
                padding: 8px; 
                border-radius: 6px; 
                width: 100%;
                max-width: 180px;
                box-sizing: border-box;
            ">
                {cuadritos_raiz}
            </div>
            
            <div style="
                position: absolute;
                bottom: -5px;
                left: 35px;
                right: 0;
                text-align: center;
                color: #c084fc;
                font-weight: bold;
                font-size: 13px;
                white-space: nowrap;
            ">
                ← Base: ❓ →
            </div>
        </div>
    </div>
    """
    st.components.v1.html(html_raiz, height=310)
    
    # BANNER ROJO INTERACTIVE
    st.markdown("""
        <div style="background-color: rgba(220, 53, 69, 0.1); padding: 10px; border-radius: 6px; border-left: 5px solid #dc3545; margin: 15px 0 10px 0;">
            <span style="color: #ff6b6b; font-weight: bold; font-size: 15px; letter-spacing: 0.5px;">🚨 RESUELVE LO SIGUIENTE:</span>
        </div>
    """, unsafe_allow_html=True)
    st.code(f"Misión de Examen: √{r['c_raiz']}", language="text")
    
    user_raiz = st.number_input("Medida secreta de la pared:", step=1, key=f"f_r_{gid}", value=None, placeholder="Busca: ? × ? = " + str(r['c_raiz']))
    
    # =========================================================================
    # 🏟️ EVALUACIÓN DEL MÓDULO
    # =========================================================================
    st.write("")
    if st.button("⚒️ Sellar Registros en la Forja"):
        if user_pot == r['c_pot'] and user_raiz == r['b_raiz']:
            st.balloons()
            st.success(f"¡PERFECTO MAESTRO! Sabes construir con potencias ({r['b_pot']}² = {r['c_pot']}) y desmantelar con raíces (√{r['c_raiz']} = {r['b_raiz']}).")
        else:
            st.error("Uno de los dos planos no está bien calculated. Revisa tus multiplicaciones mentales.")
            
    if st.button("🔄 Generar Nuevos Planos"):
        st.session_state.game_id_forja += 1
        del st.session_state.reto_forja
        st.rerun()