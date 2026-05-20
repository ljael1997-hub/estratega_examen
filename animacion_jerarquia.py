import streamlit as st
import random

def modulo_jerarquia_streamlit():
    st.title("🛡️ Asalto a Fortalezas (Signos de Agrupación)")
    
    st.markdown("""
    ### 🏰 Las Leyes del Asedio
    Cuando una operación tiene paréntesis `()`, corchetes `[]` o llaves `{}`, estos actúan como **muros de defensa**.
    
    * 🚨 **La Regla Suprema:** Las operaciones de **ADENTRO** del muro tienen máxima prioridad, sin importar si son simples sumas del pueblo. ¡Primero se rescata a los de adentro!
    * 🧭 **Orden de Invasión:** Siempre se ataca desde el núcleo hacia afuera:
      1. **`()` Paréntesis** (Campamento interno)
      2. **`[]` Corchetes** (Muro medio)
      3. **`{}` Llaves** (Fortaleza exterior)
    """)
    
    if 'game_id_j复杂' not in st.session_state:
        st.session_state.game_id_j复杂 = 0
        
    if 'reto_j复杂' not in st.session_state:
        # Generamos un reto guiado de estructura: A + [ B × ( C - D ) ]
        c = random.randint(5, 12)
        d = random.randint(1, 4)
        inner_res = c - d          # Resultado del paréntesis
        
        b = random.randint(2, 4)
        mid_res = b * inner_res    # Resultado del corchete
        
        a = random.randint(5, 15)
        final_res = a + mid_res    # Resultado final
        
        st.session_state.reto_j复杂 = {
            "txt": f"{a} + [ {b} × ({c} - {d}) ]",
            "a": a, "b": b, "c": c, "d": d,
            "p1_pide": f"Destruir el campamento interno: ({c} - {d})",
            "p1_res": inner_res,
            "p2_pide": f"Derribar el muro medio: [ {b} × {inner_res} ]",
            "p2_res": mid_res,
            "final": final_res
        }
        
    r = st.session_state.reto_j复杂
    gid = st.session_state.game_id_j复杂
    
    st.divider()
    
    # --- INTERFAZ VISUAL: EL ESCÁNER DE FORTALEZAS (HTML/CSS) ---
    html_fortaleza = f"""
    <div style="
        background-color: #1e293b; 
        padding: 20px; 
        border-radius: 12px; 
        border: 2px solid #ec4899;
        max-width: 400px;
        margin: 0 auto;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.3);
        font-family: 'Segoe UI', sans-serif;
        text-align: center;
    ">
        <div style="color: #f472b6; font-weight: bold; font-size: 13px; margin-bottom: 15px; text-transform: uppercase; letter-spacing: 1px;">
            📡 Escáner de Asedio Activo
        </div>
        
        <div style="border: 2px dashed #94a3b8; padding: 12px; border-radius: 8px; background-color: #0f172a;">
            <span style="color: #94a3b8; font-size: 16px; font-weight: bold;">{r['a']} + [</span>
            
            <div style="display: inline-block; border: 2px solid #3b82f6; padding: 6px 10px; border-radius: 6px; margin: 4px; background-color: rgba(59, 130, 246, 0.1);">
                <span style="color: #60a5fa; font-weight: bold;">{r['b']} × </span>
                
                <div style="display: inline-block; border: 2px solid #ec4899; padding: 4px 8px; border-radius: 4px; background-color: rgba(236, 72, 153, 0.15); color: #f472b6; font-weight: bold; box-shadow: 0 0 8px rgba(236, 72, 153, 0.4);">
                    ({r['c']} - {r['d']})
                </div>
                
                <span style="color: #60a5fa; font-weight: bold;"> ]</span>
            </div>
        </div>
        
        <div style="color: #94a3b8; font-size: 11px; margin-top: 12px; line-height: 15px;">
            El objetivo brillante <span style="color: #ec4899; font-weight: bold;">Rosa</span> es el núcleo. ¡Ningún soldado exterior puede tocarlo hasta que resuelvas lo de adentro!
        </div>
    </div>
    """
    st.components.v1.html(html_fortaleza, height=170)
    
    # --- PANEL DE ACCIONES DE REFUERZO ---
    st.subheader("⚔️ Fase 1: Infiltración al Núcleo")
    st.write(f"Resuelve primero el campamento protegido: `{r['p1_pide']}`")
    user_p1 = st.number_input("Resultado del núcleo rosa:", step=1, key=f"fort_a_{gid}", value=None, placeholder="¿Cuánto da la resta?")
    
    st.divider()
    
    st.subheader("🛡️ Fase 2: Romper el Muro Medio")
    st.write(f"Con el campamento destruido, el corchete azul queda expuesto: `{r['p2_pide']}`")
    user_p2 = st.number_input("Resultado del muro azul:", step=1, key=f"fort_b_{gid}", value=None, placeholder="¿Cuánto da la multiplicación?")
    
    st.divider()
    
    st.subheader("👑 Fase 3: El Veredicto del Rey")
    st.write(f"Por último, suma el soldado libre del inicio con lo que quedó de la fortaleza destruida.")
    user_final = st.number_input(f"¿Cuál es el valor final de toda la fortaleza?", step=1, key=f"fort_f_{gid}", value=None, placeholder=f"Suma: {r['a']} + Tu Paso 2")
    
    st.write("")
    if st.button("🏟️ Derribar Fortaleza"):
        if user_p1 == r['p1_res'] and user_p2 == r['p2_res'] and user_final == r['final']:
            st.balloons()
            st.success(f"¡VICTORIA TOTAL COMANDANTE! Conquistaste la fortaleza paso a paso. El resultado real es {r['final']}.")
        else:
            st.error("El asedio falló. Algún muro se defendió bien. Revisa el orden de operaciones (Primero adentro, luego afuera).")
            
    if st.button("🔄 Buscar Nueva Fortaleza"):
        st.session_state.game_id_j复杂 += 1
        del st.session_state.reto_j复杂
        st.rerun()