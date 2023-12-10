import os
import time
from flask import Flask, jsonify, send_from_directory, request, make_response
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import joblib
import traceback
import pandas as pd
import numpy as np


app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)


class PredictionRequest(db.Model):
    __tablename__ = 'prediction_request'

    id_request = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(255), nullable=False)

    def json(self):
        return {'id_request': self.id_request, 'status': self.status}


# get all prediction request
@app.route('/prediction_request', methods=['GET'])
def get_prediction_request():
  try:
    prediction_request = PredictionRequest.query.all()
    return make_response(jsonify([PredictionRequest.json() for PredictionRequest in prediction_request]), 200)
  except e:
    return make_response(jsonify({'message': 'error getting prediction_request'}), 500)
    

# ML model predictions
@app.route('/predict', methods=['POST'])
def predict():
    #print(os.getcwd())
    lr = joblib.load("model.pkl")
    print('Model loaded')
    model_columns = joblib.load("model_columns.pkl")
    print('Model columns loaded')
    
    if lr:
        new_prediction_request = PredictionRequest(status='Loading')
        db.session.add(new_prediction_request)
        db.session.commit()
        
        try:
            # time.sleep(10) # test threads, celery here in the future
            json_ = request.json
            print(json_)
            query = pd.get_dummies(pd.DataFrame(json_))
            query = query.reindex(columns=model_columns, fill_value=0)
            print(query)
            prediction = list(lr.predict(query))
            
            new_prediction_request.status = 'Finished'
            db.session.commit()
            
            return jsonify({'prediction': str(prediction)})

        except:
            print('Not valid input')
            new_prediction_request.status = 'Failed'
            db.session.commit()
            
            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Train the model first')
        return ('No model here to use')