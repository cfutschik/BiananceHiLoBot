def check_engulf_entry(all_data):
    
    open_now = all_data['open'][-1]
    open_prev = all_data['open'][-2]
    high_prev = all_data['high'][-2]
    close_now = all_data['close'][-1]
    close_prev = all_data['close'][-2] 

    entry_quality = 0

    #Bullish Engulfing & above-below candle
    if open_prev > close_prev and close_now > open_now:
        # Checking close above
        if close_now > open_prev:
            return True

        else:
            return False

