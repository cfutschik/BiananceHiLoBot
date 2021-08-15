import numpy, talib

def get_MA(all_closes, SMA, LMA):

    np_closes = numpy.array(all_closes)
    ALL_SMA = talib.MA(np_closes, timeperiod=SMA)
    ALL_LMA = talib.MA(np_closes, timeperiod=LMA)

    MA_SMA = []
    MA_LMA = []

    for x in ALL_SMA[-20:]:
        MA_SMA.append(x)

    for x in ALL_LMA[-20:]:
        MA_LMA.append(x)

    return MA_SMA, MA_LMA