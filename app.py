import random
import streamlit as st
import streamlit.components.v1 as components
import statistics
from animacion_sustitucion import animacion_sustitucion
from animacion_porcentaje import modulo_porcentajes_streamlit
from animacion_porcentajes_combinados import modulo_combinados_streamlit
from animacion_jerarquia_basica import modulo_jerarquia_basica_streamlit

# --- CONFIGURACIÓN INICIAL ---
st.set_page_config(page_title="La Estratega de Exámenes", layout="centered")

# --- CONFIGURACIÓN DE ACCESIBILIDAD (DALTONISMO GLOBAL) ---
st.sidebar.title("🛠️ Configuración")
modo_daltonico = st.sidebar.toggle("👁️ Modo Daltonismo (Accesible)", value=False)

if modo_daltonico:
    COLOR_POSITIVO = "#005fcc"
    COLOR_NEGATIVO = "#d97706"
    TEXTO_POS = "🔵 Saco Azul (Tengo +)"
    TEXTO_NEG = "🟠 Saco Naranja (Debo -)"
    
    st.markdown(f"""
        <style>
        button.step-up, button.step-down {{ display: none; }}
        div[data-baseweb="input"] > div {{ border-radius: 4px; }}
        input::placeholder {{ color: #888 !important; }}
        div[data-testid="stNotificationVisibility"] > div:has(div[class*="st-emotion-cache-16ids93"]) {{
            background-color: rgba(0, 95, 204, 0.1) !important;
            color: #005fcc !important;
            border-left: 5px solid #005fcc !important;
        }}
        div[data-testid="stNotificationVisibility"] > div:has(div[class*="st-emotion-cache-1z7809x"]) {{
            background-color: rgba(217, 119, 6, 0.1) !important;
            color: #d97706 !important;
            border-left: 5px solid #d97706 !important;
        }}
        </style>
    """, unsafe_allow_html=True)
else:
    COLOR_POSITIVO = "#28a745"
    COLOR_NEGATIVO = "#dc3545"
    TEXTO_POS = "🟢 Saco Verde (Tengo +)"
    TEXTO_NEG = "🔴 Saco Rojo (Debo -)"
    st.markdown("""
        <style>
        button.step-up, button.step-down { display: none; }
        div[data-baseweb="input"] > div { border-radius: 4px; }
        input::placeholder { color: #888 !important; }
        </style>
    """, unsafe_allow_html=True)


# --- 1. MÓDULO: EL DUELO DE LOS SACOS (Suma y Resta) ---
def modulo_sacos():
    st.title("⚔️ El Duelo de los Sacos")
    
    st.markdown("""
    ### 📝 ¿Cómo ganar este juego?
    Imagina que los números **positivos** son billetes que tienes en tu cartera y los **negativos** son deudas que debes pagar.
    1. **Junta tus billetes:** Suma todos los positivos en el Saco Positivo.
    2. **Junta tus deudas:** Suma todos los negativos en el Saco Negativo.
    3. **Paga la deuda:** Resta los dos sacos para ver si te sobró dinero o quedaste debiendo.
    """)

    if 'game_id' not in st.session_state: st.session_state.game_id = 0
    if 'soldados' not in st.session_state:
        st.session_state.soldados = [random.randint(-20, 20) for _ in range(5)]
        st.session_state.revisado = False
    
    soldados = st.session_state.soldados
    gid = st.session_state.game_id

    puntos_visuales = [f"<span style='color:{COLOR_POSITIVO if n >= 0 else COLOR_NEGATIVO}; font-weight:bold; font-size:28px;'>{n:+}</span>" for n in soldados]
    st.markdown(f"### 🎯 Tu Misión: {' '.join(puntos_visuales)} = ?", unsafe_allow_html=True)
    st.divider()

    st.write("👇 **Paso 1: Separa tu dinero de tus deudas.**")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader(TEXTO_POS)
        st.text_input("Anota los positivos aquí:", key=f"txt_v_{gid}", placeholder="Ej: +5 +10")
        user_verde = st.number_input("¿Cuánto dinero tienes en total?", step=1, key=f"num_v_{gid}", value=None, placeholder="Suma los positivos")
        
    with col2:
        st.subheader(TEXTO_NEG)
        st.text_input("Anota los negativos aquí:", key=f"txt_r_{gid}", placeholder="Ej: -8 -4")
        user_rojo = st.number_input("¿Cuánto debes en total? (Usa el signo -)", step=1, key=f"num_r_{gid}", value=None, placeholder="Suma los negativos")

    if st.button("💰 Revisar mis Sacos"):
        total_v = sum([n for n in soldados if n > 0])
        total_r = sum([n for n in soldados if n < 0])
        if user_verde == total_v and user_rojo == total_r:
            st.success("¡Perfecto! Tus cuentas están claras. Ahora ve al Paso 2.")
            st.session_state.revisado = True
            st.rerun()
        else:
            st.error(f"Algo no cuadra. Los positivos suman {total_v} y los negativos suman {total_r}.")

    if st.session_state.get('revisado'):
        st.divider()
        st.write("👇 **Paso 2: Paga tus deudas con lo que tienes.**")
        res_final = sum(soldados)
        user_final = st.number_input("¿Cuánto dinero te queda al final? (Pon el signo)", step=1, key=f"final_{gid}", value=None)
        if st.button("🏟️ ¡Ejecutar Duelo Final!"):
            if user_final == res_final:
                st.balloons()
                st.success(f"¡LOGRADO! El resultado es {res_final}.")
            else:
                st.error("El resultado final no es correcto. Intenta la resta de los sacos otra vez.")

    if st.button("🔄 Nuevos Números"):
        st.session_state.game_id += 1
        del st.session_state.soldados
        st.session_state.revisado = False
        st.rerun()


# --- 2. MÓDULO: SISTEMAS 2x2 (La Llave y el Candado) ---
def modulo_ecuaciones():
    st.title("🎯 La Llave y el Candado (Ecuaciones)")
    
    st.markdown("""
    ### 📝 ¿Cómo ganar este juego?
    La ecuación es un **Candado** que está cerrado. Las opciones de respuesta son **Llaves**.
    1. **Prueba una llave:** Quita las letras (x, y) y pon los números de la opción que elijas.
    2. **Haz la cuenta:** Si el resultado es igual al número después del '=', ¡esa llave abre el candado!
    """)

    if 'pregunta' not in st.session_state:
        a, b = random.choice([-5, 5]), random.choice([-5, 5])
        xc, yc = random.randint(-5, 5), random.randint(-5, 5)
        c = a * xc + b * yc
        opts = sorted(list(set([(xc, yc)] + [(random.randint(-5,5), random.randint(-5,5)) for _ in range(5)])))[:4]
        while len(opts) < 4:
            opts.append((random.randint(-5,5), random.randint(-5,5)))
            opts = sorted(list(set(opts)))
        st.session_state.pregunta = {"a": a, "b": b, "c": c, "x": xc, "y": yc, "opciones": opts}
        st.session_state.mostrar_hack = False
    
    p = st.session_state.pregunta
    st.code(f"Candado: ({p['a']})x + ({p['b']})y = {p['c']}")

    opciones_texto = [f"Llave {i+1}: x = {o[0]}, y = {o[1]}" for i, o in enumerate(p['opciones'])]
    eleccion = st.radio("¿Qué llave quieres probar?", opciones_texto, index=None, key=f"radio_{p['c']}_{p['a']}")

    if st.button("🗝️ Probar Llave"):
        if eleccion:
            idx = opciones_texto.index(eleccion)
            x_sel, y_sel = p['opciones'][idx]
            cuenta_real = p['a'] * x_sel + p['b'] * y_sel
            
            if cuenta_real == p['c']:
                st.success("¡EL CANDADO SE ABRIÓ! Esa es la respuesta correcta.")
                st.balloons()
                st.session_state.mostrar_hack = False
            else:
                st.session_state.err = {"x": x_sel, "y": y_sel, "res": cuenta_real}
                st.session_state.mostrar_hack = True
        else: 
            st.warning("Elige una llave primero.")

    if st.session_state.get('mostrar_hack'):
        e = st.session_state.err
        st.error(f"❌ Esa llave no abrió. Tu cuenta dio {e['res']}, pero el candado pide {p['c']}.")
        
        st.markdown("### 💡 ¡Así es como se abría el candado! (Estrategia Correcta):")
        
        html_anim = animacion_sustitucion(a=p['a'], x_val=p['x'], b=p['b'], y_val=p['y'], c=p['c'])
        components.html(html_anim, height=400)

    if st.button("🔄 Nuevo Candado"):
        if 'pregunta' in st.session_state: del st.session_state.pregunta
        st.session_state.mostrar_hack = False
        st.rerun()


# --- 3. MÓDULO: ESTADÍSTICA (La Fila del Cine) ---
def modulo_estadistica():
    st.title("📊 La Fila del Cine (Estadística)")
    
    if 'game_id_est' not in st.session_state: st.session_state.game_id_est = 0
    if 'datos_est' not in st.session_state:
        st.session_state.datos_est = [random.randint(1, 15) for _ in range(random.choice([5, 6]))]
    
    datos = st.session_state.datos_est
    gid = st.session_state.game_id_est
    es_par = len(datos) % 2 == 0

    st.success(f"🍿 **Tus números en la fila:** `{datos}`")
    st.divider()

    # MODA
    st.subheader("1. La Moda 🎀 (El más popular)")
    st.write("¿Qué número aparece más veces en la lista de arriba?")
    user_moda = st.text_input("¿Quién es el más popular?", key=f"moda_{gid}", placeholder="Escribe el número")

    # MEDIA
    st.subheader("2. La Media 🤝 (La Cooperacha)")
    st.write(f"Imagina que todos juntan su dinero y se lo reparten igual entre los {len(datos)} que son.")
    col1, col2 = st.columns(2)
    with col1: user_suma = st.number_input("Paso A: Suma todos los números:", step=1, key=f"suma_{gid}", value=None)
    with col2: user_media = st.number_input(f"Paso B: Suma ÷ {len(datos)}:", step=0.1, key=f"media_{gid}", value=None)

    # MEDIANA
    st.subheader("3. La Mediana 📍 (El del centro)")
    st.error("🚨 **¡REGLA DE ORO!** Tienes que formarlos por tamaño (del más chico al más grande) o el resultado estará MAL.")
    st.text_input("Fórmalos aquí (ordenados):", key=f"orden_{gid}", placeholder="Ej: 1, 2, 5...")
    
    if es_par: st.warning(f"💡 **Hack:** Tienes 2 números en medio. ¡Súmalos y divídelos entre 2!")
    else: st.warning(f"💡 **Hack:** Tienes solo 1 número en el centro. ¡Ese mero es!")
    user_mediana = st.number_input("¿Quién quedó en medio?", step=0.1, key=f"mediana_{gid}", value=None)

    if st.button("🚀 Revisar todo"):
        try:
            moda_real = str(statistics.mode(datos))
        except statistics.StatisticsError:
            moda_real = "no hay"
        
        correcto_moda = (user_moda.strip() == moda_real or (user_moda.strip() == "" and len(set(datos)) == len(datos)))
        correcto_suma = (user_suma == sum(datos))
        correcto_media = (user_media == round(sum(datos)/len(datos), 1))
        correcto_mediana = (user_mediana == statistics.median(datos))

        if correcto_suma and correcto_media and correcto_mediana:
            st.success("¡Felicidades! Lo entendiste perfectamente.")
            st.balloons()
        else: 
            st.error("Algo está mal. ¡Revisa tus cuentas, el promedio o el orden de la mediana!")

    if st.button("🔄 Nuevas Personas"):
        st.session_state.game_id_est += 1
        del st.session_state.datos_est
        st.rerun()


# --- 4. MÓDULO: REGLA DE TRES (El Hechizo de la Balanza) ---
def modulo_regla_de_tres():
    st.title("⚖️ El Hechizo de la Balanza (Regla de Tres)")
    
    st.markdown("""
    ### 📝 ¿Cómo ganar este juego?
    Resuelve el reto matemático guiándote con el mapa de operaciones de abajo. 
    Las flechas te indican qué números debes **multiplicar**, y la flecha final te dice entre cuál número debes **dividir** el resultado.
    """)

    # Inicializamos la pregunta si no existe en la sesión
    if 'pregunta_prop' not in st.session_state:
        tipo = random.choice(["directa", "inversa"])
        if tipo == "directa":
            a1, b1, a2 = random.choice([(3, 45, 9), (2, 50, 6), (5, 100, 15), (4, 20, 12)])
            x_correcta = int((a2 * b1) / a1)
            problema_texto = f"{a1} libretas"
            problema_val = f"${b1} pesos"
            problema_pregunta = f"¿Cuánto costarán {a2} libretas?"
        else:
            a1, b1, a2 = random.choice([(4, 12, 6), (2, 24, 8), (3, 10, 5), (6, 8, 4)])
            x_correcta = int((a1 * b1) / a2)
            problema_texto = f"{a1} pintores"
            problema_val = f"{b1} horas"
            problema_pregunta = f"¿Cuánto tardarán {a2} pintores?"
            
        st.session_state.pregunta_prop = {
            "prob_linea": f"🔹 {problema_texto} ───▶ {problema_val}",
            "prob_pregunta": f"❓ {problema_pregunta}",
            "tipo": tipo, 
            "x": x_correcta, 
            "datos": (a1, b1, a2)
        }

    p = st.session_state.pregunta_prop
    a1, b1, a2 = p['datos']

    # Planteamiento limpio y estructurado de forma matemática
    st.info(f"""
    📋 **Planteamiento del Reto Razonado:**
    {p['prob_linea']}
    **{p['prob_pregunta']}**
    """)

    # --- DISEÑO INTEGRADO CON INDICADOR DE TIPO Y FLECHAS VECTORIALES ---
    if p['tipo'] == "directa":
        html_mapa = f"""
        <div style="background-color: #1e293b; padding: 20px 25px 25px 25px; border-radius: 12px; text-align: center; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; color: white; max-width: 340px; margin: 0 auto; border: 2px solid #475569; box-shadow: 0px 4px 12px rgba(0,0,0,0.2);">
            <div style="background-color: rgba(96, 165, 250, 0.15); color: #60a5fa; border: 1px solid #60a5fa; padding: 4px; border-radius: 6px; font-size: 14px; font-weight: bold; margin-bottom: 20px; text-transform: uppercase; letter-spacing: 1px;">
                🎯 Regla de Tres Directa
            </div>
            
            <div style="position: relative; height: 140px; width: 100%;">
                <div style="position: absolute; top: 0px; left: 30px; font-size: 28px; font-weight: bold; color: #60a5fa;">{a1}</div>
                <div style="position: absolute; top: 0px; right: 30px; font-size: 28px; font-weight: bold; color: white;">{b1}</div>
                <div style="position: absolute; bottom: 0px; left: 30px; font-size: 28px; font-weight: bold; color: white;">{a2}</div>
                <div style="position: absolute; bottom: 0px; right: 30px; font-size: 28px; font-weight: bold; color: #ec4899;">❓</div>
                
                <svg style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none;">
                    <defs>
                        <marker id="arrow-orange" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                            <path d="M 0 1 L 10 5 L 0 9 z" fill="#f59e0b" />
                        </marker>
                        <marker id="arrow-blue" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                            <path d="M 0 1 L 10 5 L 0 9 z" fill="#3b82f6" />
                        </marker>
                    </defs>
                    <line x1="60" y1="110" x2="225" y2="30" stroke="#f59e0b" stroke-width="3" marker-end="url(#arrow-orange)" stroke-dasharray="4"/>
                    <line x1="220" y1="25" x2="65" y2="25" stroke="#3b82f6" stroke-width="3" marker-end="url(#arrow-blue)"/>
                </svg>
                
                <div style="position: absolute; top: 65px; left: 125px; background: #f59e0b; color: #0f172a; padding: 2px 8px; border-radius: 4px; font-size: 13px; font-weight: bold;">× Multiplicar</div>
                <div style="position: absolute; top: -12px; left: 110px; background: #3b82f6; color: white; padding: 2px 8px; border-radius: 4px; font-size: 13px; font-weight: bold;">÷ Dividir</div>
            </div>
        </div>
        """
    else:
        html_mapa = f"""
        <div style="background-color: #1e293b; padding: 20px 25px 25px 25px; border-radius: 12px; text-align: center; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; color: white; max-width: 340px; margin: 0 auto; border: 2px solid #475569; box-shadow: 0px 4px 12px rgba(0,0,0,0.2);">
            <div style="background-color: rgba(245, 158, 11, 0.15); color: #f59e0b; border: 1px solid #f59e0b; padding: 4px; border-radius: 6px; font-size: 14px; font-weight: bold; margin-bottom: 20px; text-transform: uppercase; letter-spacing: 1px;">
                🔄 Regla de Tres Inversa
            </div>
            
            <div style="position: relative; height: 140px; width: 100%;">
                <div style="position: absolute; top: 0px; left: 30px; font-size: 28px; font-weight: bold; color: #60a5fa;">{a1}</div>
                <div style="position: absolute; top: 0px; right: 30px; font-size: 28px; font-weight: bold; color: white;">{b1}</div>
                <div style="position: absolute; bottom: 0px; left: 30px; font-size: 28px; font-weight: bold; color: white;">{a2}</div>
                <div style="position: absolute; bottom: 0px; right: 30px; font-size: 28px; font-weight: bold; color: #ec4899;">❓</div>
                
                <svg style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none;">
                    <defs>
                        <marker id="arrow-orange2" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                            <path d="M 0 1 L 10 5 L 0 9 z" fill="#f59e0b" />
                        </marker>
                        <marker id="arrow-blue2" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                            <path d="M 0 1 L 10 5 L 0 9 z" fill="#3b82f6" />
                        </marker>
                    </defs>
                    <line x1="75" y1="20" x2="210" y2="20" stroke="#f59e0b" stroke-width="3" marker-end="url(#arrow-orange2)"/>
                    <line x1="220" y1="30" x2="60" y2="110" stroke="#3b82f6" stroke-width="3" marker-end="url(#arrow-blue2)"/>
                </svg>
                
                <div style="position: absolute; top: -12px; left: 100px; background: #f59e0b; color: #0f172a; padding: 2px 8px; border-radius: 4px; font-size: 13px; font-weight: bold;">× Multiplicar</div>
                <div style="position: absolute; top: 65px; left: 125px; background: #3b82f6; color: white; padding: 2px 8px; border-radius: 4px; font-size: 13px; font-weight: bold;">÷ Dividir</div>
            </div>
        </div>
        """

    components.html(html_mapa, height=240) # Aumenté ligeramente la altura por el letrero superior
    st.write("")

    user_resp = st.number_input("¿Cuál es el valor final de la incógnita (❓)?", step=1, value=None, key="prop_input")

    if st.button("🔮 Lanzar Hechizo"):
        if user_resp == p['x']:
            st.success(f"¡LOGRADO! El valor de ❓ es {p['x']}. La balanza quedó equilibrada.")
            st.balloons()
        else:
            st.error("La balanza se inclinó. Sigue la dirección de las flechas y vuelve a calcular.")

    if st.button("🔄 Nuevo Reto"):
        if 'pregunta_prop' in st.session_state: del st.session_state.pregunta_prop
        st.rerun()

 # --- 5. MÓDULO: GEOMETRÍA (Las Crónicas del Castillo) ---
def modulo_geometria_castillo():
    st.title("🏰 Las Crónicas del Castillo (Geometría)")
    
    # Menú para que el alumno elija qué juego jugar dentro del castillo
    mision = st.selectbox(
        "🗺️ Elige qué zona del Castillo quieres explorar:",
        ["Misión 1: La Muralla (Perímetros)", "Misión 2: El Patio de Armas (Áreas)", "Misión 3: La Escalera de la Torre (Pitágoras)"]
    )
    st.divider()

    # ================= MISIÓN 1: PERÍMETROS =================
    if mision == "Misión 1: La Muralla (Perímetros)":
        st.markdown("""
        ### 🛡️ Contorno de la Fortaleza
        Los centinelas enemigos acechan. Tu deber es **calcular la longitud total de la muralla exterior** para patrullar el perímetro.
        *⚡ Hack:* El **Perímetro** es caminar por toda la orilla sumando cada una de las 6 paredes del castillo.
        """)

        if 'pregunta_geo' not in st.session_state:
            b_larga = random.choice([12, 15, 20, 18])
            h_larga = random.choice([10, 14, 16, 12])
            b_corta, h_corta = b_larga // 2, h_larga // 2
            l_sup, l_der = b_larga - b_corta, h_larga - h_corta
            st.session_state.pregunta_geo = {
                "b_larga": b_larga, "h_larga": h_larga, "b_corta": b_corta,
                "h_corta": h_corta, "l_sup": l_sup, "l_der": l_der,
                "total": b_larga + h_larga + b_corta + h_corta + l_sup + l_der
            }

        g = st.session_state.pregunta_geo

        html_castillo = f"""
        <div style="background-color: #1e293b; padding: 20px; border-radius: 12px; text-align: center; font-family: 'Segoe UI', sans-serif; color: white; max-width: 340px; margin: 0 auto; border: 2px solid #475569; box-shadow: 0px 4px 12px rgba(0,0,0,0.3);">
            <div style="font-size: 13px; font-weight: bold; color: #f59e0b; margin-bottom: 10px; text-transform: uppercase; letter-spacing: 1px;">⚔️ Croquis de la Fortaleza</div>
            <div style="position: relative; height: 160px; width: 100%;">
                <svg style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;">
                    <defs>
                        <marker id="patrol-arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
                            <path d="M 0 1 L 10 5 L 0 9 z" fill="#f59e0b" />
                        </marker>
                    </defs>
                    <line x1="40" y1="140" x2="260" y2="140" stroke="#f59e0b" stroke-width="4" marker-end="url(#patrol-arrow)"/>
                    <line x1="260" y1="140" x2="260" y2="80" stroke="#f59e0b" stroke-width="4" marker-end="url(#patrol-arrow)"/>
                    <line x1="260" y1="80" x2="160" y2="80" stroke="#f59e0b" stroke-width="4" marker-end="url(#patrol-arrow)"/>
                    <line x1="160" y1="80" x2="160" y2="20" stroke="#f59e0b" stroke-width="4" marker-end="url(#patrol-arrow)"/>
                    <line x1="160" y1="20" x2="40" y2="20" stroke="#f59e0b" stroke-width="4" marker-end="url(#patrol-arrow)"/>
                    <line x1="40" y1="20" x2="40" y2="140" stroke="#f59e0b" stroke-width="4" marker-end="url(#patrol-arrow)"/>
                </svg>
                <div style="position: absolute; bottom: 0px; left: 135px; font-weight: bold; font-size: 16px; color: #60a5fa;">{g['b_larga']}m</div>
                <div style="position: absolute; bottom: 40px; right: 45px; font-weight: bold; font-size: 16px;">{g['l_der']}m</div>
                <div style="position: absolute; top: 90px; left: 180px; font-weight: bold; font-size: 16px;">{g['b_corta']}m</div>
                <div style="position: absolute; top: 35px; right: 195px; font-weight: bold; font-size: 16px;">{g['h_corta']}m</div>
                <div style="position: absolute; top: -5px; left: 90px; font-weight: bold; font-size: 16px;">{g['l_sup']}m</div>
                <div style="position: absolute; top: 70px; left: 10px; font-weight: bold; font-size: 16px; color: #60a5fa;">{g['h_larga']}m</div>
            </div>
        </div>
        """
        components.html(html_castillo, height=240)
        
        user_resp = st.number_input("¿Cuántos metros mide la muralla completa en total?", step=1, value=None, key="geo_input_p")
        if st.button("🏰 Reportar al Capitán"):
            if user_resp == g['total']:
                st.success(f"¡Excelente! Perímetro asegurado. Registraste los {g['total']}m con precisión.")
                st.balloons()
            else: 
                st.error("Tu conteo falló. Suma con cuidado las 6 paredes.")

        if st.button("🔄 Cambiar de Castillo"):
            if 'pregunta_geo' in st.session_state: del st.session_state.pregunta_geo
            st.rerun()

    # ================= MISIÓN 2: ÁREAS =================
    elif mision == "Misión 2: El Patio de Armas (Áreas)":
        st.markdown("""
        ### 🧱 Pavimentar el Patio de Armas
        El Rey quiere cubrir el suelo de diferentes zonas del castillo con losetas de piedra cuadradas. Tu misión es **calcular cuántos bloques caben en total** según la forma del terreno.
        """)

        if 'pregunta_area' not in st.session_state:
            tipo_patio = random.choice(["rectángulo", "triángulo", "círculo", "hexágono"])
            
            if tipo_patio == "rectángulo":
                base = random.choice([6, 8, 10, 12])
                altura = random.choice([5, 4, 6, 3])
                area = base * altura
                problema = f"El piso del Salón del Trono es un **rectángulo** de Base = {base}m y Altura = {altura}m.<br>⚡ <i>Estrategia: Multiplica directamente el largo por el ancho (Base × Altura).</i>"
                datos = (base, altura, 0)
                
            elif tipo_patio == "triángulo":
                base = random.choice([6, 8, 10, 12])
                altura = random.choice([4, 6, 8, 5])
                area = int((base * altura) / 2)
                problema = f"El jardín de la torre es un **triángulo** de Base = {base}m y Altura = {altura}m.<br>⚡ <i>Estrategia: Multiplica Base × Altura y divide el resultado entre 2.</i>"
                datos = (base, altura, 0)
                
            elif tipo_patio == "círculo":
                radio = random.choice([3, 5, 10])
                area = int(3.14 * radio * radio)
                problema = f"El fondo del foso es un **círculo** con un Radio = {radio}m.<br>⚡ <i>Estrategia: Multiplica el Radio por sí mismo ({radio} × {radio}) y luego por 3.14.</i>"
                datos = (radio, 0, 0)
                
            else:
                lado = random.choice([4, 5, 6])
                apotema = random.choice([3, 4, 5])
                perimetro = lado * 6
                area = int((perimetro * apotema) / 2)
                problema = f"La plaza central es un **hexágono regular**. Cada lado mide {lado}m y su Apotema es de {apotema}m.<br>⚡ <i>Estrategia: Saca la orilla total ({lado} × 6), multiplícala por el apotema y divide entre 2.</i>"
                datos = (lado, apotema, perimetro)

            st.session_state.pregunta_area = {"tipo": tipo_patio, "prob": problema, "total": area, "datos": datos}

        a = st.session_state.pregunta_area
        st.markdown(f"<div style='background-color: rgba(168,85,247,0.1); padding:15px; border-radius:8px; border-left:5px solid #a855f7;'>📋 <b>Reto:</b> {a['prob']}</div>", unsafe_allow_html=True)
        st.write("")

        if a['tipo'] == "rectángulo":
            b, h, _ = a['datos']
            html_patio = f"""
            <div style="background-color: #1e293b; padding: 20px; border-radius: 12px; text-align: center; font-family: 'Segoe UI', sans-serif; color: white; max-width: 340px; margin: 0 auto; border: 2px solid #475569;">
                <div style="position: relative; height: 130px; width: 100%;">
                    <svg style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;">
                        <rect x="60" y="20" width="180" height="90" fill="rgba(168,85,247,0.15)" stroke="#a855f7" stroke-width="3"/>
                    </svg>
                    <div style="position: absolute; bottom: -5px; left: 130px; font-weight: bold; font-size: 15px; color: #60a5fa;">Base: {b}m</div>
                    <div style="position: absolute; top: 50px; right: 45px; font-weight: bold; font-size: 15px; color: #f59e0b;">Altura: {h}m</div>
                </div>
            </div>
            """
        elif a['tipo'] == "triángulo":
            b, h, _ = a['datos']
            html_patio = f"""
            <div style="background-color: #1e293b; padding: 20px; border-radius: 12px; text-align: center; font-family: 'Segoe UI', sans-serif; color: white; max-width: 340px; margin: 0 auto; border: 2px solid #475569;">
                <div style="position: relative; height: 130px; width: 100%;">
                    <svg style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;">
                        <polygon points="60,110 240,110 240,20" fill="rgba(168,85,247,0.15)" stroke="#a855f7" stroke-width="3"/>
                    </svg>
                    <div style="position: absolute; bottom: -5px; left: 130px; font-weight: bold; font-size: 15px; color: #60a5fa;">Base: {b}m</div>
                    <div style="position: absolute; top: 50px; right: 45px; font-weight: bold; font-size: 15px; color: #f59e0b;">Altura: {h}m</div>
                </div>
            </div>
            """
        elif a['tipo'] == "círculo":
            r, _, _ = a['datos']
            html_patio = f"""
            <div style="background-color: #1e293b; padding: 20px; border-radius: 12px; text-align: center; font-family: 'Segoe UI', sans-serif; color: white; max-width: 340px; margin: 0 auto; border: 2px solid #475569;">
                <div style="position: relative; height: 130px; width: 100%;">
                    <svg style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;">
                        <circle cx="150" cy="65" r="50" fill="rgba(168,85,247,0.15)" stroke="#a855f7" stroke-width="3"/>
                        <line x1="150" y1="65" x2="200" y2="65" stroke="#60a5fa" stroke-width="3" stroke-dasharray="3"/>
                    </svg>
                    <div style="position: absolute; top: 45px; left: 155px; font-weight: bold; font-size: 14px; color: #60a5fa;">Radio: {r}m</div>
                </div>
            </div>
            """
        else:
            lado, ap, _ = a['datos']
            html_patio = f"""
            <div style="background-color: #1e293b; padding: 20px; border-radius: 12px; text-align: center; font-family: 'Segoe UI', sans-serif; color: white; max-width: 340px; margin: 0 auto; border: 2px solid #475569;">
                <div style="position: relative; height: 140px; width: 100%;">
                    <svg style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;">
                        <polygon points="150,15 195,40 195,90 150,115 105,90 105,40" fill="rgba(168,85,247,0.15)" stroke="#a855f7" stroke-width="3"/>
                        <line x1="150" y1="65" x2="150" y2="115" stroke="#f59e0b" stroke-width="3" stroke-dasharray="3"/>
                    </svg>
                    <div style="position: absolute; bottom: 30px; left: 155px; font-weight: bold; font-size: 13px; color: #f59e0b;">Apotema: {ap}m</div>
                    <div style="position: absolute; bottom: 0px; left: 60px; font-weight: bold; font-size: 13px; color: #60a5fa;">Cada Lado: {lado}m</div>
                </div>
            </div>
            """
        
        components.html(html_patio, height=190)
        st.write("")

        user_resp = st.number_input("¿Cuántas losetas cuadradas de área se necesitan? (Usa números enteros)", step=1, value=None, key="geo_input_a")
        if st.button("🧱 Entregar Patio"):
            if user_resp == a['total']:
                st.success(f"¡LOGRADO! El área calculada es de {a['total']} metros cuadrados.")
                st.balloons()
            else: 
                st.error(f"La cuenta falló. Revisa la estrategia para aplicar los pasos correctos.")

        if st.button("🔄 Cambiar de Terreno"):
            if 'pregunta_area' in st.session_state: del st.session_state.pregunta_area
            st.rerun()

    # ================= MISIÓN 3: PITÁGORAS =================
    else:
        st.markdown("""
        ### 🪜 La Escalera de Asalto (Teorema de Pitágoras)
        Necesitamos apoyar una escalera para alcanzar la ventana de la torre. Conocemos los bloques que mide el suelo y los que mide la pared.
        
        **💡 Cómo resolverlo sin matemáticas raras (Paso a Paso):**
        1. **Haz los cuadrados:** Multiplica el número del suelo por sí mismo, y el de la pared por sí mismo.
        2. **Júntalos:** Suma esos dos resultados.
        3. **Busca el lado:** Piensa qué número multiplicado **por sí mismo** te da ese total. ¡Esa es la longitud de tu escalera!
        """)

        if 'pregunta_pit' not in st.session_state:
            base, altura, diagonal = random.choice([(3, 4, 5), (6, 8, 10), (5, 12, 13)])
            st.session_state.pregunta_pit = {"b": base, "h": altura, "c": diagonal}

        p = st.session_state.pregunta_pit

        html_torre = f"""
        <div style="background-color: #1e293b; padding: 25px; border-radius: 12px; text-align: center; font-family: 'Segoe UI', sans-serif; color: white; max-width: 340px; margin: 0 auto; border: 2px solid #475569;">
            <div style="font-size: 13px; font-weight: bold; color: #ec4899; margin-bottom: 15px; text-transform: uppercase; letter-spacing: 1px;">📐 El Mapa de la Torre</div>
            <div style="position: relative; height: 140px; width: 100%;">
                <svg style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;">
                    <polygon points='60,110 240,110 240,20' fill='none' stroke='#374151' stroke-width='2'/>
                    <line x1="60" y1="110" x2="240" y2="20" stroke="#ec4899" stroke-width="4" stroke-dasharray="5"/>
                </svg>
                <div style="position: absolute; bottom: -5px; left: 130px; font-weight: bold; color: #60a5fa; font-size: 15px;">Suelo: {p['b']}m</div>
                <div style="position: absolute; top: 50px; right: 35px; font-weight: bold; color: #f59e0b; font-size: 15px; transform: rotate(90deg);">Pared: {p['h']}m</div>
                <div style="position: absolute; top: 45px; left: 90px; font-weight: bold; color: #ec4899; font-size: 18px;">Escalera: ❓</div>
            </div>
            <div style="margin-top: 15px; font-size: 12px; color: #94a3b8; line-height: 18px; text-align: left; background: rgba(0,0,0,0.2); padding: 10px; border-radius: 6px;">
                📋 <b>Tu acordeón de apoyo:</b><br>
                • Cuadrado del suelo: {p['b']} × {p['b']} = <b>{p['b']*p['b']}</b><br>
                • Cuadrado de la pared: {p['h']} × {p['h']} = <b>{p['h']*p['h']}</b><br>
                • Bloques totales combinados: {p['b']*p['b']} + {p['h']*p['h']} = <b>{p['b']*p['b'] + p['h']*p['h']}</b><br>
                • <i>Busca qué número multiplicado por sí mismo da {p['b']*p['b'] + p['h']*p['h']}...</i>
            </div>
        </div>
        """
        components.html(html_torre, height=360)

        user_resp = st.number_input("¿Cuánto debe medir la longitud de la escalera (❓)?", step=1, value=None, key="geo_input_pit")
        if st.button("🪜 Desplegar Escalera"):
            if user_resp == p['c']:
                st.success(f"¡EMBATE EXITOSO! {p['c']} × {p['c']} es igual a {p['c']*p['c']}. ¡Lograste subir a la torre!")
                st.balloons()
            else: 
                st.error("La escalera quedó corta o colapsó. Intenta sumando los dos resultados del acordeón gris.")

        if st.button("🔄 Cambiar de Torre"):
            if 'pregunta_pit' in st.session_state: del st.session_state.pregunta_pit
            st.rerun()

# --- CONTROL DE NAVEGACIÓN GLOBAL ---
lista_temas = ["Duelo de Sacos", "Leyes del Trono (Jerarquía Básica)", "Sistemas 2x2", "Estadística", "Magia del Punto", "Porcentajes Combinados", "Regla de Tres", "Las Crónicas del Castillo"]

# CORRECCIÓN CENTRAL: Reincorporación del componente nativo de control de menú de barra lateral
with st.sidebar:
    st.title("La Estratega")
    seleccion_final = st.radio(
        "Entrenamiento:", 
        lista_temas, 
        key="nav_unica"
    )

st.markdown("""
    <div style="background-color: #1e293b; padding: 15px; border-radius: 10px; border-left: 6px solid #f59e0b; margin-bottom: 20px; box-shadow: 0px 4px 10px rgba(0,0,0,0.3);">
        📱 <b>¿Estás en celular?</b> Para cambiar de juego o ver los siguientes temas, 
        toca la flechita <b>&gt;&gt;</b> que está arriba en la <b>esquina superior izquierda</b> de tu pantalla.
    </div>
""", unsafe_allow_html=True)


# --- ACORDEÓN DE SIGNOS (DICCIONARIO GLOBAL) ---
with st.sidebar:
    with st.expander("📚 Acordeón: ¿Qué significan estas operaciones?"):
        st.markdown("""
        **✖️ Multiplicar:**
        * **(5)(4)** o **5 * 4** -> Significa sumar el 5 cuatro veces ($5 + 5 + 5 + 5 = 20$).
        
        **➗ Dividir:**
        * **20 / 4** o **20 ÷ 4** -> Repartir 20 cosas entre 4 personas en partes iguales.
        
        **⏹️ Elevar al Cuadrado (²):**
        * **$5^2$** -> Es multiplicar el número **por sí mismo** ($5 \\times 5 = 25$). 
        * *Visualmente:* Si haces un piso cuadrado de $5 \\times 5$ bloques, usarás $25$ bloques en total.
        
        **🌱 Raíz Cuadrada (√):**
        * **$\\sqrt{25}$** -> Es la operación al revés. Si te dan un piso cuadrado de $25$ bloques y te preguntan: *¿Cuánto mide su pared de largo?*, la respuesta es $5$.
        """)


# --- RENDERIZADO DE LOS JUEGOS ---
st.divider()

if seleccion_final == "Duelo de Sacos": 
    modulo_sacos()
elif seleccion_final == "Leyes del Trono (Jerarquía Básica)":
    modulo_jerarquia_basica_streamlit()
elif seleccion_final == "Sistemas 2x2": 
    modulo_ecuaciones()
elif seleccion_final == "Estadística": 
    modulo_estadistica()
elif seleccion_final == "Magia del Punto": 
    modulo_porcentajes_streamlit()
elif seleccion_final == "Porcentajes Combinados":
    modulo_combinados_streamlit()
elif seleccion_final == "Regla de Tres": 
    modulo_regla_de_tres()
else:
    modulo_geometria_castillo()
