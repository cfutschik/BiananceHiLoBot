def get_sup_res(all_data):

    units = 192 #8 days
    #units = 96
    highs = all_data['high'][-units:]
    lows = all_data['low'][-units:]
    date = all_data['date'][-units:]

    # Splitting data into 32 chunks of 6 data pieces
    # past 4 days
    # past 4-8 days
    data = []
    counter = 0
    for x in range(32):
        sub_data = []
        for y in range(6):
            sub_data.append({'date' : date[counter],
                        'high' : highs[counter],
                        'low' : lows[counter]
                        }) 
            counter+=1
        data.append(sub_data)

    #Finding maxs in each 6 piece
    high_8 = []
    high_4 = []
    peaks = []
    for i in range(32):
        if i >= 16:
            high_4.append(max(data[i], key=lambda x:x['high']))
        
        high_8.append(max(data[i], key=lambda x:x['high']))

    # finding top 2 maxes and lows
    max_8 = max(high_8, key=lambda x:x['high'])
    max_4 = max(high_4, key=lambda x:x['high'])
    peaks = [max_8, max_4]

    return peaks