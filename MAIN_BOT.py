from GET_DATA import get_data
from WRITE_DATA import write_candlestick_data
from PORTFOLIO_DATA import write_portfolios
import TRADE_BOOK_DATA
from CHECK_TRADE import check_trade

def main_bot(raw_data, PORTFOLIO, TRADE_BOOK, DATA_PERIOD, SMA, LMA, all_data, TEST):

    if len(all_data['close']) >= DATA_PERIOD:
        all_data = get_data(all_data, raw_data, PORTFOLIO, DATA_PERIOD)
        check_trade(PORTFOLIO, TRADE_BOOK, all_data, SMA, LMA, TEST)

    elif len(all_data['close']) < DATA_PERIOD and PORTFOLIO['ACTIVE_TRADES'] != 0:
        all_data = get_data(all_data, raw_data, PORTFOLIO, DATA_PERIOD)
        check_trade(PORTFOLIO, TRADE_BOOK, all_data, SMA, LMA, TEST)
        
    else:
        all_data = get_data(all_data, raw_data, PORTFOLIO, DATA_PERIOD)
    
    write_portfolios(PORTFOLIO)
    TRADE_BOOK_DATA.update_trade_book(TRADE_BOOK)