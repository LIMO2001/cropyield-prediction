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


@app.route('/about')
def about():
    """About page route"""
    return render_template('about.html')


@app.route('/predict')
def predict():
    """Prediction form page route"""
    regions = data.iloc[:, 0]
    return render_template('predict.html', data=regions)


@app.route('/contact')
def contact():
    """Contact page route"""
    return render_template('contact.html')


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
        
        # Split NPK values
        try:
            N, P, K = NPK.split(":")
            N = int(N)
            P = int(P)
            K = int(K)
        except ValueError:
            # If NPK format is incorrect, set default values
            N, P, K = 10, 5, 5
        
        print(f"NPK Values - N: {N}, P: {P}, K: {K}")
        
        temperature_val = get_temperature(city)
        print(f"Temperature: {temperature_val}")
        
        rainfall_val = get_rainfall(city)
        print(f"Rainfall: {rainfall_val}")
        
        # Check if values are valid
        if temperature_val is None or rainfall_val is None:
            return render_template("error.html", error="Could not retrieve weather data for the selected city")
        
        # Prepare data for prediction
        df = dataPrepare(rainfall_val, temperature_val, soil_type, soil_ph,
                         pest_disease_prevalence, seed_variety, N, P, K)
        
        # Convert to numpy array for prediction
        features = df.values.astype(float)
        final_features = features.reshape(1, -1)  # Reshape for single prediction
        
        print(f"Features shape: {final_features.shape}")
        print(f"Features: {final_features}")
        
        # Make prediction
        try:
            result = model.predict(final_features)
            print(f"Prediction result: {result}")
            return render_template("result.html", result=result)
        except Exception as e:
            print(f"Prediction error: {e}")
            return render_template("error.html", error=f"Prediction failed: {str(e)}")
    
    # If GET request, redirect to prediction form
    return render_template('predict.html', data=data.iloc[:, 0])


# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors"""
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    """Handle 500 errors"""
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)