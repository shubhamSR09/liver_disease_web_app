from flask import Flask, render_template, request
import pickle
import numpy as np



filename = 'liver.pkl'
lr = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('liver.html')



@app.route('/predict', methods=['POST'])
def predict():
    
    if request.method == 'POST':
        Age = int(request.form['Age'])
        Gender = int(request.form['Gender'])
        Total_Bilirubin = int(request.form['Total_Bilirubin'])
        Direct_Bilirubin = int(request.form['Direct_Bilirubin'])
        Alkaline_Phosphotase = int(request.form['Alkaline_Phosphotase'])
        Alamine_Aminotransferase = int(request.form['Alamine_Aminotransferase'])
        Aspartate_Aminotransferase = int(request.form['Aspartate_Aminotransferase'])
        Total_Protiens = int(request.form['Total_Protiens'])
        Albumin = int(request.form['Albumin'])
        Albumin_and_Globulin_Ratio=int(request.form['Albumin_and_Globulin_Ratio'])
        
        
        data = np.array([[Age,Gender,Total_Bilirubin,Direct_Bilirubin,Alkaline_Phosphotase,Alamine_Aminotransferase,Aspartate_Aminotransferase,Total_Protiens,Albumin,Albumin_and_Globulin_Ratio]])
        my_prediction = lr.predict(data)
        
        
    return render_template('liver_result.html', prediction=my_prediction)

if __name__ == '__main__':
	app.run(debug=True)