from flask import Flask, render_template, request

app = Flask(__name__)

def calcular_sueldo_neto_mensual(sueldo_bruto_mensual):
    # Porcentaje de retención del Impuesto sobre la Renta de las Personas Físicas
    porcentaje_retencion_irpf = 0.02  # Retención mínima del 2%

    # Aportaciones a la Seguridad Social
    aportacion_contingencias_comunes = sueldo_bruto_mensual * 0.047
    aportacion_desempleo = sueldo_bruto_mensual * 0.0155
    aportacion_formacion_profesional = sueldo_bruto_mensual * 0.001
    # Si se han realizado horas extras, se añade el 2% de sueldo_bruto_mensual
    aportacion_horas_extras = 0.02 * sueldo_bruto_mensual  

    # Calculamos la retención de IRPF
    retencion_irpf = sueldo_bruto_mensual * porcentaje_retencion_irpf

    # Calculamos el total de aportaciones a la Seguridad Social
    total_aportaciones_ss = (aportacion_contingencias_comunes + aportacion_desempleo +
                             aportacion_formacion_profesional + aportacion_horas_extras)

    # Restamos la retención de IRPF y las aportaciones a la Seguridad Social del sueldo bruto mensual
    sueldo_neto_mensual = sueldo_bruto_mensual - retencion_irpf - total_aportaciones_ss

    return sueldo_neto_mensual

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        sueldo_bruto_mensual = float(request.form['sueldo_bruto'])
        sueldo_neto_mensual = calcular_sueldo_neto_mensual(sueldo_bruto_mensual)
        return render_template('index.html', sueldo_neto_mensual=sueldo_neto_mensual)
    return render_template('index.html', sueldo_neto_mensual=None)

if __name__ == '__main__':
    app.run(debug=True)
