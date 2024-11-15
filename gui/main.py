import streamlit as st


def setup():
    st.header("NAThacks24 Artists Interface")
    mode = st.selectbox(
        "Select Mode",
        ["Data Collection", "Data Analysis", "Data Visualization"],
    )
    filename = st.text_input("Enter File Name")

    if st.button("Enter"):
        st.session_state.mode = mode
        st.session_state.filename = filename
        st.rerun()


col_main = st.Page("collection/col_main.py", title="Data Collection")

collection_pages = [col_main]


if __name__ == "__main__":
    logo_path = "gui/images/logo.png"
    st.logo(logo_path)
    if "mode" in st.session_state:
        if st.session_state.mode == "Data Collection":
            pg = st.navigation()
        elif st.session_state.mode == "Data Analysis":
            st.write("Data Analysis Mode")
        elif st.session_state.mode == "Data Visualization":
            st.write("Data Visualization Mode")
    else:
        setup()
