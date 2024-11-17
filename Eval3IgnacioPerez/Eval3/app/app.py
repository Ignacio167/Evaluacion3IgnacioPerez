from flask import Flask,request,render_template
app= Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ejercicio1', methods=['GET','POST'])
def formularioE1():
    if request.method == 'POST':
        num1 = int(request.form['nota1'])
        num2 = int(request.form['nota2'])
        num3 = int(request.form['nota3'])
        asist = int(request.form['asistencia'])
        estado=""
        promedio = (num1+num2+num3)/3
        if promedio >=40 and asist>=75:
                estado="APROBADO"
        else:
                estado="REPROBADO"
        return render_template('ejercicio1.html', promedio=promedio,estado=estado)
    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET','POST'])
def formularioE2():
    if request.method == 'POST':
        nom1 = request.form['nombre1']
        nom2 = request.form['nombre2']
        nom3 = request.form['nombre3']
        nom_res=""
        lar_res=0
        if len(nom1)>=len(nom2) and len(nom1)>=len(nom3):
            nom_res=nom1
            lar_res=len(nom1)
        elif len(nom2)>=len(nom3):
            nom_res=nom2
            lar_res=len(nom2)
        else:
            nom_res=nom3
            lar_res=len(nom3)
        return render_template('ejercicio2.html',nombre=nom_res,largo=lar_res)
    return render_template('ejercicio2.html')


if __name__ == '__main__':
    app.run()