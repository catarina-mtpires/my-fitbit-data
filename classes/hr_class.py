import datetime
import pandas as pd
import utils.constants as c
from time import strptime
from classes.base_class import DataClass


class HeartRateClass(DataClass):
    def __init__(self, initialize_df=True):
        self.minute_int = 1
        directory = c.HR
        orig_dir = directory["orig"]
        new_dir = directory["new"]
        super().__init__(orig_dir=orig_dir, new_dir=new_dir, initialize_df=initialize_df)

    def create_df(self):
        hr_data = self.read_json()
        dt, values, confidences = [], [], []
        for hr in hr_data:
            dt_var = datetime.datetime.strptime(hr["dateTime"], "%m/%d/%y %H:%M:%S")
            minute = round(dt_var.minute / self.minute_int) * self.minute_int
            if minute == 60:
                dt_var += datetime.timedelta(hours=1)
                minute = 0
            dt.append(dt_var.replace(second=0, minute=minute))
            values.append(hr["value"]["bpm"])
            confidences.append(hr["value"]["confidence"])

        df = pd.DataFrame({self.dt_col: dt, self.value_col: values, "confidence": confidences})
        df = df.groupby(self.dt_col).agg("mean").reset_index().round(1)

        return df


class RestingHeartRateClass(DataClass):
    def __init__(self, initialize_df=True):
        directory = c.RHR
        orig_dir = directory["orig"]
        new_dir = directory["new"]
        super().__init__(orig_dir=orig_dir, new_dir=new_dir, initialize_df=initialize_df)

    def create_df(self):
        rhr_data = self.read_json()
        dt, values, errors = [], [], []
        for rhr in rhr_data:
            if rhr["value"]["date"] is not None:
                dt_var = datetime.datetime.strptime(rhr["value"]["date"], "%m/%d/%y")
                dt.append(dt_var)
                values.append(round(rhr["value"]["value"], 1))
                errors.append(round(rhr["value"]["error"], 1))
        df = pd.DataFrame({self.dt_col: dt, self.value_col: values, "error": errors})

        return df


class ECGClass(DataClass):
    def __init__(self, initialize_df=True):
        directory = c.ECG
        orig_dir = directory["orig"]
        new_dir = directory["new"]
        self.id_col = "id"
        super().__init__(orig_dir=orig_dir, new_dir=new_dir, initialize_df=initialize_df, sort_values=False)

    def create_df(self):
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
            df = pd.DataFrame({self.id_col: id, self.dt_col: signal_time, self.value_col: signal, "bpm": bpm,
                               "result_classification": result_clf})
            df = df.sort_values(self.dt_col).reset_index(drop=True)
            dfs += [df]
        df = pd.concat(dfs).reset_index(drop=True)

        return df

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
    def __init__(self, year, month, day, initialize_df=True):
        self.date = datetime.date(year=year, month=month, day=day)
        orig_dir = f"{c.ORIG_HEART_DIR}heart_rate/heart_rate-{self.date}.json"
        new_dir = f"{c.NEW_HEART_DIR}heart_rate_{self.date}.csv"
        super().__init__(orig_dir=orig_dir, new_dir=new_dir, initialize_df=initialize_df)

    def create_df(self):
        hr_data = self.read_json()
        assert hr_data != [], "Date not available"
        dt, values, confidences = [], [], []
        for hr in hr_data:
            dt_var = datetime.datetime.strptime(hr["dateTime"], "%m/%d/%y %H:%M:%S")
            seconds = round(dt_var.second / 5) * 5
            if seconds == 60:
                dt_var += datetime.timedelta(minutes=1)
                seconds = 0
            dt.append(dt_var.replace(second=seconds))
            values.append(hr["value"]["bpm"])
            confidences.append(hr["value"]["confidence"])
        df = pd.DataFrame({self.dt_col: dt, self.value_col: values, "confidence": confidences})
        df = df.groupby(self.dt_col).agg("mean").reset_index().round(1)

        return df
