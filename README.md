# 🌽 Maize Yield Prediction System

A machine learning project that predicts maize yield based on environmental and soil factors.  
This system helps farmers and agricultural stakeholders make data-driven decisions to improve productivity.

---

## 📌 Project Overview
Maize is a staple food crop in many countries, especially in Kenya. However, its yield is highly affected by factors such as rainfall, temperature, soil conditions, and pest prevalence.

This project uses **Machine Learning (Linear Regression)** to analyze these factors and predict maize yield, enabling better planning and smarter farming practices.

---

## 🎯 Objectives
- Analyze key factors affecting maize yield  
- Build a predictive model using historical data  
- Estimate expected yield before harvesting  
- Support smart agriculture and decision-making  

---

## 🛠️ Tech Stack
- **Python** – Core programming language  
- **Jupyter Notebook** – Development environment  
- **Pandas** – Data manipulation and analysis  
- **NumPy** – Numerical computations  
- **Matplotlib** – Data visualization  
- **Scikit-learn** – Machine learning (Linear Regression, preprocessing, evaluation)  
- **Joblib** – Model saving and loading  

---

## 📊 Dataset Features
The model uses the following features:
- Rainfall (mm)  
- Temperature (°C)  
- Soil Type  
- Soil pH  
- Soil Nutrients (N, P, K)  
- Pest & Disease Prevalence (%)  
- Previous Year Yield  
- Seed Variety  

---

## ⚙️ Methodology

### 1. Data Preprocessing
- Cleaned and selected relevant features  
- Converted categorical variables into numerical values  
- Split NPK values into Nitrogen (N), Phosphorus (P), and Potassium (K)  
- Scaled features using StandardScaler  

### 2. Exploratory Data Analysis (EDA)
- Performed statistical analysis  
- Visualized relationships between variables  
- Identified correlations affecting yield  

### 3. Model Development
- Applied **Linear Regression**  
- Split dataset into training (80%) and testing (20%) sets  

### 4. Model Evaluation
- Evaluated using **Mean Squared Error (MSE)**  
- Compared predicted vs actual values  

---

## 🤖 Model
The project uses **Linear Regression**, which models the relationship between input variables and maize yield.

It helps to:
- Understand the impact of each factor  
- Predict yield based on new input data  

---

## 📈 Results
- The model successfully predicts maize yield  
- Key influencing factors include:
  - Rainfall  
  - Temperature  
  - Soil nutrients (especially Nitrogen)  

---

## 💡 Applications
- Decision support for farmers  
- Agricultural advisory systems  
- Integration into mobile or web farming applications  

---

## ⚠️ Limitations
- Assumes linear relationships between variables  
- Accuracy depends on data quality  
- Cannot fully capture complex environmental interactions  

---

## 🚀 Future Improvements
- Use advanced models (Random Forest, XGBoost)  
- Integrate real-time weather data  
- Develop a user-friendly web or mobile application  
- Expand dataset for improved accuracy  

---

## ▶️ How to Run the Project

1. Clone the repository:

[git clone https://github.com/yourusername/maize-yield-prediction.git](https://github.com/LIMO2001/cropyield-prediction.git)
<img width="955" height="499" alt="image" src="https://github.com/user-attachments/assets/12add991-cce4-49f5-9862-da492fe029b3" />
<img width="1887" height="951" alt="Screenshot 2026-03-31 112849" src="https://github.com/user-attachments/assets/163ba83c-fda8-4d77-a24e-24b9073ea808" />

