import streamlit as st
import streamlit.components.v1 as components

def modulo_divisibilidad_streamlit():
    # Títulos con MCM y MCD correctamente en mayúsculas
    st.title("👑 Reglas del Reino (MCM y MCD)")
    
    sub_tema = st.radio(
        "Elige tu entrenamiento:",
        ["Sincronización de Antorchas (MCM)", "El Reparto Justo del Botín (MCD)"],
        horizontal=True
    )
    st.divider()

    if sub_tema == "Sincronización de Antorchas (MCM)":
        st.markdown("""
        ### 📊 ¿Qué es el Mínimo Común Múltiplo (MCM)?
        Imagina que varios eventos se repiten en tiempos diferentes (como el parpadeo de luces o las guardias de los vigías). 
        El **MCM** es simplemente **el momento más cercano en el futuro en el que todos van a coincidir al mismo tiempo**.
        """)
        
        tab_explicacion, tab_reto = st.tabs(["📖 ¿Cómo se calcula? (Ejemplo)", "🎯 ¡Pruébalo tú mismo!"])
        
        with tab_explicacion:
            st.markdown("""
            #### El método de las listas (Ideal para empezar)
            Para encontrar el MCM de varios números, escribimos sus tablas de multiplicar hasta encontrar el **primer número** que aparezca en todas las listas por igual.
            
            **Ejemplo Resuelto: Encontrar el MCM de 4 y 5**
            1. Escribimos los múltiplos de 4: 4, 8, 12, 16, **20**, 24, 28...
            2. Escribimos los múltiplos de 5: 5, 10, 15, **20**, 25, 30...
            
            *El menor número que comparten es el **20**. Por lo tanto, el MCM(4, 5) = 20.*
            """)
            
        with tab_reto:
            if 'datos_mcm' not in st.session_state:
                # Nivel Examen: Introducimos una terna con un MCM más elevado (8, 12, 15)
                st.session_state.datos_mcm = (8, 12, 15)
                
            t1, t2, t3 = st.session_state.datos_mcm
            
            st.info(f"""
            🏰 **Misión del Reino (Dificultad de Examen):** Para evitar que el castillo quede a oscuras, los vigías cambian sus antorchas en intervalos más complejos:
            * 🎯 **Torre Norte:** Cada **{t1}** horas.
            * 🎯 **Torre Sur:** Cada **{t2}** horas.
            * 🎯 **Torre Este:** Cada **{t3}** horas.
            """)

            # Contenedor visual estable adaptado a números más grandes
            html_linea_tiempo = f"""
            <div style="background-color: #1e293b; padding: 15px; border-radius: 12px; font-family: 'Segoe UI', sans-serif; color: white; border: 2px solid #475569;">
                <div style="color: #60a5fa; font-weight: bold; margin-bottom: 10px; font-size: 14px; text-transform: uppercase; text-align: center;">⏳ Línea de Tiempo de las Torres</div>
                <div style="text-align: left; font-size: 13px; color: #94a3b8; line-height: 24px;">
                    • <b>Torre Norte ({t1}h):</b> {t1}, {t1*2}, {t1*3}, {t1*4}, {t1*5}, {t1*6}, {t1*7}, {t1*8}, {t1*9}, {t1*10}, ... <br>
                    • <b>Torre Sur ({t2}h):</b> {t2}, {t2*2}, {t2*3}, {t2*4}, {t2*5}, {t2*6}, {t2*7}, {t2*8}, {t2*9}, {t2*10}, ... <br>
                    • <b>Torre Este ({t3}h):</b> {t3}, {t3*2}, {t3*3}, {t3*4}, {t3*5}, {t3*6}, {t3*7}, {t3*8}, {t3*9}, {t3*10}, ... <br>
                </div>
                <div style="margin-top: 12px; padding: 6px; background: rgba(0,0,0,0.2); font-size: 12px; color: #f59e0b; text-align: center; border-radius: 4px;">
                    💡 <i>Estrategia: Desarrolla las tablas un poco más allá del 100 o usa la descomposición en factores primos.</i>
                </div>
            </div>
            """
            components.html(html_linea_tiempo, height=185)
            
            user_mcm = st.number_input("¿En cuántas horas volverán a coincidir todos los vigías?", step=1, value=None, placeholder="Encuentra el MCM de 8, 12 y 15")
            
            if st.button("🔏 Sellar Guardia (Verificar)"):
                if user_mcm is not None:
                    if user_mcm == 120: # MCM exacto de 8, 12, 15
                        st.success("¡VÍCTORIA! A las 120 horas todas las antorchas coinciden. Has blindado el castillo.")
                        st.balloons()
                    else:
                        st.error(f"A las {user_mcm} horas no coinciden todos los vigías. Sigue buscando el primer múltiplo común real.")
                else:
                    st.warning("Por favor, introduce un número antes de verificar.")

    elif sub_tema == "El Reparto Justo del Botín (MCD)":
        st.markdown("""
        ### 📦 ¿Qué es el Máximo Común Divisor (MCD)?
        Imagina que tienes grandes cantidades de recursos diferentes y quieres **organizarlos en grupos o cofres exactamente iguales**, sin que sobre nada y haciendo los grupos **lo más grandes posibles**.
        """)

        tab_explicacion, tab_reto = st.tabs(["📖 ¿Cómo se calcula? (Ejemplo)", "🎯 ¡Pruébalo tú mismo!"])

        with tab_explicacion:
            st.markdown("""
            #### El método de divisores completos
            Para encontrar el MCD, buscamos todos los números que dividen de forma exacta (sin dejar residuo) a cada una de nuestras cantidades. Luego, elegimos el **más grande** que tengan en común.
            
            **Ejemplo Resuelto: Encontrar el MCD de 12 y 16**
            1. Divisores de 12: 1, 2, 3, **4**, 6, 12.
            2. Divisores de 16: 1, 2, **4**, 8, 16.
            
            *Ambos comparten los divisores 1, 2 y 4. El mayor de ellos es el **4**. Por lo tanto, el MCD(12, 16) = 4.*
            """)

        with tab_reto:
            if 'datos_mcd' not in st.session_state:
                # Nivel Examen: Desafío masivo con 4 números simultáneos
                st.session_state.datos_mcd = {
                    "oro": 36,
                    "plata": 48,
                    "gemas": 60,
                    "pergaminos": 72
                }

            d = st.session_state.datos_mcd

            st.warning(f"""
            💰 **Bóveda del Tesoro Real (4 Elementos):** Los cofres deben contener piezas de:
            * 🪙 **{d['oro']}** Monedas de Oro.
            * 🥈 **{d['plata']}** Barras de Plata.
            * 💎 **{d['gemas']}** Gemas de Amatista.
            * 📜 **{d['pergaminos']}** Pergaminos Antiguos.
            """)

            html_fraccionamiento = f"""
            <div style="background-color: #1e293b; padding: 15px; border-radius: 12px; font-family: 'Segoe UI', sans-serif; color: white; border: 2px solid #475569;">
                <div style="color: #a855f7; font-weight: bold; margin-bottom: 10px; font-size: 14px; text-transform: uppercase; text-align: center;">📐 Regla de Fraccionamiento Real</div>
                <div style="text-align: left; font-size: 13px; color: #94a3b8; line-height: 22px;">
                    • Divisores de <b>Oro ({d['oro']})</b>: 1, 2, 3, 4, 6, 9, <b>12</b>, 18, 36.<br>
                    • Divisores de <b>Plata ({d['plata']})</b>: 1, 2, 3, 4, 6, 8, <b>12</b>, 16, 24, 48.<br>
                    • Divisores de <b>Gemas ({d['gemas']})</b>: 1, 2, 3, 4, 5, 6, 10, <b>12</b>, 15, 20, 30, 60.<br>
                    • Divisores de <b>Pergaminos ({d['pergaminos']})</b>: 1, 2, 3, 4, 6, 8, 9, <b>12</b>, 18, 24, 36, 72.<br>
                </div>
                <div style="margin-top: 12px; padding: 5px; background: rgba(0,0,0,0.2); font-size: 12px; color: #f59e0b; text-align: center; border-radius: 4px;">
                    💡 <i>¿Cuál es el divisor común más grande que comparten los 4 recursos a la vez?</i>
                </div>
            </div>
            """
            components.html(html_fraccionamiento, height=215)

            user_mcd = st.number_input("¿Cuál es el número máximo de cofres iguales que puedes armar?", step=1, value=None, placeholder="Encuentra el MCD de 36, 48, 60 y 72")

            if st.button("👑 Distribuir Botín"):
                if user_mcd is not None:
                    if user_mcd == 12: # MCD exacto de 36, 48, 60, 72
                        st.success(f"¡LOGRADO! Armaste un máximo de 12 cofres perfectos (cada uno con {d['oro']//12} de oro, {d['plata']//12} de plata, {d['gemas']//12} gemas y {d['pergaminos']//12} pergaminos).")
                        st.balloons()
                    else:
                        st.error("Ese número de divisiones no reparte los 4 recursos de forma exacta o no es el divisor máximo común.")
                else:
                    st.warning("Por favor, introduce un número antes de verificar.")