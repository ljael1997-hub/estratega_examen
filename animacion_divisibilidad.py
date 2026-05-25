import streamlit as st
import random
import math

# Función auxiliar para calcular el mcm de tres números
def calcular_mcm(a, b, c):
    lcm_ab = (a * b) // math.gcd(a, b)
    return (lcm_ab * c) // math.gcd(lcm_ab, c)

def modulo_divisibilidad_streamlit():
    st.title("🧮 Las Reglas del Reino: mcm y MCD")
    
    # Selector de sub-tema dentro del módulo
    herramienta = st.radio(
        "Elige tu entrenamiento de divisibilidad:",
        ["⚔️ El Relevo de las Guardias (mcm)", "👑 El Reparto del Botín (MCD)"],
        horizontal=True
    )
    
    st.divider()
    
    if "game_id_div" not in st.session_state:
        st.session_state.game_id_div = 0
        
    gid = st.session_state.game_id_div

    # =========================================================================
    # CASE 1: MÍNIMO COMÚN MÚLTIPLO
    # =========================================================================
    if herramienta == "⚔️ El Relevo de las Guardias (mcm)":
        st.markdown("""
        ### 🏰 Sincronización de Antorchas (mcm)
        Para evitar que el castillo quede a oscuras, los vigías de las tres torres principales cambian sus antorchas en intervalos diferentes.
        Tu misión es calcular **el menor tiempo posible** en el que todos los vigías coincidirán cambiando sus antorchas al mismo tiempo.
        """)
        
        if 'reto_mcm' not in st.session_state:
            # Seleccionamos tres números amigables para examen
            t1, t2, t3 = random.choice([(3, 4, 6), (4, 6, 8), (2, 5, 10), (3, 5, 6)])
            st.session_state.reto_mcm = {
                "t1": t1, "t2": t2, "t3": t3,
                "resultado": calcular_mcm(t1, t2, t3)
            }
            
        m = st.session_state.reto_mcm
        
        st.info(f"""
        📋 **Reporte de los Vigías:**
        * 🔥 **Torre del Norte:** Cambia antorcha cada **{m['t1']} horas**.
        * 🔥 **Torre del Sur:** Cambia antorcha cada **{m['t2']} horas**.
        * 🔥 **Torre del Este:** Cambia antorcha cada **{m['t3']} horas**.
        """)
        
        # Mapa visual del reloj del reino en HTML/CSS
        html_mcm = f"""
        <div style="background-color: #1e293b; padding: 15px; border-radius: 12px; border: 2px solid #3b82f6; max-width: 400px; margin: 0 auto; color: white; font-family: sans-serif; text-align: center;">
            <div style="font-weight: bold; color: #60a5fa; margin-bottom: 10px;">⏰ LÍNEA DE TIEMPO DEL REINO</div>
            <div style="display: flex; justify-content: space-around; font-size: 14px; background: rgba(0,0,0,0.2); padding: 10px; border-radius: 6px;">
                <div>🏰 T1: {m['t1']}h, {m['t1']*2}h, {m['t1']*3}h...</div>
                <div>Castillo</div>
                <div>🏰 T2: {m['t2']}h, {m['t2']*2}h, {m['t2']*3}h...</div>
            </div>
            <div style="margin-top: 10px; font-size: 12px; color: #94a3b8;">Buscamos el primer número que aparezca en la lista de las 3 torres.</div>
        </div>
        """
        st.components.v1.html(html_mcm, height=110)
        
        # Banner reutilizable de resolución
        st.markdown("""
            <div style="background-color: rgba(220, 53, 69, 0.1); padding: 10px; border-radius: 6px; border-left: 5px solid #dc3545; margin: 15px 0 10px 0;">
                <span style="color: #ff6b6b; font-weight: bold; font-size: 15px; letter-spacing: 0.5px;">🚨 RESUELVE LO SIGUIENTE:</span>
            </div>
        """, unsafe_allow_html=True)
        st.code(f"Misión de Examen: Obtén el mcm de ({m['t1']}, {m['t2']}, {m['t3']})", language="text")
        
        user_mcm = st.number_input("¿En cuántas horas volverán a coincidir todos los vigías?", step=1, key=f"input_mcm_{gid}", value=None, placeholder="Encuentra el múltiplo común más pequeño")
        
        col_eval, col_next = st.columns(2)
        with col_eval:
            if st.button("🏹 Sellar Guardia (Verificar)", use_container_width=True):
                if user_mcm == m['resultado']:
                    st.balloons()
                    st.success(f"¡EXCELENTE ESTRATEGA! Coinciden exactamente a las {m['resultado']} horas. Las defensas del reino están sincronizadas.")
                else:
                    st.error(f"¡Alerta! A las {user_mcm} horas alguna torre se quedará sin fuego. Revisa los múltiplos.")
        with col_next:
            if st.button("🔄 Nuevas Guardias", use_container_width=True):
                st.session_state.game_id_div += 1
                if 'reto_mcm' in st.session_state: del st.session_state.reto_mcm
                st.rerun()

    # =========================================================================
    # CASE 2: MÁXIMO COMÚN DIVISOR
    # =========================================================================
    else:
        st.markdown("""
        ### 💰 El Reparto Justo del Botín (MCD)
        Los caballeros han regresado con valiosos recursos. El Rey exige repartirlos en **cofres idénticos** de manera que se use la **máxima cantidad de cofres posibles** y no sobre absolutamente nada.
        """)
        
        if 'reto_mcd' not in st.session_state:
            # Pares de recursos amigables con MCD claro
            oro, plata = random.choice([(24, 36), (30, 45), (18, 27), (40, 60)])
            st.session_state.reto_mcd = {
                "oro": oro,
                "plata": plata,
                "resultado": math.gcd(oro, plata)
            }
            
        d = st.session_state.reto_mcd
        
        st.warning(f"📦 **Recursos en la Cámara Real:** `{d['oro']} Monedas de Oro` y `{d['plata']} Barras de Plata`.")
        
        html_mcd = f"""
        <div style="background-color: #1e293b; padding: 15px; border-radius: 12px; border: 2px solid #a855f7; max-width: 400px; margin: 0 auto; color: white; font-family: sans-serif; text-align: center;">
            <div style="font-weight: bold; color: #c084fc; margin-bottom: 10px;">📦 REGLA DE FRACCIONAMIENTO</div>
            <div style="font-size: 13px; color: #94a3b8; line-height: 18px;">
                Debes cortar el total de oro ({d['oro']}) y plata ({d['plata']}) en grupos del mismo tamaño. 
                Buscamos el número más grande que pueda dividir a ambos exactamente.
            </div>
        </div>
        """
        st.components.v1.html(html_mcd, height=110)
        
        st.markdown("""
            <div style="background-color: rgba(220, 53, 69, 0.1); padding: 10px; border-radius: 6px; border-left: 5px solid #dc3545; margin: 15px 0 10px 0;">
                <span style="color: #ff6b6b; font-weight: bold; font-size: 15px; letter-spacing: 0.5px;">🚨 RESUELVE LO SIGUIENTE:</span>
            </div>
        """, unsafe_allow_html=True)
        st.code(f"Misión de Examen: Determina el MCD de ({d['oro']}, {d['plata']})", language="text")
        
        user_mcd = st.number_input("¿Cuál es el número máximo de cofres iguales que puedes armar?", step=1, key=f"input_mcd_{gid}", value=None, placeholder="Busca el divisor común más grande")
        
        col_eval, col_next = st.columns(2)
        with col_eval:
            if st.button("👑 Distribuir Botín", use_container_width=True):
                if user_mcd == d['resultado']:
                    st.balloons()
                    st.success(f"¡PERFECTO! Puedes armar un máximo de {d['resultado']} cofres. Cada cofre tendrá {d['oro']//d['resultado']} monedas de oro y {d['plata']//d['resultado']} barras de plata.")
                else:
                    st.error(f"No es posible armar {user_mcd} cofres idénticos sin romper las piezas o dejar fuera recursos.")
        with col_next:
            if st.button("🔄 Nuevo Botín", use_container_width=True):
                st.session_state.game_id_div += 1
                if 'reto_mcd' in st.session_state: del st.session_state.reto_mcd
                st.rerun()