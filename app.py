import streamlit as st
import pandas as pd
import plotly.express as px

from src.map import create_map


st.set_page_config(layout="wide")
px.set_mapbox_access_token(open("./secrets/mapbox-token.txt").read())

#--------------------------------------------------------
# Prepping Map Data 
#--------------------------------------------------------

map_info = pd.read_csv("./data/geographical_information_summarised.csv")

map_info.fillna('NA', inplace=True)
map_info.rename(columns={"Programmes and Projects": "programmes_and_projects"}, inplace=True)

map_info["programmes_and_projects"] = map_info["programmes_and_projects"].str.replace(",", "<br>")
map_info["SDGs"] = map_info["SDGs"].str.replace(",", "<br>")

map_info["size"]= 8
map_info["color"] = "#001f3f"

map_fig = create_map(map_info)

#--------------------------------------------------------
# Prepping SDG Data
#--------------------------------------------------------

sdg_info = pd.read_csv("./data/sdgs.csv")

sdg_info["SDG16 Peaceful and Strong Institutions"]= sdg_info["SDG16 Peaceful and Strong Institutions"]+sdg_info["SDG16 Peaceful and Inclusive Societies"]
sdg_info.drop("SDG16 Peaceful and Inclusive Societies",axis=1,inplace=True)
sdg_info.loc[sdg_info["SDG16 Peaceful and Strong Institutions"]>1,"SDG16 Peaceful and Strong Institutions"] = 1



# subset=
sdg_sum = sdg_info.loc[:,sdg_info.columns!="club_name_clean"].sum(axis=0)
sdg_sum=pd.DataFrame({
    'SDG':sdg_sum.index,
    'Count':sdg_sum.to_list()
    })


sdg_fig = px.bar(sdg_sum, 
                 x='SDG', 
                 y='Count',
                 color_discrete_sequence =['#7FDBFF']*len(sdg_sum))
sdg_fig.update_xaxes(categoryorder='array', 
                 categoryarray= ['SDG1 No Poverty', 
                                                        'SDG2 Zero Hunger', 
                                                        "SDG3 Good Health and Wellbeing",
                                                        'SDG4 Quality Education', 
                                                        'SDG5 Gender Equality', 
                                                        'SDG8 Decent Work and Economic Growth', 
                                                        'SDG10 Reduced Inequalities', 
                                                        'SDG11 Sustainable Cities and Communities', 
                                                        'SDG13 Climate Action', 
                                                        'SDG16 Peaceful and Strong Institutions'],
                    tickangle=330)

#--------------------------------------------------------
# Prepping Programs Data
#--------------------------------------------------------

programs_info = pd.read_csv("./data/programs_and_projects.csv")
# subset=
programs_sum = programs_info.loc[:,programs_info.columns!="club_name_clean"].sum(axis=0)
programs_sum=pd.DataFrame({
    'Program':programs_sum.index,
    'Count':programs_sum.to_list()
    })

x_ticks_order = programs_sum["Program"].sort_values()
x_ticks_order = [x for x in x_ticks_order if x != "Other"] + ["Other"]


program_fig = px.bar(programs_sum, x='Program', y='Count')
program_fig.update_xaxes(tickangle=330,
    categoryorder='array', 
                 categoryarray= x_ticks_order)

#--------------------------------------------------------
# Building App
#--------------------------------------------------------
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
    
    # st.selectbox(label="Club", options=map_info.club_name_clean)

#--------------------------------------------------------
# Plotting Column
#--------------------------------------------------------

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


