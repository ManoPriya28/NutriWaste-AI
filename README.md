# 🥗 NutriWaste AI
**AI-Powered Personalized Meal Planning with Zero Food Waste**

### 🚀 Project Overview
NutriWaste AI bridges the gap between personalized nutrition and sustainable living. While most apps track calories, they don't help users buy the *exact* amount of food needed. This leads to overbuying and massive food waste.

**NutriWaste AI** uses Machine Learning (TensorFlow) to optimize grocery lists down to the gram, ensuring you meet your health goals while reducing food waste to near zero.

---

### 🌟 Key Features
*   **Personalized Nutrition Engine:** Calculates BMR, TDEE, and Macro splits using the Harris-Benedict equation.
*   **AI Optimization (TensorFlow):** Uses Gradient Descent to solve the "Perfect Meal Plan" problem—finding the exact combination of foods to match protein/carb goals.
*   **Zero-Waste Calculator:** Compares AI-optimized buying vs. typical shopper behavior to visualize waste reduction (kg) and cost savings ($).
*   **Modern UI:** Glassmorphism design with real-time feedback.

---

### 🛠️ Tech Stack
*   **Frontend:** HTML5, CSS3, JavaScript (Vanilla)
*   **Backend:** Python 3.10+, Flask
*   **AI/ML:** TensorFlow, Pandas, NumPy
*   **Tools:** VS Code, Git

---

### 📸 How It Works
1.  **User Input:** Enter Age, Weight, Height, Activity Level, and Goal (Loss/Gain).
2.  **Processing:** The Python backend calculates daily caloric needs.
3.  **Optimization:** The Neural Network iteratively adjusts food portions to hit macro targets with <1% error.
4.  **Result:** A precise shopping list is generated, highlighting the difference between "Buying Smart" vs. "Buying Typical".

---

### 🔧 How to Run Locally

1. **Clone the Repository**
   ```bash
   git clone https://github.com/ManoPriya28/NutriWaste-AI.git
   cd NutriWaste-AI
