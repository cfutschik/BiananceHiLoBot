def get_RSI_data():
    
    with open('RSI1.txt','r') as file:
        for line in file:
            RSI = line.split(',')

    RSI.pop(-1)

    x = 0
    while x < len(RSI):
        RSI[x] = float(RSI[x])
        x+=1
        
    return RSI