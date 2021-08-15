import numpy as np
from GET_MA import get_MA
from WRITE_DATA import write_candlestick_data

def get_data(all_data, raw_data, PORTFOLIO, DATA_PERIOD):

    if raw_data['k']['x']:

        if len(all_data['close']) < DATA_PERIOD:
            #print('Getting data: '+str(len(all_data['date'])))
            all_data['open'].append(np.float64(raw_data['k']['o']))
            all_data['close'].append(np.float64(raw_data['k']['c']))
            all_data['high'].append(np.float64(raw_data['k']['h']))
            all_data['low'].append(np.float64(raw_data['k']['l']))
            all_data['date'].append(raw_data['k']['T'])
            all_data['20_MA'].append(np.NaN)
            #all_data['50_MA'].append(np.NaN)

        if len(all_data['close']) == DATA_PERIOD:

            all_data['open'].pop(0)
            all_data['close'].pop(0)
            all_data['high'].pop(0)
            all_data['low'].pop(0)
            all_data['date'].pop(0)  
            all_data['20_MA'].pop(0)
            #all_data['50_MA'].pop(0)
            
            all_data['open'].append(np.float64(raw_data['k']['o']))
            all_data['close'].append(np.float64(raw_data['k']['c']))
            all_data['high'].append(np.float64(raw_data['k']['h']))
            all_data['low'].append(np.float64(raw_data['k']['l']))
            all_data['date'].append(raw_data['k']['T'])
            
            #ma_20, lma = get_MA(all_data['close'])
            all_data['20_MA'].append(np.nan)
            #all_data['50_MA'].append(ma_50[-1])

        write_candlestick_data(all_data)
        PORTFOLIO['BUY_HOLD'] = 0


    return all_data