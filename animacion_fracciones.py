import streamlit as st
import streamlit.components.v1 as components
import random

def generar_svg_lingote(cortes, pintados, color_pintado="#f59e0b"):
    ancho_total = 300
    alto_total = 60
    pintados = max(0, min(pintados, cortes))
    ancho_bloque = ancho_total / cortes
    
    svg = f"""
    <svg width="100%" height="{alto_total}" viewBox="0 0 {ancho_total} {alto_total}" xmlns="http://www.w3.org/2000/svg" style="background-color: #1e293b; border-radius: 6px;">
        <rect x="0" y="0" width="{ancho_total}" height="{alto_total}" fill="#475569" rx="6" ry="6" stroke="#334155" stroke-width="2"/>
    """
    for i in range(cortes):
        x_pos = i * ancho_bloque
        fill_actual = color_pintado if i < pintados else "#475569"
        svg += f'<rect x="{x_pos}" y="0" width="{ancho_bloque}" height="{alto_total}" fill="{fill_actual}" stroke="#1e293b" stroke-width="2"/>'
    
    svg += f'<rect x="2" y="2" width="{ancho_total - 4}" height="6" fill="white" opacity="0.15" rx="3"/></svg>'
    return svg

def modulo_fracciones_streamlit():
    # --- LIMPIEZA PREVENTIVA ---
    # Esto elimina llaves de sesiones pasadas que causan el DuplicateWidgetID
    for key in list(st.session_state.keys()):
        if any(x in key for x in ["s_equiv_", "btn_sub_", "btn_next_", "form_simp_", "in_p_", "in_c_"]):
            # Solo borramos si el contador ya avanzó
            pass 

    st.title("⚒️ La Fundición Real (Fracciones de Lingotes)")
    
    if 'v_equiv' not in st.session_state: st.session_state.v_equiv = 0
    if 'v_simp' not in st.session_state: st.session_state.v_simp = 0

    sub_tema = st.radio(
        "Selecciona tu entrenamiento:",
        ["Los Lingotes del Rey (Equivalencia)", "El Escribano Real (Simplificación)"],
        horizontal=True,
        key="global_radio_fracciones"
    )
    st.divider()

    # --- EQUIVALENCIA ---
    if sub_tema == "Los Lingotes del Rey (Equivalencia)":
        if 'reto_equiv' not in st.session_state:
            st.session_state.reto_equiv = {"base_c": 3, "base_p": 1, "texto": "1/3 de un cristal mágico", "color": "#a855f7"}
            st.session_state.multiplicador = 2
            
        req = st.session_state.reto_equiv
        factor = st.session_state.multiplicador
        num_cortes = req['base_c'] * factor
        
        st.markdown(f"#### 🎯 Misión: {req['texto']}")
        st.markdown("**📐 Referencia:**")
        st.components.v1.html(generar_svg_lingote(req['base_c'], req['base_p'], req['color']), height=70)
        
        # KEY DINÁMICA: Cambia cada vez que v_equiv aumenta
        num_pintados = st.slider("Pintar bloques:", 0, num_cortes, 1, key=f"s_equiv_{st.session_state.v_equiv}")
        st.components.v1.html(generar_svg_lingote(num_cortes, num_pintados, req['color']), height=70)
        
        if st.button("⚔️ Entregar Lingote", key=f"btn_sub_equiv_{st.session_state.v_equiv}"):
            if num_pintados * req['base_c'] == num_cortes * req['base_p']:
                st.success("¡FORJA PERFECTA!")
            else:
                st.error("¡No coincide!")
        
        if st.button("🔄 Siguiente Plano", key=f"btn_next_equiv_{st.session_state.v_equiv}"):
            st.session_state.v_equiv += 1
            st.session_state.reto_equiv = random.choice([{"base_c": 3, "base_p": 1, "texto": "1/3...", "color": "#a855f7"}, {"base_c": 4, "base_p": 3, "texto": "3/4...", "color": "#10b981"}])
            st.session_state.multiplicador = random.choice([2, 3])
            st.rerun()

    # --- SIMPLIFICACIÓN ---
    else:
        if 'reto_simp' not in st.session_state:
            st.session_state.reto_simp = {"original_p": 6, "original_c": 18, "ans_p": 1, "ans_c": 3}
            
        simp = st.session_state.reto_simp
        st.markdown(f"#### 📝 Reduce la proporción {simp['original_p']}/{simp['original_c']}")
        st.components.v1.html(generar_svg_lingote(simp['original_c'], simp['original_p'], '#38bdf8'), height=70)
        
        # KEY DINÁMICA en el form
        with st.form(key=f"form_simp_{st.session_state.v_simp}"):
            col1, col2 = st.columns(2)
            u_p = col1.text_input("Numerador", key=f"in_p_{st.session_state.v_simp}")
            u_c = col2.text_input("Denominador", key=f"in_c_{st.session_state.v_simp}")
            submit = st.form_submit_button("Sellar Registro")
            
            if submit and u_p and u_c:
                try:
                    if int(u_p) == simp['ans_p'] and int(u_c) == simp['ans_c']:
                        st.success("¡Excelente!")
                    else:
                        st.warning("Incorrecto o no simplificado al máximo.")
                except:
                    st.error("Ingresa solo números.")
                    
        if st.button("🔄 Siguiente Pergamino", key=f"btn_next_simp_{st.session_state.v_simp}"):
            st.session_state.v_simp += 1
            st.session_state.reto_simp = random.choice([{"original_p": 6, "original_c": 18, "ans_p": 1, "ans_c": 3}, {"original_p": 8, "original_c": 12, "ans_p": 2, "ans_c": 3}])
            st.rerun()