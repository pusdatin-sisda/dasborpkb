############ 1. IMPORTING LIBRARIES ############
import streamlit as st
import pandas as pd
import numpy as np
from streamlit_tags import st_tags

############ 2. SETTING UP THE PAGE LAYOUT AND TITLE ############
st.set_page_config(
    layout="centered", page_title="Dasbor | Analisis Helpdesk", page_icon=""
)


############ SIDEBAR CONTENT ############

st.sidebar.write("")

st.sidebar.text_input(
    "Kata kunci",
    help="Masukan kata kunci yang umum ditemukan pada pesan di helpdesk",
    type="default",
)

st.sidebar.markdown("---")



############ TABBED NAVIGATION ############

# First, we're going to create a tabbed navigation for the app via st.tabs()
# tabInfo displays info about the app.
# tabMain displays the main app.

MainTab, InfoTab = st.tabs(["Main", "Info"])

with InfoTab:
    st.subheader("Tentang Dasbor")
    st.markdown(
        "Dasbor ini adalah ..."
    )

    st.subheader("Sumber Data")
    st.markdown(
        """
    - Post Message Help Desk
    - Pusdatin
    - dll
    """
    )

    st.subheader("Deploy")
    st.markdown(
        "Aplikasi inidideploy menggunakan Streamlit apps [Streamlit Community Cloud](https://streamlit.io/cloud) dengan beberapa klik"
    )


with MainTab:

    st.write("")
    st.markdown(
        """
    Tambahan kata kunci..

    """
    )

    st.write("")

    with st.form(key="my_form"):
        labels_from_st_tags = st_tags(
            value=["Transactional", "Informational", "Navigational"],
            maxtags=3,
            suggestions=["Transactional", "Informational", "Navigational"],
            label="",
        )

        submit_button = st.form_submit_button(label="Submit")

    if not submit_button:
        st.stop()
    elif submit_button and not labels_from_st_tags:
        st.warning("Silahkan tambah label")
        st.stop()
    elif submit_button and len(labels_from_st_tags) == 1:
        st.warning("Minimal 2 label")
        st.stop()
    elif submit_button:
        print(labels_from_st_tags)
        