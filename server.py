# from re import I
# from sre_constants import IN
from flask import Flask,render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

data = pd.read_csv('aLL_location.csv')
pipe = pickle.load(open('pipe.pkl','rb'))


@app.route('//')
def index():
    locations = data['location'].unique()
    return render_template('web.html',locations=locations)


@app.route('/predict',methods=['POST'])
def predict():
    locations = request.form.get('location')
    bhk = int(request.form['mbhk'])
    bath = int(request.form['nbath'])
    sqft = request.form.get('sqft')
    input = pd.DataFrame([[locations,sqft,bath,bhk]],columns=['location', 'total_sqft', 'bath', 'bed'])
    prediction = pipe.predict(input)[0]*100000
    #print(locations,bhk,bath,sqft)
    return str(round(prediction,2))


if __name__ == '__main__':
    app.run(debug=True)
