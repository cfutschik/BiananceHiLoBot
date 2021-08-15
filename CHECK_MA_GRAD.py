import csv

from GET_MA_GRAD import get_ma_grad

def check_ma_grad(all_data):

    grad =  get_ma_grad(all_data)

    grad_score = 0
    
    if grad[0] > 0 and grad[1] > 0:
        grad_score = 1
    elif grad[0] > 0 or grad[1] > 0:
        grad_score = 0.5

    with open('dataFiles/ma_grad_data.csv', 'a', newline='') as f:
        data_writer = csv.writer(f, delimiter=',',quoting=csv.QUOTE_MINIMAL)
        data_writer.writerow([grad[0], grad[1], grad_score])

    return grad_score