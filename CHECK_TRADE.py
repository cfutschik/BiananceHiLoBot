from CHECK_ENTRY import check_entry
import EXECUTE_TRADE
import GET_MA

def check_trade(PORTFOLIO, TRADE_BOOK, all_data, SMA, LMA, TEST):

    if PORTFOLIO['ACTIVE_TRADES'] < 1:

        if PORTFOLIO["BUY_HOLD"] == 0:

            S_MA, L_MA = GET_MA.get_MA(all_data['close'], SMA, LMA,)
            if S_MA[-1] > L_MA[-1]:

                EXECUTE_TRADE.execute_buy(PORTFOLIO, TRADE_BOOK, all_data, TEST)

    if PORTFOLIO["ACTIVE_TRADES"] != 0:

        S_MA, L_MA = GET_MA.get_MA(all_data['close'], SMA, LMA,)
        if S_MA[-1] < L_MA[-1]:

            EXECUTE_TRADE.execute_sell(PORTFOLIO, TRADE_BOOK, all_data, TEST)