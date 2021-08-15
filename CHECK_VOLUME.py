def check_volume(all_volume):

    if all_volume[-1] > all_volume[-2]:
        return True
    else:
        return False