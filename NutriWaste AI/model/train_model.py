import tensorflow as tf
import pandas as pd
import numpy as np
import os

# 1. Load Data (Fixed for Windows Paths)
def load_food_data():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.normpath(os.path.join(current_dir, '..', 'backend', 'data', 'food_data.csv'))
    
    print(f"🔍 DEBUG: Loading data from: {data_path}")
    
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"Cannot find data file at: {data_path}")
        
    df = pd.read_csv(data_path)
    return df

# 2. The AI Optimizer
def predict_meal_plan(target_calories, target_protein, target_carbs, target_fat):
    print(f"\n🧠 AI Thinking... Optimizing for: {target_calories}kcal, {target_protein}g P, {target_carbs}g C, {target_fat}g F")
    
    try:
        df = load_food_data()
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        return []
    
    # --- CRITICAL FIX HERE: Force data to be Float32 ---
    nutrients = df[['Calories', 'Carbs', 'Protein', 'Fat']].values.astype('float32') / 100.0
    food_names = df['FoodItem'].values
    
    # Initialize Weights
    num_foods = len(df)
    food_quantities = tf.Variable(tf.random.uniform([num_foods], minval=10, maxval=100), dtype=tf.float32)

    targets = tf.constant([target_calories, target_carbs, target_protein, target_fat], dtype=tf.float32)
    optimizer = tf.optimizers.Adam(learning_rate=0.1)

    # 3. Training Loop
    print("   Training Model...", end="")
    for i in range(500):
        with tf.GradientTape() as tape:
            current_quantities = tf.nn.relu(food_quantities)
            
            # Now both inputs are float32, so this will work!
            current_totals = tf.linalg.matvec(tf.transpose(nutrients), current_quantities)
            
            loss = tf.reduce_mean(tf.square(targets - current_totals))
        
        gradients = tape.gradient(loss, [food_quantities])
        optimizer.apply_gradients(zip(gradients, [food_quantities]))
    print(" Done!")

    # 4. Result
    final_grams = tf.nn.relu(food_quantities).numpy()
    
    shopping_list = []
    for i, grams in enumerate(final_grams):
        if grams > 10: 
            item = {
                "Food": food_names[i],
                "Grams": int(grams),
                "Calories": int(grams * nutrients[i][0]),
                "Protein": int(grams * nutrients[i][2])
            }
            shopping_list.append(item)
            
    return shopping_list