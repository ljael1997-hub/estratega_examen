import streamlit as st
import streamlit.components.v1 as components
import random
import math

def generar_svg_escudo(cortes, pintados, color_pintado="#ef4444"):
    """
    Genera un escudo circular en SVG dividido en 'cortes' partes iguales,
    donde 'pintados' partes se rellenan con color y el resto se quedan vacías.
    """
    svg_ancho = 200
    svg_alto = 200
    centro_x = 100
    centro_y = 100
    radio = 80
    
    # Asegurar que pintados no desborde los cortes por seguridad
    pintados = max(0, min(pintados, cortes))
    
    # Inicio del SVG con estilos medievales limpios
    svg = f"""
    <svg width="{svg_ancho}" height="{svg_alto}" viewBox="0 0 {svg_ancho} {svg_alto}" xmlns="http://www.w3.org/2000/svg" style="background-color: #1e293b; border-radius: 50%;">
        <circle cx="{centro_x}" cy="{centro_y}" r="{radio}" fill="#475569" stroke="#94a3b8" stroke-width="4"/>
    """
    
    # Caso especial: Si solo hay 1 corte
    if cortes == 1:
        color_fill = color_pintado if pintados == 1 else "#475569"
        svg += f'<circle cx="{centro_x}" cy="{centro_y}" r="{radio}" fill="{color_fill}" stroke="#94a3b8" stroke-width="4"/>'
    else:
        # Dibujar cada rebanada del escudo usando arcos trigonométricos
        for i in range(cortes):
            angulo_inicio = (2 * math.pi / cortes) * i - math.pi / 2
            angulo_fin = (2 * math.pi / cortes) * (i + 1) - math.pi / 2
            
            x1 = centro_x + radio * math.cos(angulo_inicio)
            y1 = centro_y + radio * math.sin(angulo_inicio)
            x2 = centro_x + radio * math.cos(angulo_fin)
            y2 = centro_y + radio * math.sin(angulo_fin)
            
            # Condición de pintado exacta
            fill_actual = color_pintado if i < pintados else "#475569"
            
            svg += f"""
            <path d="M {centro_x} {centro_y} L {x1} {y1} A {radio} {radio} 0 0 1 {x2} {y2} Z" 
                  fill="{fill_actual}" stroke="#1e293b" stroke-width="2"/>
            """
            
    # Detalles estéticos finales
    svg += f"""
        <circle cx="{centro_x}" cy="{centro_y}" r="{radio}" fill="none" stroke="#cbd5e1" stroke-width="3" stroke-dasharray="6,4"/>
        <circle cx="{centro_x}" cy="{centro_y}" r="{radio - 4}" fill="none" stroke="#cbd5e1" stroke-width="1"/>
    </svg>
    """
    return svg

def modulo_fracciones_streamlit():
    st.title("🛡️ El Taller de Escudos (Fracciones)")
    
    sub_tema = st.radio(
        "Selecciona tu entrenamiento:",
        ["Los Escudos del Rey (Equivalencia)", "El Escribano Real (Simplificación)"],
        horizontal=True
    )
    st.divider()

    # --- 1. SUB-TEMA: EQUIVALENCIA ---
    if sub_tema == "Los Escudos del Rey (Equivalencia)":
        st.markdown("""
        ### 🎨 Fracciones Equivalentes
        Imagina que el Rey manda pintar de **rojo** la mitad de los escudos del ejército. 
        No importa si cortas el escudo en **2 pedazos grandes** o en **8 cachitos pequeños**, ¡al final la cantidad de pintura roja que protege al soldado es exactamente la misma!
        """)
        
        tab_explicacion, tab_reto = st.tabs(["📖 Ver la regla visual", "🎯 ¡Pruébalo tú mismo!"])
        
        with tab_explicacion:
            st.markdown("#### Diferentes números, misma protección")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown("<center><b>1 / 2</b></center>", unsafe_allow_html=True)
                st.components.v1.html(f"<center>{generar_svg_escudo(2, 1)}</center>", height=210)
            with col2:
                st.markdown("<center><b>2 / 4</b></center>", unsafe_allow_html=True)
                st.components.v1.html(f"<center>{generar_svg_escudo(4, 2)}</center>", height=210)
            with col3:
                st.markdown("<center><b>4 / 8</b></center>", unsafe_allow_html=True)
                st.components.v1.html(f"<center>{generar_svg_escudo(8, 4)}</center>", height=210)
                
            st.info("💡 **Conclusión:** Las fracciones son **equivalentes** porque el escudo está cubierto en la misma cantidad.")

        with tab_reto:
            banco_equivalencias = [
                {"base_c": 3, "base_p": 1, "texto": "1/3 de un escudo mágico de Amatista", "color": "#a855f7"},
                {"base_c": 4, "base_p": 3, "texto": "3/4 de un escudo pesado de Esmeralda", "color": "#10b981"},
                {"base_c": 5, "base_p": 2, "texto": "2/5 de un escudo místico de Oro Real", "color": "#f59e0b"},
                {"base_c": 2, "base_p": 1, "texto": "1/2 de un escudo de Infantería de Rubí", "color": "#ef4444"}
            ]
            
            if 'reto_equiv' not in st.session_state:
                st.session_state.reto_equiv = random.choice(banco_equivalencias)
                st.session_state.v_equiv = 1
                
            req = st.session_state.reto_equiv
            gid = st.session_state.v_equiv
            
            st.markdown(f"#### 🎯 Tu Misión: Forjar un escudo equivalente")
            st.write(f"El capitán te pide replicar exactamente la misma cantidad de pintura: **{req['texto']}**.")
            
            # Sacamos los Sliders del formulario para controlar de forma reactiva y limpia el renderizado
            col_plano, col_usuario = st.columns(2)
            with col_plano:
                st.markdown(f"<center><b>📐 Plano Original ({req['base_p']}/{req['base_c']})</b></center>", unsafe_allow_html=True)
                st.components.v1.html(f"<center>{generar_svg_escudo(req['base_c'], req['base_p'], req['color'])}</center>", height=210)
                
            with col_usuario:
                st.markdown("<center><b>🔨 Tu Escudo Forjado</b></center>", unsafe_allow_html=True)
                # Removimos el string dinámico de la key para estabilizar el refresco reactivo de Streamlit
                num_cortes = st.slider("¿En cuántas partes cortarás tu escudo?", min_value=1, max_value=20, value=6, key=f"cortes_fixed_{gid}")
                num_pintados = st.slider("¿Cuántas partes vas a pintar?", min_value=0, max_value=num_cortes, value=1, key=f"pintados_fixed_{gid}")
                
                st.components.v1.html(f"<center>{generar_svg_escudo(num_cortes, num_pintados, req['color'])}</center>", height=210)
                
            with st.form(key=f"form_equiv_fixed_{gid}"):
                st.write(f"Tu escudo actual representa la fracción: **{num_pintados} / {num_cortes}**")
                submit_eq = st.form_submit_button("⚔️ Presentar Escudo al Capitán")
                
                if submit_eq:
                    if num_pintados * req['base_c'] == num_cortes * req['base_p']:
                        if num_cortes == req['base_c'] and num_pintados == req['base_p']:
                            st.warning("¡Tiene el mismo número de cortes! El capitán quiere que uses una fracción equivalente DIFERENTE para demostrar tu habilidad.")
                        else:
                            st.success(f"¡FORJA PERFECTA! {num_pintados}/{num_cortes} es equivalente a {req['base_p']}/{req['base_c']}.")
                            st.balloons()
                    else:
                        st.error("No es equivalente. Mira las imágenes con cuidado; tu escudo no cubre la misma proporción.")
                        
            if st.button("🔄 Cambiar de Plano (Nuevo Reto)", key="btn_new_eq"):
                st.session_state.reto_equiv = random.choice([b for b in banco_equivalencias if b['texto'] != req['texto']])
                st.session_state.v_equiv += 1
                st.rerun()

    # --- 2. SUB-TEMA: SIMPLIFICACIÓN ---
    elif sub_tema == "El Escribano Real (Simplificación)":
        st.markdown("""
        ### 📝 Simplificar Fracciones
        Simplificar es **unir los pedacitos incómodos para hacer pedazos más grandes**. ¡Es mucho más limpio para los registros reales!
        """)
        
        tab_explicacion, tab_reto = st.tabs(["📖 Ver el ejemplo de reducción", "🎯 ¡Pruébalo tú mismo!"])
        
        with tab_explicacion:
            st.markdown("#### El Gran Escape de los pedacitos")
            c1, c2 = st.columns(2)
            with c1:
                st.markdown("<center>❌ <b>4 / 12</b> (Muy amontonado)</center>", unsafe_allow_html=True)
                st.components.v1.html(f"<center>{generar_svg_escudo(12, 4, '#38bdf8')}</center>", height=210)
            with c2:
                st.markdown("<center>✅ <b>1 / 3</b> (Simplificado al máximo)</center>", unsafe_allow_html=True)
                st.components.v1.html(f"<center>{generar_svg_escudo(3, 1, '#38bdf8')}</center>", height=210)

        with tab_reto:
            banco_simplificar = [
                {"original_p": 6, "original_c": 18, "ans_p": 1, "ans_c": 3},
                {"original_p": 8, "original_c": 12, "ans_p": 2, "ans_c": 3},
                {"original_p": 10, "original_c": 15, "ans_p": 2, "ans_c": 3},
                {"original_p": 4, "original_c": 16, "ans_p": 1, "ans_c": 4},
                {"original_p": 12, "original_c": 16, "ans_p": 3, "ans_c": 4}
            ]
            
            if 'reto_simp' not in st.session_state:
                st.session_state.reto_simp = random.choice(banco_simplificar)
                st.session_state.v_simp = 1
                
            simp = st.session_state.reto_simp
            vsmp = st.session_state.v_simp
            
            st.warning(f"📜 **Registro Enredado:** Ayuda al Escribano Real a reducir **{simp['original_p']}/{simp['original_c']}** a su forma más simple.")
            st.components.v1.html(f"<center>{generar_svg_escudo(simp['original_c'], simp['original_p'], '#38bdf8')}</center>", height=210)
            
            # CAMBIO CRÍTICAL: Cambiado st.number_input por st.text_input manual sin botones molestos
            with st.form(key=f"form_simp_fixed_{vsmp}"):
                st.write("Escribe los números de la fracción completamente simplificada:")
                col_inp1, col_inp2 = st.columns(2)
                
                with col_inp1:
                    user_p_str = st.text_input("Numerador (Arriba)", key=f"inp_p_{vsmp}", placeholder="Ej: 1")
                with col_inp2:
                    user_c_str = st.text_input("Denominador (Abajo)", key=f"inp_c_{vsmp}", placeholder="Ej: 3")
                    
                submit_simp = st.form_submit_button("✒️ Sellar Registro Oficial")
                
                if submit_simp:
                    try:
                        if user_p_str.strip() == "" or user_c_str.strip() == "":
                            st.warning("⚠️ Por favor, rellena ambos campos antes de mandar el sello.")
                        else:
                            user_p = int(user_p_str.strip())
                            user_c = int(user_c_str.strip())
                            
                            if user_p * simp['original_c'] == user_c * simp['original_p']:
                                if user_p == simp['ans_p'] and user_c == simp['ans_c']:
                                    st.success(f"¡Excelente trabajo! La mínima expresión es {simp['ans_p']}/{simp['ans_c']}.")
                                    st.balloons()
                                else:
                                    st.warning(f"Tu fracción ({user_p}/{user_c}) equivale al terreno, ¡pero se puede simplificar más!")
                            else:
                                st.error("Esos números no equivalen a las tierras originales.")
                    except ValueError:
                        st.error("❌ Escribe solo números enteros válidos (sin letras ni símbolos extra).")
                        
            if st.button("🔄 Siguiente Pergamino", key="btn_new_simp"):
                st.session_state.reto_simp = random.choice([b for b in banco_simplificar if b['original_c'] != simp['original_c'] or b['original_p'] != simp['original_p']])
                st.session_state.v_simp += 1
                st.rerun()