from flask import Flask, render_template, redirect, request
import joblib
import numpy as np

model= joblib.load('model.pkl')

#__name__ == __main__
app= Flask(__name__)


@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def prediction():
    if request.method=="POST":
        temp=float(request.form['Temperature'])
        massloss=float(request.form['Mass Loss'])
        density=float(request.form['Density'])
        porosity=float(request.form['Porosity'])
        pwave=float(request.form['P-Wave'])
        swave=float(request.form['S-Wave'])
        ed=float(request.form['Ed'])
        
        para=np.array([temp, massloss, density, porosity, pwave, swave, ed])
        para=para.reshape(1,-1)
        thermalcoefficient= str(model.predict(para)[0])
    
    return render_template("index.html", tc= thermalcoefficient)


if __name__=='__main__':
    #app.debug = True
    app.run(debug = True)
    
    
