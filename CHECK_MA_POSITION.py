from GET_MA import get_MA

def check_ma_position(all_closes):

    MA = get_MA(all_closes)

    if all_closes[-1] >= MA[-1]:
        print('Check MA Position: '+str(all_closes[-1])+' - '+str(MA[-1]))
        return True

    else:
        return False