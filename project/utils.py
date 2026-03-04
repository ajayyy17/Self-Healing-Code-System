import os
import json
import pickle
import joblib
import numpy as np
import pandas as pd

def load_artifacts():
    global _bmi_sc
    global _ss_ohe
    global _allergies_ohe
    global _apl_ohe
    global _pal_ohe
    global _logit_model

    try:
        print('Loading the Artifacts.......')
        _bmi_sc = joblib.load('./artifacts/bmi_sc.pkl')
        _ss_ohe = joblib.load('./artifacts/ss_ohe.pkl')
        _allergies_ohe = joblib.load('./artifacts/allergies_ohe.pkl')
        _apl_ohe = joblib.load('./artifacts/apl_ohe.pkl')
        _pal_ohe = joblib.load('./artifacts/pal_ohe.pkl')
        _logit_model = joblib.load('./artifacts/logit_model.pkl')

    except Exception as e:
        print(f'Error Loading the Artifacts: {e}')
    
    return _bmi_sc, _ss_ohe, _allergies_ohe, _apl_ohe, _pal_ohe, _logit_model

def asthma_prediction(BMI, Family_History, Smoking_Status, Allergies, Air_Pollution_Level, Physical_Activity_Level):
    bmi_df = pd.DataFrame({'BMI':[BMI]})
    BMI_scaled = _bmi_sc.transform(bmi_df)

    fh_arr = np.array([[Family_History]], dtype=int)

    ss_enc = _ss_ohe.transform([[Smoking_Status]])
    allergies_enc = _allergies_ohe.transform([[Allergies]])
    apl_enc = _apl_ohe.transform([[Air_Pollution_Level]])
    pal_enc = _pal_ohe.transform([[Physical_Activity_Level]])
    
    # Concatenate horizontally to form a single feature vector for prediction
    x_data = np.hstack((BMI_scaled, fh_arr, ss_enc, allergies_enc, apl_enc, pal_enc))  # shape (1, n_features)
    asthma_pred = _logit_model.predict(x_data)[0]            # scalar class
    proba = _logit_model.predict_proba(x_data)[0,1]       # probabilities for all classes
    
    return int(asthma_pred), proba

if __name__ == '__main__':
    load_artifacts()
    print(asthma_prediction(
    BMI=22,
    Family_History=1,
    Smoking_Status='Never',
    Allergies='Dust',
    Air_Pollution_Level='Moderate',
    Physical_Activity_Level='Moderate'
))