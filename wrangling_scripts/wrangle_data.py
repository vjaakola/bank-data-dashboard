import pandas as pd
import plotly.graph_objs as go
from pandas_datareader import data, wb
import datetime
from datetime import datetime


"""Prepare Yahoo Finance bank data for a visualizaiton dashboard

    Args:
        dataset: Pandas data reader to open the data


    """    
    

def return_figures():
    """Creates four plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """

  # chart plots
 
    
    graph_one = []
    # Set up End and Start times for data grab
    end = datetime(2009,12,31)
    start = datetime(2008,9,1)

    # JPMorgan Chase & Co.
    JPM_08 = data.DataReader("JPM", 'yahoo', start, end)
    # iShares Latin America 40 ETF
    ILF_08 = data.DataReader("ILF", 'yahoo', start, end)
    # Deutsche Bank Aktiengesellschaft
    DB_08 = data.DataReader("DB", 'yahoo', start, end)
    # National Australia Bank Limited
    NABAX_08 = data.DataReader("NAB.AX", 'yahoo', start, end)
    # Bank of China Limited 
    BCL_08 = data.DataReader("3988.HK", 'yahoo', start, end)
    # Barclays Africa Group Limited
    AGRPY_08 = data.DataReader("AGRPY", 'yahoo', start, end)
    
    
    
    trace0 = go.Scatter(x=JPM_08.index, y=JPM_08['Adj Close'], name='JPM')
    trace1 = go.Scatter(x = ILF_08.index,y = ILF_08['Adj Close'], name='ILF')
    trace2 = go.Scatter(x = DB_08.index,y = DB_08['Adj Close'], name='DB')
    trace3 = go.Scatter(x = NABAX_08.index,y = NABAX_08['Adj Close'], name='NABAX')
    trace4 = go.Scatter(x = BCL_08.index,y = BCL_08['Adj Close'], name='BCL')
    trace5 = go.Scatter(x = AGRPY_08.index,y = AGRPY_08['Adj Close'], name='AGRPY')

    graph_one = [trace0, trace1,trace2, trace3, trace4, trace5]
    
    
    layout_one = dict(title = 'Adjusted Closing Price 2008 <br> The Great Recession',
                font=dict(size=10),
                yaxis = dict(title = 'Adjusted Closing Price'))


    graph_two = []

    # Set up End and Start times for data grab
    end = datetime.now()
    start = datetime(2019,1,1)

    # JPMorgan Chase & Co.
    JPM_20 = data.DataReader("JPM", 'yahoo', start, end)
    # iShares Latin America 40 ETF
    ILF_20 = data.DataReader("ILF", 'yahoo', start, end)
    # Deutsche Bank Aktiengesellschaft
    DB_20 = data.DataReader("DB", 'yahoo', start, end)
    # National Australia Bank Limited
    NABAX_20 = data.DataReader("NAB.AX", 'yahoo', start, end)
    # Bank of China Limited 
    BCL_20 = data.DataReader("3988.HK", 'yahoo', start, end)
    # Barclays Africa Group Limited
    AGRPY_20 = data.DataReader("AGRPY", 'yahoo', start, end)
    
    
    trace0 = go.Scatter(x=JPM_20.index, y=JPM_20['Adj Close'], name='JPM')
    trace1 = go.Scatter(x = ILF_20.index,y = ILF_20['Adj Close'], name='ILF')
    trace2 = go.Scatter(x = DB_20.index,y = DB_20['Adj Close'], name='DB')
    trace3 = go.Scatter(x = NABAX_20.index,y = NABAX_20['Adj Close'], name='NABAX')
    trace4 = go.Scatter(x = BCL_20.index,y = BCL_20['Adj Close'], name='BCL')
    trace5 = go.Scatter(x = AGRPY_20.index,y = AGRPY_20['Adj Close'], name='AGRPY')
    

    graph_two = [trace0, trace1,trace2, trace3, trace4, trace5]
    
    
    layout_two = dict(title = 'Adjusted Closing Price 2020 <br> Covid-19',
                font=dict(size=10),
                yaxis = dict(title = 'Adjusted Closing Price'))
    

    
    graph_three = []
    # Set up End and Start times for data grab
    end = datetime.now() 
    start = datetime(2008,9,1)
    
    JPM = data.DataReader("JPM", 'yahoo', start, end)
    DB = data.DataReader("DB", 'yahoo', start, end)
    
  
    trace0 = go.Scatter(x=JPM.index, y=JPM['Adj Close'], name='JPM')
    trace1 = go.Scatter(x = DB.index,y = DB['Adj Close'], name='DB')
    graph_three = [trace0, trace1]
                                                
    layout_three = dict(title = 'JPMorgan and Deutsche Bank Historical View <br> of the Adjusted Closing Price',
                font=dict(size=10),
                yaxis = dict(title = 'Adjusted Closing Price'))
    
    
    graph_four = []
    end = datetime.now()
    start = datetime(end.year - 1,end.month,end.day)
    
    # JPMorgan candlestick
    JPM = data.DataReader("JPM", 'yahoo', start, end)
    df = JPM[['Open', 'High', 'Low', 'Close']]
    df['Date']= df.index

    trace0 = go.Candlestick(x=df.index,open=df['Open'],high=df['High'],low=df['Low'],close=df['Close'],name = 'JPM')
    
    
    graph_four= [trace0]

    layout_four = dict(title= 'JPM and the Covid-19 Impact', 
                font=dict(size=10),
                yaxis = dict(title= 'Adjusted Closing Price'))
    
   

    graph_five = [trace1, trace2, trace3, trace4]
    layout_five = dict(title= 'JPM and the Great Recession 2020',              
                yaxis = dict(title= 'JPM Stock'))
  

    # append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))
    figures.append(dict(data=graph_three, layout=layout_three))
    figures.append(dict(data=graph_four, layout=layout_four))
   
 

    return figures
