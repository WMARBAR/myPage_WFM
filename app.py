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

@app.route('/resenas')
def resenas():
    return render_template('resenas.html')  # Archivo H_ElDiaQueElSol.html


@app.route('/rese_tfundacion_asimov')
def rese_tfundacion_asimov():
    return render_template('rese_tfundacion_asimov.html')  # Archivo H_ElDiaQueElSol.html

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Usa el puerto de Render o 5000 por defecto
    app.run(debug=True, host='0.0.0.0', port=port)  # Cambia host a '0.0.0.0'
