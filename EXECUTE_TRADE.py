import WRITE_DATA
from binance.client import Client
import config
import numpy as np
from binance.enums import ORDER_TYPE_MARKET, SIDE_BUY, SIDE_SELL
from binance.client import Client
import config

#PORTFOLIO['Balance_1'] = ADA_BALANCE 
#PORTFOLIO['Balance_2'] = EUR_BALANCE 


def execute_buy(PORTFOLIO, TRADE_BOOK, all_data, TEST):

    print('Sending order - Buy')
    try:

        if TEST == False:
            client = Client(config.API_KEY, config.API_SECRET)
            order = client.create_order(symbol = PORTFOLIO['Stock'], 
                                                side = SIDE_BUY, 
                                                type = ORDER_TYPE_MARKET, 
                                                quantity = round(PORTFOLIO['Balance_2']/all_data['close'][-1]-0.01,2))
            print(order)

        PORTFOLIO['ACTIVE_TRADES'] += 1
        PORTFOLIO['BUY_HOLD'] = 1
        TRADE_BOOK['TIME'].append(all_data['date'][-1])
        TRADE_BOOK['BUY_PRICE'].append(all_data['close'][-1])
        #TRADE_BOOK['SELL_PRICE'].append(np.NaN)
        #TRADE_BOOK['GAIN'].append(np.NaN)

    except Exception as e:
        print("An exception has occured - {}".format(e))


def execute_sell(PORTFOLIO, TRADE_BOOK, all_data, TEST):
    
    print('Sending order - Sell')
    try:     
        if TEST == False:  
            client = Client(config.API_KEY, config.API_SECRET)
            order = client.create_order(symbol = PORTFOLIO['Stock'], 
                                                side = SIDE_SELL, 
                                                type = ORDER_TYPE_MARKET, 
                                                quantity = round(PORTFOLIO['Balance_1']-0.01,2))
            print(order)
        
    except Exception as e:
        print("An exception has occured - {}".format(e))

    TRADE_BOOK['SELL_PRICE'].append(all_data['close'][-1])
    gain = (all_data['close'][-1]/TRADE_BOOK['BUY_PRICE'][0]-1)*100-.18

    PORTFOLIO['ACTIVE_TRADES'] -= 1
    TRADE_BOOK['GAIN'] += gain

    if gain > 0:
        TRADE_BOOK['GOOD_TRD'] += 1
    TRADE_BOOK['TOTAL_TRD'] += 1
    #print(all_data['close'][-1])

    WRITE_DATA.write_sell(TRADE_BOOK)

    TRADE_BOOK['TIME'].pop(0)
    TRADE_BOOK['BUY_PRICE'].pop(0)
    TRADE_BOOK['SELL_PRICE'].pop(0)
    #TRADE_BOOK['GAIN'].pop(0)
        
   