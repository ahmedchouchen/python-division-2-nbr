from flask import Flask, request, jsonify, render_template

# Create the app object
app = Flask(__name__)


# importing function for calculations
from division_function import division

# Define calculator
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    a = request.form['a']
    b = request.form['b']
    

    result = division(a,b)

    return render_template('index.html', prediction_text=str(result))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=82)
