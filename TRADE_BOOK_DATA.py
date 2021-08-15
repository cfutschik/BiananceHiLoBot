# importing the module
import json
def import_trade_book():
    # reading the data from the file
    with open('dataFiles/TRADE_BOOK.txt') as f:
        data1 = json.loads(f.read())

    return data1

def update_trade_book(data1):

    with open('dataFiles/TRADE_BOOK.txt', 'r+') as f:
        f.seek(0)
        f.truncate()
        f.write(json.dumps(data1))

