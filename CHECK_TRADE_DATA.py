import os
import csv
from typing import Text
import numpy as np
import pandas as pd

def check_trade_book():

    TRADE_BOOK = []

    if os.path.exists('dataFiles/TRADE_BOOK.csv'):

        with open('dataFiles/TRADE_BOOK.csv', 'r') as f:
            data = csv.reader(f)

            for line in data:
                array = np.array(line)
                TRADE_BOOK.append(array.astype(np.float64))

        return TRADE_BOOK    

    else:
        return TRADE_BOOK


def update_trade_data(TRADE_BOOK):
    with open('dataFiles/TRADES_BOOK.csv', 'w', newline='') as f:
        data_writer = csv.writer(f, delimiter=',',quoting=csv.QUOTE_MINIMAL)

        for line in TRADE_BOOK:

            data_writer.writerow(line)



TRADE = check_trade_book()

del TRADE[0]

update_trade_data(TRADE)
