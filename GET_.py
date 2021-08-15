import pandas as pd
import numpy as np
import talib

def ATR(all_closes,all_highs,all_lows,dataperiod):
    
    np_closes = np.array(all_closes)
    np_highs = np.array(all_highs)
    np_lows = np.array(all_lows)
    ATR = talib.ATR(np_highs, np_lows, np_closes, timeperiod=dataperiod)

    return ATR

def data():

    #df = pd.read_csv("Bitfinex_ETHUSD_minute.csv") #Length = 307957
    df = pd.read_csv("Bitfinex_ETHUSD_1h.csv") #LEn = 27235
    #df = pd.read_csv("Bitfinex_ETHUSD_d.csv")
    #print(len(df))
    df['date'] = pd.to_datetime(df['date']) #date corrector

    #df.drop(df.tail(307957).index, inplace=True) #minute
    #df.drop(df.tail(290957).index, inplace=True)
    
    #df.drop(df.tail(27235).index, inplace=True) #hr
    df.drop(df.tail(23235).index, inplace=True)
    
    
    df = df.iloc[::-1] #inverting data
    df.reset_index(drop=True, inplace=True)

    return df

def ma_grad(all_closes,all_highs,all_lows,dataperiod):
    
    ATR = ATR(all_closes,all_highs,all_lows,dataperiod)

    avg_ATR = sum(ATR[-50:])/len(ATR[-50:])

    ma_short, ma_long = MA(all_closes)
    ma_data = [ma_short, ma_long]
    x = [0, avg_ATR, 2*avg_ATR]
    grad_factor = []

    for i in range(len(ma_data)):
        y = ma_data[i][-4:-1]
        pol = np.polyfit(x, y, 1)
        angle = np.rad2deg(np.arctan(pol[0]))
        grad_factor.append(angle/90)

    return grad_factor

def grad(all_closes,all_highs,all_lows,dataperiod):

    ATR = get_ATR(all_closes,all_highs,all_lows,dataperiod)

    avg_ATR = sum(ATR[-50:])/len(ATR[-50:])

    ma_short, ma_long = get_MA(all_closes)
    ma_data = [ma_short, ma_long]
    x = [0, avg_ATR, 2*avg_ATR]
    grad_factor = []

    for i in range(len(ma_data)):
        y = ma_data[i][-4:-1]
        pol = np.polyfit(x, y, 1)
        angle = np.rad2deg(np.arctan(pol[0]))
        grad_factor.append(angle/90)

    return grad_factor

def MA(all_closes):

    np_closes = np.array(all_closes)
    ALL_SHORT_MA = talib.MA(np_closes, timeperiod=20, matype=0)
    ALL_LONG_MA = talib.MA(np_closes, timeperiod=50, matype=0)

    SHORT_MA = []
    LONG_MA =[]

    for x in ALL_SHORT_MA[-20:]:
        SHORT_MA.append(x)

    for x in ALL_LONG_MA[-50:]:
        LONG_MA.append(x)

    return SHORT_MA, LONG_MA

def trend(all_closes):
    
    # Uses both 20 and 50 MAV to caculate Up or Down trend

    SHORT_MA, LONG_MA = get_MA(all_closes)

    period = [0,1]
    #data_length = [short_period, long_period]
    data_length = [5,5]
    trend_data = [SHORT_MA, LONG_MA]
    trends = []

    for x in period:
        count = 0  
        trend_value = 0
        while count < data_length[x]:
            value = count - data_length[x]
            trend = all_closes[value]/trend_data[x][value]

            if trend > 1:
                trend_value+=(trend-1)
            elif trend <= 1:
                trend_value-=trend
            
            count+=1

        #print(trend_value)

        if trend_value > 0:
            # Up trend
            trends.append(1)
        elif trend_value < 0:
            # Down trend
            trends.append(-1)
        else:
            # No trend
            trends.append(0)

    return trends