import csv
from GET_TREND import get_trend

def check_ma_trend(close_data):

    trend = get_trend(close_data)

    trend_score = 0
    #1 postive
    #2 semi postive
    #3 20 above 50
    x = 3
    if x == 1: 
        # positive
        if trend[0] == 1 and trend[1] == 1:
            trend_score = 1
        elif trend[0] == 1 or trend[1] == 1:
            trend_score = 0.5

    if x == 2:
        # semi positive
        if trend[0] == 1 and trend[1] == 1:
            trend_score = 0.5
        elif trend[0] == 0 and trend[1] == 1:
            trend_score = 1
        elif trend[1] == 0:
            trend_score = 0

    with open('dataFiles/ma_trend_data.csv', 'a', newline='') as f:
        data_writer = csv.writer(f, delimiter=',',quoting=csv.QUOTE_MINIMAL)
        data_writer.writerow([trend[0], trend[1], trend_score])

    return trend_score