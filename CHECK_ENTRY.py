from CHECK_ENGULF_ENTRY import check_engulf_entry
from CHECK_MA_POSITION import check_ma_position

def check_entry(all_data):
    
    if check_ma_position(all_data['close']):
        return True