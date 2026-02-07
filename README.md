🌾 KrishiMind — Smart Irrigation System (AICTE Virtual Internship)

KrishiMind is an AI-powered Smart Irrigation System developed as a project under the AICTE Virtual Internship (Cycle 2).
The goal of this project is to predict which sprinklers should be turned ON/OFF based on sensor values (scaled between 0 to 1) using a trained Machine Learning model.
🚀 Live Demo

👉 Streamlit App: https://smart-irrigation-system-project-aicte-vansh-somal.streamlit.app/

▶️ How to Run This Project Locally
1️⃣ Clone the repository
git clone https://github.com/VanshSomal/Smart_Irrigation_Project-AICTE.git
cd your-repo-name
2️⃣ Install dependencies
pip install streamlit numpy pandas scikit-learn joblib matplotlib
3️⃣ Run the Streamlit App
streamlit run app.py

This project includes:

A Jupyter Notebook for data preprocessing, model training, and evaluation
A Streamlit Web App for real-time sprinkler prediction and interactive visualization

📌 Project Overview

Efficient irrigation is essential for saving water and improving crop productivity.
KrishiMind uses sensor data and an ML model to predict sprinkler activation across multiple farm parcels.

The model is trained using:
✅ RandomForestClassifier
✅ MultiOutputClassifier (for predicting multiple sprinklers at once)

The trained model is then deployed using Streamlit for a clean and user-friendly interface.

🚀 Features
🔍 ML Prediction

Takes 20 sensor inputs (scaled between 0 and 1)

Predicts sprinkler status for each parcel:

🟢 ON
🔴 OFF

🌦️ Weather Selection

Sunny ☀️
Cloudy 🌥️
Rainy 🌧️ (shows warning to reduce irrigation)

📊 Data Visualization

Bar chart visualization of sensor values
Optional CSV upload for viewing past irrigation data
Sprinkler status shown in a clean grid layout

💧 Insights

Active sprinklers count
Estimated water usage
Progress bar showing sprinkler activation %

🌱 Tips Section

Provides simple irrigation tips for better water management.

🛠 Tech Stack
👨‍💻 Programming & Deployment

Python
Streamlit

📚 Libraries Used

NumPy
Pandas
Scikit-learn
Joblib
Matplotlib

📂 Project Structure
KrishiMind/
│
├── app.py                         # Streamlit Web App
├── Smart_Irrigation_System.ipynb   # Model training notebook
├── Farm_Irrigation_System.pkl      # Trained ML model (saved using joblib)
├── irrigation_machine.csv          # Dataset
├── farm_image.jpg                  # Image used in UI
└── README.md                       # Project documentation

🧠 Machine Learning Workflow
✅ Step 1: Data Loading & Cleaning

Dataset loaded using Pandas
Removed unwanted column (Unnamed: 0)

✅ Step 2: Feature & Label Selection

Features: sensor_0 to sensor_19
Labels: parcel_0, parcel_1, parcel_2 (sprinkler ON/OFF)

✅ Step 3: Scaling

Applied MinMaxScaler
Converted values into the range 0 to 1

✅ Step 4: Model Training
Used Random Forest with tuned hyperparameters
Wrapped using MultiOutputClassifier

✅ Step 5: Evaluation

Classification report generated
Visual analysis of sprinkler patterns
✅ Step 6: Model Saving

Model saved as:

Farm_Irrigation_System.pkl

🧾 Notes / Credits

This project was created as part of the AICTE Virtual Internship (Cycle 2).
The base Jupyter Notebook and initial Streamlit structure were introduced during internship training.
The complete UI redesign, styling, layout, extra features, and interactive enhancements were implemented by me with some assistance from ChatGPT.

📌 Developer

👤 Vansh Somal
🎓 B.Tech (CSE) Student
📍 Delhi, India

🌟 Future Improvements (Planned)

Add real-time sensor input support (IoT integration)
Add soil type / crop type options
Add rainfall probability using weather API

Deploy on Streamlit Cloud

Add irrigation scheduling recommendations
⭐ If you like this project

Give this repo a ⭐ and feel free to suggest improvements!
