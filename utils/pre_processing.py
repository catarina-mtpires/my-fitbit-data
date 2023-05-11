import os
import json
import glob
import datetime

import pandas as pd
import utils.constants as c


def read_json(files_dir):
    data = []
    files = glob.glob(files_dir)
    for f_name in files:
        with open(f_name, 'r') as f:
            data += json.load(f)
    return data


def create_hr_csv(minute_int=1):
    hr_data = read_json(c.HR_DIR)
    dt, bpm, confidence = [], [], []
    for hr in hr_data:
        dt_var = datetime.datetime.strptime(hr["dateTime"], "%m/%d/%y %H:%M:%S")
        minute = round(dt_var.minute / minute_int) * minute_int
        if minute == 60:
            dt_var += datetime.timedelta(hours=1)
            minute = 0
        dt.append(dt_var.replace(second=0, minute=minute))
        bpm.append(hr["value"]["bpm"])
        confidence.append(hr["value"]["confidence"])

    df = pd.DataFrame({"datetime": dt, "bpm": bpm, "confidence": confidence})
    df = df.groupby("datetime").agg("mean").reset_index().round()

    df.to_csv(c.NEW_HEART_DIR + "heart_rate.csv", index=False)


def create_hr_complete_csv(date):
    files_dir = c.HR_DIR[:-5] + f"{date}.json"
    hr_data = read_json(files_dir)
    assert hr_data != [], "Date not available"
    dt, bpm, confidence = [], [], []
    for hr in hr_data:
        dt_var = datetime.datetime.strptime(hr["dateTime"], "%m/%d/%y %H:%M:%S")
        dt.append(dt_var)
        bpm.append(hr["value"]["bpm"])
        confidence.append(hr["value"]["confidence"])

    df = pd.DataFrame({"datetime": dt, "bpm": bpm, "confidence": confidence})
    df = df.groupby("datetime").agg("mean").reset_index().round()

    df.to_csv(c.NEW_HEART_DIR + f"heart_rate-{date}.csv", index=False)


def get_hr_complete_data(year, month, day):
    date = datetime.date(year=year, month=month, day=day)
    file_name = c.NEW_HEART_DIR + f"heart_rate-{date}.csv"
    if not os.path.exists(file_name):
        create_hr_complete_csv(date)
    df = pd.read_csv(file_name)

    return df