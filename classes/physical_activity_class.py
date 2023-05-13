import pandas as pd
import datetime
import utils.constants as c
from classes.base_class import DataClass


class DailyDataClass(DataClass):
    def __init__(self):
        super().__init__()
        self.dt_col = "datetime"

    def create_csv(self):
        data = self.read_json()
        dt, value = [], []
        for sample in data:
            if sample["value"] != 0:
                dt_var = datetime.datetime.strptime(sample["dateTime"], "%m/%d/%y %H:%M:%S")
                dt.append(dt_var.replace(second=0))
                value.append(sample["value"])
        df = pd.DataFrame({"datetime": dt, "value": value})
        df = df.drop_duplicates()
        df.to_csv(self.new_dir, index=False)


class StepsClass(DailyDataClass):
    def __init__(self):
        super().__init__()
        self.orig_dir = c.ORIG_STEPS_DIR
        self.new_dir = c.STEPS_DIR
        self.df = self.get_df()


class DistanceClass(DailyDataClass):
    def __init__(self):
        super().__init__()
        self.orig_dir = c.ORIG_DISTANCE_DIR
        self.new_dir = c.DISTANCE_DIR
        self.df = self.get_df()


class AltitudeClass(DailyDataClass):
    def __init__(self):
        super().__init__()
        self.orig_dir = c.ORIG_ALTITUDE_DIR
        self.new_dir = c.ALTITUDE_DIR
        self.df = self.get_df()


class CaloriesClass(DailyDataClass):
    def __init__(self):
        super().__init__()
        self.orig_dir = c.ORIG_CALORIES_DIR
        self.new_dir = c.CALORIES_DIR
        self.df = self.get_df()
