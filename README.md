# 🏏 IPL Victory Predictor

<p align="center">
  <b>Machine Learning Based IPL Winning Probability Predictor</b>
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-150458?style=for-the-badge&logo=pandas)
![Scikit-learn](https://img.shields.io/badge/Scikit--Learn-ML-F7931E?style=for-the-badge&logo=scikit-learn)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?style=for-the-badge&logo=streamlit)

</p>

<p align="center">

🚀 **[Live Demo](https://ipl-victory-predictor-v0yw.onrender.com)**  
💻 **[GitHub Repository](https://github.com/shyamsharan973/ipl-victory-predictor)**

</p>

---

## 📖 About

**IPL Victory Predictor** is a Machine Learning web application that predicts the **winning probability of an IPL team based on the current match situation**.

Users can enter the batting team, bowling team, venue, target, current score, overs completed, and wickets down.

The application calculates important match features such as **runs left, balls left, wickets remaining, CRR, and RRR**, and uses a trained Machine Learning model to predict the likely winner.

---

## ✨ Features

- 🏏 Match situation-based prediction
- 📊 Winning probability for both teams
- 🏆 Predicted winner
- 📍 Venue-based prediction
- 📈 Automatic CRR & RRR calculation
- 🎨 Interactive Streamlit interface
- ☁️ Deployed on Render

---

## 🧠 Machine Learning

The project uses a **Logistic Regression classification model** with a Scikit-learn pipeline.

### Input Features

```text
Batting Team
Bowling Team
Venue
Runs Left
Balls Left
Wickets Remaining
Target
Current Run Rate
Required Run Rate```


## 🔄 Workflow
IPL Historical Data
        ↓
Data Preprocessing
        ↓
Feature Engineering
        ↓
Model Training
        ↓
Scikit-learn Pipeline
        ↓
Streamlit Application
        ↓
Winning Probability
        ↓
Predicted Winner


🛠️ Tech Stack

Python • Pandas • Scikit-learn • Logistic Regression • Streamlit • Git • GitHub • Render


📁 Project Structure
IPL-Victory-Predictor/
│
├── main.py
├── pipe.pkl
├── requirements.txt
├── render.yaml
├── README.md
├── .gitignore
├── background.jpg
│
└── Team Logos
    ├── CSK.png
    ├── RCB.png
    ├── GT.png
    ├── RR.png
    ├── LSG.png
    ├── PBKS.png
    ├── SRH.png
    ├── DC.png
    └── KKR.png


⚙️ Run Locally
git clone https://github.com/shyamsharan973/ipl-victory-predictor.git

cd ipl-victory-predictor

pip install -r requirements.txt

streamlit run main.py


⭐ If you found this project interesting, consider giving the repository a star!
This is the version I'd recommend for your repo: **short enough that recruiters will actually read it, but detailed enough to understand the project.**

Also, the Logistic Regression and One-Hot Encoding claims match your actual trained pipeline, rather than the more advanced models in the reference README. :contentReference[oaicite:0]{index=0}
