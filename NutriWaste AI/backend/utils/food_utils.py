# backend/utils/food_utils.py

def calculate_tdee(weight_kg, height_cm, age, gender, activity_level):
    """
    Calculates Total Daily Energy Expenditure (TDEE) using the Mifflin-St Jeor Equation.
    """
    # 1. Calculate BMR (Basal Metabolic Rate)
    if gender.lower() == 'male':
        bmr = (10 * weight_kg) + (6.25 * height_cm) - (5 * age) + 5
    else:
        bmr = (10 * weight_kg) + (6.25 * height_cm) - (5 * age) - 161

    # 2. Activity Multipliers
    multipliers = {
        'sedentary': 1.2,      # Little or no exercise
        'lightly_active': 1.375, # Light exercise 1-3 days/week
        'moderately_active': 1.55, # Moderate exercise 3-5 days/week
        'active': 1.725        # Hard exercise 6-7 days/week
    }

    # Default to sedentary if input is wrong
    multiplier = multipliers.get(activity_level.lower(), 1.2)
    
    tdee = bmr * multiplier
    return int(tdee)

def calculate_macros(tdee, goal):
    """
    Splits calories into Carbs/Protein/Fat based on goal.
    Returns grams per day.
    """
    # Goal adjustments to calories
    if goal == 'weight_loss':
        target_calories = tdee - 500
        # High protein for weight loss: 40% P / 35% C / 25% F
        ratios = {'protein': 0.40, 'carbs': 0.35, 'fat': 0.25}
    elif goal == 'weight_gain':
        target_calories = tdee + 500
        # High carb for gain: 30% P / 50% C / 20% F
        ratios = {'protein': 0.30, 'carbs': 0.50, 'fat': 0.20}
    else: # maintenance
        target_calories = tdee
        # Balanced: 30% P / 40% C / 30% F
        ratios = {'protein': 0.30, 'carbs': 0.40, 'fat': 0.30}

    # Convert calories to grams
    # Protein = 4 cal/g, Carbs = 4 cal/g, Fat = 9 cal/g
    macros = {
        'calories': int(target_calories),
        'protein_grams': int((target_calories * ratios['protein']) / 4),
        'carbs_grams': int((target_calories * ratios['carbs']) / 4),
        'fat_grams': int((target_calories * ratios['fat']) / 9)
    }
    
    return macros