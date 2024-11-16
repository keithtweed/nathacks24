import streamlit as st


def setup():
    """Define the initial setup page to collect required parameters"""
    st.header("NAThacks24 Artists Interface")
    mode = st.selectbox(
        "Select Mode",
        ["Collection", "Analysis", "Visualization"],
    )
    filename = st.text_input("Enter File Name")

    # Save the selected mode and filename to session state and rerun to load next page
    if st.button("Enter"):
        if len(filename) > 0:
            st.session_state.mode = mode
            st.session_state.filename = filename
            st.rerun()


col_main = st.Page("collection/col_main.py", title="Data Collection")

collection_pages = [col_main]
visualization_pages = []
analysis_pages = []


# Define modes
MODES = [None, "Collection", "Analysis", "Visualization"]

# Initialise available pages for mode
page_dict = {}

# Set the logo
logo_path = "gui/images/logo.png"
st.logo(logo_path)

# Initialise params
if "mode" not in st.session_state:
    st.session_state.mode = None
if "filename" not in st.session_state:
    st.session_state.filename = None

# Define available pages based on mode
if st.session_state.mode in ["Collection", "Debug"]:
    page_dict["Collection"] = collection_pages
elif st.session_state.mode in ["Analysis", "Debug"]:
    page_dict["Analysis"] = analysis_pages
elif st.session_state.mode in ["Visualization", "Debug"]:
    page_dict["Visualization"] = visualization_pages

# Populate nav or boot to setup
if len(page_dict) > 0:
    pg = st.navigation(page_dict)
    pg.run()
else:
    setup()
