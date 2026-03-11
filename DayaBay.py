import streamlit as st
import time

st.title("Click as fast as you can")

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

timer_placeholder = st.empty()
button_placeholder = st.empty()

if st.session_state.show_intro:
    st.write("Welcome to the Ultimate Clicking Challenge! 🖱️")
    st.write("Here’s how it works:")
    st.write("- You have 10 seconds to click the button as many times as possible.")
    st.write("- Each click adds 1 point to your score.")
    st.write("- Try to beat your own record or mine that is 73")
    st.write("Get ready to test your fingerzzz")
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
        st.success(f"Time's up. Your final score is: {st.session_state.score}")

if st.session_state.game_over:
    st.write(f"Your final score: {st.session_state.score}")
    if st.button("Play Again"):
        st.session_state.score = 0
        st.session_state.start_time = None
        st.session_state.game_over = False
        st.session_state.game_started = False
        st.session_state.show_intro = True