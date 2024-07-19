from flask import Flask, render_template, request
import sklearn
import numpy as np
import pandas as pd
import joblib

app = Flask(__name__)

model = joblib.load('model.pkl')
data = pd.read_excel("climate-dataset-kenya.xlsx")


def dataPrepare(rainfall, temperature, soilType, soilPH, pestDiseasePrevalence, seedVariety, N, P, K):
    # Creating a dictionary with the provided data
    data_dict = {
        'Rainfall (mm)': [rainfall],
        'Temperature (°C)': [temperature],
        'Soil Type': [soilType],
        'Soil pH': [soilPH],
        'N': [N],
        'P': [P],
        'K': [K],
        'Pest & Disease Prevalence (%)': [pestDiseasePrevalence],
        'Maize Seed Variety': [seedVariety]
    }

    # Creating a DataFrame
    df = pd.DataFrame(data_dict)

    return df


def get_temperature(city):
    # Assuming data is your DataFrame
    try:
        temperature_value = data.loc[data['Towns/Cities'] == city, 'Temperature'].values
        if len(temperature_value) > 0:
            temperature_value = int(temperature_value[0])
            print("Temperature for", city, ":", temperature_value)
            return temperature_value
        else:
            print("No data found for", city)
            return None  # or any default value you prefer if no data is found
    except ValueError as e:
        print("Error:", e)
        print("Non-numeric value found in the 'Temperature' column.")
        return None


def get_rainfall(city):
    # Assuming data is your DataFrame
    try:
        rainfall_value = data.loc[data['Towns/Cities'] == city, 'Rainfall'].values
        if len(rainfall_value) > 0:
            rainfall_value = int(rainfall_value[0])
            print("Rainfall for", city, ":", rainfall_value)
            return rainfall_value
        else:
            print("No data found for", city)
            return None  # or any default value you prefer if no data is found
    except ValueError as e:
        print("Error:", e)
        print("Non-numeric value found in the 'Rainfall' column.")
        return None


@app.route('/')
def root():
    regions = data.iloc[:, 0]
    return render_template('index.html', data=regions)


@app.route('/form', methods=['POST', 'GET'])
def form():
    return request.form


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        city = request.form['town']
        NPK = request.form['NPK']
        soil_type = request.form['soilType']
        soil_ph = request.form['ph']
        pest_disease_prevalence = request.form['pestPrevalence']
        seed_variety = request.form['seedVariety']
        N, P, K = NPK.split(":")
        print(N, P, K)
        temperature_val = get_temperature(city)
        print(temperature_val)
        rainfall_val = get_rainfall(city)
        df = dataPrepare(rainfall_val, temperature_val, soil_type, soil_ph,
                         pest_disease_prevalence, seed_variety, N, P, K)
        features = df.values.astype(int)
        final_features = np.array([np.array(features)])
        final_features = final_features.reshape(-1, 9)  # Adjust the number of columns accordingly
        print(df)
        result = model.predict(final_features)
        return render_template("result.html",result=result)


if __name__ == '__main__':
    app.run(debug=True)