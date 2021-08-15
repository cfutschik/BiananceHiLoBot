import os
import numpy as np
import pandas as pd
import csv

def check_all_data(DATA_PERIOD):

    all_data = {
    'open': [],
    'close': [],
    'high': [],
    'low': [],
    'date': [],
    '20_MA': []
    }

    if os.path.exists('dataFiles/candle_stick_data.csv'):

        try:
            previous_data = []

            with open('dataFiles/candle_stick_data.csv', 'r', newline='') as f:
                csv_reader = csv.reader(f, delimiter=',',quoting=csv.QUOTE_MINIMAL)

                for row in csv_reader:
                    row = np.array(row).astype(np.float64)
                    previous_data.append(row)

            if len(previous_data) > DATA_PERIOD:
                load_length = DATA_PERIOD
            else:
                load_length = len(previous_data)

            for i in reversed(range(1,load_length+1)):

                # ['date', 'high', 'low', 'open', 'close', '20_MA']
                #print(-i)
                #print(previous_data[-i])
                all_data['date'].append(previous_data[-i][0])
                all_data['high'].append(previous_data[-i][1])
                all_data['low'].append(previous_data[-i][2])
                all_data['open'].append(previous_data[-i][3])
                all_data['close'].append(previous_data[-i][4])
                all_data['20_MA'].append(previous_data[-i][5])

            print("Data imported from previous data set.")

            return all_data
        except:
            print("Data could not be imported from previous data set.")

    else:
        return all_data