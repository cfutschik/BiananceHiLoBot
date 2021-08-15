import os
import shutil
from BINANCE_BOT import binance_bot
import pandas as pd
import WRITE_DATA
import csv

MA_LONG = [40,45,50,55,60,65,70,75,80,85,90]
MA_SHRT = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]

data_set = 4 * 96

all_data = "testData/ETHEUR-15m-2021-08-11.csv"
all_ticker_data = pd.read_csv(all_data)

sets = int(len(all_ticker_data)/data_set)

for i in range(sets):

    raw_data = []

    if i == 0:
        x = data_set*i
        y = data_set*(i+1)
    else:
        x = data_set*i-90
        y = data_set*(i+1)

    while x < y:
        data = {'k': {
                    'o': all_ticker_data['o'][x],
                    'c': all_ticker_data['c'][x],
                    'h': all_ticker_data['h'][x],
                    'l': all_ticker_data['l'][x],
                    'x': all_ticker_data['x'][x],
                    'T': all_ticker_data['date'][x]
                    }}
        raw_data.append(data)
        x+=1

    if os.path.exists('dataFiles/ALL_TESTS.csv'):
        os.remove('dataFiles/ALL_TESTS.csv')

    for LMA in MA_LONG:
        for SMA in MA_SHRT:
            print('STARTING TEST - '+str(SMA*LMA)+' and '+str(LMA))
            if os.path.exists('dataFiles/candle_stick_data.csv'):
                os.remove('dataFiles/candle_stick_data.csv')
            
            if os.path.exists('dataFiles/TRADE_BOOK.txt'):
                os.remove('dataFiles/TRADE_BOOK.txt')
            
            if os.path.exists('dataFiles/TRADES.csv'):
                os.remove('dataFiles/TRADES.csv')

            shutil.copyfile("dataFiles/TRADE"+"_BOOK_.txt","dataFiles/TRADE_BOOK.txt")

            DATA_PERIOD = LMA
            SMA = LMA*SMA

            binance_bot(DATA_PERIOD, SMA, LMA, raw_data)

    test_data = pd.read_csv("dataFiles/ALL_TESTS.csv", header=None)
    test_data.columns = ["GAIN", "GOOD_TRD", "TOTAL_TRD", "rate", "SMA", "LMA"]
    
    gain_data = test_data.sort_values(by="GAIN",ascending=False).reset_index(drop=True).head(5)

    #print(gain_data)
    #print(gain_data.iloc[0]['GAIN'])

    with open('dataFiles/BEST_GAIN.csv', 'a', newline='') as f:
        data_writer = csv.writer(f, delimiter=',',quoting=csv.QUOTE_MINIMAL)
        data_writer.writerow(['Week: '+str(i)])
        for f in range(5):
            data_writer.writerow([gain_data.iloc[f]['GAIN'],
                                gain_data.iloc[f]['GOOD_TRD'],
                                gain_data.iloc[f]['TOTAL_TRD'],
                                gain_data.iloc[f]['rate'],
                                gain_data.iloc[f]['SMA'],
                                gain_data.iloc[f]['LMA']])


    rate_data = test_data.sort_values(by="rate",ascending=False).head(5)

    with open('dataFiles/BEST_RATIO.csv', 'a', newline='') as f:
        data_writer = csv.writer(f, delimiter=',',quoting=csv.QUOTE_MINIMAL)

        data_writer.writerow(['Week: '+str(i)])
        for f in range(5):
            data_writer.writerow([rate_data.iloc[f]['GAIN'],
                                rate_data.iloc[f]['GOOD_TRD'],
                                rate_data.iloc[f]['TOTAL_TRD'],
                                rate_data.iloc[f]['rate'],
                                rate_data.iloc[f]['SMA'],
                                rate_data.iloc[f]['LMA']])


    shutil.copyfile("dataFiles/ALL_TESTS.csv","dataFiles/ALL_TESTS_"+str(i)+".csv")

                # GAIN, GOOD_TRD, TOTAL_TRD, rate, SMA, LMA

