import os
import json
import glob
import datetime

import pandas as pd
import utils.constants as c

from time import strptime


def read_json(files_dir):
    data = []
    files = glob.glob(files_dir)
    for f_name in files:
        with open(f_name, 'r') as f:
            data += json.load(f)
    return data


def read_csv(files_dir):
    data = []
    files = glob.glob(files_dir)
    for f_name in files:
        data += [pd.read_csv(f_name)]
    data_df = pd.concat(data).reset_index(drop=True)
    return data_df


def create_hr_csv(minute_int=1):
    hr_data = read_json(c.HR_DIR)
    dt, value, confidence = [], [], []
    for hr in hr_data:
        dt_var = datetime.datetime.strptime(hr["dateTime"], "%m/%d/%y %H:%M:%S")
        minute = round(dt_var.minute / minute_int) * minute_int
        if minute == 60:
            dt_var += datetime.timedelta(hours=1)
            minute = 0
        dt.append(dt_var.replace(second=0, minute=minute))
        value.append(hr["value"]["bpm"])
        confidence.append(hr["value"]["confidence"])

    df = pd.DataFrame({"datetime": dt, "value": value, "confidence": confidence})
    df = df.groupby("datetime").agg("mean").reset_index().round(1)
    df.to_csv(c.NEW_HEART_DIR + "heart_rate.csv", index=False)


def create_rhr_csv():
    rhr_data = read_json(c.RHR_DIR)

    dt, value, error = [], [], []
    for rhr in rhr_data:
        if rhr["value"]["date"] is not None:
            dt_var = datetime.datetime.strptime(rhr["value"]["date"], "%m/%d/%y")
            dt.append(dt_var)
            value.append(round(rhr["value"]["value"], 1))
            error.append(round(rhr["value"]["error"], 1))
    df = pd.DataFrame({"datetime": dt, "value": value, "confidence": error})
    df = df.drop_duplicates()
    df.to_csv(c.NEW_HEART_DIR + f"resting_heart_rate.csv", index=False)


def create_hr_complete_csv(date):
    files_dir = c.HR_DIR[:-5] + f"{date}.json"
    hr_data = read_json(files_dir)
    assert hr_data != [], "Date not available"
    dt, value, confidence = [], [], []
    for hr in hr_data:
        dt_var = datetime.datetime.strptime(hr["dateTime"], "%m/%d/%y %H:%M:%S")
        dt.append(dt_var)
        value.append(hr["value"]["bpm"])
        confidence.append(hr["value"]["confidence"])

    df = pd.DataFrame({"datetime": dt, "value": value, "confidence": confidence})
    df = df.drop_duplicates()
    df.to_csv(c.NEW_HEART_DIR + f"heart_rate-{date}.csv", index=False)


def get_hr_complete_data(year, month, day):
    date = datetime.date(year=year, month=month, day=day)
    file_name = c.NEW_HEART_DIR + f"heart_rate-{date}.csv"
    if not os.path.exists(file_name):
        create_hr_complete_csv(date)
    df = pd.read_csv(file_name)

    return df


def get_dt_from_str(reading_time):
    reading_time = reading_time.split(" ")
    month = strptime(reading_time[1], "%b").tm_mon
    day = reading_time[2]
    start_time = reading_time[3]
    year = reading_time[5]
    dt = datetime.datetime.strptime(f"{month}/{day}/{year} {start_time}", "%m/%d/%Y %H:%M:%S")
    return dt


def pre_process_ecg():
    signal_duration = 30
    ecg_df = read_csv(c.ECG_DIR)
    cols = ["wire_id", "heart_rate_alert", "firmware_version", "device_app_version", "hardware_version"]
    ecg_df = ecg_df.drop(columns=cols, axis=1)

    for ecg in ecg_df.iloc:
        id = ecg.reading_id
        dt = get_dt_from_str(ecg.reading_time)
        signal = ecg.waveform_samples[1:-1].split("  ")
        signal = [int(sample) for sample in signal]
        sample_freq = len(signal)/signal_duration
        signal_time = [dt + datetime.timedelta(seconds=i/sample_freq) for i in range(len(signal))]
        df = pd.DataFrame({"datetime": signal_time, "value": signal})
        df.to_csv(f"{c.NEW_HEART_DIR}ecg_{ecg.heart_rate}_{ecg.result_classification}_{id}.csv", index=False)
