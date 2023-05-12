import os
import glob
import json
import datetime
import pandas as pd
import utils.constants as c
from time import strptime


class HeartRateClass:
    def __init__(self):
        self.orig_hr_dir = c.HR_DIR
        self.orig_ecg_dir = c.ECG_DIR
        self.orig_rhr_dir = c.RHR_DIR
        self.hr_dir = f"{c.NEW_HEART_DIR}heart_rate.csv"
        self.ecg_dir = f"{c.NEW_HEART_DIR}ecg.csv"
        self.rhr_dir = f"{c.NEW_HEART_DIR}resting_heart_rate.csv"

    @staticmethod
    def read_json(files_dir):
        data = []
        files = glob.glob(files_dir)
        for f_name in files:
            with open(f_name, 'r') as f:
                data += json.load(f)
        return data

    @staticmethod
    def read_csv(files_dir):
        data = []
        files = glob.glob(files_dir)
        for f_name in files:
            data += [pd.read_csv(f_name)]
        data_df = pd.concat(data).drop_duplicates().reset_index(drop=True)
        return data_df


class HeartRateSimpleClass(HeartRateClass):
    def __init__(self):
        super().__init__()
        self.df = None

    def get_df(self, minute_int=1):
        if self.df is None:
            file_name = self.hr_dir
            if not os.path.exists(file_name):
                self.create_hr_csv(minute_int=minute_int)
            df = self.read_csv(file_name)
            self.df = df

    def create_hr_csv(self, minute_int):
        hr_data = self.read_json(self.orig_hr_dir)
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


class RestingHeartRateClass(HeartRateClass):

    def __init__(self):
        super().__init__()
        self.df = None

    def get_df(self):
        if self.df is None:
            file_name = self.rhr_dir
            if not os.path.exists(file_name):
                self.create_rhr_csv()
            df = pd.read_csv(file_name)
            self.df = df

    def create_rhr_csv(self):
        rhr_data = self.read_json(self.orig_rhr_dir)
        dt, value, error = [], [], []
        for rhr in rhr_data:
            if rhr["value"]["date"] is not None:
                dt_var = datetime.datetime.strptime(rhr["value"]["date"], "%m/%d/%y")
                dt.append(dt_var)
                value.append(round(rhr["value"]["value"], 1))
                error.append(round(rhr["value"]["error"], 1))
        df = pd.DataFrame({"date": dt, "value": value, "confidence": error})
        df = df.drop_duplicates()
        df.to_csv(c.NEW_HEART_DIR + f"resting_heart_rate.csv", index=False)


class ECGClass(HeartRateClass):
    def __init__(self):
        super().__init__()
        self.df = None

    def get_df(self):
        if self.df is None:
            file_name = self.ecg_dir
            if not os.path.exists(file_name):
                self.create_ecg_csv()
            df = pd.read_csv(file_name)
            self.df = df

    def create_ecg_csv(self):
        signal_duration = 30
        ecg_df = self.read_csv(self.orig_ecg_dir)
        cols = ["wire_id", "heart_rate_alert", "firmware_version", "device_app_version", "hardware_version",
                "reading_id"]
        ecg_df = ecg_df.drop(columns=cols, axis=1)
        dfs = []

        for ecg in ecg_df.iloc:
            dt = self.get_dt_from_str(ecg.reading_time)
            signal = ecg.waveform_samples[1:-1].split("  ")
            signal = [int(sample) for sample in signal]
            sample_freq = len(signal) / signal_duration
            signal_time = [dt + datetime.timedelta(seconds=i / sample_freq) for i in range(len(signal))]
            bpm = [ecg.heart_rate] * len(signal)
            result_clf = [ecg.result_classification] * len(signal)
            dfs += [pd.DataFrame({"datetime": signal_time, "value": signal, "bpm": bpm,
                                  "result_classification": result_clf})]

        df = pd.concat(dfs).reset_index(drop=True)
        df.to_csv(f"{c.NEW_HEART_DIR}ecg.csv", index=False)

    @staticmethod
    def get_dt_from_str(reading_time):
        reading_time = reading_time.split(" ")
        month = strptime(reading_time[1], "%b").tm_mon
        day = reading_time[2]
        start_time = reading_time[3]
        year = reading_time[5]
        dt = datetime.datetime.strptime(f"{month}/{day}/{year} {start_time}", "%m/%d/%Y %H:%M:%S")
        return dt
