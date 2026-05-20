def animacion_sustitucion(a, x_val, b, y_val, c):
    """
    Genera el contenedor HTML interactivo con estilos oscuros coordinados 
    para explicarle de forma razonada al alumno cómo la llave correcta 
    abre el candado mediante la sustitución de valores.
    """
    paso1 = f"({a})({x_val}) + ({b})({y_val}) = {c}"
    mult_a = a * x_val
    mult_b = b * y_val
    paso2 = f"{mult_a:+} {mult_b:+} = {c}"
    
    html_content = f"""
    <div style="
        background-color: #1e293b; 
        padding: 20px; 
        border-radius: 12px; 
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
        color: white; 
        max-width: 450px; 
        margin: 10px auto; 
        border: 2px solid #3b82f6;
        box-shadow: 0px 4px 15px rgba(59, 130, 246, 0.2);
    ">
        <div style="
            text-align: center; 
            font-weight: bold; 
            color: #60a5fa; 
            font-size: 16px; 
            margin-bottom: 15px; 
            text-transform: uppercase; 
            letter-spacing: 0.5px;
        ">
            🗝️ Mecanismo del Candado Desarmado
        </div>
        
        <div style="line-height: 24px; font-size: 15px;">
            <p style="margin: 8px 0;">
                <b style="color: #f59e0b;">Paso 1:</b> Cambiamos las letras por los números de la llave:
                <br>
                <span style="font-family: monospace; background: rgba(0,0,0,0.3); padding: 2px 6px; border-radius: 4px; font-size: 16px; display: inline-block; margin-top: 4px;">
                    {a}(<span style="color: #ec4899; font-weight: bold;">{x_val}</span>) + {b}(<span style="color: #ec4899; font-weight: bold;">{y_val}</span>) = {c}
                </span>
            </p>
            
            <p style="margin: 16px 0 8px 0;">
                <b style="color: #f59e0b;">Paso 2:</b> Hacemos los duelos de multiplicación:
                <br>
                <span style="font-size: 13px; color: #94a3b8; display: block; margin-left: 10px;">
                    • {a} × {x_val} = <b>{mult_a}</b>
                    <br>
                    • {b} × {y_val} = <b>{mult_b}</b>
                </span>
                <span style="font-family: monospace; background: rgba(0,0,0,0.3); padding: 2px 6px; border-radius: 4px; font-size: 16px; display: inline-block; margin-top: 4px;">
                    {mult_a} {mult_b:+} = {c}
                </span>
            </p>
            
            <div style="
                margin-top: 15px; 
                background: rgba(34, 197, 94, 0.1); 
                border-left: 4px solid #22c55e; 
                padding: 8px 12px; 
                border-radius: 0 6px 6px 0;
                font-size: 14px;
            ">
                <span style="color: #4ade80; font-weight: bold;">✔ Resultado Final:</span> 
                Como <b>{mult_a + mult_b}</b> es igual a <b>{c}</b>, ¡el candado cede y se abre por completo!
            </div>
        </div>
    </div>
    """
    return html_content