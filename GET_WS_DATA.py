import websocket, json
import config
from binance.client import Client
from binance.enums import *

def get_ws_data():

    SOCKET = "wss://stream.binance.com:9443/ws/ethusdt@kline_1m"
    #client = Client(config.API_KEY, config.API_SECRET, tld='us')

    def on_open(ws):
        print('opened connection')

    def on_close(ws):
        print('closed connection')

    def on_message(ws, message):
        global closes, in_position
        json_message = json.loads(message)
        #pprint.pprint(json_message)
        print(json_message['E'])

        if json_message['k']['x']:
            ws.close()
            return json_message

    ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)
    ws.run_forever()