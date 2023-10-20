import streamlit as st
import pandas as pd
import plotly.express as px

from src.map import create_map
from src.sdg_summary import sdg_barchart
from src.program_summary import program_barchart

st.set_page_config(layout="wide")
# px.set_mapbox_access_token(open("./secrets/mapbox-token.txt").read())
px.set_mapbox_access_token(st.secrets["map_box_token"])


main_file = pd.read_excel

column1, column2 = st.columns([1,3])

#--------------------------------------------------------
# Intro Column
#--------------------------------------------------------

with column1:

    st.title("Football SDG Impact Dashboard")

    st.write('''Football clubs, and their respective Club Community Organisations (CCOs) 
            work to improve their local communities. They focus on a number of key areas, 
            including improving access to education, creating opportunities for employment, 
            and promoting greater participation in physical activities.''')
            
    st.write('''Tom Woodhouse has collated information on 65 different EFL clubs. This
            pilot dashboard maps the focus of each club in terms of:''')

    st.write('''
            1. The focus of their portfolio of projects
            2. How the projects of each club align with the United Nation's Sustainable Development Goals (SDGs)
            ''')
    
    uploaded_file = st.file_uploader("Choose a file")


    # st.selectbox(label="Club", options=map_info.club_name_clean)
    #--------------------------------------------------------
    # Plotting Column
    #--------------------------------------------------------
    if uploaded_file is not None:


        map_info = pd.read_excel(uploaded_file, sheet_name="club_location_summary")

        map_fig = create_map(map_info)

        sdg_info = pd.read_excel(uploaded_file, sheet_name="sdg_counts")
        sdg_fig = sdg_barchart(sdg_info)

        programs_info = pd.read_excel(uploaded_file, sheet_name="programs_counts")
        program_fig=program_barchart(programs_info)

        with column2:

            tab1, tab2, tab3 = st.tabs(["Map", "SDGs", "Programs"])

            #--------------------------------------------------------
            # SDG Map
            #--------------------------------------------------------
            with tab1:
                st.plotly_chart(map_fig,use_container_width=True)

            #--------------------------------------------------------
            # SDG Barplot
            #--------------------------------------------------------
            with tab2:
                st.plotly_chart(sdg_fig,use_container_width=True)

            #--------------------------------------------------------
            # Program Barplot
            #--------------------------------------------------------

            with tab3:
                st.plotly_chart(program_fig,use_container_width=True)


