from CHECK_CANDLESTICK_382 import check_candlestick_382

def check_morningStar_entry(all_data):

    check = 0

    if check_candlestick_382(all_data,1): #checks second candle stick
        check+=1

    if all_data['close'][-1] > all_data['open'][-1]: #checks engulfing
        if all_data['close'][-1] > all_data['open'][-2] or all_data['close'][-1] > all_data['close'][-2]:
            check+=1

    if all_data['close'][-3] < all_data['open'][-3]:
        check+=1

    halfway = (all_data['high'][-3] - all_data['low'][-3])/2 + all_data['low'][-3]

    if all_data['close'][-1] > halfway:
        check+=1

    if check == 4:
        return True
    else:
        return False
