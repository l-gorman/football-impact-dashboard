import pandas as pd
import plotly.express as px

def create_map(data):
    fig = px.scatter_mapbox(data, 
                        lat="lat", 
                        lon="lon", 
                        size="size",
                        color_discrete_sequence=[data.color],
                        hover_name="club_name_clean",
                        hover_data={  
                                    "lat":False, 
                                    "lon":False,
                                    "SDGs": True,
                                    "size":False,
                                    "color":False,
                                    "programmes_and_projects":True
                                    },
                        height=700,
                        width=1000,
                        zoom=6,
                        size_max=15,
                        custom_data=['club_name_clean','SDGs','programmes_and_projects']
                        )

    fig.update_traces(hovertemplate="<br>".join([
            "<b> %{customdata[0]}</b>",
            "",
            "<b>SDGs</b>",
            " %{customdata[1]}",
            "",
            "<b>Programs and Projects</b>",
            " %{customdata[2]}"

        ]))


    fig.update_layout(mapbox_style="carto-positron")

    return(fig)