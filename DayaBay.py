import streamlit as st
import time

st.set_page_config(page_title="Clicking Game", page_icon="🎯")

TIME_LIMIT = 10

if "score" not in st.session_state:
    st.session_state.score = 0
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "game_over" not in st.session_state:
    st.session_state.game_over = False
if "game_started" not in st.session_state:
    st.session_state.game_started = False
if "show_intro" not in st.session_state:
    st.session_state.show_intro = True

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Game", "About"])

if page == "About":
    st.header("About This Clicking Game")
    st.write("**What the app does:** Tests your reaction speed by having you click a button as many times as possible within 10 seconds.")
    st.write("**Target user:** Anyone who wants a fun, fast-paced game to test their clicking speed.")
    st.write("**Inputs collected:** Clicking the button.")
    st.write("**Outputs shown:** Final score, time remaining, visual effects (the balloons).")
    st.write("**UI Components used:** Buttons, sliders, text inputs, columns, sidebar, balloons, headers, subheaders, etc.")

elif page == "Game":
    st.title("Click as fast as you can")
    
    timer_placeholder = st.empty()
    button_placeholder = st.empty()
    
    if st.session_state.show_intro:
        st.write("Welcome to a Clicking Test")
        st.write("Here’s how it works:")
        st.write("- You have 10 seconds to click the button as many times as possible.")
        st.write("- Each click adds 1 point to your score.")
        st.write("- Try to beat your own record or mine which is 98")
        if st.button("Start Game"):
            st.session_state.start_time = time.time()
            st.session_state.game_started = True
            st.session_state.show_intro = False

    if st.session_state.game_started and not st.session_state.game_over:
        elapsed_time = time.time() - st.session_state.start_time
        time_left = max(0, int(TIME_LIMIT - elapsed_time))
        timer_placeholder.text(f"Time left: {time_left}s")
        
        if button_placeholder.button("CLICK ME"):
            st.session_state.score += 1

        if elapsed_time >= TIME_LIMIT:
            st.session_state.game_over = True
            st.success(f"Time is up. Your final score is: {st.session_state.score}")
            st.balloons()

    if st.session_state.game_over:
        st.subheader("Summary")
        st.write(f"Your final score: {st.session_state.score}")
        st.slider("How much did you enjoy this game?", 0, 10, 5)
        st.text_area("Optional feedback")
        if st.button("Play Again"):
            st.session_state.score = 0
            st.session_state.start_time = None
            st.session_state.game_over = False
            st.session_state.game_started = False
            st.session_state.show_intro = True