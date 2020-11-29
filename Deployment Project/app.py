# import libraries
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# create app and load the trained Model
app = Flask(__name__)
model = pickle.load(open('Trained_Model.pkl', 'rb'))

# Route to handle HOME
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle PREDICTED RESULT
@app.route('/',methods=['POST'])
def predict():
  
    inputs = [] # declaring input array

    p = request.form['pclass']
    g = request.form['gender']
    s = request.form['siblings']
    e = request.form['embarked']

    if p == "1":
        pclass = "First"
    elif p == "2":
        pclass = "Second"
    elif p == "3":
        pclass = "Third"

    if g == "1":
        gender = "Male"
    elif g == "0":
        gender = "Female"

    if s == "0":
        siblings = "None"
    elif s == "1":
        siblings = "One"
    elif s == "2":
        siblings = "Two"
    elif s == "3":
        siblings = "Three"

    if e == "0":
        embarked = "Cherbourg"
    elif e == "1":
        embarked = "Queenstown"
    elif e == "2":
        embarked = "Southampton"

    inputs.append(p)
    inputs.append(g)
    inputs.append(s)
    inputs.append(e)

    final_inputs = [np.array(inputs)]
    prediction = model.predict(final_inputs)

    if(prediction[0] == 1):
        return render_template('index.html', predicted_result = 'Survived',pclass = pclass,gender = gender,siblings = siblings,embarked = embarked)
    if(prediction[0] == 0):
        return render_template('index.html',  predicted_result = 'Not Survived',pclass = pclass,gender = gender,siblings = siblings,embarked = embarked)


if __name__ == "__main__":
    app.run(debug=True)
