import talib, numpy

def get_ATR(all_data,dataperiod):
    
    np_closes = numpy.array(all_data['close'])
    np_highs = numpy.array(all_data['high'])
    np_lows = numpy.array(all_data['low'])
    ATR = talib.ATR(np_highs, np_lows, np_closes, timeperiod=dataperiod)

    return ATR[-1]