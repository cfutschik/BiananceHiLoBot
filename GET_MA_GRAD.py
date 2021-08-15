import numpy as np
from GET_MA import get_MA
#from GET_ATR import get_ATR

def get_ma_grad(all_data):

    ma_short, ma_long = get_MA(all_data['close'])
    ma_data = [ma_short, ma_long]
    x = [0, 25, 50]
    grad_factor = []

    for i in range(len(ma_data)):
        y = ma_data[i][-4:-1]
        pol = np.polyfit(x, y, 1)
        angle = np.rad2deg(np.arctan(pol[0]))
        grad_factor.append(angle/90)

    return grad_factor