import yfinance as yf
import plotly.graph_objects as go

fig = go.Figure()

def draw_lines(stock_list):

    for tckr in stock_list:
        df = yf.download(tckr)
        fig.add_trace(go.Scatter(
        x=df.index,
        y=df['Adj Close'],
        name=tckr
        ))

    fig.update_layout(title=f"Price Movement Comparision between {stock_list}",
    legend_title_text='Stocks',
    xaxis_title='Date',
    yaxis_title='Price in INR',
    # plot_bgcolor='grey',
    # paper_bgcolor='grey'
    )

    fig.update_xaxes(showgrid=False,)
    fig.update_yaxes(showgrid=False)

    fig.show()

it_stock_list = ['TECHM.NS','WIPRO.NS','TCS.NS','INFY.NS','HCLTECH.NS','COFORGE.NS','LTI.NS']

draw_lines(['TECHM.NS','WIPRO.NS'])