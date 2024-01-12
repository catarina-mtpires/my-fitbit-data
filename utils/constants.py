# Main Directories
ORIG_HEART_DIR = "fitbit_data/original_data/heart/"
ORIG_PH_DIR = "fitbit_data/original_data/physical_activity/"
ORIG_SLEEP_DATA_DIR = "fitbit_data/original_data/sleep/"
ORIG_STRESS_DIR = "fitbit_data/original_data/stress/"
ORIG_O2_DIR = "fitbit_data/original_data/estimated_oxygen_variation/"

NEW_HEART_DIR = "fitbit_data/new_data/heart/"
NEW_PH_DIR = "fitbit_data/new_data/physical_activity/"
NEW_SLEEP_DIR = "fitbit_data/new_data/sleep/"
NEW_STRESS_DIR = "fitbit_data/new_data/stress/"
NEW_O2_DIR = "fitbit_data/new_data/estimated_oxygen_variation/"

RHR = {"orig": ORIG_HEART_DIR + "resting_heart_rate/*.json",
       "new": NEW_HEART_DIR + "resting_heart_rate.csv"}
DRS = {"orig": ORIG_PH_DIR + "daily_readiness/*.csv",
       "new": NEW_PH_DIR + "daily_readiness.csv"}
VO2_MAX = {"orig": ORIG_PH_DIR + "demographic_vo2_max/*.json",
           "new": NEW_PH_DIR + "demographic_vo2_max.csv"}
DRR = {"orig": ORIG_SLEEP_DATA_DIR + "respiratory_rate/*.csv",
       "new": NEW_SLEEP_DIR + "respiratory_rate.csv"}
HRV_DAILY = {"orig": ORIG_SLEEP_DATA_DIR + "heart_rate_variability/daily/*.csv",
             "new": NEW_SLEEP_DIR + "heart_rate_variability_daily.csv"}
HRV_HIST = {"orig": ORIG_SLEEP_DATA_DIR + "heart_rate_variability/histogram/*.csv",
            "new": NEW_SLEEP_DIR + "heart_rate_variability_histogram.csv"}
SLEEP_SCORE = {"orig": ORIG_SLEEP_DATA_DIR + "sleep/*.csv",
               "new": NEW_SLEEP_DIR + "sleep_score.csv"}

# Multiple daily data
HR = {"orig": ORIG_HEART_DIR + "heart_rate/*.json",
      "new": NEW_HEART_DIR + "heart_rate.csv"}
O2_VAR = {"orig": ORIG_O2_DIR + "*.csv",
          "new": NEW_O2_DIR + "o2_var.csv"}
STEPS = {"orig": ORIG_PH_DIR + "steps/*.json",
         "new": NEW_PH_DIR + "steps.csv"}
DISTANCE = {"orig": ORIG_PH_DIR + "distance/*.json",
            "new": NEW_PH_DIR + "distance.csv"}
ALTITUDE = {"orig": ORIG_PH_DIR + "altitude/*json",
            "new": NEW_PH_DIR + "altitude.csv"}
CALORIES = {"orig": ORIG_PH_DIR + "calories/*.json",
            "new": NEW_PH_DIR + "calories.csv"}
HRV_DETAILED = {"orig": ORIG_SLEEP_DATA_DIR + "heart_rate_variability/details/*.csv",
                "new": NEW_SLEEP_DIR + "heart_rate_variability_details.csv"}
WRIST_TEMP = {"orig": ORIG_SLEEP_DATA_DIR + "temperature/wrist/*.csv",
              "new": NEW_SLEEP_DIR + "wrist_temperature.csv"}

# Recorded activity and signals
ECG = {"orig": ORIG_HEART_DIR + "ecg/*.csv",
       "new": NEW_HEART_DIR + "ecg.csv"}


# Missing
ORIG_STRESS_SCORE_DIR = ORIG_STRESS_DIR + "stress_score/*.csv"
STRESS_SCORE_DIR = NEW_STRESS_DIR + "stress_score.csv"

ORIG_COMP_TEMP_DIR = ORIG_SLEEP_DATA_DIR + "temperature/computed/Computed Temperature - *.csv"
COMP_TEMP_DIR = NEW_SLEEP_DIR + "computed_temperature.csv"

ORIG_SLEEP_DIR = ORIG_SLEEP_DATA_DIR + "sleep/*.json"
SLEEP_DIR = NEW_SLEEP_DIR + "sleep_data.csv"

ORIG_TIME_IN_HR_ZONES_DIR = ORIG_PH_DIR + "time_in_heart_rate_zones/*.json"
TIME_IN_HR_ZONES_DIR = NEW_PH_DIR + "time_in_heart_rate_zones.csv"

ORIG_AZM_DIR = ORIG_PH_DIR + "active_minutes/active_zone_minutes/*.csv"
AZM_DIR = NEW_PH_DIR + "active_zone_minutes.csv"

ORIG_AZM_LIGHT_DIR = ORIG_PH_DIR + "active_minutes/lightly_active_minutes/*.json"
AZM_LIGHT_DIR = NEW_PH_DIR + "lightly_active_minutes.csv"

ORIG_AZM_MODERATE_DIR = ORIG_PH_DIR + "active_minutes/moderately_active_minutes/*.json"
AZM_MODERATE_DIR = NEW_PH_DIR + "moderately_active_minutes.csv"

ORIG_AZM_SEDENTARY_DIR = ORIG_PH_DIR + "active_minutes/sedentary_minutes/*.json"
AZM_SEDENTARY_DIR = NEW_PH_DIR + "sedentary_minutes.csv"

ORIG_AZM_VERY_ACTIVE_DIR = ORIG_PH_DIR + "active_minutes/very_active_minutes/*.json"
AZM_VERY_ACTIVE_DIR = NEW_PH_DIR + "very_active_minutes.csv"

# Recorded activity and signals
ORIG_EXERCISE_DIR = ORIG_PH_DIR + "exercise/*.json"
EXERCISE_DIR = NEW_PH_DIR + "exercise_data.csv"

ORIG_SNORE_DIR = ORIG_SLEEP_DATA_DIR + "snore/*.csv"
SNORE_DIR = NEW_SLEEP_DIR + "snore_data.csv"

ORIG_EDA_DIR = ORIG_STRESS_DIR + "eda/*.csv"
EDA_DIR = NEW_STRESS_DIR + "eda_data.csv"

