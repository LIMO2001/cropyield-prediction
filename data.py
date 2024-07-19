import pandas as pd
import numpy as np

# Seed for reproducibility
np.random.seed(42)

# Define the crops, counties, and the number of samples
crops = ['Beans', 'Maize', 'Wheat', 'Rice', 'Soybeans']
kenyan_counties = [
    'Baringo', 'Bomet', 'Bungoma', 'Busia', 'Elgeyo-Marakwet', 'Embu', 'Garissa', 
    'Homa Bay', 'Isiolo', 'Kajiado', 'Kakamega', 'Kericho', 'Kiambu', 'Kilifi', 
    'Kirinyaga', 'Kisii', 'Kisumu', 'Kitui', 'Kwale', 'Laikipia', 'Lamu', 
    'Machakos', 'Makueni', 'Mandera', 'Marsabit', 'Meru', 'Migori', 'Mombasa', 
    'Murang\'a', 'Nairobi', 'Nakuru', 'Nandi', 'Narok', 'Nyamira', 'Nyandarua', 
    'Nyeri', 'Samburu', 'Siaya', 'Taita-Taveta', 'Tana River', 'Tharaka-Nithi', 
    'Trans Nzoia', 'Turkana', 'Uasin Gishu', 'Vihiga', 'Wajir', 'West Pokot'
]
num_samples = 200

# Generate random data
data = {
    'Crop': np.random.choice(crops, num_samples),
    'County': np.random.choice(kenyan_counties, num_samples),
    'Nitrogen (N)': np.random.uniform(0, 200, num_samples),
    'Phosphorus (P)': np.random.uniform(0, 200, num_samples),
    'Potassium (K)': np.random.uniform(0, 200, num_samples),
    'Soil pH': np.random.uniform(5.5, 7.5, num_samples),
    'Rainfall (mm)': np.random.uniform(300, 1500, num_samples),
    'Temperature (C)': np.random.uniform(15, 35, num_samples)
}

# Assume some simplistic relationship for yield prediction
data['Yield (kg/ha)'] = (
    0.1 * data['Nitrogen (N)'] +
    0.08 * data['Phosphorus (P)'] +
    0.05 * data['Potassium (K)'] +
    2 * (data['Soil pH'] - 6.5) +  # Optimal pH around 6.5
    0.02 * (data['Rainfall (mm)'] - 800) +  # Optimal rainfall around 800mm
    -0.1 * (data['Temperature (C)'] - 25) +  # Optimal temperature around 25C
    np.random.uniform(-10, 10, num_samples)  # Add some random noise
)

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('crop_yield_prediction_dataset.csv', index=False)

print("Dataset generated and saved to 'crop_yield_prediction_dataset.csv'")
