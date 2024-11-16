import streamlit as st

st.header("Data Collection")

st.write("This is the data collection page.")

st.write("Current session: " + st.session_state.filename)

if "runstate" not in st.session_state:
    st.session_state.runstate = "Stopped"

if st.session_state.runstate == "Stopped":
    if st.button("Start"):
        st.session_state.runstate = "Running"
        st.rerun()
elif st.session_state.runstate == "Running":
    if st.button("Stop"):
        st.session_state.runstate = "Stopped"
        st.rerun()
    if st.button("Pause"):
        st.session_state.runstate = "Paused"
        st.rerun()
elif st.session_state.runstate == "Paused":
    if st.button("Stop"):
        st.session_state.runstate = "Stopped"
        st.rerun()
    if st.button("Resume"):
        st.session_state.runstate = "Running"
        st.rerun()
