from flask import Flask, render_template
import os
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/historias')
def historias():
    return render_template('historias.html')

@app.route('/H_ElDiaQueElSol')
def H_ElDiaQueElSol():
    return render_template('H_ElDiaQueElSol.html')  # Archivo H_ElDiaQueElSol.html

@app.route('/H_eLEco')
def H_eLEco():
    return render_template('H_eLEco.html')  # Archivo H_eLEco.html

@app.route('/H_cyberRevuelta')
def H_cyberRevuelta():
    return render_template('H_cyberRevuelta.html')  # Archivo H_cyberRevuelta.html

@app.route('/resenas')
def resenas():
    return render_template('resenas.html')  # reseñas.html

@app.route('/rese_tfundacion_asimov')
def rese_tfundacion_asimov():
    return render_template('rese_tfundacion_asimov.html')  # rese_tfundacion_asimov.html

@app.route('/rese_frankenstein_mary')
def rese_frankenstein_mary():
    return render_template('rese_frankenstein_mary.html')  # Archivo rese_frankenstein_mary

@app.route('/rese_fwtbt_Heminghway')
def rese_fwtbt_Heminghway():
    return render_template('rese_fwtbt_Heminghway.html')  # Archivo rese_fwtbt_Heminghway

@app.route('/rese_trilogiaCosmica_Lewis')
def rese_trilogiaCosmica_Lewis():
    return render_template('rese_trilogiaCosmica_Lewis.html')  # Archivo rese_trilogiaCosmica_Lewis

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Usa el puerto de Render o 5000 por defecto
    app.run(debug=True, host='0.0.0.0', port=port)  # Cambia host a '0.0.0.0'
