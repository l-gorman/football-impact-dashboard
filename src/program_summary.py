import pandas as pd
import plotly.express as px

def program_barchart(programs_info):
    programs_info=programs_info.drop("Unnamed: 0", axis=1)
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
    
    return(program_fig)