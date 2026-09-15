import base64
import streamlit as st
import pickle
import pandas as pd
import time
import os

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(page_title="IPL Victory Predictor", layout="centered")

# ---------------- BACKGROUND IMAGE ---------------- #
@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_img_as_base64("background.jpg")

page_bg_img = f"""
<style>

[data-testid="stAppViewContainer"] {{
background-image: url("data:image/jpeg;base64,{img}");
background-size: cover;
background-position: center;
background-repeat: no-repeat;
background-attachment: fixed;
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

h1, h2, h3, h4, h5, h6 {{
color: white !important;
}}

div[data-testid="stWidgetLabel"] label,
label {{
color: white !important;
font-weight: 600;
}}

div[data-baseweb="select"] > div {{
background-color: white !important;
color: black !important;
}}

input {{
background-color: white !important;
color: black !important;
}}

div.stButton > button {{
background-color: white !important;
color: black !important;
border-radius: 12px;
padding: 10px 24px;
font-weight: bold;
border: none;
transition: 0.3s ease;
}}

div.stButton > button:hover {{
background-color: #f0f0f0 !important;
transform: scale(1.05);
}}

div[data-testid="stSpinner"] {{
color: white !important;
}}

</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

# ---------------- TITLE ---------------- #
st.markdown("<h1 style='text-align:center;'>🏏 IPL VICTORY PREDICTOR</h1>", unsafe_allow_html=True)

# ---------------- DATA ---------------- #
teams = ['--- select ---',
        'Gujarat Titans',
        'Sunrisers Hyderabad',
        'Chennai Super Kings',
        'Kings XI Punjab',
        'Rajasthan Royals',
        'Kolkata Knight Riders',
        'Delhi Capitals',
        'Royal Challengers Bangalore',
        'Lucknow Super Giants']

cities = ['Ahmedabad','Kolkata','Delhi','Dubai','Bangalore','Hyderabad',
          'Pune','Navi Mumbai','Abu Dhabi','Mumbai','Chandigarh','Lucknow',
          'East London','Centurion','Cape Town','Jaipur','Mohali','Chennai',
          'Cuttack','Visakhapatnam','Dharamsala','Raipur','Nagpur',
          'Johannesburg','Durban','Indore','Ranchi','Sharjah',
          'Bloemfontein','Bengaluru','New Chandigarh','Guwahati',
          'Port Elizabeth','Kimberley']

pipe = pickle.load(open('pipe.pkl','rb'))

# ---------------- TEAM NAME → LOGO FILE MAP ---------------- #
team_logo = {
    "Chennai Super Kings": "csk.png",
    "Royal Challengers Bangalore": "rcb.png",
    "Gujarat Titans": "gt.png",
    "Rajasthan Royals": "rr.png",
    "Lucknow Super Giants": "lsg.png",
    "Kings XI Punjab": "pbks.png",
    "Sunrisers Hyderabad": "srh.png",
    "Delhi Capitals": "dc.png",
    "Kolkata Knight Riders": "kkr.png"
}

# ---------------- INPUT SECTION ---------------- #
col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select Batting Team', teams)

with col2:
    if batting_team == '--- select ---':
        bowling_team = st.selectbox('Select Bowling Team', teams)
    else:
        filtered_teams = [team for team in teams if team != batting_team]
        bowling_team = st.selectbox('Select Bowling Team', filtered_teams)

selected_city = st.selectbox('Select Venue', cities)
target = st.number_input('Target')

col1, col2, col3 = st.columns(3)

with col1:
    score = st.number_input('Score')

with col2:
    overs = st.number_input('Over Completed')

with col3:
    wickets = st.number_input('Wickets Down')

# ---------------- PREDICTION ---------------- #
if st.button('Predict Winning Probability'):
    try:
        with st.spinner("Analyzing match situation..."):
            time.sleep(1.5)

            runs_left = target - score
            balls_left = 120 - (overs * 6)
            wickets_remaining = 10 - wickets
            crr = score / overs if overs != 0 else 0
            rrr = runs_left / (balls_left / 6) if balls_left != 0 else 0

            input_data = pd.DataFrame({
                'batting_team':[batting_team],
                'bowling_team':[bowling_team],
                'city':[selected_city],
                'runs_left':[runs_left],
                'balls_left':[balls_left],
                'wickets_remaining':[wickets_remaining],
                'total_runs':[target],
                'crr':[crr],
                'rrr':[rrr]
            })

            result = pipe.predict_proba(input_data)

            loss = result[0][0]
            win = result[0][1]

        # ---------------- RESULT DISPLAY ---------------- #
        st.markdown(
            "<h2 style='color:black;'>Winning Probability</h2>",
            unsafe_allow_html=True
        )

        col1, col2 = st.columns(2)

        with col1:
            st.markdown(f"### {batting_team}")
            bar1 = st.progress(0)
            for i in range(int(win * 100)):
                time.sleep(0.004)
                bar1.progress(i + 1)
            st.markdown(f"<h2 style='color:white;'>{round(win*100)}%</h2>", unsafe_allow_html=True)

        with col2:
            st.markdown(f"### {bowling_team}")
            bar2 = st.progress(0)
            for i in range(int(loss * 100)):
                time.sleep(0.004)
                bar2.progress(i + 1)
            st.markdown(f"<h2 style='color:white;'>{round(loss*100)}%</h2>", unsafe_allow_html=True)

        # ---------------- GLASS WINNER CARD WITH LOGO ---------------- #
        winner = batting_team if win > loss else bowling_team
        logo_file = team_logo.get(winner, "")

        if logo_file and os.path.exists(logo_file):
            logo_base64 = get_img_as_base64(logo_file)
            logo_html = f'<img src="data:image/png;base64,{logo_base64}" style="width:130px; margin-bottom:10px;">'
        else:
            logo_html = ""

        st.markdown(
            f"""
            <div style="
                background: rgba(255,255,255,0.15);
                backdrop-filter: blur(12px);
                padding: 20px;
                border-radius: 20px;
                text-align: center;
                margin-top: 30px;
                border: 1px solid rgba(255,255,255,0.3);
                width: 55%;
                margin-left: auto;
                margin-right: auto;
                box-shadow: 0px 8px 30px rgba(0,0,0,0.4);
            ">
                <h3 style='color:white;'>🏆 Predicted Winner</h3>
                {logo_html}
                <h1 style='color:white; margin-top:10px;'>{winner}</h1>
            </div>
            """,
            unsafe_allow_html=True
        )

    except:
        st.error("Some error occurred.. Please check your inputs !!")