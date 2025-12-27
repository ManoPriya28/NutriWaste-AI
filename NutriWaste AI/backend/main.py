import sys
import os

# Add the 'model' folder to the system path so we can import the AI script
sys.path.append(os.path.join(os.path.dirname(__file__), '../model'))

from utils.food_utils import calculate_tdee, calculate_macros
from train_model import predict_meal_plan

def run_nutriwaste_ai():
    print("\n=========================================")
    print("      NUTRIWASTE AI - SYSTEM START       ")
    print("=========================================")

    # 1. User Input (Simulated)
    user = {'age': 28, 'gender': 'female', 'weight': 65, 'height': 165, 'activity': 'moderately_active', 'goal': 'weight_loss'}
    
    # 2. Calculate Needs
    tdee = calculate_tdee(user['weight'], user['height'], user['age'], user['gender'], user['activity'])
    macros = calculate_macros(tdee, user['goal'])
    print(f"🎯 Goal: {macros['calories']} kcal | P: {macros['protein_grams']}g | C: {macros['carbs_grams']}g")

    # 3. AI Optimization
    grocery_list = predict_meal_plan(macros['calories'], macros['protein_grams'], macros['carbs_grams'], macros['fat_grams'])

    # 4. Waste & Savings Output
    print("\n=========================================")
    print("      WEEKLY SHOPPING LIST & SAVINGS     ")
    print("=========================================")
    print(f"{'FOOD ITEM':<20} | {'BUY (AI)':<10} | {'TYPICAL':<10} | {'SAVED'}")
    print("-" * 60)

    total_waste = 0
    for item in grocery_list:
        weekly = item['Grams'] * 7
        typical = int(weekly * 1.25) # 25% overbuy
        saved = typical - weekly
        total_waste += saved
        print(f"{item['Food']:<20} | {weekly}g     | {typical}g     | {saved}g")

    print("=========================================")
    print(f"🌱 TOTAL WASTE SAVED: {total_waste/1000:.2f} kg")

if __name__ == "__main__":
    run_nutriwaste_ai()