import csv

def write_sell(TRADE_BOOK):
    with open('dataFiles/TRADES.csv', 'a', newline='') as f:
        data_writer = csv.writer(f, delimiter=',',quoting=csv.QUOTE_MINIMAL)

        data_writer.writerow([TRADE_BOOK['TIME'][0],
                              TRADE_BOOK['BUY_PRICE'][0],
                              TRADE_BOOK['SELL_PRICE'][0],
                              TRADE_BOOK['GAIN']])


def write_candlestick_data(all_data):
    
    with open('dataFiles/candle_stick_data.csv', 'a', newline='') as f:
        data_writer = csv.writer(f, delimiter=',',quoting=csv.QUOTE_MINIMAL)

        data_writer.writerow([all_data['date'][-1],
                            all_data['high'][-1], 
                            all_data['low'][-1],
                            all_data['open'][-1], 
                            all_data['close'][-1],
                            all_data['20_MA'][-1]])

def write_all_tests(TRADE_BOOK, SMA, LMA):

    with open('dataFiles/ALL_TESTS.csv', 'a', newline='') as f:
        data_writer = csv.writer(f, delimiter=',',quoting=csv.QUOTE_MINIMAL)

        if TRADE_BOOK['TOTAL_TRD'] == 0:
            rate = 0
        else:
            rate = round(TRADE_BOOK['GOOD_TRD']/TRADE_BOOK['TOTAL_TRD']*100,2)

        data_writer.writerow([TRADE_BOOK['GAIN'],
                              TRADE_BOOK['GOOD_TRD'],
                              TRADE_BOOK['TOTAL_TRD'],
                              rate,
                              SMA,
                              LMA])

            



