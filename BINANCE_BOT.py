# General Functions
import websocket, json, config
from binance.client import Client
from binance.enums import *
from datetime import datetime
from MAIN_BOT import main_bot
from PORTFOLIO_DATA import import_trade_portfolio
from TRADE_BOOK_DATA import import_trade_book
from CHECK_ALL_DATA import check_all_data
from GET_MA import get_MA
import WRITE_DATA

def binance_bot(DATA_PERIOD,SMA,LMA):

    client = Client(config.API_KEY, config.API_SECRET)
    SOCKET = "wss://stream.binance.com:9443/ws/adaeur@kline_15m"

    all_data = check_all_data(DATA_PERIOD)

    print(type(all_data['close'][-1]))

    PORTFOLIO = import_trade_portfolio()
    TRADE_BOOK = import_trade_book()
    PORTFOLIO['ACTIVE_TRADES'] = len(TRADE_BOOK['BUY_PRICE'])

    TEST = False

    if TEST:

        print('Starting Test')

        raw_data = 1

        for i in range(len(raw_data)):
            main_bot(raw_data[i], PORTFOLIO, TRADE_BOOK, DATA_PERIOD, SMA, LMA, all_data, True)
            print(str(i))

        WRITE_DATA.write_all_tests(TRADE_BOOK, SMA, LMA)

    else:

        #ETH_BALANCE = round(float(client.get_account()['balances'][2]['free']),6)
        EUR_BALANCE = round(float(client.get_account()['balances'][197]['free']),6) #EUR_BALANCE
        ADA_BALANCE = round(float(client.get_account()['balances'][86]['free']),6)

        PORTFOLIO['Balance_1'] = ADA_BALANCE 
        PORTFOLIO['Balance_2'] = EUR_BALANCE 

        def on_open(ws):
                print('Opened connection')

        def on_close(ws):
            print('closed connection')

        def on_message(ws, message):
            raw_data = json.loads(message)

            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            #SHORT_MA = get_MA(all_data['close'])
            #print(raw_data['k']['c']+' - ',str(SHORT_MA[-1])+' - ', current_time, ' - Active Trades: '+str(len(TRADE_BOOK['BUY_PRICE'])))
            print(raw_data['k']['c']+' - ', current_time, ' - Active Trades: '+str(len(TRADE_BOOK['BUY_PRICE'])))

            try:
                main_bot(raw_data, PORTFOLIO, TRADE_BOOK, DATA_PERIOD, SMA, LMA, all_data, False)
            except Exception as e:
                print("Main issue - {}".format(e))

    ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)
    websocket.setdefaulttimeout(5)
    ws.run_forever()                
