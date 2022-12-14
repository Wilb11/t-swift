import streamlit as st
import pandas as pd
import plotly.express as px
from bokeh.palettes import Category20b, Spectral, Plasma, Viridis, YlOrRd, PuOr, BuPu, BuGn, brewer, GnBu, PRGn, Inferno256, PuRd, RdPu, PiYG, RdYlGn, YlGnBu, Reds, Purples
import datetime

#### 1st step always: make layout wider #####
st.set_page_config(layout="wide", page_title="T-Swift")

st.title('Taylor Swift song analysis')

# load df
df = pd.read_csv('clean_df.csv')

# make lists of colors to use for the color_disgrete_sequence argument
color_purd = list(PuRd[9])
color_prgn = list(PRGn[9])
color_piyg = list(PiYG[9])
color_bupu = list(BuPu[9])


## get list of attributes
attributes = list(df.columns)
attributes.remove('name')
attributes.remove('album')
attributes.remove('release_date')
attributes.remove('loudness')
attributes.remove('instrumentalness')



## make list of markers
marker_list = ["diamond","circle" , "square" ,  "cross" , "pentagon" , "hexagram" , \
               "star" ," diamond" , "hourglass" , "bowtie"]

# function to make a scatterplot in plotly express
def create_plotly_scatter_by_album(df, x, y, hover_data, color, color_discrete_sequence, title, template, size, symbol, width, linecolor):
    fig = px.scatter(df, x=x, y=y, hover_data=hover_data, color=color, opacity=0.8, 
                    color_discrete_sequence=color_discrete_sequence, title=title, template=template)
    # update default marker size and symbol
    fig.update_traces(marker=dict(size=size, symbol=symbol,
                                line=dict(width=width,
                                            color=linecolor)),
                                selector=dict(mode='markers'))

    fig.update_yaxes(rangemode= 'nonnegative',
                        title_font = dict(size=16),
                        tickfont=dict(size=15))
    fig.update_yaxes(showgrid=False,
        gridcolor='grey',
                      range=[0, df[y].max()*1.1]) 
    fig.update_xaxes(showgrid=True,
        gridcolor='maroon',
                        title_font = dict(size=16),
                        tickfont=dict(size=15))
    # st.markdown(f'{df[y].max()}')
    st.plotly_chart(fig, use_container_width=True)
    

st.markdown('### Choose a feature to create an album overview for!')

col1, col2 = st.columns(2)

with col1:
    scatter_option = st.selectbox(
            "What attribute do you want to view?",
            attributes
            # ("popularity", "acousticness", "length", "energy", "danceability")
    )
with col2:
    marker_option = st.selectbox(
            "What marker do you want to use?",
            marker_list
    ) 

create_plotly_scatter_by_album(df, "album", scatter_option, ['name'], 'album', color_purd, f'{scatter_option} of songs per album', 'plotly_white', 15, marker_option, 1, 'DarkSlateGrey')



st.markdown('### Choose two features to create an album scatterplot for!')

    
# function to show scatterplot of 2 features, using different shapes based on album
def create_plotly_scatter_two_columns(df, x, y, hover_data, color, color_discrete_sequence, title, template, size, width, linecolor):
    fig = px.scatter(df, x=x, y=y, hover_data=['name'], color='album',
                    title=title, color_discrete_sequence=color_discrete_sequence,
                    template=template, opacity=0.7, symbol="album") #, size="energy")

    fig.update_traces(marker=dict(size=size,  #symbol='diamond',
                                    line=dict(width=width,
                                                color=linecolor)),
                                    selector=dict(mode='markers'))
    fig.update_yaxes(rangemode= 'nonnegative',
                        title_font = dict(size=16),
                        tickfont=dict(size=15))
    fig.update_yaxes(showgrid=True,
        gridcolor='maroon')
                    #   range=[0, df[y].max()*1.1]) 
    fig.update_xaxes(showgrid=True,
        gridcolor='maroon',
                        title_font = dict(size=16),
                        tickfont=dict(size=15))
    # save the plot as an html
    # fig.write_html('./images/'+title+'.html')
    st.plotly_chart(fig, use_container_width=True)
    
col1, col2 = st.columns(2)

with col1:
    scatter1 = st.selectbox(
            "What 1st attribute do you want to view?",
            attributes,
            index=0
    )
with col2:
    scatter2 = st.selectbox(
            "What 2nd attribute do you want to view?",
            attributes,
            index=1
    ) 


# energy and danceability
create_plotly_scatter_two_columns(df, scatter1, scatter2, ['name'], 'album', color_purd, f'{scatter1} versus {scatter2}', 'plotly_dark', 15, 0.5, 'white')


# # popularity scatter
# create_plotly_scatter_by_album(df, "album", "popularity", ['name'], 'album', color_purd, 'Popularity of songs', 'plotly_white', 15, 'diamond', 1, 'DarkSlateGrey')

# # acousticness scatter
# create_plotly_scatter_by_album(df, "album", "acousticness", ['name'], 'album', color_purd, 'Acousticness of songs', 'plotly_white', 15, 'star', 1, 'DarkSlateGrey')


####### plot 1

# ## show the amount of songs per album
# # first need to make a df with one row per album containing the number of songs.
# df_song_count = pd.DataFrame(df.album.value_counts().reset_index())
# df_song_count.columns = ['album', 'Songs']
# # df_song_count

# # now plot
# fig = px.bar(df_song_count, x="album", y="Songs", title="Number of songs per album", color='album', 
#             template='plotly_white', 
#             # color_discrete_sequence=color_purd, 
#             # #orientation='h', 
#             category_orders={ # replaces default order by column name
#             "album": ["Taylor Swift", "Fearless", "Speak Now", "Red", "1989", "reputation", "Lover",
#                       "folklore", "evermore"]},
#             color_discrete_map={ # replaces default color mapping by value
#                 "Taylor Swift": "lightgrey",  "Fearless": "lightgrey", "Speak Now": "lightgrey", "1989": "lightgrey",  "Red": "maroon",
#                  "Lover": "lightgrey", "reputation": "lightgrey", "folklore": "lightgrey", "evermore": "lightgrey",
#             },
#             width=900, height=450)

# fig.update_layout( # customize font and legend orientation & position
#     font_family="Rockwell",
#     showlegend=False,
#     # font_family="Courier New",
#     font_color="#696969",
#     # title_font_family="Times New Roman",
#     title_font_color="#696969",
#     # legend_title_font_color="green"
#     # legend=dict(
#     #     title=None, orientation="v", y=0.15, yanchor="bottom", x=1.2, xanchor="center"
#     # )
# )

# fig.add_annotation( # add a text callout with arrow
#     text="Red has the most songs!", x="Red", y=23, arrowhead=3, showarrow=True
# )


# # fig.write_html('./images/number_songs_per_album.html')
# st.plotly_chart(fig, use_container_width=True)
