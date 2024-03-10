import pandas as pd
import datetime
import utils.constants as c
from classes.base_class import DataClass


class DailyDataClass(DataClass):
    def __init__(self, orig_dir=None, new_dir=None, daily=False, dt_col="datetime", value_col="value",
                 initialize_df=True):
        self.daily = daily
        super().__init__(orig_dir=orig_dir, new_dir=new_dir, dt_col=dt_col, value_col=value_col,
                         initialize_df=initialize_df)

    def create_df(self):
        data = self.read_json()
        dt, value = [], []
        for sample in data:
            dt_var = datetime.datetime.strptime(sample["dateTime"], "%m/%d/%y %H:%M:%S")
            dt.append(dt_var.replace(second=0))
            value.append(sample["value"])
        df = pd.DataFrame({self.dt_col: dt, self.value_col: value})
        if self.daily:
            df[self.dt_col] = df[self.dt_col].dt.date

        return df


class StepsClass(DailyDataClass):
    def __init__(self, initialize_df=True):
        directory = c.STEPS
        orig_dir = directory["orig"]
        new_dir = directory["new"]
        super().__init__(orig_dir=orig_dir, new_dir=new_dir, initialize_df=initialize_df)


class DistanceClass(DailyDataClass):
    def __init__(self, initialize_df=True):
        directory = c.DISTANCE
        orig_dir = directory["orig"]
        new_dir = directory["new"]
        super().__init__(orig_dir=orig_dir, new_dir=new_dir, initialize_df=initialize_df)


class AltitudeClass(DailyDataClass):
    def __init__(self, initialize_df=True):
        directory = c.ALTITUDE
        orig_dir = directory["orig"]
        new_dir = directory["new"]
        super().__init__(orig_dir=orig_dir, new_dir=new_dir, initialize_df=initialize_df)


class CaloriesClass(DailyDataClass):
    def __init__(self, initialize_df=True):
        directory = c.CALORIES
        orig_dir = directory["orig"]
        new_dir = directory["new"]
        super().__init__(orig_dir=orig_dir, new_dir=new_dir, initialize_df=initialize_df)


class LightlyActiveClass(DailyDataClass):
    def __init__(self, initialize_df=True):
        directory = c.AZM_LIGHT
        orig_dir = directory["orig"]
        new_dir = directory["new"]
        super().__init__(orig_dir=orig_dir, new_dir=new_dir, daily=True, initialize_df=initialize_df)


class ModeratelyActiveClass(DailyDataClass):
    def __init__(self, initialize_df=True):
        directory = c.AZM_MODERATE
        orig_dir = directory["orig"]
        new_dir = directory["new"]
        super().__init__(orig_dir=orig_dir, new_dir=new_dir, daily=True, initialize_df=initialize_df)


class SedentaryClass(DailyDataClass):
    def __init__(self, initialize_df=True):
        directory = c.AZM_SEDENTARY
        orig_dir = directory["orig"]
        new_dir = directory["new"]
        super().__init__(orig_dir=orig_dir, new_dir=new_dir, daily=True, initialize_df=initialize_df)


class VeryActiveClass(DailyDataClass):
    def __init__(self, initialize_df=True):
        directory = c.AZM_VERY_ACTIVE
        orig_dir = directory["orig"]
        new_dir = directory["new"]
        super().__init__(orig_dir=orig_dir, new_dir=new_dir, daily=True, initialize_df=initialize_df)


class DailyReadinessClass(DataClass):
    def __init__(self, initialize_df=True):
        directory = c.DRS
        orig_dir = directory["orig"]
        new_dir = directory["new"]
        super().__init__(orig_dir=orig_dir, new_dir=new_dir, initialize_df=initialize_df)

    def create_df(self):
        df = self.read_csv()
        df.date = pd.to_datetime(df.date)
        df = df.rename(columns={"date": self.dt_col, "readiness_score_value": self.value_col,
                                "activity_subcomponent": "activity_value",
                                "sleep_subcomponent": "sleep_value", "hrv_subcomponent": "hrv_value"})

        return df


class Vo2MaxClass(DataClass):
    def __init__(self, initialize_df=True):
        directory = c.VO2_MAX
        orig_dir = directory["orig"]
        new_dir = directory["new"]
        super().__init__(orig_dir=orig_dir, new_dir=new_dir, initialize_df=initialize_df)

    def create_df(self):
        data = self.read_json()
        dt, value = [], []
        for sample in data:
            dt_var = datetime.datetime.strptime(sample["dateTime"], "%m/%d/%y %H:%M:%S")
            dt.append(dt_var.date())
            value.append(sample["value"]["demographicVO2Max"])
        df = pd.DataFrame({self.dt_col: dt, self.value_col: value})

        return df


class TimeHRZonesClass(DataClass):
    def __init__(self, initialize_df=True):
        directory = c.TIME_IN_HR_ZONES
        orig_dir = directory["orig"]
        new_dir = directory["new"]
        self.fat_burn = 121
        self.cardio = 147
        self.peak = 180
        self.custom_low = 40
        self.custom_high = 200
        super().__init__(orig_dir=orig_dir, new_dir=new_dir, initialize_df=initialize_df)

    def create_df(self):
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

        return df


class ActiveZoneMinClass(DataClass):
    def __init__(self, initialize_df=True):
        directory = c.AZM
        orig_dir = directory["orig"]
        new_dir = directory["new"]
        super().__init__(orig_dir=orig_dir, new_dir=new_dir, initialize_df=initialize_df)

    def create_df(self):
        df = self.read_csv()
        df.date_time = pd.to_datetime(df.date_time)
        df = df.rename(columns={"date_time": self.dt_col, "heart_zone_id": "heart_zone", "total_minutes": "minutes"})

        return df

