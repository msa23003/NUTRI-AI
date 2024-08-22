import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define the function to generate diet recommendations
@st.cache_data
def generate_diet_chart(df, user_input):
    # Placeholder implementation: update with your actual recommendation logic
    filtered_df = df.copy()
    # Example score calculation
    filtered_df['Score'] = np.random.rand(len(filtered_df))  # Replace with actual logic
    filtered_df = filtered_df.sort_values(by='Score', ascending=False)
    return filtered_df.head(user_input['num_recommendations'])

# Streamlit app
st.title("NutriAI Diet Chart Generator")

# Sidebar
st.sidebar.title("Choose Phase")
phase = st.sidebar.radio("Select Phase", ["Diet Recommendation", "Custom Food Recommendation"])

if phase == "Diet Recommendation":
    st.sidebar.subheader("Automatic Diet Recommendation")
    
    # Inputs
    age = st.number_input("Age", min_value=0, value=30)
    height = st.number_input("Height (cm)", min_value=50, value=170)
    weight = st.number_input("Weight (kg)", min_value=10, value=70)
    gender = st.selectbox("Gender", ["Male", "Female"])
    activity = st.selectbox("Activity Level", ["Little/no exercise", "Extra active (very active & physical job)"])
    goal = st.selectbox("Weight Loss Plan", ["Maintain weight", "Mild weight loss", "Weight loss", "Extreme weight loss"])
    meals_per_day = st.selectbox("Meals per day", [3, 5])
    
    # Calculate BMI
    bmi = weight / (height / 100) ** 2
    if bmi < 18.5:
        bmi_status = "Underweight"
    elif 18.5 <= bmi < 25:
        bmi_status = "Normal weight"
    elif 25 <= bmi < 30:
        bmi_status = "Overweight"
    else:
        bmi_status = "Obesity"

    # Calculate Calories
    # Placeholder values: adjust according to your calculation logic
    calorie_options = {
        "Maintain weight": 489,
        "Mild weight loss": 440,
        "Weight loss": 391,
        "Extreme weight loss": 293
    }
    calories_per_day = calorie_options.get(goal, 489)
    
    # Display Results
    st.write(f"**BMI**: {bmi:.1f} ({bmi_status})")
    st.write(f"**Calories per day**: {calories_per_day} for {goal}")
    
    # Placeholder DataFrame
    df = pd.read_csv('recipes.csv', sep=',', nrows=5000)  # Ensure the file path is correct

    if st.button("Generate Diet Chart"):
        user_input = {
            'age': age,
            'height': height,
            'weight': weight,
            'gender': gender,
            'activity': activity,
            'goal': goal,
            'meals_per_day': meals_per_day,
            'num_recommendations': 5  # Placeholder
        }
        recommendations = generate_diet_chart(df, user_input)
        st.write("**Recommended Recipes**")
        st.write(recommendations[['Name', 'Score']])
        
        # Show bar and pie chart for nutrition values
        st.write("**Nutritional Values Overview**")
        nutrition_data = recommendations[['Calories', 'FatContent', 'CarbohydrateContent', 'ProteinContent']]
        
        # Bar chart
        st.write("**Bar Chart**")
        st.bar_chart(nutrition_data)
        
        # Pie chart
        st.write("**Pie Chart**")
        nutrition_sums = nutrition_data.sum()
        fig, ax = plt.subplots()
        ax.pie(nutrition_sums, labels=nutrition_sums.index, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        st.pyplot(fig)

elif phase == "Custom Food Recommendation":
    st.sidebar.subheader("Custom Food Recommendation")
    
    # Filters
    max_calories = st.select_slider("Maximum Calories", options=list(range(0, 2001, 100)), value=2000)
    max_fat = st.select_slider("Maximum Fat Content (g)", options=list(range(0, 101, 5)), value=100)
    max_carbs = st.select_slider("Maximum Carbohydrates (g)", options=list(range(0, 301, 10)), value=300)
    max_sugar = st.select_slider("Maximum Sugar Content (g)", options=list(range(0, 101, 5)), value=100)
    min_protein = st.select_slider("Minimum Protein Content (g)", options=list(range(0, 101, 5)), value=0)
    min_calories = st.select_slider("Minimum Calories", options=list(range(0, 2001, 100)), value=0)
    num_recommendations = st.select_slider("Number of Recommendations", options=list(range(1, 21)), value=5)

    ingredients = st.text_input("Specify ingredients to include in the recommendations (separated by ';'):", "butter;chicken")
    allergies = st.text_input("Enter any allergies (comma-separated):").split(',')
    diseases = st.text_input("Enter any health conditions (comma-separated):").split(',')
    goal = st.selectbox("Enter your health goal:", ["Weight loss", "Diabetes control", "Muscle gain"])
    activity_level = st.selectbox("Enter your activity level:", ["No activity", "Less activity", "Moderately active", "Highly active"])
    food_type = st.selectbox("Food Type", ["All", "Veg", "Non-Veg"])

    user_input = {
        'max_calories': max_calories,
        'max_fat': max_fat,
        'max_carbs': max_carbs,
        'max_sugar': max_sugar,
        'min_protein': min_protein,
        'min_calories': min_calories,
        'num_recommendations': num_recommendations,
        'ingredients': ingredients.split(';'),
        'allergies': allergies,
        'diseases': diseases,
        'goal': goal,
        'activity_level': activity_level,
        'food_type': food_type
    }

    if st.button("Generate Recommendations"):
        df = pd.read_csv('recipes.csv', sep=',', nrows=5000)  # Ensure the file path is correct

        # Apply food type filter
        if user_input['food_type'] != "All":
            df = df[df['RecipeCategory'].str.contains(user_input['food_type'], case=False, na=False)]
        
        recommendations = generate_diet_chart(df, user_input)
        st.write("**Recommended Recipes**")
        st.write(recommendations[['Name', 'Score']])

        # Display nutritional values
        st.write("**Nutritional Values Overview**")
        nutrition_data = recommendations[['Calories', 'FatContent', 'CarbohydrateContent', 'ProteinContent']]
        
        # Bar chart
        st.write("**Bar Chart**")
        st.bar_chart(nutrition_data)
        
        # Pie chart
        st.write("**Pie Chart**")
        nutrition_sums = nutrition_data.sum()
        fig, ax = plt.subplots()
        ax.pie(nutrition_sums, labels=nutrition_sums.index, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        st.pyplot(fig)
