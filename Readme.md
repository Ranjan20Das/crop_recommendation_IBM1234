🌱 Crop Recommendation System (AI/ML)

An AI-powered Crop Recommendation System that suggests the most suitable crop based on soil nutrients and environmental conditions. The model is trained using machine learning and deployed with an interactive Streamlit web interface.

🚀 Live Demo

👉 Hosted on Streamlit Cloud (Free Tier)

The app predicts the best crop using inputs such as N, P, K, temperature, humidity, pH, and rainfall.

📌 Features

🌾 Predicts the best crop for given soil & climate conditions

🤖 Machine Learning model (Random Forest Classifier)

⚡ Fast and accurate predictions (~99% accuracy)

🖥️ Interactive Streamlit UI

☁️ Deployed on Streamlit Cloud

🧠 Machine Learning Details

Algorithm: Random Forest Classifier

Dataset Size: ~2200 records

Input Features:

Nitrogen (N)

Phosphorus (P)

Potassium (K)

Temperature (°C)

Humidity (%)

pH value

Rainfall (mm)

Target Variable: label (Crop Name)

🗂️ Project Structure
crop-recommendation-app/
│
├── crop_recommendation.py   # Streamlit application
├── Crop_recommendation.csv  # Dataset
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
🛠️ Technologies Used

Python

Pandas

NumPy

Scikit-learn

Streamlit

⚙️ Installation & Setup (Local)
1️⃣ Clone the Repository
git clone https://github.com/your-username/crop-recommendation-app.git
cd crop-recommendation-app
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Run the Application
streamlit run crop_recommendation.py
🌐 Deployment

This project is deployed using Streamlit Cloud:

Steps:

Push the code to GitHub

Go to https://streamlit.io/cloud

Select the repository

Set main file path: crop_recommendation.py

Click Deploy

⚠️ Streamlit Cloud provides long-term free hosting but does not guarantee lifetime uptime.

📊 Sample Input
Parameter	Value
Nitrogen (N)	90
Phosphorus (P)	42
Potassium (K)	43
Temperature	20.8
Humidity	82.0
pH	6.5
Rainfall	202.9
✅ Output
Recommended Crop: RICE
🔮 Future Enhancements

🌍 Location-based weather data

🧪 Fertilizer recommendation system

📱 Mobile-friendly UI

🌐 REST API (FastAPI/Flask)

🐳 Docker support

👨‍💻 Author

Ranjan Das
AI / ML Enthusiast | Full Stack Learner

📜 License

This project is for educational and research purposes.

Feel free to fork, modify, and use it for learning.
