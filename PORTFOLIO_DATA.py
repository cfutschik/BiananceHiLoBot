# importing the module
import json
def import_trade_portfolio():
    # reading the data from the file
    with open('dataFiles/PORTFOLIO.txt') as f:
        data1 = json.loads(f.read())

    return data1

def write_portfolios(PORTFOLIO):

    with open('dataFiles/PORTFOLIO.txt', 'r+') as f:
        f.seek(0)
        f.truncate()
        f.write(json.dumps(PORTFOLIO))
