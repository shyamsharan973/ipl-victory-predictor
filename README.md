# IPL Victory Predictor

A Streamlit-based machine learning application that predicts IPL winning probability from the current match situation.

## Features
- Select batting and bowling teams
- Select venue
- Enter target, current score, overs completed, and wickets down
- Calculates runs left, balls left, wickets remaining, current run rate (CRR), and required run rate (RRR)
- Displays winning probability and predicted winner

## Tech Stack
- Python
- Pandas
- Scikit-learn
- Streamlit
- Logistic Regression
- One-Hot Encoding

## Run locally

```bash
pip install -r requirements.txt
py -m streamlit run main.py
```

## Deployment

This project can be deployed as a free Render Web Service using the included `render.yaml`.
