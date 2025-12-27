# backend/server.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import os

# Fix paths to find the AI model
sys.path.append(os.path.join(os.path.dirname(__file__), '../model'))
from utils.food_utils import calculate_tdee, calculate_macros
from train_model import predict_meal_plan

app = Flask(__name__)
CORS(app) # Allow the website to talk to this server

@app.route('/api/generate', methods=['POST'])
def generate_plan():
    data = request.json
    print(f"📩 Received Request: {data}")

    # 1. Calculate Needs
    tdee = calculate_tdee(
        float(data['weight']), 
        float(data['height']), 
        int(data['age']), 
        data['gender'], 
        data['activity']
    )
    macros = calculate_macros(tdee, data['goal'])

    # 2. Run AI
    grocery_list = predict_meal_plan(
        macros['calories'], 
        macros['protein_grams'], 
        macros['carbs_grams'], 
        macros['fat_grams']
    )

    # 3. Calculate Waste
    results = []
    total_waste_kg = 0
    total_savings_usd = 0
    
    for item in grocery_list:
        weekly_grams = item['Grams'] * 7
        typical_buy = int(weekly_grams * 1.25)
        saved_grams = typical_buy - weekly_grams
        
        # Estimate $0.01 per gram (roughly $10/kg)
        money_saved = saved_grams * 0.01
        
        total_waste_kg += saved_grams
        total_savings_usd += money_saved

        results.append({
            "food": item['Food'],
            "buy_ai": weekly_grams,
            "buy_typical": typical_buy,
            "saved_grams": saved_grams
        })

    response = {
        "macros": macros,
        "shopping_list": results,
        "total_waste_kg": round(total_waste_kg / 1000, 2),
        "total_savings": round(total_savings_usd, 2)
    }

    return jsonify(response)

if __name__ == '__main__':
    print("🚀 Server starting at http://127.0.0.1:5000")
    app.run(debug=True, port=5000)