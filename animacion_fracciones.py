import streamlit as st
import streamlit.components.v1 as components
import random

def generar_svg_lingote(cortes, pintados, color_pintado="#f59e0b"):
    """
    Genera un lingote rectangular en SVG dividido en 'cortes' bloques verticales,
    donde 'pintados' bloques se rellenan con color y el resto se quedan vacíos.
    Diseñado para ser perfectamente responsivo y ultra legible.
    """
    ancho_total = 300
    alto_total = 60
    
    pintados = max(0, min(pintados, cortes))
    ancho_bloque = ancho_total / cortes
    
    # Contenedor SVG con fondo oscuro medieval
    svg = f"""
    <svg width="100%" height="{alto_total}" viewBox="0 0 {ancho_total} {alto_total}" xmlns="http://www.w3.org/2000/svg" style="background-color: #1e293b; border-radius: 6px;">
        <rect x="0" y="0" width="{ancho_total}" height="{alto_total}" fill="#475569" rx="6" ry="6" stroke="#334155" stroke-width="2"/>
    """
    
    # Dibujar cada uno de los bloques individuales
    for i in range(cortes):
        x_pos = i * ancho_bloque
        # Si el bloque actual está dentro de los pintados, usa el color brillante; si no, el gris oscuro
        fill_actual = color_pintado if i < pintados else "#475569"
        
        svg += f"""
        <rect x="{x_pos}" y="0" width="{ancho_bloque}" height="{alto_total}" 
              fill="{fill_actual}" stroke="#1e293b" stroke-width="2"/>
        """
        
    # Detalles estéticos: un brillo metálico superior para que parezca un lingote o gema
    svg += f"""
        <rect x="2" y="2" width="{ancho_total - 4}" height="6" fill="white" opacity="0.15" rx="3"/>
    </svg>
    """
    return svg

def modulo_fracciones_streamlit():
    st.title("⚒️ La Fundición Real (Fracciones de Lingotes)")
    
    sub_tema = st.radio(
        "Selecciona tu entrenamiento:",
        ["Los Lingotes del Rey (Equivalencia)", "El Escribano Real (Simplificación)"],
        horizontal=True
    )
    st.divider()

    # --- 1. SUB-TEMA: EQUIVALENCIA (REDISEÑADO CON RECTÁNGULOS) ---
    if sub_tema == "Los Lingotes del Rey (Equivalencia)":
        st.markdown("""
        ### 🎨 Lingotes Equivalentes
        Imagina que el Rey te pide fundir un lingote de oro usando una proporción exacta. 
        No importa si divides el lingote en **pocos bloques grandes** o en **muchos bloques pequeños**, ¡al final el tamaño físico del oro pintado que obtienes es exactamente el mismo!
        """)
        
        tab_explicacion, tab_reto = st.tabs(["📖 Ver la regla visual", "🎯 ¡Pruébalo tú mismo!"])
        
        with tab_explicacion:
            st.markdown("#### Misma longitud, diferentes divisiones")
            st.write("Mira cómo estas tres barras representan exactamente la misma cantidad de material:")
            
            st.markdown("<b>Barra 1 / 2</b> (Mitad de oro)", unsafe_allow_html=True)
            st.components.v1.html(generar_svg_lingote(2, 1, "#f59e0b"), height=70)
            
            st.markdown("<b>Barra 2 / 4</b> (Mismo tamaño, bloques más chicos)", unsafe_allow_html=True)
            st.components.v1.html(generar_svg_lingote(4, 2, "#f59e0b"), height=70)
            
            st.markdown("<b>Barra 4 / 8</b> (Equivalente al máximo)", unsafe_allow_html=True)
            st.components.v1.html(generar_svg_lingote(8, 4, "#f59e0b"), height=70)
            
            st.info("💡 **Conclusión:** Las tres son **equivalentes** porque la franja de oro cubre exactamente la misma distancia horizontal.")

        with tab_reto:
            banco_equivalencias = [
                {"base_c": 3, "base_p": 1, "texto": "1/3 de un cristal mágico de Amatista", "color": "#a855f7"},
                {"base_c": 4, "base_p": 3, "texto": "3/4 de un lingote pesado de Esmeralda", "color": "#10b981"},
                {"base_c": 5, "base_p": 2, "texto": "2/5 de un lingote místico de Oro Real", "color": "#f59e0b"},
                {"base_c": 2, "base_p": 1, "texto": "1/2 de un cristal ardiente de Rubí", "color": "#ef4444"}
            ]
            
            if 'reto_equiv' not in st.session_state:
                st.session_state.reto_equiv = random.choice(banco_equivalencias)
                st.session_state.multiplicador = random.choice([2, 3])
                st.session_state.v_equiv = 1
                
            req = st.session_state.reto_equiv
            factor = st.session_state.multiplicador
            num_cortes = req['base_c'] * factor
            gid = st.session_state.v_equiv
            
            st.markdown(f"#### 🎯 Tu Misión: Fundir un lingote equivalente")
            st.write(f"El maestro fundidor te pide replicar el plano original: **{req['texto']}**.")
            
            if factor == 2:
                st.info(f"⚖️ **Orden de la Fragua:** Tu nuevo lingote debe estar dividido en el **doble** de secciones ({num_cortes} bloques totales). ¡Ajusta el material pintado para que mida lo mismo!")
            else:
                st.info(f"⚖️ **Orden de la Fragua:** Tu nuevo lingote debe estar dividido en el **triple** de secciones ({num_cortes} bloques totales). ¡Ajusta el material pintado para que mida lo mismo!")

            # Despliegue de los lingotes uno arriba del otro para comparación visual perfecta
            st.markdown(f"**📐 Plano Original de Referencia ({req['base_p']}/{req['base_c']})**")
            st.components.v1.html(generar_svg_lingote(req['base_c'], req['base_p'], req['color']), height=70)
            
            st.markdown(f"**🔨 Tu Fundición Actual ({num_cortes} bloques totales)**")
            num_pintados = st.slider("Mueve el deslizador para pintar los bloques de color:", min_value=0, max_value=num_cortes, value=1, key=f"pintados_rect_{gid}")
            st.components.v1.html(generar_svg_lingote(num_cortes, num_pintados, req['color']), height=70)
                
            with st.form(key=f"form_equiv_rect_{gid}"):
                st.write(f"Tu lingote actual representa la proporción: **{num_pintados} / {num_cortes}**")
                submit_eq = st.form_submit_button("⚔️ Entregar Lingote a los Almacenes")
                
                if submit_eq:
                    if num_pintados * req['base_c'] == num_cortes * req['base_p']:
                        st.success(f"¡FRIGIDOR PERFECTO! Has alineado el material exactamente igual. La proporción {num_pintados}/{num_cortes} es equivalente a {req['base_p']}/{req['base_c']}.")
                        st.balloons()
                    else:
                        st.error("¡No coincide! Mira las barras: tu lingote es más corto o más largo que el plano original.")
                        
            if st.button("🔄 Siguiente Plano (Nuevo Reto)", key="btn_new_eq"):
                st.session_state.reto_equiv = random.choice([b for b in banco_equivalencias if b['texto'] != req['texto']])
                st.session_state.multiplicador = random.choice([2, 3])
                st.session_state.v_equiv += 1
                st.rerun()

    # --- 2. SUB-TEMA: SIMPLIFICACIÓN (CON RECTÁNGULOS Y MEJORAS ESTÉTICAS) ---
    elif sub_tema == "El Escribano Real (Simplificación)":
        st.markdown("""
        ### 📝 Simplificar Fracciones
        Simplificar es **unir los pedacitos amontonados para hacer bloques más grandes e inteligibles**. ¡Es mucho más limpio para los registros reales!
        """)
        
        tab_explicacion, tab_reto = st.tabs(["📖 Ver el ejemplo de reducción", "🎯 ¡Pruébalo tú mismo!"])
        
        with tab_explicacion:
            st.markdown("#### Compactando el material")
            st.markdown("❌ <b>4 / 12</b> (Demasiado fragmentado y difícil de leer)")
            st.components.v1.html(generar_svg_lingote(12, 4, "#38bdf8"), height=70)
            
            st.markdown("✅ <b>1 / 3</b> (Simplificado al máximo, misma cantidad física)")
            st.components.v1.html(generar_svg_lingote(3, 1, "#38bdf8"), height=70)
            st.info("💡 **¿Cómo se hace?** Dividimos arriba y abajo entre 4. Pasamos de 12 pedacitos a solo 3 bloques grandes.")

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
                st.session_state.completado_simp = False
                
            simp = st.session_state.reto_simp
            vsmp = st.session_state.v_simp
            
            # Cuadro amarillo formal ultra gigante con tipografía monospace resaltada
            html_alerta_gigante = f"""
            <div style="background-color: #fef08a; border-left: 8px solid #eab308; padding: 20px; border-radius: 8px; margin-bottom: 20px;">
                <p style="color: #854d0e; font-size: 18px; margin: 0; font-family: sans-serif;">
                    📜 <b>REGISTRO ENREDADO DEL MENSAJERO:</b>
                </p>
                <p style="color: #713f12; font-size: 26px; font-weight: bold; margin: 10px 0 0 0; text-align: center; font-family: monospace; letter-spacing: 2px;">
                    ¡Reduce la proporción {simp['original_p']}/{simp['original_c']} a su mínima expresión!
                </p>
            </div>
            """
            st.markdown(html_alerta_gigante, unsafe_allow_html=True)
            
            st.components.v1.html(generar_svg_lingote(simp['original_c'], simp['original_p'], '#38bdf8'), height=70)
            
            with st.form(key=f"form_simp_rect_{vsmp}"):
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
                                    st.session_state.completado_simp = True
                                    st.success("¡Excelente trabajo! Has guardado la proporción perfecta.")
                                    st.balloons()
                                else:
                                    st.warning(f"Tu fracción ({user_p}/{user_c}) es correcta, ¡pero todavía se puede simplificar más!")
                            else:
                                st.error("Esos números no representan el tamaño real del lingote del pergamino.")
                    except ValueError:
                        st.error("❌ Escribe solo números enteros válidos.")

            if st.session_state.completado_simp:
                st.write("")
                html_cuadro_matematico = f"""
                <div style="background-color: #1e293b; border: 2px solid #38bdf8; padding: 15px; border-radius: 10px; text-align: center;">
                    <span style="color: #38bdf8; font-size: 18px; font-weight: bold; display: block; margin-bottom: 5px;">📜 Fracción Oficial Almacenada en los Libros Reales:</span>
                </div>
                """
                st.markdown(html_cuadro_matematico, unsafe_allow_html=True)
                st.latex(r"\frac{" + str(simp['ans_p']) + r"}{" + str(simp['ans_c']) + r"}")
                        
            if st.button("🔄 Siguiente Pergamino", key="btn_new_simp"):
                st.session_state.reto_simp = random.choice([b for b in banco_simplificar if b['original_c'] != simp['original_c'] or b['original_p'] != simp['original_p']])
                st.session_state.v_simp += 1
                st.session_state.completado_simp = False
                st.rerun()