import requests
import pandas as pd
import time
import datetime
import re
import numpy as np
import tzlocal


class TimeFrameError(ValueError):
    pass


class ReturnError(ValueError):
    pass


class DateError(ValueError):
    pass


class SepError(ValueError):
    pass


class CategoryError(ValueError):
    pass


def _check_timeframe(timeframe):
    if timeframe not in {"D", "M", "W"} and not isinstance(timeframe, int):
        raise TimeFrameError(f"Значения в 'timeframe' должны быть натуральными или D, W, M")

    if timeframe not in {1, 3, 5, 15, 30, 60, 120, 240, 360, 720, "D", "M", "W"}:
        raise TimeFrameError("Значения timeframe должны быть 1, 3, 5, 15, 30, 60, 120, 240, 360, 720 минут или D, W, M")


def _change_df(df):
    df[0] = df[0].astype(np.uint64)
    df[list(range(1, 5))] = df[list(range(1, 5))].astype("float_")
    df[5] = df[5].astype("float_")
    df.columns = ["Start time of the candle", "Open price", "Highest price", "Lowest price",
                  "Close price", "Trade volume", "-"]
    df.drop(["-"], axis=1, inplace=True)
    df.reset_index(drop=True, inplace=True)
    df["Start time of the candle"] = pd.to_datetime(df["Start time of the candle"], unit='ms', utc=True)
    df["Start time of the candle"] = df["Start time of the candle"].dt.tz_convert(tzlocal.get_localzone())
    df["Start time of the candle"] = df["Start time of the candle"].dt.strftime('%d/%m/%Y %H.%M')
    return df


def getdata(ticker, timeframe, periods, spot=False):
    _check_timeframe(timeframe=timeframe)
    url = "https://api.bybit.com/v5/market/kline"

    params = {
        'symbol': ticker,
        'interval': timeframe,
        'limit': periods}

    if spot:
        params["category"] = "spot"

    response = requests.get(url, params=params)
    response = response.json()

    if response['retMsg'] != "OK":
        raise ReturnError(response['retMsg'])

    response = response["result"]["list"]
    df = pd.DataFrame(response)

    if periods > 1000:
        params["end"] = int(df[0].iloc[-1]) - 1
        params["limit"] = 1000
        for i in range(periods // 1000 - 1):
            start_time = time.time()
            response = requests.get(url, params=params)
            df = pd.concat([df, pd.DataFrame(response.json()["result"]["list"])])
            params["end"] = int(df[0].iloc[-1]) - 1
            t = float(time.time() - start_time)
            time.sleep(max(0, 0.015 - t))
        if periods % 1000 != 0:
            params["limit"] = periods % 1000
            response = requests.get(url, params=params)
            df = pd.concat([df, pd.DataFrame(response.json()["result"]["list"])])

    return _change_df(df=df)


# Дата передается в формате "DD.MM.YY HH.MM"
def getdata_period(ticker, timeframe, start, end, spot=False):
    pattern = r"\d{2}\.\d{2}\.\d{2} \d{2}\.\d{2}"
    date_format = "%d.%m.%y %H.%M"
    if re.match(pattern, start) is None or re.match(pattern, end) is None:
        raise DateError("Измените формат ввода даты")
    _check_timeframe(timeframe=timeframe)

    start = int(datetime.datetime.strptime(start, date_format).timestamp()) * 1000
    end = int(datetime.datetime.strptime(end, date_format).timestamp()) * 1000

    if end <= start:
        raise DateError("Дата конца преиода должна идти после даты начала")
    change = {"D": 1440, "W": 10080, "M": 44671}
    periods = int((end - start) / (change.get(timeframe, timeframe) * 60000)) + 1
    url = "https://api.bybit.com/v5/market/kline"
    params = {
        'symbol': ticker,
        'interval': timeframe,
        'limit': periods,
        "end": end}

    if spot:
        params["category"] = "spot"

    response = requests.get(url, params=params)
    response = response.json()

    if response['retMsg'] != "OK":
        raise ReturnError(response['retMsg'])

    response = response["result"]["list"]
    if len(response) == 0 and periods <= 1000:
        raise ReturnError("Отсутвуют данные о периоде")
    elif len(response) == 0:
        raise ReturnError(f"Отсутвуют данные о последних 1000 значениях периода, кол-во запрашиваемых значений: {periods}")


    df = pd.DataFrame(response)
    if periods > 1000:
        params["end"] = int(df[0].iloc[-1]) - 1
        params["limit"] = 1000
        for i in range(periods // 1000 - 1):
            start_time = time.time()
            response = requests.get(url, params=params).json()["result"]["list"]
            if len(response) == 0:
                break
            df = pd.concat([df, pd.DataFrame(response)])
            params["end"] = int(df[0].iloc[-1]) - 1
            t = float(time.time() - start_time)
            time.sleep(max(0, 0.015 - t))
        else:
            if periods % 1000 != 0:
                params["limit"] = periods % 1000
                response = requests.get(url, params=params)
                df = pd.concat([df, pd.DataFrame(response.json()["result"]["list"])])

    return _change_df(df=df)


def getdata_d(ticker, timeframe, periods, name, sep, spot=False):
    if sep == ".":
        raise SepError("Выберете другой разделитель")
    with open(f"{name}.csv", "w") as f:
        print(*["Start time of the candle", "Open price", "Highest price", "Lowest price", "Close price", "Trade volume"],
            file=f, sep=sep)
        _check_timeframe(timeframe=timeframe)
        url = "https://api.bybit.com/v5/market/kline"
        params = {'symbol': ticker, 'interval': timeframe, 'limit': periods}

        if spot:
            params["category"] = "spot"

        response = requests.get(url, params=params)
        response = response.json()
        if response['retMsg'] != "OK":
            raise ReturnError(response['retMsg'])
        response = response["result"]["list"]
        for el in response:
            print(*([datetime.datetime.fromtimestamp(int(el[0]) / 1000).strftime('%d/%m/%Y %H.%M')] + el[1:-1]), sep=sep, file=f)

        if periods > 1000:
            params["end"] = int(response[-1][0]) - 1
            params["limit"] = 1000
            for i in range(periods // 1000 - 1):
                start_time = time.time()
                response = requests.get(url, params=params).json()["result"]["list"]
                for el in response:
                    print(*([datetime.datetime.fromtimestamp(int(el[0]) / 1000).strftime('%d/%m/%Y %H.%M')] + el[1:-1]), sep=sep, file=f)
                params["end"] = int(response[-1][0]) - 1
                t = float(time.time() - start_time)
                time.sleep(max(0, 0.015 - t))
            if periods % 1000 != 0:
                params["limit"] = periods % 1000
                response = requests.get(url, params=params).json()["result"]["list"]
                for el in response:
                    print(*([datetime.datetime.fromtimestamp(int(el[0]) / 1000).strftime('%d/%m/%Y %H.%M')] + el[1:-1]), sep=sep, file=f)


def getdata_period_d(ticker, timeframe, start, end, name, sep, spot=False):
    pattern = r"\d{2}\.\d{2}\.\d{2} \d{2}\.\d{2}"
    date_format = "%d.%m.%y %H.%M"
    if re.match(pattern, start) is None or re.match(pattern, end) is None:
        raise DateError("Измените формат ввода даты")
    _check_timeframe(timeframe=timeframe)

    start = int(datetime.datetime.strptime(start, date_format).timestamp()) * 1000
    end = int(datetime.datetime.strptime(end, date_format).timestamp()) * 1000

    if end <= start:
        raise DateError("Дата конца преиода должна идти после даты начала")
    change = {"D": 1440, "W": 10080, "M": 44671}
    periods = int((end - start) / (change.get(timeframe, timeframe) * 60000)) + 1
    url = "https://api.bybit.com/v5/market/kline"
    params = {
        'symbol': ticker,
        'interval': timeframe,
        'limit': periods,
        "end": end}

    if spot:
        params["category"] = "spot"

    response = requests.get(url, params=params)
    response = response.json()

    if response['retMsg'] != "OK":
        raise ReturnError(response['retMsg'])

    response = response["result"]["list"]
    if len(response) == 0 and periods <= 1000:
        raise ReturnError("Отсутвуют данные о периоде")
    elif len(response) == 0:
        raise ReturnError(f"Отсутвуют данные о последних 1000 значениях периода, кол-во запрашиваемых значений: {periods}")

    with open(f"{name}.csv", "w") as f:
        print(*["Start time of the candle", "Open price", "Highest price", "Lowest price", "Close price", "Trade volume"], file=f, sep=sep)
        for el in response:
            print(*([datetime.datetime.fromtimestamp(int(el[0]) / 1000).strftime('%d/%m/%Y %H.%M')] + el[1:-1]), sep=sep, file=f)
        if periods > 1000:
            params["end"] = int(response[-1][0]) - 1
            params["limit"] = 1000
            for i in range(periods // 1000 - 1):
                start_time = time.time()
                response = requests.get(url, params=params).json()["result"]["list"]
                if len(response) == 0:
                    break
                for el in response:
                    print(*([datetime.datetime.fromtimestamp(int(el[0]) / 1000).strftime('%d/%m/%Y %H.%M')] + el[1:-1]), sep=sep, file=f)
                params["end"] = int(response[-1][0]) - 1
                t = float(time.time() - start_time)
                time.sleep(max(0, 0.015 - t))
            else:
                if periods % 1000 != 0:
                    params["limit"] = periods % 1000
                    response = requests.get(url, params=params).json()["result"]["list"]
                    for el in response:
                        print(*([datetime.datetime.fromtimestamp(int(el[0]) / 1000).strftime('%d/%m/%Y %H.%M')] + el[1:-1]), sep=sep, file=f)


def instruments(category):
    if category not in {"spot", "linear", "inverse"}:
        raise CategoryError(f'Категория актива может принимать значения: "spot", "linear", "inverse"')

    url = "https://api.bybit.com/v5/market/tickers"
    params = {"category": category}
    response = requests.get(url, params=params).json()["result"]["list"]
    if category == "spot":
        col = ['symbol', 'bid price', 'bid size', 'ask price', 'ask size', 'last price', 'prev price 24h',
               'price change 24h perc', 'high price 24h', 'low price 24h', 'turnover 24h', 'volume 24h', 'del']
    else:
        col = ['symbol', 'last price', 'index price', 'markPrice', 'prev price 24h', 'price change 24h perc',
               'high price 24h', 'low price 24h', 'prevPrice1h', 'open interest', 'open interest val', 'turnover 24h',
               'volume 24h', 'funding rate', 'next funding time', 'predictedDeliveryPrice', 'basisRate',
               'deliveryFeeRate', 'delivery time', 'ask size', 'bid price', 'ask price', 'bid size', 'basis']
    if category == "spot":
        data = [list(el.values()) if len(el) == 13 else list(el.values()) + [0] for el in response]
    else:
        data = [el.values() for el in response]
    df = pd.DataFrame(data)
    df.columns = col
    if category == "spot":
        try:
            df[col[1:-1]] = df[col[1:-1]].astype('float_')
        except ValueError:
            df.replace([""], ["0"], inplace=True)
            df[col[1:-1]] = df[col[1:-1]].astype('float_')
        df["price change 24h perc"] *= 100
        df.drop(["del"], axis=1, inplace=True)
    else:
        df.drop(["deliveryFeeRate", "basis", "predictedDeliveryPrice", "basisRate", "prevPrice1h", "markPrice"], axis=1,
                inplace=True)

        df["next funding time"] = df["next funding time"].astype(np.uint64)
        df["next funding time"] = pd.to_datetime(df["next funding time"], unit='ms', utc=True)
        df["next funding time"] = df["next funding time"].dt.tz_convert(tzlocal.get_localzone())
        df["next funding time"] = df["next funding time"].dt.strftime('%d/%m/%Y %H.%M')
        df["next funding time"] = df["next funding time"].astype("str")
        df["next funding time"][df["next funding time"] == "01/01/1970 03.00"] = ["0"] * sum(
            df["next funding time"] == "01/01/1970 03.00")

        df["delivery time"] = df["delivery time"].astype(np.uint64)
        df["delivery time"] = pd.to_datetime(df["delivery time"], unit='ms', utc=True)
        df["delivery time"] = df["delivery time"].dt.tz_convert(tzlocal.get_localzone())
        df["delivery time"] = df["delivery time"].dt.strftime('%d/%m/%Y %H.%M')
        df["delivery time"] = df["delivery time"].astype("str")
        df["delivery time"][df["delivery time"] == "01/01/1970 03.00"] = ["perp"] * sum(
            df["delivery time"] == "01/01/1970 03.00")

        col = ['last price', 'index price', 'prev price 24h', 'price change 24h perc', 'high price 24h',
               'low price 24h', 'open interest', 'open interest val', 'turnover 24h', 'volume 24h', 'ask size',
               'bid price', 'ask price', 'bid size']
        try:
            df[col] = df[col].astype('float_')
        except ValueError:
            df.replace([""], ["0"], inplace=True)
            df[col] = df[col].astype('float_')
        df['price change 24h perc'] *= 100

        new_order = ['symbol', 'bid price', 'bid size', 'ask price', 'ask size', 'last price', 'index price',
                     'prev price 24h', 'price change 24h perc', 'high price 24h', 'low price 24h', 'open interest',
                     'open interest val', 'turnover 24h', 'volume 24h', 'funding rate', 'next funding time',
                     'delivery time']
        df = df[new_order]
    return df






