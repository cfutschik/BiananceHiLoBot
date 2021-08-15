from CHECK_ENGULF_ENTRY import check_engulf_entry
from CHECK_MORNINGSTAR_ENTRY import check_morningStar_entry

def check_pattern_entry(all_data):
    
    if check_engulf_entry(all_data):
        return True

    elif check_morningStar_entry(all_data):
        return True
        
    else: 
        return False