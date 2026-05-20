import streamlit as st
import random
import math

# --- INTERFAZ VISUAL: CORRECCIÓN DE CONTENEDORES CON FLEXBOX INTERACTIVO ---
    # Generamos los pisos. Nota: Quitamos el reversed para que se rendericen de forma natural en el contenedor flex invertido
    pisos_base_html = "".join([
        f'<div style="background-color: #3b82f6; border: 1px solid #111827; height: 18px; width: 85%; margin: 2px auto; border-radius: 4px; color: white; font-size: 11px; font-weight: bold; text-align: center; line-height: 18px; flex-shrink: 0;">Piso {i+1}</div>' 
        for i in range(r['base'])
    ])
    
    pisos_mega_html = "".join([
        f'<div style="background-color: #f59e0b; border: 1px solid #111827; height: 18px; width: 85%; margin: 2px auto; border-radius: 4px; color: #111827; font-size: 11px; font-weight: bold; text-align: center; line-height: 18px; flex-shrink: 0;">Piso {i+1}</div>' 
        for i in range(r['cuadrado'])
    ])
    
    html_torres = f"""
    <div style="
        background-color: #1e293b; 
        padding: 15px; 
        border-radius: 12px; 
        font-family: 'Segoe UI', sans-serif; 
        border: 2px solid #475569;
        display: flex;
        justify-content: space-around;
        gap: 15px;
        max-width: 500px;
        margin: 0 auto;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.3);
    ">
        <div style="width: 45%; display: flex; flex-direction: column; align-items: center;">
            <div style="color: #60a5fa; font-weight: bold; margin-bottom: 10px; font-size: 14px; text-align: center;">
                🏰 Torre Base ({r['base']} pisos)
            </div>
            <div style="
                background-color: #0f172a; 
                border-radius: 8px; 
                padding: 10px 5px; 
                width: 100%; 
                height: 220px; 
                display: flex; 
                flex-direction: column-reverse; 
                overflow-y: auto;
                border: 1px solid #334155;
            ">
                {pisos_base_html}
            </div>
        </div>

        <div style="width: 45%; display: flex; flex-direction: column; align-items: center;">
            <div style="color: #fbbf24; font-weight: bold; margin-bottom: 10px; font-size: 14px; text-align: center;">
                ⚡ Mega Torre ({r['cuadrado']} pisos)
            </div>
            <div style="
                background-color: #0f172a; 
                border-radius: 8px; 
                padding: 10px 5px; 
                width: 100%; 
                height: 220px; 
                display: flex; 
                flex-direction: column-reverse; 
                overflow-y: auto;
                border: 1px solid #334155;
            ">
                {pisos_mega_html}
            </div>
        </div>
    </div>
    """
    
    # Renderizado final con altura controlada para que no empuje el resto de la interfaz hacia abajo
    st.components.v1.html(html_torres, height=290)
    
    # --- SECCIÓN DE PREGUNTAS ---
    st.subheader("⚔️ Fase A: Desata el Crecimiento")
    st.write(f"Si aplicamos el hechizo al cuadrado a la **Torre Base de {r['base']} pisos**... ¿En cuántos pisos se convertirá?")
    st.caption(f"💡 Pista de la Forja: Multiplica la altura por sí misma (`{r['base']} × {r['base']}`).")
    user_pot = st.number_input("Pisos finales de la Mega Torre:", step=1, key=f"torre_p_{gid}", value=None, placeholder="Escribe el total de pisos")
    
    st.divider()
    
    st.subheader("🔍 Fase B: El Conjuro de Encogimiento")
    st.write(f"Ahora mira la **Mega Torre de {r['cuadrado']} pisos**. Si le aplicas una raíz cuadrada (**√{r['cuadrado']}**), volverá a su tamaño original.")
    st.info(f"🤔 *Pregunta Clave:* ¿Qué número de pisos multiplicado **por sí mismo** da como resultado {r['cuadrado']}?")
    user_raiz = st.number_input("Altura original de la torre:", step=1, key=f"torre_r_{gid}", value=None, placeholder="Busca: ? × ? = " + str(r['cuadrado']))
    
    st.write("")
    if st.button("⚒️ Conjurar en la Forja"):
        if user_pot == r['cuadrado'] and user_raiz == r['base']:
            st.balloons()
            st.success(f"¡LOGRADO! Comprendes el equilibrio perfecto del reino: la potencia estira la torre a {r['cuadrado']} pisos y la raíz la encoge de vuelta a {r['base']}.")
        else:
            st.error("Los hechizos no se equilibraron. Recuerda: la Mega Torre debe ser el resultado de multiplicar la base por sí misma.")
            
    if st.button("🔄 Forjar Nuevas Torres"):
        st.session_state.game_id_forja += 1
        del st.session_state.reto_forja
        st.rerun()