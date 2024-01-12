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
            dt_var = datetime.datetime.strptime(sample["dateTime"], "%m/%d/%y %H:%M:%S")
            dt.append(dt_var.replace(second=0))
            value.append(sample["value"])
        df = pd.DataFrame({"datetime": dt, "value": value})
        df = df.drop_duplicates()
        df.to_csv(self.new_dir, index=False)


class StepsClass(DailyDataClass):
    def __init__(self):
        super().__init__()
        directory = c.STEPS
        self.orig_dir = directory["orig"]
        self.new_dir = directory["new"]
        self.df = self.get_df()


class DistanceClass(DailyDataClass):
    def __init__(self):
        super().__init__()
        directory = c.DISTANCE
        self.orig_dir = directory["orig"]
        self.new_dir = directory["new"]
        self.df = self.get_df()


class AltitudeClass(DailyDataClass):
    def __init__(self):
        super().__init__()
        directory = c.ALTITUDE
        self.orig_dir = directory["orig"]
        self.new_dir = directory["new"]
        self.df = self.get_df()


class CaloriesClass(DailyDataClass):
    def __init__(self):
        super().__init__()
        directory = c.CALORIES
        self.orig_dir = directory["orig"]
        self.new_dir = directory["new"]
        self.df = self.get_df()


class DailyReadinessClass(DataClass):
    def __init__(self):
        super().__init__()
        directory = c.DRS
        self.orig_dir = directory["orig"]
        self.new_dir = directory["new"]
        self.dt_col = "date"
        self.df = self.get_df()

    def create_csv(self):
        df = self.read_csv()
        df.date = pd.to_datetime(df.date)
        df = df.rename(columns={"readiness_score_value": "value", "activity_subcomponent": "activity_value",
                                "sleep_subcomponent": "sleep_value", "hrv_subcomponent": "hrv_value"})
        df = df.drop_duplicates()
        df.to_csv(self.new_dir, index=False)


class Vo2MaxClass(DataClass):
    def __init__(self):
        super().__init__()
        directory = c.VO2_MAX
        self.orig_dir = directory["orig"]
        self.new_dir = directory["new"]
        self.dt_col = "date"
        self.df = self.get_df()

    def create_csv(self):
        data = self.read_json()
        dt, value = [], []
        for sample in data:
            dt_var = datetime.datetime.strptime(sample["dateTime"], "%m/%d/%y %H:%M:%S")
            dt.append(dt_var.date())
            value.append(sample["value"]["demographicVO2Max"])
        df = pd.DataFrame({"date": dt, "value": value})
        df = df.drop_duplicates()
        df.to_csv(self.new_dir, index=False)

