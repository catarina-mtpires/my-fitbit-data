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


class DailySleepClass(DataClass):
    def __init__(self, initialize_df=True):
        directory = c.SLEEP
        orig_dir = directory["orig"]
        new_dir = directory["new"]
        self.id_col = "id"
        super().__init__(orig_dir=orig_dir, new_dir=new_dir, initialize_df=initialize_df,
                         additional_dt_cols=["start", "end"])

    def create_df(self):
        sleep_data = self.read_json()
        sleep_id, sleep_date, start_time, end_time, efficiency = [], [], [], [], []
        min_fall_asleep, min_asleep, min_awake, min_after_wakeup, time_in_bed = [], [], [], [], []
        deep_count, wake_count, light_count, rem_count = [], [], [], []
        deep_minutes, wake_minutes, light_minutes, rem_minutes = [], [], [], []
        for sleep in sleep_data:
            if sleep["mainSleep"] and sleep["type"] == "stages":
                sleep_id.append(sleep["logId"])
                sleep_date.append(datetime.datetime.strptime(sleep["dateOfSleep"], "%Y-%m-%d"))
                start_time.append(datetime.datetime.strptime(sleep["startTime"], "%Y-%m-%dT%H:%M:%S.000"))
                end_time.append(datetime.datetime.strptime(sleep["endTime"], "%Y-%m-%dT%H:%M:%S.000"))
                min_fall_asleep.append(sleep["minutesToFallAsleep"])
                min_asleep.append(sleep["minutesAsleep"])
                min_awake.append(sleep["minutesAwake"])
                min_after_wakeup.append(sleep["minutesAfterWakeup"])
                time_in_bed.append(sleep["timeInBed"])
                efficiency.append(sleep["efficiency"])
                deep_count.append(sleep["levels"]["summary"]["deep"]["count"])
                deep_minutes.append(sleep["levels"]["summary"]["deep"]["minutes"])
                wake_count.append(sleep["levels"]["summary"]["wake"]["count"])
                wake_minutes.append(sleep["levels"]["summary"]["wake"]["minutes"])
                light_count.append(sleep["levels"]["summary"]["light"]["count"])
                light_minutes.append(sleep["levels"]["summary"]["light"]["minutes"])
                rem_count.append(sleep["levels"]["summary"]["rem"]["count"])
                rem_minutes.append(sleep["levels"]["summary"]["rem"]["minutes"])

        df = pd.DataFrame({self.id_col: sleep_id, self.dt_col: sleep_date, "start": start_time, "end": end_time,
                           "min_fall_asleep": min_fall_asleep, "min_asleep": min_asleep, "min_awake": min_awake,
                           "min_after_wakeup": min_after_wakeup, "time_in_bed": time_in_bed, "efficiency": efficiency,
                           "wake_count": wake_count, "wake_minutes": wake_minutes,
                           "light_count": light_count, "light_minutes": light_minutes,
                           "deep_count": deep_count, "deep_minutes": deep_minutes,
                           "rem_count": rem_count, "rem_minutes": rem_minutes})

        return df


class DetailedSleepClass(DataClass):
    def __init__(self, initialize_df=True):
        directory = c.DETAILED_SLEEP
        orig_dir = directory["orig"]
        new_dir = directory["new"]
        self.id_col = "id"
        super().__init__(orig_dir=orig_dir, new_dir=new_dir, initialize_df=initialize_df, sort_values=False)

    def create_df(self):
        sleep_data = self.read_json()
        dfs = []
        for sleep in sleep_data:
            if sleep["mainSleep"] and sleep["type"] == "stages":
                ids, dt, level, minutes, short = [], [], [], [], []
                for stage in sleep["levels"]["data"]:
                    ids.append(sleep["logId"])
                    dt.append(datetime.datetime.strptime(stage["dateTime"], "%Y-%m-%dT%H:%M:%S.000"))
                    level.append(stage["level"])
                    minutes.append(stage["seconds"]/60)
                    short.append(False)
                for stage in sleep["levels"]["shortData"]:
                    ids.append(sleep["logId"])
                    dt.append(datetime.datetime.strptime(stage["dateTime"], "%Y-%m-%dT%H:%M:%S.000"))
                    level.append(stage["level"])
                    minutes.append(stage["seconds"]/60)
                    short.append(True)
                df = pd.DataFrame({self.id_col: ids, self.dt_col: dt, "stage": level, "minutes": minutes,
                                   "short_data": short})
                df = df.sort_values(self.dt_col)
                dfs.append(df)

        df = pd.concat(dfs)

        return df


