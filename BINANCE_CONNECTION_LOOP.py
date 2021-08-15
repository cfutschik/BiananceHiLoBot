import time,os
from datetime import datetime
from BINANCE_BOT import binance_bot 

DATA_PERIOD = 65
SMA = 15
LMA = 55

print(SMA)
print(LMA)

while True:
    try:
        binance_bot(DATA_PERIOD,SMA,LMA)
    except:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print('Trying to restart - ', current_time)
        time.sleep(5)
