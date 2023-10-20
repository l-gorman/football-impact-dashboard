import pandas as pd
import plotly.express as px

def sdg_barchart(sdg_info):
    sdg_info=sdg_info.drop("Unnamed: 0", axis=1)

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
    
    return(sdg_fig)