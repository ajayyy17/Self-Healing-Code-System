import flask
from flask_cors import CORS
from flask import Flask, request, jsonify, render_template
import utils

app = Flask(__name__, template_folder='template', static_folder='static')
CORS(app, resources={r'/*': {'origin': '*'}})

utils.load_artifacts()

@app.route('/')
def index():
    return render_template('app.html')

@app.route('/predict_asthma', methods=['POST'])
def predict_ashtma():
    data = request.get_json()

    BMI = float(data['BMI'])
    Family_History = int(data['Family_History'])
    Smoking_Status = str(data['Smoking_Status'])
    Allergies = str(data['Allergies'])
    Air_Pollution_Level = str(data['Air_Pollution_Level'])
    Physical_Activity_Level = str(data['Physical_Activity_Level'])

    asthma_pred, proba = utils.asthma_prediction(BMI, Family_History, Smoking_Status, Allergies, Air_Pollution_Level, Physical_Activity_Level)
    response = {
        'asthma_result': asthma_pred,
        'probability': proba
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=8010)
