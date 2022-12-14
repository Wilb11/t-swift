import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


st.title('Taylor Swift app overview')

st.markdown('## Welcome to ny')

# load df
df = pd.read_csv('clean_df.csv')

# st.dataframe(df)

####### plot 1

## show the amount of songs per album
# first need to make a df with one row per album containing the number of songs.
df_song_count = pd.DataFrame(df.album.value_counts().reset_index())
df_song_count.columns = ['album', 'Songs']
# df_song_count

# now plot
fig = px.bar(df_song_count, x="album", y="Songs", title="Number of songs per album", color='album', 
            template='plotly_white', 
            # color_discrete_sequence=color_purd, 
            # #orientation='h', 
            category_orders={ # replaces default order by column name
            "album": ["Taylor Swift", "Fearless", "Speak Now", "Red", "1989", "reputation", "Lover",
                      "folklore", "evermore"]},
            color_discrete_map={ # replaces default color mapping by value
                "Taylor Swift": "lightgrey",  "Fearless": "lightgrey", "Speak Now": "lightgrey", "1989": "lightgrey",  "Red": "maroon",
                 "Lover": "lightgrey", "reputation": "lightgrey", "folklore": "lightgrey", "evermore": "lightgrey",
            },
            width=900, height=450)

fig.update_layout( # customize font and legend orientation & position
    font_family="Rockwell",
    showlegend=False,
    # font_family="Courier New",
    font_color="#696969",
    # title_font_family="Times New Roman",
    title_font_color="#696969",
    # legend_title_font_color="green"
    # legend=dict(
    #     title=None, orientation="v", y=0.15, yanchor="bottom", x=1.2, xanchor="center"
    # )
)

fig.add_annotation( # add a text callout with arrow
    text="Red has the most songs!", x="Red", y=23, arrowhead=3, showarrow=True
)


# fig.write_html('./images/number_songs_per_album.html')
st.plotly_chart(fig, use_container_width=True)
