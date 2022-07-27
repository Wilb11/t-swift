# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash #, dcc # html
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from bokeh.palettes import Category20b, Spectral, Plasma, Viridis, YlOrRd, PuOr, BuPu, BuGn, brewer, GnBu, PRGn, Inferno256, PuRd, RdPu, PiYG, RdYlGn, YlGnBu


app = Dash(__name__)

# make lists of colors to use for the color_disgrete_sequence argument in plot generators
color_purd = list(PuRd[9])
color_prgn = list(PRGn[9])
color_piyg = list(PiYG[9])
color_bupu = list(BuPu[9])

# create dict for easier color formatting
colors = {
    'background': '#111111',
    'text': 'orchid'
}

# load the cleaned df
df = pd.read_csv('clean_df.csv', index_col=0)
corr = df.corr()

# functions for creating graphs

# scatter per album
def create_plotly_scatter_by_album(df, x, y, hover_data, color, color_discrete_sequence, title, template, size, symbol, width, linecolor):
    fig = px.scatter(df, x=x, y=y, hover_data=hover_data, color=color, opacity=0.8, 
                    color_discrete_sequence=color_discrete_sequence, title=title, template=template)
    # update default marker size and symbol
    fig.update_traces(marker=dict(size=size, symbol=symbol,
                                line=dict(width=width,
                                            color=linecolor)),
                                selector=dict(mode='markers'))

    return(fig)


# markdown text
markdown_text = '''
### Dash and Markdown

Dash apps can be written in Markdown.
Dash uses the [CommonMark](http://commonmark.org/)
specification of Markdown.
Check out their [60 Second Markdown Tutorial](http://commonmark.org/help/)
if this is your first introduction to Markdown!
'''

# create figures here or within the layout
fig = px.imshow(corr, text_auto=".2f", color_continuous_scale='PuRd', width=700, height=700, title='Correlation between song features')
fig.update_xaxes(side="top", tickangle=30)

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

# return the layour
app.layout = html.Div(children=[
    html.H1(
        children='Hello Dash',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }),

    dcc.Markdown(children=markdown_text),

    html.Div(children='Dash: A web application framework for your data.',
    style={'textAlign': 'center',
        'color': colors['text']}),

    html.H2(children='hi'),

    dcc.Graph(
        id='example-graph',
        figure=create_plotly_scatter_by_album(df, "album", "popularity", ['name'], 'album', color_purd, 'Popularity of songs', 'plotly_white', 15, 'diamond', 1, 'DarkSlateGrey')

    ),

    dcc.Graph(
        id='test-graph',
        figure=fig
    ),

    dcc.Markdown(children='''
                # Hey
                # hi
                *what up*
                # '''),

    dcc.Graph(
    id='hi',
    figure=px.imshow(corr, text_auto=".2f", color_continuous_scale='PuRd', width=700, height=700, title='hi')
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
