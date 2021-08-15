def check_candleStick_pattern(all_data, offset):
    #print('flag 4')
    candle = 0
    # bull = 1
    # bear = -1
    
    open_now = all_data['open'][-2-offset]
    open_prev = all_data['open'][-3-offset]
    high_now = all_data['high'][-2-offset]
    high_prev = all_data['high'][-3-offset]
    low_now = all_data['low'][-2-offset]
    low_prev = all_data['low'][-3-offset]
    close_now = all_data['close'][-2-offset]
    close_prev = all_data['close'][-3-offset] 
    
    #Bullish Engulfing & above-below candle
    if open_prev > close_prev and close_now > open_now:
        if close_now > open_prev:
            candle = 1

    #Bearish Engulfing & above-below candle
    if open_prev < close_prev and close_now < open_now:
        if close_now < open_prev:
            candle = -1
    
    #Bullish 38.2 candles
    if close_now > open_now:
        upper_limit = float((high_now-low_now)*0.618+low_now)
        lower_limit = float((high_now-low_now)*0.382+low_now)
        if float(open_now) > upper_limit:
            candle = 1
        elif float(close_now) < lower_limit:
            candle = -1

    if close_now < open_now:
        upper_limit = float((high_now-low_now)*0.618+low_now)
        lower_limit = float((high_now-low_now)*0.382+low_now)
        if float(close_now) > upper_limit:
            candle = 1
        elif float(open_now) < lower_limit:
            candle = -1
 
    return candle