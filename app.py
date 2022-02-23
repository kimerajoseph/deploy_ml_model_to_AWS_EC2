from flask import Flask,request, url_for, redirect, render_template, jsonify
#from pycaret.regression import *
import pandas as pd
import pickle
import numpy as np
import copy
import xgboost as xgb
from xgboost import XGBClassifier
from sklearn.preprocessing import MinMaxScaler
import joblib
from rates import rates_function,process_list
import decode

# initaiate app
app = Flask(__name__)

# load ML model
model_name = 'finalized_model.pkl'
loaded_model = pickle.load(open(model_name, 'rb'))

# load scaler
my_scaler = joblib.load('scaler.gz')



@app.route('/')
def home():
    return render_template("home.html")


@app.route('/predict',methods=['POST'])
def predict():
    val=[x for x in request.form.values()]
    #print(val)
    # call function to process_list function from rates.py process the values from the front end
    processed_list = process_list(val)

    cols = ['gender', 'age_years', 'marital_status', 'no_of_children', 'no_of_dependants', 'income_type',
    'level_of_education','occupation_type', 'housing_type', 'property_owner','mobile','work_phone', 'email', 
     'months_employed', 'income']

    # #loan amount should be 50% of applicant's annual net income
    # # Take a tax rate of 25% for income<58000 (unmarried) and 25% for income <115,000 (married)
    # # 45%, income < 275000 and unmarried. 600k threshold for married applicants
    int_list = list(map(int, processed_list))
    # #criteria 1 not married and income < 58k
    # if int_list[2] != 2 and int_list[-1] < 58000:
    #     rate = 0.25
    
    # # married and income < 115k
    # elif int_list[2] == 2 and int_list[-1] < 115000:
    #     rate = 0.25

    # # unmarried person earning between 58k and 275k
    # elif int_list[2] != 2 and 58000 <= int_list[-1] <= 275000:
    #     rate = 0.45
    
    # elif int_list[2] == 2 and 115000 <= int_list[-1] <= 600000:
    #     rate = 0.45

    # # all other cases, use a flat rate of 30%
    # else:
    #     rate = 0.3
    
    # amount = rate * int_list[-1]

    # call rates function from rates.py file
    amount = rates_function(int_list[2],int_list[-1])
    print("amount returned is: ",amount)

    data_unseen = pd.DataFrame([int_list], columns = cols)
    #print(data_unseen.dtypes)

    # age_years,months_employed,income columns need scaling
    data_to_scale = data_unseen[['age_years','months_employed','income']]
    data_scaled = my_scaler.transform(data_to_scale)
    data_scaled = pd.DataFrame(data_scaled, columns = data_to_scale.columns)
    #print(data_scaled)

    # drop the scaled columns from the original DF
    data_unseen = data_unseen.drop(['age_years','months_employed','income'],axis=1)
    final_data = pd.concat([data_unseen,data_scaled], axis=1)

    #print(final_data.dtypes)
    prediction=loaded_model.predict(final_data)
    print("ML PREDICTION IS: ", prediction)
    ".2f"
    if prediction[0] == 1:
        result = f"Application approved. Maximum amount: {amount:,}"
    else:
        result = "Application denied"            
            
    return render_template('predict.html',result=result)

# predict using the API
@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)

    # call the decode_api_data function from decode.py
    decode_contacts = decode.decode_api_data(data)

    new_data = pd.DataFrame([decode_contacts])

    # call decode_df_columns function from decode.py
    new_decoded_data = decode.decode_df_columns(new_data)

    # get income column value before scaling it
    # call the rates function from rates.py to get maximum loan amount
    income = new_decoded_data['income']
    marital_status=new_decoded_data['marital_status']
    amount = rates_function(int(marital_status),int(income))

    # age_years,months_employed,income columns need scaling
    data_to_scale = new_decoded_data[['age_years','months_employed','income']]
    data_scaled = my_scaler.transform(data_to_scale)
    data_scaled = pd.DataFrame(data_scaled, columns = data_to_scale.columns)

     
    # final DF
    new_decoded_data = new_decoded_data.drop(['age_years','months_employed','income'],axis=1)
    data_unseen = pd.concat([new_decoded_data,data_scaled], axis=1)
    
    prediction=loaded_model.predict(data_unseen) 
    
    if prediction[0] == 1:
        result = f"Application approved. Maximum amount is: {amount:,}"
    else:
        result = "Application denied"
    # convert prediction to string
    return jsonify({'result':result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)