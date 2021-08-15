import json, numpy, io

def get_close_data():

    with io.open('Data1.txt','r') as file, \
        io.open('Data2.txt','w') as file2, \
        io.open('Data3.txt', 'w') as file3:
        data = file.read()
        data = data.replace("\\","")
        data = data.replace('"{','{')
        data = data.replace('}}",','}}')
        data1 = data
        data1 = data1.replace('"','')
        data1 = data1.replace('o:','')
        data1 = data1.replace('c:','')
        data1 = data1.replace('h:','')
        data1 = data1.replace('l:','')
        file2.write(data)
        file3.write(data1)

    with io.open('Data2.txt','r') as file:
        Data = []
        for line in file:
            Data.append(json.loads(line))
    
    x = 0
    while x < 14:
        Data.pop(0)
        x+=1

    time = []
    open = []
    high = []
    low = []
    close = []

    #print(len(Data))

    x = 0
    while x < len(Data):
        open.append(float(Data[x]['k']['o']))
        high.append(float(Data[x]['k']['h']))
        low.append(float(Data[x]['k']['l']))
        close.append(float(Data[x]['k']['c']))
        time.append(int(Data[x]['k']['T']))
  
        x +=1

    return numpy.array(open), numpy.array(high), numpy.array(low), numpy.array(close), time