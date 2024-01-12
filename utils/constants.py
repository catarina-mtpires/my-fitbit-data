# Main Directories
ORIG_HEART_DIR = "fitbit_data/original_data/heart/"
ORIG_PH_DIR = "fitbit_data/original_data/physical_activity/"
ORIG_SLEEP_DATA_DIR = "fitbit_data/original_data/sleep/"
ORIG_STRESS_DIR = "fitbit_data/original_data/stress/"
ORIG_O2_DIR = "fitbit_data/original_data/estimated_oxygen_variation/"
ORIG_MENST_DIR = "fitbit_data/original_data/menstrual_health_cycles/"

NEW_HEART_DIR = "fitbit_data/new_data/heart/"
NEW_PH_DIR = "fitbit_data/new_data/physical_activity/"
NEW_SLEEP_DIR = "fitbit_data/new_data/sleep/"
NEW_STRESS_DIR = "fitbit_data/new_data/stress/"
NEW_O2_DIR = "fitbit_data/new_data/estimated_oxygen_variation/"
NEW_MENST_DIR = "fitbit_data/new_data/menstrual_health_cycles/"

RHR = {"orig": ORIG_HEART_DIR + "resting_heart_rate/resting_heart_rate-*.json",
       "new": NEW_HEART_DIR + "resting_heart_rate.csv"}
DRS = {"orig": ORIG_PH_DIR + "daily_readiness/Daily Readiness Score - *.csv",
       "new": NEW_PH_DIR + "daily_readiness.csv"}
VO2_MAX = {"orig": ORIG_PH_DIR + "demographic_vo2_max/demographic_vo2_max-*.json",
           "new": NEW_PH_DIR + "demographic_vo2_max.csv"}
DRR = {"orig": ORIG_SLEEP_DATA_DIR + "respiratory_rate/Respiratory Rate Summary - *.csv",
       "new": NEW_SLEEP_DIR + "respiratory_rate.csv"}
HRV_DAILY = {"orig": ORIG_SLEEP_DATA_DIR + "heart_rate_variability/daily/Daily Heart Rate Variability Summary - *.csv",
             "new": NEW_SLEEP_DIR + "heart_rate_variability_daily.csv"}
HRV_HIST = {"orig": ORIG_SLEEP_DATA_DIR + "heart_rate_variability/histogram/Heart Rate Variability Histogram - *.csv",
            "new": NEW_SLEEP_DIR + "heart_rate_variability_histogram.csv"}
SLEEP_SCORE = {"orig": ORIG_SLEEP_DATA_DIR + "sleep/sleep_score.csv",
               "new": NEW_SLEEP_DIR + "sleep_score.csv"}

# Multiple daily data
HR = {"orig": ORIG_HEART_DIR + "heart_rate/heart_rate-*.json",
      "new": NEW_HEART_DIR + "heart_rate.csv"}
O2_VAR = {"orig": ORIG_O2_DIR + "estimated_oxygen_variation-*.csv",
          "new": NEW_O2_DIR + "o2_var.csv"}
STEPS = {"orig": ORIG_PH_DIR + "steps/steps-*.json",
         "new": NEW_PH_DIR + "steps.csv"}
DISTANCE = {"orig": ORIG_PH_DIR + "distance/distance-*.json",
            "new": NEW_PH_DIR + "distance.csv"}
ALTITUDE = {"orig": ORIG_PH_DIR + "altitude/altitude-*json",
            "new": NEW_PH_DIR + "altitude.csv"}
CALORIES = {"orig": ORIG_PH_DIR + "calories/calories-*.json",
            "new": NEW_PH_DIR + "calories.csv"}
HRV_DETAILED = {"orig": ORIG_SLEEP_DATA_DIR + "heart_rate_variability/details/Heart Rate Variability Details - *.csv",
                "new": NEW_SLEEP_DIR + "heart_rate_variability_details.csv"}
WRIST_TEMP = {"orig": ORIG_SLEEP_DATA_DIR + "temperature/wrist/Wrist Temperature - *.csv",
              "new": NEW_SLEEP_DIR + "wrist_temperature.csv"}

# Recorded activity and signals
ECG = {"orig": ORIG_HEART_DIR + "ecg/ecg_readings.csv",
       "new": NEW_HEART_DIR + "ecg.csv"}

# Missing
ORIG_STRESS_SCORE = ORIG_STRESS_DIR + "stress_score/Stress Score.csv"
STRESS_SCORE = NEW_STRESS_DIR + "stress_score.csv"

ORIG_COMP_TEMP = ORIG_SLEEP_DATA_DIR + "temperature/computed/Computed Temperature - *.csv"
COMP_TEMP = NEW_SLEEP_DIR + "computed_temperature.csv"

ORIG_SLEEP = ORIG_SLEEP_DATA_DIR + "sleep/sleep-*.json"
SLEEP = NEW_SLEEP_DIR + "sleep_data.csv"

ORIG_TIME_IN_HR_ZONES = ORIG_PH_DIR + "time_in_heart_rate_zones/time_in_heart_rate_zones-*.json"
TIME_IN_HR_ZONES = NEW_PH_DIR + "time_in_heart_rate_zones.csv"

ORIG_AZM = ORIG_PH_DIR + "active_minutes/active_zone_minutes/Active Zone Minutes - *.csv"
AZM = NEW_PH_DIR + "active_zone_minutes.csv"

ORIG_AZM_LIGHT = ORIG_PH_DIR + "active_minutes/lightly_active_minutes/lightly_active_minutes-*.json"
AZM_LIGHT = NEW_PH_DIR + "lightly_active_minutes.csv"

ORIG_AZM_MODERATE = ORIG_PH_DIR + "active_minutes/moderately_active_minutes/moderately_active_minutes-*.json"
AZM_MODERATE = NEW_PH_DIR + "moderately_active_minutes.csv"

ORIG_AZM_SEDENTARY = ORIG_PH_DIR + "active_minutes/sedentary_minutes/sedentary_minutes-*.json"
AZM_SEDENTARY = NEW_PH_DIR + "sedentary_minutes.csv"

ORIG_AZM_VERY_ACTIVE = ORIG_PH_DIR + "active_minutes/very_active_minutes/very_active_minutes-*.json"
AZM_VERY_ACTIVE = NEW_PH_DIR + "very_active_minutes.csv"

# Recorded activity and signals
ORIG_EXERCISE = ORIG_PH_DIR + "exercise/exercise-*.json"
EXERCISE = NEW_PH_DIR + "exercise_data.csv"

ORIG_SNORE = ORIG_SLEEP_DATA_DIR + "snore/Snore Details - *.csv"
SNORE = NEW_SLEEP_DIR + "snore_data.csv"

ORIG_EDA = ORIG_STRESS_DIR + "eda/mindfulness_eda_data_sessions.csv"
EDA = NEW_STRESS_DIR + "eda_data.csv"

ORIG_MENST = ORIG_MENST_DIR + "menstrual_health_cycles.csv"
MENST = NEW_MENST_DIR + "menstrual_cycles.csv"

ORIG_MIN_SPO2 = ORIG_SLEEP + "minute_spo2/Minute SpO2 - *.csv"
MIN_SPO2 = NEW_SLEEP_DIR + "minute_spo2.csv"
