import streamlit as st
import time

st.title("Click as fast as you can!")
st.write("Click that button as fast as you possibly can gang")

if 'score' not in st.session_state:
    st.session_state.score = 0
    TIME_LIMIT = 10
    elapsed_time = time.time() - st.session_start_time

    if not st.session_state.game_over:
        st.write(f"time left:  {max(0,int(TIME_LIMIT - elapsed_time))}s")

        if st.button("CLICK ME"):
            st.session_state.score += 1

            if elapsed_time >= TIME_LIMIT:
                st.session_state.game_over = True
                st.success(f"Time's up. Your Final Score is: {st.session_state.score}")

                if st.button("Play Again"):
                    st.session_state.score = 0
                    st.session_state.start_time - time.time()
                    st.session_state.game_over = False