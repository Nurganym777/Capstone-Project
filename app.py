from flask import Flask, render_template, jsonify
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import json

app = Flask(__name__)

# Load the dataset
df = pd.read_csv('sugar_consumption_dataset 2.csv')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/health-dashboard')
def health_dashboard():
    return render_template('health_dashboard.html')

@app.route('/policy-dashboard')
def policy_dashboard():
    return render_template('policy_dashboard.html')

# API endpoints for health dashboard
@app.route('/api/health/diabetes-obesity')
def diabetes_obesity_data():
    data = df[['Country', 'Diabetes_Prevalence', 'Obesity_Rate']].dropna()
    return jsonify(data.to_dict(orient='records'))

@app.route('/api/health/sugar-intake')
def sugar_intake_data():
    data = df[['Country', 'Avg_Daily_Sugar_Intake', 'Diabetes_Prevalence']].dropna()
    return jsonify(data.to_dict(orient='records'))

@app.route('/api/health/sugar-sources')
def sugar_sources_data():
    data = df[['Country', 'Sugar_From_Sugarcane', 'Sugar_From_Beet', 'Sugar_From_HFCS']].dropna()
    return jsonify(data.to_dict(orient='records'))

# API endpoints for policy dashboard
@app.route('/api/policy/tax-gdp')
def tax_gdp_data():
    data = df[['Country', 'Gov_Tax', 'GDP_Per_Capita', 'Obesity_Rate']].dropna()
    return jsonify(data.to_dict(orient='records'))

@app.route('/api/policy/import-export')
def import_export_data():
    data = df[['Country', 'Sugar_Imports', 'Sugar_Exports']].dropna()
    return jsonify(data.to_dict(orient='records'))

@app.route('/api/policy/production')
def production_data():
    data = df[['Country', 'Sugarcane_Production_Yield']].dropna()
    return jsonify(data.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True) 