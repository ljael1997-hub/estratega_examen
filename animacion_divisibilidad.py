import streamlit as st
import streamlit.components.v1 as components
import random

def modulo_divisibilidad_streamlit():
    # Títulos con MCM y MCD correctamente en mayúsculas
    st.title("👑 Reglas del Reino (MCM y MCD)")
    
    sub_tema = st.radio(
        "Elige tu entrenamiento:",
        ["Sincronización de Antorchas (MCM)", "El Reparto Justo del Botín (MCD)"],
        horizontal=True
    )
    st.divider()

    # --- 1. SECCIÓN: SINCRONIZACIÓN DE ANTORCHAS (MCM) ---
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
            # Banco de ejercicios nivel examen para MCM (Ternas complejas)
            banco_mcm = [
                {"valores": (8, 12, 15), "respuesta": 120},
                {"valores": (6, 9, 12), "respuesta": 36},
                {"valores": (4, 6, 14), "respuesta": 42},
                {"valores": (9, 12, 18), "respuesta": 36},
                {"valores": (5, 6, 10), "respuesta": 30}
            ]

            if 'reto_actual_mcm' not in st.session_state:
                st.session_state.reto_actual_mcm = random.choice(banco_mcm)
                st.session_state.version_mcm = 1
                
            reto = st.session_state.reto_actual_mcm
            t1, t2, t3 = reto["valores"]
            
            st.info(f"""
            🏰 **Misión del Reino (Dificultad de Examen):** Para evitar que el castillo quede a oscuras, los vigías cambian sus antorchas en intervalos complejos:
            * 🎯 **Torre Norte:** Cada **{t1}** horas.
            * 🎯 **Torre Sur:** Cada **{t2}** horas.
            * 🎯 **Torre Este:** Cada **{t3}** horas.
            """)

            html_linea_tiempo = f"""
            <div style="background-color: #1e293b; padding: 15px; border-radius: 12px; font-family: 'Segoe UI', sans-serif; color: white; border: 2px solid #475569;">
                <div style="color: #60a5fa; font-weight: bold; margin-bottom: 10px; font-size: 14px; text-transform: uppercase; text-align: center;">⏳ Línea de Tiempo de las Torres</div>
                <div style="text-align: left; font-size: 13px; color: #94a3b8; line-height: 24px;">
                    • <b>Torre Norte ({t1}h):</b> {t1}, {t1*2}, {t1*3}, {t1*4}, ... ❓ ... <br>
                    • <b>Torre Sur ({t2}h):</b> {t2}, {t2*2}, {t2*3}, {t2*4}, ... ❓ ... <br>
                    • <b>Torre Este ({t3}h):</b> {t3}, {t3*2}, {t3*3}, {t3*4}, ... ❓ ... <br>
                </div>
                <div style="margin-top: 12px; padding: 6px; background: rgba(0,0,0,0.2); font-size: 12px; color: #f59e0b; text-align: center; border-radius: 4px;">
                    💡 <i>Estrategia: Desarrolla las tres secuencias en tu cuaderno hasta encontrar el primer número en el que choquen las tres torres.</i>
                </div>
            </div>
            """
            components.html(html_linea_tiempo, height=185)
            
            with st.form(key=f"form_mcm_{st.session_state.version_mcm}"):
                user_mcm = st.number_input(f"¿En cuántas horas volverán a coincidir todos los vigías?", step=1, value=None, placeholder=f"Encuentra el MCM de {t1}, {t2} y {t3}")
                submit_mcm = st.form_submit_button("🔏 Sellar Guardia (Verificar)")
                
                if submit_mcm:
                    if user_mcm is not None:
                        if user_mcm == reto["respuesta"]: 
                            st.success(f"¡VICTORIA! A las {reto['respuesta']} horas todas las antorchas coinciden. Has blindado el castillo.")
                            st.balloons()
                        else:
                            st.error(f"A las {user_mcm} horas no coinciden todos los vigías. Sigue buscando el primer múltiplo común real.")
                    else:
                        st.warning("Por favor, introduce un número antes de verificar.")
            
            # SOLUCIÓN: Cambia el reto guardado en el estado por uno totalmente nuevo
            if st.button("🔄 Generar Nuevo Reto MCM"):
                st.session_state.reto_actual_mcm = random.choice([b for b in banco_mcm if b["valores"] != reto["valores"]])
                st.session_state.version_mcm += 1
                st.rerun()

    # --- 2. SECCIÓN: EL REPARTO JUSTO DEL BOTÍN (MCD) ---
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
            # Banco de ejercicios nivel examen para MCD (4 números simultáneos)
            banco_mcd = [
                {"items": {"oro": 36, "plata": 48, "gemas": 60, "pergaminos": 72}, "respuesta": 12},
                {"items": {"oro": 24, "plata": 36, "gemas": 48, "pergaminos": 60}, "respuesta": 12},
                {"items": {"oro": 15, "plata": 30, "gemas": 45, "pergaminos": 75}, "respuesta": 15},
                {"items": {"oro": 20, "plata": 40, "gemas": 60, "pergaminos": 80}, "respuesta": 20},
                {"items": {"oro": 16, "plata": 24, "gemas": 32, "pergaminos": 40}, "respuesta": 8}
            ]

            if 'reto_actual_mcd' not in st.session_state:
                st.session_state.reto_actual_mcd = random.choice(banco_mcd)
                st.session_state.version_mcd = 1

            reto_mcd = st.session_state.reto_actual_mcd
            d = reto_mcd["items"]

            st.warning(f"""
            💰 **Bóveda del Tesoro Real (4 Elementos):** Los cofres deben contener piezas de:
            * 🪙 **{d['oro']}** Monedas de Oro.
            * 🥈 **{d['plata']}** Barras de Plata.
            * 💎 **{d['gemas']}** Gemas de Amatista.
            * 📜 **{d['pergaminos']}** Pergaminos Antiguos.
            """)

            html_fraccionamiento = f"""
            <div style="background-color: #1e293b; padding: 15px; border-radius: 12px; font-family: 'Segoe UI', sans-serif; color: white; border: 2px solid #475569;">
                <div style="color: #a855f7; font-weight: bold; margin-bottom: 10px; font-size: 14px; text-transform: uppercase; text-align: center;">📐 Mapa de Pistas de Fraccionamiento</div>
                <div style="text-align: left; font-size: 13px; color: #94a3b8; line-height: 24px;">
                    • ¿Se pueden dividir entre <b>2</b>? Analiza si todos terminan en número par o cero... <br>
                    • ¿Se pueden dividir entre <b>3</b>? Suma los dígitos de cada cantidad y revisa si están en la tabla del 3... <br>
                    • ¿Habrá un número <b>más grande</b> (MÁXIMO) que divida a los cuatro sin dejar residuo? 📦 <b>[ ❓ ]</b>
                </div>
                <div style="margin-top: 12px; padding: 5px; background: rgba(0,0,0,0.2); font-size: 12px; color: #f59e0b; text-align: center; border-radius: 4px;">
                    💡 <i>Estrategia: Busca el divisor común más grande que compartan los números {d['oro']}, {d['plata']}, {d['gemas']} y {d['pergaminos']} al mismo tiempo.</i>
                </div>
            </div>
            """
            components.html(html_fraccionamiento, height=195)

            with st.form(key=f"form_mcd_{st.session_state.version_mcd}"):
                user_mcd = st.number_input("¿Cuál es el número máximo de cofres iguales que puedes armar?", step=1, value=None, placeholder=f"Encuentra el MCD de {d['oro']}, {d['plata']}, {d['gemas']} y {d['pergaminos']}")
                submit_mcd = st.form_submit_button("👑 Distribuir Botín")

                if submit_mcd:
                    if user_mcd is not None:
                        if user_mcd == reto_mcd["respuesta"]: 
                            st.success(f"¡LOGRADO! Armaste un máximo de {reto_mcd['respuesta']} cofres perfectos (cada uno con {d['oro']//user_mcd} de oro, {d['plata']//user_mcd} de plata, {d['gemas']//user_mcd} gemas y {d['pergaminos']//user_mcd} pergaminos).")
                            st.balloons()
                        else:
                            st.error("Ese número de divisiones no reparte los 4 recursos de forma exacta o no es el divisor máximo común.")
                    else:
                        st.warning("Por favor, introduce un número antes de verificar.")
            
            # SOLUCIÓN: Cambia el reto del botín por uno distinto con un click
            if st.button("🔄 Generar Nuevo Reto Botín"):
                st.session_state.reto_actual_mcd = random.choice([b for b in banco_mcd if b["items"] != reto_mcd["items"]])
                st.session_state.version_mcd += 1
                st.rerun()