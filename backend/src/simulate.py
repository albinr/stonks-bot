import pandas as pd

def sma_crossover(data: pd.DataFrame, short=10, long=50):
    data['SMA_short'] = data['Close'].rolling(window=short).mean()
    data['SMA_long'] = data['Close'].rolling(window=long).mean()
    data['Signal'] = 0
    data.loc[data['SMA_short'] > data['SMA_long'], 'Signal'] = 1
    data.loc[data['SMA_short'] <= data['SMA_long'], 'Signal'] = -1
    return data[['Date', 'Close', 'Signal']]
