import streamlit as st
import random
import math

def modulo_forja_streamlit():
    st.title("⚒️ La Forja de Números (Torres de Poder)")
    
    st.markdown("""
    ### 🏰 El Hechizo de las Torres
    En los exámenes de admisión, las potencias y las raíces son como conjuros de crecimiento y encogimiento para las torres del reino.
    
    * ⏫ **Elevar al Cuadrado (²):** Es el hechizo de **Crecimiento**. Si tu torre mide **3 pisos**, el hechizo la hace crecer multiplicando su altura original por sí misma ($3 \\times 3$). ¡Se transforma en una torre de **9 pisos**!
    * ⏬ **Raíz Cuadrada (√):** Es el hechizo de **Encogimiento**. Si te dan una mega torre de **9 pisos**, la raíz cuadrada descubre de qué tamaño era originalmente antes del hechizo. ¡Regresa a ser de **3 pisos**!
    """)
    
    if 'game_id_forja' not in st.session_state: 
        st.session_state.game_id_forja = 0
        
    if 'reto_forja' not in st.session_state:
        # Alturas de torre amigables para el alumno (de 2 a 6 pisos)
        altura_original = random.choice([2, 3, 4, 5, 6])
        mega_altura = altura_original ** 2
        st.session_state.reto_forja = {
            "base": altura_original,
            "cuadrado": mega_altura
        }
        
    r = st.session_state.reto_forja
    gid = st.session_state.game_id_forja
    
    st.divider()
    
    # --- INTERFAZ VISUAL: CONSTRUCCIÓN DE LAS TORRES EN HTML/CSS ---
    # Generamos los pisos apilados de abajo hacia arriba para ambas torres
    pisos_base_html = "".join([f'<div style="background-color: #3b82f6; border: 2px solid #1e293b; height: 20px; width: 80px; margin: 2px auto; border-radius: 4px; color: white; font-size: 10px; font-weight: bold; text-align: center; line-height: 16px;">Piso {_ + 1}</div>' for _ in reversed(range(r['base']))])
    
    pisos_mega_html = "".join([f'<div style="background-color: #f59e0b; border: 2px solid #1e293b; height: 12px; width: 80px; margin: 1px auto; border-radius: 2px; color: #1e293b; font-size: 8px; font-weight: bold; text-align: center; line-height: 10px;">Piso {_ + 1}</div>' for _ in reversed(range(r['cuadrado']))])
    
    html_torres = f"""
    <div style="background-color: #111827; padding: 15px; border-radius: 12px; font-family: 'Segoe UI', sans-serif; text-align: center; border: 1px solid #374151;">
        <table style="width: 100%; border-collapse: collapse;">
            <tr>
                <td style="width: 50%; vertical-align: bottom; padding: 10px; text-align: center;">
                    <div style="color: #60a5fa; font-weight: bold; margin-bottom: 10px; font-size: 13px;">🏰 Torre Base ({r['base']} pisos)</div>
                    <div style="display: block; margin: 0 auto;">{pisos_base_html}</div>
                </td>
                <td style="width: 50%; vertical-align: bottom; padding: 10px; text-align: center;">
                    <div style="color: #fbbf24; font-weight: bold; margin-bottom: 10px; font-size: 13px;">⚡ Mega Torre ({r['cuadrado']} pisos)</div>
                    <div style="display: block; margin: 0 auto;">{pisos_mega_html}</div>
                </td>
            </tr>
        </table>
    </div>
    """
    
    # Renderizamos las torres flotantes. Le damos suficiente altura (320px) para que quepan las torres de hasta 36 pisos (6x6)
    st.components.v1.html(html_torres, height=320)
    
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