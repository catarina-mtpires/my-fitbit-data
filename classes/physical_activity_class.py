import pandas as pd
import datetime
import utils.constants as c
from classes.base_class import DataClass


class DailyDataClass(DataClass):
    def __init__(self, directory, daily=False, dt_col="datetime", value_col="value",
                 initialize_df=True, name=None):
        self.daily = daily
        super().__init__(directory=directory, dt_col=dt_col, value_col=value_col,
                         initialize_df=initialize_df, name=name)

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
    def __init__(self, initialize_df=True, name="steps"):
        directory = c.STEPS
        super().__init__(directory=directory, initialize_df=initialize_df, name=name)


class DistanceClass(DailyDataClass):
    def __init__(self, initialize_df=True, name="distance"):
        directory = c.DISTANCE
        super().__init__(directory=directory, initialize_df=initialize_df, name=name)


class AltitudeClass(DailyDataClass):
    def __init__(self, initialize_df=True, name="altitude"):
        directory = c.ALTITUDE
        super().__init__(directory=directory, initialize_df=initialize_df, name=name)


class CaloriesClass(DailyDataClass):
    def __init__(self, initialize_df=True, name="calories"):
        directory = c.CALORIES
        super().__init__(directory=directory, initialize_df=initialize_df, name=name)


class LightlyActiveClass(DailyDataClass):
    def __init__(self, initialize_df=True, name="lightly_active"):
        directory = c.AZM_LIGHT
        super().__init__(directory=directory, daily=True, initialize_df=initialize_df, name=name)


class ModeratelyActiveClass(DailyDataClass):
    def __init__(self, initialize_df=True, name="moderately_active"):
        directory = c.AZM_MODERATE
        super().__init__(directory=directory, daily=True, initialize_df=initialize_df, name=name)


class SedentaryClass(DailyDataClass):
    def __init__(self, initialize_df=True, name="sedentary"):
        directory = c.AZM_SEDENTARY
        super().__init__(directory=directory, daily=True, initialize_df=initialize_df, name=name)


class VeryActiveClass(DailyDataClass):
    def __init__(self, initialize_df=True, name="very_active"):
        directory = c.AZM_VERY_ACTIVE
        super().__init__(directory=directory, daily=True, initialize_df=initialize_df, name=name)


class DailyReadinessClass(DataClass):
    def __init__(self, initialize_df=True, name="daily_readiness"):
        directory = c.DRS
        super().__init__(directory=directory, initialize_df=initialize_df, name=name)

    def create_df(self):
        df = self.read_csv()
        df.date = pd.to_datetime(df.date)
        df = df.rename(columns={"date": self.dt_col, "readiness_score_value": self.value_col,
                                "activity_subcomponent": "activity_value",
                                "sleep_subcomponent": "sleep_value", "hrv_subcomponent": "hrv_value"})

        return df


class Vo2MaxClass(DataClass):
    def __init__(self, initialize_df=True, name="vo2_max"):
        directory = c.VO2_MAX
        super().__init__(directory=directory, initialize_df=initialize_df, name=name)

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
    def __init__(self, initialize_df=True, name="time_hr_zones"):
        directory = c.TIME_IN_HR_ZONES
        self.fat_burn = 121
        self.cardio = 147
        self.peak = 180
        self.custom_low = 40
        self.custom_high = 200
        super().__init__(directory=directory, initialize_df=initialize_df, name=name)

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
    def __init__(self, initialize_df=True, name="active_zone_minutes"):
        directory = c.AZM
        super().__init__(directory=directory, initialize_df=initialize_df, name=name)

    def create_df(self):
        df = self.read_csv()
        df.date_time = pd.to_datetime(df.date_time)
        df = df.rename(columns={"date_time": self.dt_col, "heart_zone_id": "heart_zone", "total_minutes": "minutes"})

        return df


class ExerciseClass(DataClass):
    def __init__(self, initialize_df=True, name="exercise"):
        directory = c.EXERCISE
        super().__init__(directory=directory, initialize_df=initialize_df, name=name)

    def create_df(self):
        data = self.read_json()
        common_vars = ["activityName", "startTime", "duration", "averageHeartRate", "calories", "heartRateZones"]
        all_vars = common_vars + ["elevationGain", "steps"]
        var_names_dict = {
            "Aerobic Workout": common_vars + ["steps"],
            "Sport": common_vars + ["steps"],
            "Fitstar: Personal Trainer": common_vars + ["steps"],
            "Outdoor Bike": common_vars + ["elevationGain"],
            "Walk": all_vars, "Workout": all_vars, "Weights": all_vars, "Spinning": all_vars, "Elliptical": all_vars,
            "Treadmill": all_vars, "Hike": all_vars, "Run": all_vars
        }
        activity, start_time, duration, avg_hr, calories, elevation_gain, steps, out_range_min, out_range_cal,\
            fat_burn_min, fat_burn_cal, cardio_min, cardio_cal, peak_min, peak_cal = [], [], [], [], [], [], [], [],\
            [], [], [], [], [], [], []

        for exercise in data:
            if exercise["activityName"] in list(var_names_dict.keys()):
                ex_vars = var_names_dict[exercise["activityName"]]
                if set(ex_vars).difference(exercise.keys()) == set():
                    activity.append(exercise["activityName"])
                    start_time.append(datetime.datetime.strptime(exercise["startTime"], "%m/%d/%y %H:%M:%S"))
                    duration.append(round(exercise["duration"]/60000, 1))
                    avg_hr.append(exercise["averageHeartRate"])
                    calories.append(exercise["calories"])
                    for hr_zone in exercise["heartRateZones"]:
                        if hr_zone["name"] == "Out of Range":
                            out_range_min.append(hr_zone["minutes"])
                            out_range_cal.append(hr_zone["caloriesOut"])
                        elif hr_zone["name"] == "Fat Burn":
                            fat_burn_min.append(hr_zone["minutes"])
                            fat_burn_cal.append(hr_zone["caloriesOut"])
                        elif hr_zone["name"] == "Cardio":
                            cardio_min.append(hr_zone["minutes"])
                            cardio_cal.append(hr_zone["caloriesOut"])
                        elif hr_zone["name"] == "Peak":
                            peak_min.append(hr_zone["minutes"])
                            peak_cal.append(hr_zone["caloriesOut"])

                    if "elevationGain" in ex_vars:
                        elevation_gain.append(exercise["elevationGain"])
                    else:
                        elevation_gain.append(None)
                    if "steps" in ex_vars:
                        steps.append(exercise["steps"])
                    else:
                        steps.append(None)

        df = pd.DataFrame({"activity": activity, self.dt_col: start_time, "duration": duration, "average_hr": avg_hr,
                           "calories": calories, "elevation_gain": elevation_gain, "steps": steps,
                           "out_range_min": out_range_min, "out_range_cal": out_range_cal, "fat_burn_min": fat_burn_min,
                           "fat_burn_cal": fat_burn_cal, "cardio_min": cardio_min, "cardio_cal": cardio_cal,
                           "peak_min": peak_min, "peak_cal": peak_cal})

        return df
