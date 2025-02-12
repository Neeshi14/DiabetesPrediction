from flask import Flask, request, render_template

import pickle

app = Flask(__name__)


scaler = pickle.load(open('scaler.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = -1
    if request.method == 'POST':
        gluc = int(request.form.get('gluc'))
        insulin = float(request.form.get('insulin'))
        bmi = float(request.form.get('bmi'))
        func = float(request.form.get('func'))
        age = int(request.form.get('age'))

        input_features = [[gluc,insulin, bmi, func, age]]
        # print(input_features)
        prediction = model.predict(scaler.transform(input_features))
        # print(prediction)
        
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)