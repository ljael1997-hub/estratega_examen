import streamlit as st
import random
import math

def modulo_forja_streamlit():
    st.title("⚒️ La Forja de Números (El Constructor de Pisos)")
    
    st.markdown("""
    ### 🧱 El Secreto del Área Cuadrada
    En los exámenes, elevar al cuadrado y sacar la raíz es como construir o medir los pisos de una fortaleza.
    
    * ⏹️ **Elevar al Cuadrado (²):** Es **construir** un piso. Si tu base es **4**, haces un piso de $4 \\times 4$ bloques. ¡Usarás **16 bloques** en total!
    * 🌱 **Raíz Cuadrada (√):** Es **medir** el piso. Te damos un cuarto ya hecho con **16 bloques** en total. Tu misión es descubrir **cuánto mide una sola de sus paredes** (Resultado = **4**).
    """)
    
    if 'game_id_forja' not in st.session_state: 
        st.session_state.game_id_forja = 0
        
    if 'reto_forja' not in st.session_state:
        # Tamaños de lado perfectos y amigables para la cuadrícula (de 2 a 6)
        lado = random.choice([2, 3, 4, 5, 6])
        bloques_totales = lado ** 2
        st.session_state.reto_forja = {
            "base": lado,
            "cuadrado": bloques_totales
        }
        
    r = st.session_state.reto_forja
    gid = st.session_state.game_id_forja
    
    st.divider()
    
    # --- INTERFAZ VISUAL: PLANO DEL PISO CON BORDES COLOREADOS ---
    # Generamos los cuadritos coloreando la base (azul) y la altura izquierda (rosa)
    cuadritos_html = ""
    base_dinamica = r['base']
    
    for fila in range(base_dinamica):
        for col in range(base_dinamica):
            # Si es el cuadrito de la esquina inferior izquierda (intersección)
            if fila == base_dinamica - 1 and col == 0:
                color = "#3b82f6"  # Azul (predomina la base o mezcla)
            # Si es de la última fila (la base del dibujo)
            elif fila == base_dinamica - 1:
                color = "#3b82f6"  # Azul para el Largo
            # Si es de la primera columna (el lado izquierdo)
            elif col == 0:
                color = "#f472b6"  # Rosa para el Ancho
            # Bloques internos de relleno
            else:
                color = "#f59e0b"  # Ámbar original
                
            cuadritos_html += f'<div style="background-color: {color}; border: 1px solid #1e293b; border-radius: 4px; aspect-ratio: 1/1;"></div>'

    # Texto exacto de la operación (ej: "2 × 2")
    operacion_eje = f"{base_dinamica} × {base_dinamica}"

    html_constructor = f"""
    <div style="
        background-color: #1e293b; 
        padding: 15px; 
        border-radius: 12px; 
        border: 2px solid #475569;
        max-width: 360px;
        margin: 0 auto;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.3);
        font-family: 'Segoe UI', sans-serif;
        box-sizing: border-box;
    ">
        <div style="color: #ffffff; font-weight: bold; margin-bottom: 15px; font-size: 13px; text-align: center; background: rgba(0,0,0,0.2); padding: 6px; border-radius: 6px;">
            📐 Plano: Cuarto Cuadrado de <span style="color: #60a5fa;">{base_dinamica}</span> por <span style="color: #f472b6;">{base_dinamica}</span>
        </div>
        
        <div style="position: relative; width: 100%; padding-left: 30px; padding-bottom: 30px; box-sizing: border-box;">
            
            <div style="
                position: absolute; 
                left: -5px; 
                top: 40%; 
                transform: translateY(-50%) rotate(-90deg); 
                transform-origin: center center;
                color: #f472b6; 
                font-weight: bold; 
                font-size: 13px;
                white-space: nowrap;
            ">
                ← Ancho: {operacion_eje} →
            </div>
            
            <div style="
                background-color: #0f172a;
                padding: 10px;
                border-radius: 8px;
                border: 1px solid #334155;
                display: grid;
                grid-template-columns: repeat({base_dinamica}, 1fr);
                gap: 4px;
                width: 100%;
                box-sizing: border-box;
            ">
                {cuadritos_html}
            </div>
            
            <div style="
                position: absolute; 
                bottom: 5px; 
                left: 30px; 
                right: 0;
                text-align: center; 
                color: #60a5fa; 
                font-weight: bold; 
                font-size: 13px;
            ">
                ← Largo: {operacion_eje} →
            </div>
        </div>
        
        <div style="color: #94a3b8; font-size: 11px; text-align: center; margin-top: 10px; line-height: 15px;">
            Multiplica los bloques <span style="color: #60a5fa; font-weight:bold;">Azules</span> de la base por los <span style="color: #f472b6; font-weight:bold;">Rosas</span> del lado para saber el total.
        </div>
    </div>
    """
    
    st.components.v1.html(html_constructor, height=360)
    
    # --- SECCIÓN DE PREGUNTAS ---
    st.subheader("⚔️ Misión 1: Forjar la Potencia")
    st.write(f"Si diseñas una habitación cuadrada que mida **{r['base']}** bloques de largo... ¿Cuántos bloques usarás en total para llenar todo el piso (**{r['base']}²**)?")
    st.caption(f"💡 Pista del maestro de obra: Multiplica lado por lado (`{r['base']} × {r['base']}`).")
    user_pot = st.number_input("Total de bloques del piso:", step=1, key=f"forja_p_{gid}", value=None, placeholder="Cuenta los bloques o multiplica")
    
    st.divider()
    
    st.subheader("🔍 Misión 2: El Inspector de Paredes")
    st.write(f"Ahora mira el plano de arriba con sus **{r['cuadrado']}** bloques totales. Si aplicas una raíz cuadrada (**√{r['cuadrado']}**), queremos saber cuánto mide una sola pared.")
    st.info(f"🤔 *Pregunta Clave:* ¿Qué número multiplicado **por sí mismo** da como resultado {r['cuadrado']}?")
    user_raiz = st.number_input("Longitud de una pared:", step=1, key=f"forja_r_{gid}", value=None, placeholder="Busca: ? × ? = " + str(r['cuadrado']))
    
    st.write("")
    if st.button("⚒️ Registrar Obra en la Forja"):
        if user_pot == r['cuadrado'] and user_raiz == r['base']:
            st.balloons()
            st.success(f"¡LOGRADO MAESTRO! El plano cuadra a la perfección: {r['base']}² es {r['cuadrado']} y la longitud de la pared (√{r['cuadrado']}) es {r['base']}.")
        else:
            st.error("Los planos no pasaron la inspección. Recuerda: el total de bloques debe ser igual a multiplicar la pared por sí misma.")
            
    if st.button("🔄 Generar Nuevo Plano"):
        st.session_state.game_id_forja += 1
        del st.session_state.reto_forja
        st.rerun()