import streamlit as st
import random
import math

def modulo_jerarquia_basica_streamlit():
    st.title("👑 Las Leyes del Trono (Jerarquía y Opuestos)")
    
    st.markdown("""
    ### 📝 La Pirámide de Poder Social
    En el reino de las matemáticas, no todos son iguales. Cada operación pertenece a una clase social y debes respetar su rango de importancia:
    """)
    
    # --- 1. TABLA VISUAL DE JERARQUÍA (CON METÁFORAS) ---
    html_piramide = """
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <div style="background-color: #1e293b; padding: 15px; border-radius: 12px; font-family: 'Segoe UI', sans-serif; color: white; max-width: 600px; margin: 0 auto; border: 2px solid #f59e0b; box-shadow: 0px 4px 10px rgba(0,0,0,0.3);">
        <table style="width: 100%; border-collapse: collapse; text-align: left; font-size: 14px;">
            <tr style="background-color: rgba(245, 158, 11, 0.2); border-bottom: 2px solid #f59e0b;">
                <th style="padding: 10px;">🏰 Clase Social</th>
                <th style="padding: 10px;">⚡ Nivel</th>
                <th style="padding: 10px;">⚔️ Operaciones</th>
            </tr>
            <tr style="border-bottom: 1px solid #334155;">
                <td style="padding: 10px; font-weight: bold; color: #f43f5e;"><i class="fa-solid fa-crown"></i> La Realeza</td>
                <td style="padding: 10px;">Nivel 3 (Máximo)</td>
                <td style="padding: 10px;">Potencias (²) y Raíces (√)</td>
            </tr>
            <tr style="border-bottom: 1px solid #334155;">
                <td style="padding: 10px; font-weight: bold; color: #3b82f6;"><i class="fa-solid fa-shield-halved"></i> La Nobleza</td>
                <td style="padding: 10px;">Nivel 2 (Medio)</td>
                <td style="padding: 10px;">Multiplicación y División</td>
            </tr>
            <tr>
                <td style="padding: 10px; font-weight: bold; color: #10b981;"><i class="fa-solid fa-users"></i> El Pueblo</td>
                <td style="padding: 10px;">Nivel 1 (Básico)</td>
                <td style="padding: 10px;">Suma (+) y Resta (-)</td>
            </tr>
        </table>
    </div>
    """
    st.components.v1.html(html_piramide, height=220)

    st.markdown("### 🔄 El Espejo de los Opuestos")
    st.write("Cada operación tiene un archienemigo que la anula. Si ves a estos dos juntos, ¡se destruyen!")

    # --- 2. INFOGRAFÍA VISUAL DE OPERACIONES OPUESTAS (CONSTRUIDA CON HTML/CSS) ---
    html_opuestos = """
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <div style="display: flex; justify-content: space-around; align-items: center; gap: 10px; font-family: 'Segoe UI', sans-serif; padding: 10px;">
        
        <div style="background: #1e293b; border: 1px solid #10b981; padding: 15px; border-radius: 15px; text-align: center; width: 30%;">
            <div style="color: #10b981; font-size: 24px; font-weight: bold;">+ <i class="fa-solid fa-right-left" style="font-size: 14px; color: #94a3b8;"></i> -</div>
            <div style="color: #94a3b8; font-size: 12px; margin-top: 5px;">Suma vs Resta</div>
        </div>

        <div style="background: #1e293b; border: 1px solid #3b82f6; padding: 15px; border-radius: 15px; text-align: center; width: 30%;">
            <div style="color: #3b82f6; font-size: 24px; font-weight: bold;">× <i class="fa-solid fa-right-left" style="font-size: 14px; color: #94a3b8;"></i> ÷</div>
            <div style="color: #94a3b8; font-size: 12px; margin-top: 5px;">Mult vs Div</div>
        </div>

        <div style="background: #1e293b; border: 1px solid #f43f5e; padding: 15px; border-radius: 15px; text-align: center; width: 30%;">
            <div style="color: #f43f5e; font-size: 24px; font-weight: bold;">x² <i class="fa-solid fa-right-left" style="font-size: 14px; color: #94a3b8;"></i> √</div>
            <div style="color: #94a3b8; font-size: 12px; margin-top: 5px;">Potencia vs Raíz</div>
        </div>

    </div>
    """
    st.components.v1.html(html_opuestos, height=120)

    st.divider()
    
    # --- LOGICA DEL JUEGO (Mantenemos la misma que tenías) ---
    if 'game_id_jbas' not in st.session_state: 
        st.session_state.game_id_jbas = 0
        
    if 'reto_jbas' not in st.session_state:
        tipo = random.choice(["potencia", "raiz"])
        if tipo == "potencia":
            a, b, c = random.randint(3, 10), random.randint(2, 4), random.choice([2, 3, 5])
            p1_res = c ** 2
            p2_res = b * p1_res
            final = a + p2_res
            st.session_state.reto_jbas = {
                "tipo": tipo, "txt": f"{a} + {b} × {c}²",
                "p1_pide": f"Elevar al cuadrado: {c}²", "p1_res": p1_res,
                "p2_pide": f"Multiplicar: {b} × {p1_res}", "p2_res": p2_res,
                "final": final
            }
        else:
            a, b, c = random.choice([4, 9, 16, 25]), random.randint(2, 5), random.randint(1, 5)
            p1_res = int(math.sqrt(a))
            p2_res = b * p1_res
            final = p2_res - c
            st.session_state.reto_jbas = {
                "tipo": tipo, "txt": f"{b} × √{a} - {c}",
                "p1_pide": f"Sacar raíz cuadrada: √{a}", "p1_res": p1_res,
                "p2_pide": f"Multiplicar: {b} × {p1_res}", "p2_res": p2_res,
                "final": final
            }
            
    r = st.session_state.reto_jbas
    gid = st.session_state.game_id_jbas
    
    st.info(f"⚔️ **Reto de Leyes: ¿Quién tiene el poder aquí?** `{r['txt']}`")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("💥 Paso A: El más fuerte")
        st.write(f"Resuelve primero el Nivel 3: `{r['p1_pide']}`")
        user_p1 = st.number_input("Resultado del Paso A:", step=1, key=f"jbas_a_{gid}", value=None)
    with col2:
        st.subheader("🛡️ Paso B: El nivel medio")
        st.write(f"Ahora calcula la multiplicación:")
        user_p2 = st.number_input("Resultado del Paso B:", step=1, key=f"jbas_b_{gid}", value=None)
        
    user_final = st.number_input("¿Cuál es el veredicto final?", step=1, key=f"jbas_f_{gid}", value=None)
    
    if st.button("👑 Aplicar Leyes del Trono"):
        if user_p1 == r['p1_res'] and user_p2 == r['p2_res'] and user_final == r['final']:
            st.balloons()
            st.success(f"¡PERFECTO! El resultado es {r['final']}.")
        else:
            st.error("Revisa la jerarquía: La Realeza (²) va antes que la Nobleza (×), y el Pueblo (+) al final.")
            
    if st.button("🔄 Siguiente Ley"):
        st.session_state.game_id_jbas += 1
        del st.session_state.reto_jbas
        st.rerun()