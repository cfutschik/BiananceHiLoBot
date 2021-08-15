from CHECK_CANDLESTICK_PATTERN import check_candleStick_pattern
import csv

def check_candlestick_trend(all_data, candles):

    check = 0
    candle_score = 0

    for i in range(candles):
        candle = check_candleStick_pattern(all_data, i)
        check+= candle

    # Need more than 1 more positives than negative patterns
    if check > 1:
        candle_score = 1
    elif check == 1:
        candle_score = 0.5
    else:
        candle_score = 0

    with open('dataFiles/candle_pattern_data.csv', 'a', newline='') as f:
        data_writer = csv.writer(f, delimiter=',',quoting=csv.QUOTE_MINIMAL)
        data_writer.writerow([check, candle_score])

    return candle_score 