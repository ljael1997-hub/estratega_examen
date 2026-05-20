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
    
    # --- INTERFAZ VISUAL: AJUSTE DE ESPACIOS Y DEGRADADO DE INTERSECCIÓN ---
    cuadritos_html = ""
    base_dinamica = r['base']
    
    for fila in range(base_dinamica):
        for col in range(base_dinamica):
            # Esquina inferior izquierda (Intersección: Última fila, Primera columna)
            if fila == base_dinamica - 1 and col == 0:
                estilo_color = "background: linear-gradient(135deg, #f472b6, #3b82f6);"
            # Última fila completa: La Base del Largo (Azul)
            elif fila == base_dinamica - 1:
                estilo_color = "background-color: #3b82f6;"
            # Primera columna completa: La Pared del Ancho (Rosa)
            elif col == 0:
                estilo_color = "background-color: #f472b6;"
            # Relleno del cuarto (Ámbar)
            else:
                estilo_color = "background-color: #f59e0b;"
                
            cuadritos_html += f'<div style="{estilo_color} border: 1px solid #1e293b; border-radius: 4px; aspect-ratio: 1/1;"></div>'

    operacion_eje = f"{base_dinamica} × {base_dinamica}"

    html_constructor = f"""
    <div style="
        background-color: #1e293b; 
        padding: 15px; 
        border-radius: 12px; 
        border: 2px solid #475569;
        max-width: 400px;
        margin: 0 auto;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.3);
        font-family: 'Segoe UI', sans-serif;
        box-sizing: border-box;
    ">
        <div style="color: #ffffff; font-weight: bold; margin-bottom: 20px; font-size: 13px; text-align: center; background: rgba(0,0,0,0.2); padding: 6px; border-radius: 6px;">
            📐 Plano: Cuarto Cuadrado de <span style="color: #60a5fa;">{base_dinamica}</span> por <span style="color: #f472b6;">{base_dinamica}</span>
        </div>
        
        <table style="width: 100%; border-collapse: collapse; box-sizing: border-box;">
            <tr>
                <td style="vertical-align: middle; width: 50px; min-width: 50px; padding-right: 10px; text-align: center; box-sizing: border-box;">
                    <div style="
                        color: #f472b6; 
                        font-weight: bold; 
                        font-size: 13px;
                        writing-mode: vertical-rl;
                        transform: rotate(180deg);
                        white-space: nowrap;
                        display: inline-block;
                        line-height: 1;
                    ">
                        ← Ancho: {operacion_eje} →
                    </div>
                </td>
                
                <td style="vertical-align: bottom; padding-bottom: 10px;">
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
                </td>
            </tr>
            <tr>
                <td style="width: 50px;"></td>
                <td style="padding-top: 10px; text-align: center; box-sizing: border-box;">
                    <div style="color: #60a5fa; font-weight: bold; font-size: 13px; white-space: nowrap; line-height: 1;">
                        ← Largo: {operacion_eje} →
                    </div>
                </td>
            </tr>
        </table>
        
        <div style="color: #94a3b8; font-size: 11px; text-align: center; margin-top: 15px; line-height: 15px;">
            Multiplica la base <span style="color: #60a5fa; font-weight:bold;">Azul</span> por la altura <span style="color: #f472b6; font-weight:bold;">Rosa</span>. La esquina <span style="background: linear-gradient(45deg, #f472b6, #3b82f6); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight:bold;">Fusión</span> une ambos caminos.
        </div>
    </div>
    """
    
    # Mantenemos los 380px de altura para que el texto inferior no se corte nunca con el borde del componente
    st.components.v1.html(html_constructor, height=380)
    
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