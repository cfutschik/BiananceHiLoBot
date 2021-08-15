from os import close
import talib,numpy,csv


def check_RSI(close_data):
    
    RSI = talib.RSI(numpy.array(close_data), timeperiod=14)
    
    weight = [.5,.25,.125,.125]
    RSI_score = 0

    for i in range(4):

        if RSI[-2-i] < 35:
            RSI_score+= 1*weight[i]

        elif RSI[-2-i] >= 35 and RSI[-2-i] < 50:
            RSI_score+= 0.5*weight[i]

    with open('dataFiles/RSI_data.csv', 'a', newline='') as f:
        data_writer = csv.writer(f, delimiter=',',quoting=csv.QUOTE_MINIMAL)
        data_writer.writerow([RSI[-1], RSI_score])

    return RSI_score
