import datetime
import pandas as pd
import utils.constants as c
from time import strptime
from classes.base_class import DataClass


class HeartRateVariabilityClass(DataClass):
    def __init__(self):
        super().__init__()
        self.orig_dir = c.ORIG_HRV_DIR
        self.new_dir = c.HRV_DIR
        self.dt_col = "datetime"
        self.df = self.get_df()

    def create_csv(self):
        df = self.read_csv()
        df.timestamp = pd.to_datetime(df.timestamp)
        df = df.rename(columns={"timestamp": "datetime", "rmssd": "value"})
        df = df.drop_duplicates()
        df.to_csv(self.new_dir, index=False)


class WristTemperatureClass(DataClass):
    def __init__(self):
        super().__init__()
        self.orig_dir = c.ORIG_WRIST_TEMP_DIR
        self.new_dir = c.WRIST_TEMP_DIR
        self.dt_col = "datetime"
        self.df = self.get_df()

    def create_csv(self):
        df = self.read_csv()
        df.recorded_time = pd.to_datetime(df.recorded_time)
        df = df.rename(columns={"recorded_time": "datetime", "temperature": "value"})
        df = df.drop_duplicates()
        df.to_csv(self.new_dir, index=False)
