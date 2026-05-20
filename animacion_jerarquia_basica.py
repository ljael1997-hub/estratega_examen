import streamlit as st
import random
import math

def modulo_jerarquia_basica_streamlit():
    st.title("👑 Las Leyes del Trono (Jerarquía y Opuestos)")
    
    st.markdown("""
    ### 📝 La Pirámide de Poder Matemático
    No todas las operaciones tienen el mismo peso. En el examen, debes resolverlas siguiendo este estricto orden de rangos:
    """)
    
    # --- TABLA VISUAL DE JERARQUÍA ---
    html_piramide = """
    <div style="background-color: #1e293b; padding: 15px; border-radius: 12px; font-family: 'Segoe UI', sans-serif; color: white; max-width: 450px; margin: 0 auto; border: 2px solid #f59e0b;">
        <table style="width: 100%; border-collapse: collapse; text-align: left;">
            <tr style="background-color: rgba(245, 158, 11, 0.2); border-bottom: 2px solid #f59e0b;">
                <th style="padding: 8px;">👑 Rango (Poder)</th>
                <th style="padding: 8px;">⚔️ Operaciones</th>
                <th style="padding: 8px;">🔄 Opuesto Directo</th>
            </tr>
            <tr style="border-bottom: 1px solid #334155;">
                <td style="padding: 8px; font-weight: bold; color: #f43f5e;">⚡ Nivel 3 (Máximo)</td>
                <td style="padding: 8px;">Potencias (²)/ Raíces (√)</td>
                <td style="padding: 8px; color: #94a3b8;">Son opuestas entre sí</td>
            </tr>
            <tr style="border-bottom: 1px solid #334155;">
                <td style="padding: 8px; font-weight: bold; color: #3b82f6;">🛡️ Nivel 2 (Medio)</td>
                <td style="padding: 8px;">Multiplicación / División</td>
                <td style="padding: 8px; color: #94a3b8;">Son opuestas entre sí</td>
            </tr>
            <tr>
                <td style="padding: 8px; font-weight: bold; color: #10b981;">🟢 Nivel 1 (Bajo)</td>
                <td style="padding: 8px;">Suma (+) / Resta (-)</td>
                <td style="padding: 8px; color: #94a3b8;">Son opuestas entre sí</td>
            </tr>
        </table>
    </div>
    """
    st.components.v1.html(html_piramide, height=160)
    
    st.markdown("""
    *⚠️ El Secreto de Empate:* Si dos operaciones del mismo nivel están juntas (por ejemplo, una multiplicación y una división), **¡resuelve siempre de izquierda a derecha!**
    """)
    st.divider()
    
    if 'game_id_jbas' not in st.session_state: 
        st.session_state.game_id_jbas = 0
        
    if 'reto_jbas' not in st.session_state:
        # Generamos un reto tipo: A + B * C^2 o A * B - sqrt(C)
        tipo = random.choice(["potencia", "raiz"])
        if tipo == "potencia":
            a = random.randint(3, 10)
            b = random.randint(2, 4)
            c = random.choice([2, 3, 5]) # Exponentes amigables
            
            paso_1 = c ** 2
            paso_2 = b * paso_1
            final = a + paso_2
            st.session_state.reto_jbas = {
                "tipo": tipo, "a": a, "b": b, "c": c,
                "txt": f"{a} + {b} × {c}²",
                "p1_pide": f"Elevar al cuadrado: {c}²", "p1_res": paso_1,
                "p2_pide": f"Multiplicar: {b} × {paso_1}", "p2_res": paso_2,
                "final": final
            }
        else:
            a = random.choice([4, 9, 16, 25])
            b = random.randint(2, 5)
            c = random.randint(1, 5)
            
            paso_1 = int(math.sqrt(a))
            paso_2 = b * paso_1
            final = paso_2 - c
            st.session_state.reto_jbas = {
                "tipo": tipo, "a": a, "b": b, "c": c,
                "txt": f"{b} × √{a} - {c}",
                "p1_pide": f"Sacar raíz cuadrada: √{a}", "p1_res": paso_1,
                "p2_pide": f"Multiplicar: {b} × {paso_1}", "p2_res": paso_2,
                "final": final
            }
            
    r = st.session_state.reto_jbas
    gid = st.session_state.game_id_jbas
    
    st.info(f"⚔️ **Reto de Leyes: ¿Quién tiene el poder aquí?** `{r['txt']}`")
    
    st.write("👇 **Desarma la operación respetando los rangos:**")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("💥 Paso A: El más fuerte")
        st.write(f"Resuelve primero el Nivel 3: `{r['p1_pide']}`")
        user_p1 = st.number_input("Resultado del Paso A:", step=1, key=f"jbas_a_{gid}", value=None)
        
    with col2:
        st.subheader("🛡️ Paso B: El nivel medio")
        st.write(f"Ahora calcula la multiplicación correspondiente:")
        user_p2 = st.number_input("Resultado del Paso B:", step=1, key=f"jbas_b_{gid}", value=None)
        
    st.write("")
    st.subheader("🟢 Paso C: El golpe final")
    user_final = st.number_input("¿Cuál es el veredicto final de toda la operación?", step=1, key=f"jbas_f_{gid}", value=None)
    
    if st.button("👑 Aplicar Leyes del Trono"):
        if user_p1 == r['p1_res'] and user_p2 == r['p2_res'] and user_final == r['final']:
            st.balloons()
            st.success(f"¡PERFECTO! Dictaste las leyes con justicia. El resultado es {r['final']}.")
        else:
            st.error("La jerarquía fue violada. Revisa los rangos: las potencias/raíces van antes que las multiplicaciones, y las sumas/restas se dejan al final.")
            
    if st.button("🔄 Siguiente Ley"):
        st.session_state.game_id_jbas += 1
        del st.session_state.reto_jbas
        st.rerun()