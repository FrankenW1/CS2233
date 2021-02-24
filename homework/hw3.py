# The Solar Project - (Because its not warm enough outside to be speaking about solar power)
#  You will submit this project individually but work collaboratively. You will also be graded as a team meaning
#  if 1 member does not submit the code to their repository, and response on blackboard
#  but the other 3 team members do both parts perfectly. The final grade project will be a 75% for everyone.
#
#  Black Board Submission
#    Submit a review of each member of the as part of the blackboard submission.
#    1. I am not expecting much here, just 2 or 3 sentences reviewing each team member.
#    2. What did you enjoy about the project?
#    3. What did you not enjoy?

#  Code Submission:
#    Use the data set for creating  /data/power_readings.csv
#    Required functions in the git repository are below and should be located under /homework/hw3.py
from datetime import datetime, date
from pathlib import Path
from datetime import datetime
from typing import Dict
import pandas as pd
from in_class import data
import csv


def read_file():
    d = Path("C:/Users/wafra/PycharmProjects/CS2233 class/data/power_readings.csv")
    with open(d, "r") as fp:
        data = fp.readline()
    return data


def read_file_pandas():
    d = Path("C:/Users/wafra/PycharmProjects/CS2233 class/data/power_readings.csv")
    df = pd.read_csv(d)
    # electric = pd.read_csv("../data/power_readings.csv", index_col=0, header=None, squeeze=True).to_dict()
    return df


power = pd.read_csv("C:/Users/wafra/PycharmProjects/CS2233 class/data/power_readings.csv", index_col=0, header=None, squeeze=True).to_dict()
key_list = []

read_file()
read_file_pandas()


def hourly_demand_summary() -> Dict[datetime, float]:
    total = 0
    total_dict = {}
    for key in power:
        key_list.append(key)
    n = 1
    m = 288
    for key in power:
        total = 0
        for i in range(n, m):
            total += float(power[key_list[i]])
        key_list[i]
        total_dict[key_list[i]] = total
        n += 288
        m += 288
        if i >= 2015:
            break
    return total_dict
    """
        This function will return an hourly breakdown of the dataset.
        {
            datetime(2020,2,1,0,0): 0.0,
            datetime(2020,2,1,1,0): 0.0,
            ...,
            datetime(2020,2,7,23,0): 0.0,
        }


        i = 1
        x = 0
        total = 0
        int(power[key])

        total = total + power[key]
        i += 1
        if (i % 12) == 0:
            hourly_data = []
            hourly_data.append(total)
            print(hourly_data[x])
            x += 1
            total *= 0
            continue
        else:
            continue
        """
    ...


def daily_demand_summary() -> Dict[datetime, float]:
    total = 0
    total_dict = {}
    for key in power:
        key_list.append(key)
    n = 1
    m = 288
    for key in power:
        total = 0
        for i in range(n, m):
            total += float(power[key_list[i]])
        key_list[i]
        total_dict[key_list[i]] = total
        n += 288
        m += 288
        if i >= 2015:
            break
    return total_dict
    """
    This function will return an daily breakdown of the dataset.
    {
        datetime(2020,2,1): 0.0,
        datetime(2020,2,2): 0.0,
        ...,
        datetime(2020,2,7): 0.0,
    }
    """
    ...


def weekly_power_summary() -> float:
    for key in power:
        key_list.append(key)
    n = 1
    m = 2017
    for key in power:
        total = 0
        for i in range(n, m):
            total += float(power[key_list[i]])
        # print(total)
        if i >= 2015:
            break
    return total
    """
    Summary of total power produced during the week
    """
    ...


def maximum_hourly_data() -> datetime:
    total = 0
    total_dict = {}
    for key in power:
        key_list.append(key)
    n = 1
    m = 13
    for key in power:
        total = 0
        for i in range(n, m):
            total += float(power[key_list[i]])
        key_list[i]
        total_dict[key_list[i]] = total

        n += 12
        m += 12
        if i >= 2016:
            break
    MaxKey = max(total_dict, key=total_dict.get)
    final = total_dict[MaxKey]
    return MaxKey
    """
    This function will return hour that produced the maximum total power.
    e.g. datetime(2020,2,1,12): 100
         datetime(2020,2,1,13): 200
    :return datetime(2020,2,1,13)

    """
    ...

