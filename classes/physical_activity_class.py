import pandas as pd
import datetime
import utils.constants as c
from classes.base_class import DataClass


class DailyDataClass(DataClass):
    def __init__(self):
        super().__init__()

    def create_csv(self):
        data = self.read_json()
        dt, value = [], []
        for sample in data:
            dt_var = datetime.datetime.strptime(sample["dateTime"], "%m/%d/%y %H:%M:%S")
            dt.append(dt_var.replace(second=0))
            value.append(sample["value"])
        df = pd.DataFrame({self.dt_col: dt, self.value_col: value})
        df = df.drop_duplicates()
        df.to_csv(self.new_dir, index=False)


class StepsClass(DailyDataClass):
    def __init__(self):
        super().__init__()
        directory = c.STEPS
        self.orig_dir = directory["orig"]
        self.new_dir = directory["new"]


class DistanceClass(DailyDataClass):
    def __init__(self):
        super().__init__()
        directory = c.DISTANCE
        self.orig_dir = directory["orig"]
        self.new_dir = directory["new"]


class AltitudeClass(DailyDataClass):
    def __init__(self):
        super().__init__()
        directory = c.ALTITUDE
        self.orig_dir = directory["orig"]
        self.new_dir = directory["new"]


class CaloriesClass(DailyDataClass):
    def __init__(self):
        super().__init__()
        directory = c.CALORIES
        self.orig_dir = directory["orig"]
        self.new_dir = directory["new"]


class DailyReadinessClass(DataClass):
    def __init__(self):
        super().__init__()
        directory = c.DRS
        self.orig_dir = directory["orig"]
        self.new_dir = directory["new"]

    def create_csv(self):
        df = self.read_csv()
        df.date = pd.to_datetime(df.date)
        df = df.rename(columns={"date": self.dt_col, "readiness_score_value": self.value_col, "activity_subcomponent": "activity_value",
                                "sleep_subcomponent": "sleep_value", "hrv_subcomponent": "hrv_value"})
        df = df.drop_duplicates()
        df.to_csv(self.new_dir, index=False)


class Vo2MaxClass(DataClass):
    def __init__(self):
        super().__init__()
        directory = c.VO2_MAX
        self.orig_dir = directory["orig"]
        self.new_dir = directory["new"]

    def create_csv(self):
        data = self.read_json()
        dt, value = [], []
        for sample in data:
            dt_var = datetime.datetime.strptime(sample["dateTime"], "%m/%d/%y %H:%M:%S")
            dt.append(dt_var.date())
            value.append(sample["value"]["demographicVO2Max"])
        df = pd.DataFrame({self.dt_col: dt, self.value_col: value})
        df = df.drop_duplicates()
        df.to_csv(self.new_dir, index=False)


class TimeHRZonesClass(DataClass):
    def __init__(self):
        super().__init__()
        directory = c.TIME_IN_HR_ZONES
        self.orig_dir = directory["orig"]
        self.new_dir = directory["new"]
        self.fat_burn = 121
        self.cardio = 147
        self.peak = 180
        self.custom_low = 40
        self.custom_high = 200

    def create_csv(self):
        data = self.read_json()
        dt, zone0, zone1, zone2, zone3, below_custom, in_custom, above_custom = [], [], [], [], [], [], [], []
        for sample in data:
            dt_var = datetime.datetime.strptime(sample["dateTime"], "%m/%d/%y %H:%M:%S")
            dt.append(dt_var.date())
            zone0.append(sample["value"]["valuesInZones"]["BELOW_DEFAULT_ZONE_1"])
            zone1.append(sample["value"]["valuesInZones"]["IN_DEFAULT_ZONE_1"])
            zone2.append(sample["value"]["valuesInZones"]["IN_DEFAULT_ZONE_2"])
            zone3.append(sample["value"]["valuesInZones"]["IN_DEFAULT_ZONE_3"])
            if "BELOW_CUSTOM_ZONE" in sample["value"]["valuesInZones"]:
                below_custom.append(sample["value"]["valuesInZones"]["BELOW_CUSTOM_ZONE"])
                in_custom.append(sample["value"]["valuesInZones"]["IN_CUSTOM_ZONE"])
                above_custom.append(sample["value"]["valuesInZones"]["ABOVE_CUSTOM_ZONE"])
            else:
                below_custom.append(0)
                in_custom.append(0)
                above_custom.append(0)

        df = pd.DataFrame({self.dt_col: dt, "below_0": zone0, "fat_burn": zone1, "cardio": zone2, "peak": zone3,
                           "below_custom": below_custom, "in_custom": in_custom, "above_custom": above_custom})
        df = df.drop_duplicates()
        df.to_csv(self.new_dir, index=False)

