import pandas as pd
import utils.constants as c
from classes.base_class import DataClass


class HeartRateVariabilityClass(DataClass):
    def __init__(self):
        super().__init__()
        directory = c.HRV_DETAILED
        self.orig_dir = directory["orig"]
        self.new_dir = directory["new"]
        self.dt_col = "datetime"

    def create_csv(self):
        df = self.read_csv()
        df.timestamp = pd.to_datetime(df.timestamp)
        df = df.rename(columns={"timestamp": self.dt_col, "rmssd": "value"})
        df = df.drop_duplicates()
        df.to_csv(self.new_dir, index=False)


class WristTemperatureClass(DataClass):
    def __init__(self):
        super().__init__()
        directory = c.WRIST_TEMP
        self.orig_dir = directory["orig"]
        self.new_dir = directory["new"]
        self.dt_col = "datetime"

    def create_csv(self):
        df = self.read_csv()
        df.recorded_time = pd.to_datetime(df.recorded_time)
        df = df.rename(columns={"recorded_time": self.dt_col, "temperature": "value"})
        df = df.drop_duplicates()
        df.to_csv(self.new_dir, index=False)


class RespiratoryRateClass(DataClass):
    def __init__(self):
        super().__init__()
        directory = c.DRR
        self.orig_dir = directory["orig"]
        self.new_dir = directory["new"]
        self.dt_col = "date"

    def create_csv(self):
        df = self.read_csv()
        df.timestamp = pd.to_datetime(df.timestamp)
        df = df.groupby(df.timestamp.dt.date).head(1)
        df.timestamp = df.timestamp.dt.date
        df = df.rename(columns={"timestamp": self.dt_col})
        df.to_csv(self.new_dir, index=False)


class DailyHeartRateVariabilityClass(DataClass):
    def __init__(self):
        super().__init__()
        directory = c.HRV_DAILY
        self.orig_dir = directory["orig"]
        self.new_dir = directory["new"]
        self.dt_col = "date"

    def create_csv(self):
        df = self.read_csv()
        df.timestamp = pd.to_datetime(df.timestamp)
        df = df.drop(columns=["nremhr", "entropy"], axis=1)
        df = df.rename(columns={"timestamp": self.dt_col, "rmssd": "value"})
        df = df.drop_duplicates()
        df.to_csv(self.new_dir, index=False)


class HeartRateVariabilityHistClass(DataClass):
    def __init__(self):
        super().__init__()
        directory = c.HRV_HIST
        self.orig_dir = directory["orig"]
        self.new_dir = directory["new"]
        self.dt_col = "date"

    def create_csv(self):
        df = self.read_csv()
        df.timestamp = pd.to_datetime(df.timestamp)
        df = df.groupby(df.timestamp.dt.date).head(1)
        df.timestamp = df.timestamp.dt.date
        dfs = []
        for hist in df.iloc:
            signal = hist.bucket_values[1:-1].split(", ")
            signal = [float(sample) for sample in signal]
            dt = [hist.timestamp] * len(signal)
            dfs += [pd.DataFrame({"date": dt, "value": signal})]
        df = pd.concat(dfs).reset_index(drop=True)
        df.to_csv(self.new_dir, index=False)


class SleepScoreClass(DataClass):
    def __init__(self):
        super().__init__()
        directory = c.SLEEP_SCORE
        self.orig_dir = directory["orig"]
        self.new_dir = directory["new"]
        self.dt_col = "date"

    def create_csv(self):
        df = self.read_csv()
        df = df.drop(columns=["sleep_log_entry_id"], axis=1)
        df.timestamp = pd.to_datetime(df.timestamp)
        df = df.groupby(df.timestamp.dt.date).head(1)
        df.timestamp = df.timestamp.dt.date
        df = df.rename(columns={"timestamp": self.dt_col})
        df.to_csv(self.new_dir, index=False)



