# NUTRI-AI #

**NUTRI-AI Diet Chat Generator** is a Streamlit-based application designed to provide personalized diet recommendations. It utilizes user inputs to generate diet charts and food recommendations based on various parameters. The application also visualizes nutritional values with bar and pie charts for better insight.

## Features

- **Automatic Diet Recommendation**: Based on user inputs such as age, height, weight, gender, activity level, and weight loss goal.
- **Custom Food Recommendation**: Filters and recommends recipes based on calorie, fat, carbohydrate, sugar content, and user-specific requirements such as allergies, health conditions, and food type.
- **Nutritional Visualization**: Displays bar and pie charts for nutritional values of recommended recipes.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/NutriAI.git
    cd NutriAI
    ```

2. Install the required Python packages:

    ```bash
    pip install streamlit pandas numpy matplotlib
    ```

3. Download the dataset (`recipes.csv`) and place it in the project directory. Ensure the dataset has columns like `Name`, `Calories`, `FatContent`, `CarbohydrateContent`, `ProteinContent`, and `RecipeCategory`.

## Usage

1. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

2. Open your browser and go to `http://localhost:8501` to interact with the app.

## How It Works

### Automatic Diet Recommendation

- **Input Parameters**: Age, Height, Weight, Gender, Activity Level, Weight Loss Goal, Meals Per Day.
- **Output**: BMI calculation, daily calorie needs, and recommended recipes based on the highest scores.

![Diet Recommendation](![image](https://github.com/user-attachments/assets/853c1bed-edbe-4067-8cb0-e63811c549c6)
![image](https://github.com/user-attachments/assets/8ccae925-5063-4add-ac96-8bf9c6e41b29)
![image](https://github.com/user-attachments/assets/d0f341f1-fc96-40df-9991-26c828c6822f)
![image](https://github.com/user-attachments/assets/216cbabf-b071-4a92-b7d3-d35bdd751d79)
) 

### Custom Food Recommendation

- **Input Filters**: Maximum/Minimum Calories, Fat, Carbohydrates, Sugar, Protein, Ingredients, Allergies, Health Conditions, Goal, Activity Level, Food Type.
- **Output**: Recipes that match the specified filters and nutritional values visualization.

![Custom Food Recommendation](![image](https://github.com/user-attachments/assets/742ed8cb-3604-4eb6-82fd-5df77a1bc010)
![image](https://github.com/user-attachments/assets/36004228-da39-4dff-95d4-39d48923d86d)
![image](https://github.com/user-attachments/assets/059aa2c1-a226-4ff4-8eb5-8b7cd6460fb1)
![image](https://github.com/user-attachments/assets/0b357472-912f-4d33-b0e8-6cc3b71e6540)
![image](https://github.com/user-attachments/assets/f131474e-06b4-4569-81ee-809ff625e733)
)

## Code Overview

- **`app.py`**: Main Streamlit app script containing the logic for diet recommendations and custom food filtering.
- **`recipes.csv`**: Dataset containing recipe information used for generating recommendations.

## Contributing

Feel free to fork the repository, make changes, and create a pull request. Any contributions to improve the application are welcome!

