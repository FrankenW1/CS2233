from typing import List, Tuple
from datetime import datetime
from typing import Dict
from collections import Counter
import calendar
from pprint import pprint
import math


def read_solar_data(p: str = None) -> List[Tuple[datetime, float]]:
    ret = []
    with open(
            "/Users/wafra/PycharmProjects/CS2233 class/data/power_readings.csv",
            "r",
    ) as fp:
        data = fp.readlines()
    for idx, row in enumerate(data):
        if idx == 0:
            continue
        date, power = row.split(",")
        date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S %z")
        ret.append((date, float(power)))
    return ret


def trunc_datetime(dt: datetime):
    return dt.replace(minute=0, second=0, microsecond=0, tzinfo=None)


def hourly_demand_summary(data: List[Tuple[datetime, float]]) -> Dict[datetime, float]:
    """
    This function will return an hourly breakdown of the dataset. This hourly data will include the hour before meaning datetime(2020,2,1,1,0,0) will range from 01:00 - 01:59
    {
        datetime(2020,2,1,0,0): 0.0,
        datetime(2020,2,1,1,0): 0.0,
        ...,
        datetime(2020,2,7,23,0): 0.0,
    }
    """
    ret = {}
    for date, power in data:
        date = trunc_datetime(date)
        if date in ret:
            ret[date] += power
        else:
            ret[date] = power

    return ret


def round_to_30_minutes(dt: datetime):
    if dt.minute >= 30:
        return dt.replace(minute=30, second=0, microsecond=0, tzinfo=None)
    return dt.replace(minute=0, second=0, microsecond=0, tzinfo=None)


def thirty_minute_demand_summary(data: List[Tuple[datetime, float]]) -> Dict[datetime, float]:
    """
    This function will return an half hour breakdown of the dataset. This  data will include the hour before meaning datetime(2020,2,1,1,0,0) will range from 01:00:00 - 01:29:59 and the second set will range from 01:30:00 - 01:59:59
    {
        datetime(2020,2,1,0,0): 0.0,
        datetime(2020,2,1,0,30): 10.0,
        datetime(2020,2,1,1,0): 20.0,
        datetime(2020,2,1,1,30): 10.0,
        ...,
        datetime(2020,2,7,23,0): 0.0,
    }
    """
    ret = {}
    for date, power in data:
        # date = trunc_datetime(date)
        date = round_to_30_minutes(date)
        if date in ret:
            ret[date] += power
        else:
            ret[date] = power

    return ret


def round_to_daily(dt: datetime):
    return dt.replace(hour=0, minute=0, second=0, microsecond=0, tzinfo=None)


def daily_demand_summary(data: List[Tuple[datetime, float]]) -> Dict[datetime, float]:
    ret = {}
    for date, power in data:
        date = round_to_daily(date)
        if date in ret:
            ret[date] += power
        else:
            ret[date] = power

    return ret


def max_hourly_data_produced(data: List[Tuple[datetime, float]]) -> Dict[datetime, float]:
    y = hourly_demand_summary(data)
    k = Counter(y)
    high = k.most_common(1)
    z = high[0]
    return z


def max_format(dt: datetime):
    return dt.replace(tzinfo=None)


def max_average_power_produced(data: List[Tuple[datetime, float]]) -> Dict[datetime, float]:
    ret = {}
    for date, power in data:
        date = max_format(date)
        if date in ret:
            ret[date] += power
        else:
            ret[date] = power
    k = Counter(ret)
    high = k.most_common(1)
    z = high[0]
    return z


def weekly_power_summary(data: List[Tuple[datetime, float]]) -> Dict[datetime, float]:
    daily = daily_demand_summary(data)
    ret = {}
    for key in daily:
        day = key.day
        if day == 1 or day % 8 == 1:
            week_key = key
            sum = 0
        sum += daily[key]
        ret[week_key] = sum
    return ret






if __name__ == "__main__":
    from pprint import pprint

    data = read_solar_data()
    print(thirty_minute_demand_summary(data))
    print(daily_demand_summary(data))
    print(max_average_power_produced(data))
    print(max_hourly_data_produced(data))
    print(weekly_power_summary(data))
