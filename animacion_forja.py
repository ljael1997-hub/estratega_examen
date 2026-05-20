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
    
    # --- INTERFAZ VISUAL: PLANO DEL PISO CON EJES EN COLORES ---
    cuadritos_html = "".join([
        '<div style="background-color: #f59e0b; border: 1px solid #1e293b; border-radius: 4px; aspect-ratio: 1/1;"></div>' 
        for _ in range(r['cuadrado'])
    ])
    
    # Generamos la cadena visual de la operación para los ejes (ej: "2 x 2")
    operacion_eje = f"{r['base']} × {r['base']}"
    
    html_constructor = f"""
    <div style="
        background-color: #1e293b; 
        padding: 20px; 
        border-radius: 12px; 
        border: 2px solid #475569;
        max-width: 420px;
        margin: 0 auto;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.3);
        font-family: 'Segoe UI', sans-serif;
    ">
        <div style="color: #ffffff; font-weight: bold; margin-bottom: 20px; font-size: 14px; text-align: center; background: rgba(0,0,0,0.2); padding: 6px; border-radius: 6px;">
            📐 Plano: Cuarto Cuadrado de <span style="color: #60a5fa;">{r['base']}</span> por <span style="color: #f472b6;">{r['base']}</span>
        </div>
        
        <div style="position: relative; max-width: 300px; margin: 0 auto; padding-left: 40px; padding-bottom: 40px;">
            
            # Etiqueta del Ancho (Eje Vertical Izquierdo en Rosa)
            <div style="
                position: absolute; 
                left: 0; 
                top: 35%; 
                transform: translateY(-50%) rotate(-90deg); 
                transform-origin: left bottom;
                color: #f472b6; 
                font-weight: bold; 
                font-size: 14px;
                white-space: nowrap;
            ">
                ← Ancho: {operacion_eje} →
            </div>
            
            # Plano Central de la Cuadrícula
            <div style="
                background-color: #0f172a;
                padding: 12px;
                border-radius: 8px;
                border: 1px solid #334155;
                display: grid;
                grid-template-columns: repeat({r['base']}, 1fr);
                gap: 4px;
                width: 100%;
                box-sizing: border-box;
            ">
                {cuadritos_html}
            </div>
            
            # Etiqueta del Largo (Eje Horizontal Inferior en Azul)
            <div style="
                position: absolute; 
                bottom: 10px; 
                left: 40px; 
                right: 0;
                text-align: center; 
                color: #60a5fa; 
                font-weight: bold; 
                font-size: 14px;
            ">
                ← Largo: {operacion_eje} →
            </div>
        </div>
        
        <div style="color: #94a3b8; font-size: 12px; text-align: center; margin-top: 15px; line-height: 16px;">
            Multiplica la línea <span style="color: #60a5fa; font-weight:bold;">Azul</span> por la línea <span style="color: #f472b6; font-weight:bold;">Rosa</span> para rellenar todo el suelo.
        </div>
    </div>
    """
    
    # Renderizado corregido sin el parámetro html_content
    st.components.v1.html(html_constructor, height=340)
    
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