import streamlit as st
import streamlit.components.v1 as components
import random

def modulo_divisibilidad_streamlit():
    # --- DETALLE 2: Títulos con MCM y MCD correctamente en mayúsculas ---
    st.title("👑 Reglas del Reino (MCM y MCD)")
    
    sub_tema = st.radio(
        "Elige tu entrenamiento:",
        ["Sincronización de Antorchas (MCM)", "El Reparto Justo del Botín (MCD)"],
        horizontal=True
    )
    st.divider()

    if sub_tema == "Sincronización de Antorchas (MCM)":
        # --- DETALLE 3: Definición ultra clara para personas que inician desde cero ---
        st.markdown("""
        ### 📊 ¿Qué es el Mínimo Común Múltiplo (MCM)?
        Imagina que varios eventos se repiten en tiempos diferentes (como el parpadeo de luces o las guardias de los vigías). 
        El **MCM** es simplemente **el momento más cercano en el futuro en el que todos van a coincidir al mismo tiempo**.
        * **Múltiplo:** Los números que salen de la tabla de multiplicar de cada valor.
        * **Común:** Que es el mismo número para todos.
        * **Mínimo:** El primero que encuentres en la línea del tiempo.
        """)
        
        if 'datos_mcm' not in st.session_state:
            st.session_state.datos_mcm = (3, 4, 6) # Puedes hacerlo dinámico después
            
        t1, t2, t3 = st.session_state.datos_mcm
        
        st.info(f"""
        🏰 **Misión del Reino:** Para evitar que el castillo quede a oscuras, los vigías cambian sus antorchas en intervalos diferentes:
        * 🎯 **Torre Norte:** Cada **{t1}** horas.
        * 🎯 **Torre Sur:** Cada **{t2}** horas.
        * 🎯 **Torre Este:** Cada **{t3}** horas.
        """)

        # --- DETALLE 1: HTML/SVG Estable con altura explícita para que no se pierda ---
        html_linea_tiempo = f"""
        <div style="background-color: #1e293b; padding: 15px; border-radius: 12px; text-align: center; font-family: 'Segoe UI', sans-serif; color: white; border: 2px solid #475569;">
            <div style="color: #60a5fa; font-weight: bold; margin-bottom: 10px; font-size: 14px; text-transform: uppercase;">⏳ Línea de Tiempo del Reino</div>
            <div style="text-align: left; font-size: 13px; color: #94a3b8; line-height: 22px;">
                • <b>Vigía 1 ({t1}h):</b> {t1}h, {t1*2}h, {t1*3}h, {t1*4}h, {t1*5}h... <br>
                • <b>Vigía 2 ({t2}h):</b> {t2}h, {t2*2}h, {t2*3}h, {t2*4}h, {t2*5}h... <br>
                • <b>Vigía 3 ({t3}h):</b> {t3}h, {t3*2}h, {t3*3}h, {t3*4}h, {t3*5}h... <br>
            </div>
            <div style="margin-top: 10px; padding: 5px; background: rgba(0,0,0,0.2); font-size: 12px; color: #f59e0b;">
                💡 <i>Busca el número más chico que aparezca en las tres filas.</i>
            </div>
        </div>
        """
        components.html(html_linea_tiempo, height=160)
        
        # Entrada del usuario
        user_mcm = st.number_input("¿En cuántas horas volverán a coincidir todos los vigías?", step=1, value=None, placeholder="Encuentra el MCM")
        
        if st.button("🔏 Sellar Guardia (Verificar)"):
            if user_mcm == 12: # MCM de 3, 4, 6
                st.success("¡Excelente estratega! A las 12 horas todas las antorchas se sincronizan.")
                st.balloons()
            else:
                st.error("Ese tiempo no es común para todos o no es el más pequeño. Revisa las listas de arriba.")

    elif sub_tema == "El Reparto Justo del Botín (MCD)":
        # --- DETALLE 3: Definición conceptual intuitiva para MCD ---
        st.markdown("""
        ### 📦 ¿Qué es el Máximo Común Divisor (MCD)?
        Imagina que tienes grandes cantidades de recursos diferentes y quieres **organizarlos en grupos o cofres exactamente iguales**, sin que sobre nada y haciendo los grupos **lo más grandes posibles**.
        * **Divisor:** Un número que corta o divide a tus recursos de forma exacta (sin dejar decimales).
        * **Común:** El tamaño de grupo sirve tanto para el oro como para la plata.
        * **Máximo:** El contenedor más grande posible para terminar más rápido.
        """)

        if 'datos_mcd' not in st.session_state:
            st.session_state.datos_mcd = (18, 27)

        oro, plata = st.session_state.datos_mcd

        st.warning(f"""
        💰 **Recursos en la Cámara Real:** Tienen **{oro} Monedas de Oro** y **{plat} Barras de Plata**.
        El Rey exige guardarlos en cofres idénticos. No se pueden mezclar tipos de monedas en la misma división interna y no debe sobrar absolutamente nada.
        """)

        # --- DETALLE 1: Renderizado fijo garantizado ---
        html_fraccionamiento = f"""
        <div style="background-color: #1e293b; padding: 15px; border-radius: 12px; text-align: center; font-family: 'Segoe UI', sans-serif; color: white; border: 2px solid #475569;">
            <div style="color: #a855f7; font-weight: bold; margin-bottom: 10px; font-size: 14px; text-transform: uppercase;">📐 Regla de Fraccionamiento</div>
            <div style="text-align: left; font-size: 13px; color: #94a3b8; line-height: 22px;">
                • Números que dividen al <b>Oro ({oro})</b> exactamente: 1, 2, 3, 6, <b>9</b>, 18.<br>
                • Números que dividen al la <b>Plata ({plata})</b> exactamente: 1, 3, <b>9</b>, 27.<br>
            </div>
            <div style="margin-top: 10px; padding: 5px; background: rgba(0,0,0,0.2); font-size: 12px; color: #f59e0b;">
                💡 <i>¿Cuál es el número más grande que comparte la plata y el oro para hacer los cofres?</i>
            </div>
        </div>
        """
        components.html(html_fraccionamiento, height=160)

        user_mcd = st.number_input("¿Cuál es el número máximo de cofres iguales que puedes armar?", step=1, value=None, placeholder="Busca el divisor común más grande")

        if st.button("👑 Distribuir Botín"):
            if user_mcd == 9: # MCD de 18, 27
                st.success("¡LOGRADO! Puedes armar 9 cofres idénticos (cada uno con 2 de oro y 3 de plata).")
                st.balloons()
            else:
                st.error("Ese tamaño de cofre deja recursos fuera o no es el más óptimo.")