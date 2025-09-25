#Jenna Tran | GTID# 904121767 | WebDevLab Phase II - Section D

import streamlit as st
import info2

#cd OneDrive/Documents/cs1301/WebDevLab01
#streamlit run Buzzfeed_Quiz.py

#Intro
st.title("⛱️ Which *The Summer I Turned Pretty* Character Are You?")
st.image(info2.intro_pic, width = 1000)
st.write("Answer a few personality questions to find your Cousins Beach twin!")

#Sidebar Links
def side_section():
    st.sidebar.header("Characters")
    st.sidebar.write("**Belly**")
    st.sidebar.image(info2.belly_pic, width = 300)
    st.sidebar.write("**Conrad**")
    st.sidebar.image(info2.conrad_pic, width = 300)
    st.sidebar.write("**Jeremiah**")
    st.sidebar.image(info2.jeremiah_pic, width = 300)
    st.sidebar.write("**Steven**")
    st.sidebar.image(info2.steven_pic, width = 300)
    st.sidebar.write("**Taylor**")
    st.sidebar.image(info2.taylor_pic, width = 300)
    st.sidebar.write("**Laurel**")
    st.sidebar.image(info2.laurel_pic, width = 300)
side_section()

#Quiz logistics
if "submitted" not in st.session_state:
    st.session_state.submitted = False
if "scores" not in st.session_state:
    st.session_state.scores = {k: 0 for k in info2.Character_Options}

#Question 1
st.header("Q1: Your ideal beach day? 🌞")
#NEW (radio selection)
q1 = st.radio(  
    "Pick one:",
    ["Quiet sunrise by the water", "Competitive beach volleyball with friends", "Long swim, just thinking", "Boardwalk snacks + photos + shopping", "Family cookout!"],
    index=None,
)
if q1:
    info2.score_q1(q1, st.session_state.scores)

#Question 2
st.header("Q2: What’s your go-to summer music? ♫")
#NEW (drop-down select)
q2 = st.selectbox(  
    "Choose a vibe",
    ("Indie", "Pop", "Rock", "R&B", "Acoustic",),
    index=None,
)
if q2:
    info2.score_q2(q2, st.session_state.scores)

#Question 3
st.header("Q3: Spontaneity slider 🤩")
#NEW (value/number slider)
q3 = st.slider(  
    "How likely are you to say yes to last‑minute plans?",
    min_value=0,
    max_value=10,
    value=5,
)
info2.score_q3(q3, st.session_state.scores)

#Question 4
st.header("Q4: Pick your must‑have summer activities 🌊")
#NEW (drop-down multiselect)
q4 = st.multiselect(
    "Select all that fit:",
    ["Bonfire storytelling", "Night swim", "Beach volleyball league", "Photo walk for the aesthetic", "Cooking for everyone", "Solo journaling"],
)
if q4:
    info2.score_q4(q4, st.session_state.scores) 

#Question 5
st.header("Q5: How loyal are you to your people? 🫂")
#NEW (value/number input)
q5 = st.number_input(
    "Type a number from 0–10:",
    min_value=0,
    max_value=10,
    value=8,
    step=1,
)
info2.score_q5(q5, st.session_state.scores)

#Submitting & Results
st.write('---')
if st.button("✨ Get My Result"):
    st.session_state.submitted = True

if st.session_state.submitted:
    result_key = max(st.session_state.scores, key=st.session_state.scores.get)
    result = info2.Results[result_key]

    st.success(f"🎉 You are **{result['name']}**!")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(result["image"], width=260)
    with col2:
        st.write(result["description"])

    with st.expander("See how your match breaks down:"):
        total = sum(st.session_state.scores.values())
        if total > 0:
            breakdown = sorted(st.session_state.scores.items(), key=lambda x: x[1], reverse=True)
            for name, score in breakdown:
                pct = int(round((score / total) * 100))
                st.write(f"{name}: {pct}%")
                st.progress(pct)

    if st.button("Restart Quiz"):
        st.session_state.submitted = False
        st.session_state.scores = {k: 0 for k in info2.Character_Options}
        st.rerun()
