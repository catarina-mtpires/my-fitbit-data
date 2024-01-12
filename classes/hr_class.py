import datetime
import pandas as pd
import utils.constants as c
from time import strptime
from classes.base_class import DataClass


class HeartRateClass(DataClass):
    def __init__(self):
        super().__init__()
        self.minute_int = 1
        directory = c.HR
        self.orig_dir = directory["orig"]
        self.new_dir = directory["new"]
        self.dt_col = "datetime"

    def create_csv(self):
        hr_data = self.read_json()
        dt, values, confidences = [], [], []
        for hr in hr_data:
            dt_var = datetime.datetime.strptime(hr["dateTime"], "%m/%d/%y %H:%M:%S")
            minute = round(dt_var.minute / self.minute_int) * self.minute_int
            if minute == 60:
                dt_var += datetime.timedelta(hours=1)
                minute = 0
            dt.append(dt_var.replace(second=0, minute=minute))
            values.append(round(hr["value"]["bpm"]))
            confidences.append(hr["value"]["confidence"])

        df = pd.DataFrame({"datetime": dt, "value": values, "confidence": confidences})
        df = df.groupby("datetime").agg("mean").reset_index().round(1)
        df.to_csv(self.new_dir, index=False)


class RestingHeartRateClass(DataClass):

    def __init__(self):
        super().__init__()
        directory = c.RHR
        self.orig_dir = directory["orig"]
        self.new_dir = directory["new"]
        self.dt_col = "date"

    def create_csv(self):
        rhr_data = self.read_json()
        dt, value, error = [], [], []
        for rhr in rhr_data:
            if rhr["value"]["date"] is not None:
                dt_var = datetime.datetime.strptime(rhr["value"]["date"], "%m/%d/%y")
                dt.append(dt_var)
                value.append(round(rhr["value"]["value"], 1))
                error.append(round(rhr["value"]["error"], 1))
        df = pd.DataFrame({"date": dt, "value": value, "confidence": error})
        df = df.drop_duplicates()
        df.to_csv(self.new_dir, index=False)


class ECGClass(DataClass):
    def __init__(self):
        super().__init__()
        directory = c.ECG
        self.orig_dir = directory["orig"]
        self.new_dir = directory["new"]
        self.dt_col = "datetime"

    def create_csv(self):
        signal_duration = 30
        ecg_df = self.read_csv()
        cols = ["wire_id", "heart_rate_alert", "firmware_version", "device_app_version", "hardware_version"]
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
            id = [ecg.reading_id] * len(signal)
            dfs += [pd.DataFrame({"id": id, "datetime": signal_time, "value": signal, "bpm": bpm,
                                  "result_classification": result_clf})]

        df = pd.concat(dfs).reset_index(drop=True)
        df.to_csv(self.new_dir, index=False)

    @staticmethod
    def get_dt_from_str(reading_time):
        reading_time = reading_time.split(" ")
        month = strptime(reading_time[1], "%b").tm_mon
        day = reading_time[2]
        start_time = reading_time[3]
        year = reading_time[5]
        dt = datetime.datetime.strptime(f"{month}/{day}/{year} {start_time}", "%m/%d/%Y %H:%M:%S")
        return dt


class HeartRateCompleteClass(DataClass):
    def __init__(self, year, month, day):
        super().__init__()
        self.date = datetime.date(year=year, month=month, day=day)
        self.orig_dir = f"{c.ORIG_HEART_DIR}heart_rate/heart_rate-{self.date}.json"
        self.new_dir = f"{c.NEW_HEART_DIR}heart_rate_{self.date}.csv"
        self.dt_col = "datetime"

    def create_csv(self):
        hr_data = self.read_json()
        assert hr_data != [], "Date not available"
        dt, value, confidence = [], [], []
        for hr in hr_data:
            dt_var = datetime.datetime.strptime(hr["dateTime"], "%m/%d/%y %H:%M:%S")
            seconds = round(dt_var.second / 5) * 5
            if seconds == 60:
                dt_var += datetime.timedelta(minutes=1)
                seconds = 0
            dt.append(dt_var.replace(second=seconds))
            value.append(hr["value"]["bpm"])
            confidence.append(hr["value"]["confidence"])
        df = pd.DataFrame({"datetime": dt, "value": value, "confidence": confidence})
        df = df.drop_duplicates()
        df.to_csv(self.new_dir, index=False)
