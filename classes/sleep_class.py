import datetime
import pandas as pd
import utils.constants as c
from classes.base_class import DataClass


class HeartRateVariabilityClass(DataClass):
    def __init__(self, initialize_df=True):
        directory = c.HRV_DETAILED
        orig_dir = directory["orig"]
        new_dir = directory["new"]
        super().__init__(orig_dir=orig_dir, new_dir=new_dir, initialize_df=initialize_df)

    def create_df(self):
        df = self.read_csv()
        df.timestamp = pd.to_datetime(df.timestamp)
        df = df.rename(columns={"timestamp": self.dt_col, "rmssd": self.value_col})

        return df


class WristTemperatureClass(DataClass):
    def __init__(self, initialize_df=True):
        directory = c.WRIST_TEMP
        orig_dir = directory["orig"]
        new_dir = directory["new"]
        super().__init__(orig_dir=orig_dir, new_dir=new_dir, initialize_df=initialize_df)

    def create_df(self):
        df = self.read_csv()
        df.recorded_time = pd.to_datetime(df.recorded_time)
        df = df.rename(columns={"recorded_time": self.dt_col, "temperature": self.value_col})

        return df


class ComputedTemperatureClass(DataClass):
    def __init__(self, initialize_df=True):
        directory = c.COMP_TEMP
        orig_dir = directory["orig"]
        new_dir = directory["new"]
        super().__init__(orig_dir=orig_dir, new_dir=new_dir, initialize_df=initialize_df)

    def create_df(self):
        df = self.read_csv()
        df = df.drop(columns=["type", "sleep_start"], axis=1)
        df = df.rename(columns={"sleep_end": self.dt_col, "nightly_temperature": self.value_col})
        df[self.dt_col] = pd.to_datetime(df[self.dt_col].str[:16]).dt.date

        return df


class RespiratoryRateClass(DataClass):
    def __init__(self, initialize_df=True):
        directory = c.RR
        orig_dir = directory["orig"]
        new_dir = directory["new"]
        super().__init__(orig_dir=orig_dir, new_dir=new_dir, initialize_df=initialize_df)

    def create_df(self):
        df = self.read_csv()
        df.timestamp = pd.to_datetime(df.timestamp)
        df = df.groupby(df.timestamp.dt.date).head(1)
        df.timestamp = df.timestamp.dt.date
        df = df.rename(columns={"timestamp": self.dt_col})

        return df


class DailyHeartRateVariabilityClass(DataClass):
    def __init__(self, initialize_df=True):
        directory = c.HRV_DAILY
        orig_dir = directory["orig"]
        new_dir = directory["new"]
        super().__init__(orig_dir=orig_dir, new_dir=new_dir, initialize_df=initialize_df)

    def create_df(self):
        df = self.read_csv()
        df.timestamp = pd.to_datetime(df.timestamp)
        # df = df.drop(columns=["nremhr", "entropy"], axis=1)
        df = df.rename(columns={"timestamp": self.dt_col, "rmssd": self.value_col})

        return df


class HeartRateVariabilityHistClass(DataClass):
    def __init__(self, initialize_df=True):
        directory = c.HRV_HIST
        orig_dir = directory["orig"]
        new_dir = directory["new"]
        super().__init__(orig_dir=orig_dir, new_dir=new_dir, initialize_df=initialize_df, sort_values=False)

    def create_df(self):
        df = self.read_csv()
        df.timestamp = pd.to_datetime(df.timestamp)
        df = df.groupby(df.timestamp.dt.date).head(1)
        df.timestamp = df.timestamp.dt.date
        dfs = []
        for hist in df.iloc:
            signal = hist.bucket_values[1:-1].split(", ")
            signal = [float(sample) for sample in signal]
            dt = [hist.timestamp] * len(signal)
            hrv = [round(0.3 + x * 0.05, 2) for x in range(len(signal))]
            dfs += [pd.DataFrame({self.dt_col: dt, self.value_col: signal, "hrv": hrv})]
        df = pd.concat(dfs).reset_index(drop=True)

        return df


class SleepScoreClass(DataClass):
    def __init__(self, initialize_df=True):
        directory = c.SLEEP_SCORE
        orig_dir = directory["orig"]
        new_dir = directory["new"]
        super().__init__(orig_dir=orig_dir, new_dir=new_dir, initialize_df=initialize_df)

    def create_df(self):
        df = self.read_csv()
        df = df.drop(columns=["sleep_log_entry_id"], axis=1)
        df.timestamp = pd.to_datetime(df.timestamp)
        df = df.groupby(df.timestamp.dt.date).head(1)
        df.timestamp = df.timestamp.dt.date
        df = df.rename(columns={"timestamp": self.dt_col, "overall_score": self.value_col})

        return df


class MinSPO2Class(DataClass):
    def __init__(self, initialize_df=True):
        directory = c.MIN_SPO2
        orig_dir = directory["orig"]
        new_dir = directory["new"]
        super().__init__(orig_dir=orig_dir, new_dir=new_dir, initialize_df=initialize_df)

    def create_df(self):
        df = self.read_csv()
        df.timestamp = pd.to_datetime(df.timestamp).dt.round(freq="min")
        df = df.rename(columns={"timestamp": self.dt_col})
        df = df.groupby(self.dt_col).agg("mean").reset_index().round(1)

        return df


class SnoreClass(DataClass):
    def __init__(self, initialize_df=True):
        directory = c.SNORE
        orig_dir = directory["orig"]
        new_dir = directory["new"]
        super().__init__(orig_dir=orig_dir, new_dir=new_dir, initialize_df=initialize_df)

    def create_df(self):
        df = self.read_csv()
        df.timestamp = pd.to_datetime(df.timestamp)
        df = df.drop(columns=["sample_duration"], axis=1)
        df = df.rename(columns={"timestamp": self.dt_col, "mean_dba": self.value_col})

        return df
