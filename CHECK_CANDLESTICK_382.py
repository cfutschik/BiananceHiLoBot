def check_candlestick_382(candle_data, offset):

    open = candle_data['open'][-1-offset] 
    close = candle_data['close'][-1-offset] 
    high = candle_data['high'][-1-offset] 
    low = candle_data['close'][-1-offset] 
    
    if close > open:
        upper_limit = float((high-low)*0.618+low)
        lower_limit = float((high-low)*0.382+low)
        if float(open) > upper_limit:
            return 1
        elif float(close) < lower_limit:
            return -1

    if close < open:
        upper_limit = float((high-low)*0.618+low)
        lower_limit = float((high-low)*0.382+low)
        if float(close) > upper_limit:
            return 1
        elif float(open) < lower_limit:
            return -1