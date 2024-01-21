# Main Directories
ORIG_HEART_DIR = "fitbit_data/original_data/heart/"
ORIG_PH_DIR = "fitbit_data/original_data/physical_activity/"
ORIG_SLEEP_DIR = "fitbit_data/original_data/sleep/"
ORIG_STRESS_DIR = "fitbit_data/original_data/stress/"
ORIG_O2_DIR = "fitbit_data/original_data/estimated_oxygen_variation/"
ORIG_MENST_DIR = "fitbit_data/original_data/menstrual_cycles/"

NEW_HEART_DIR = "fitbit_data/new_data/heart/"
NEW_PH_DIR = "fitbit_data/new_data/physical_activity/"
NEW_SLEEP_DIR = "fitbit_data/new_data/sleep/"
NEW_STRESS_DIR = "fitbit_data/new_data/stress/"
NEW_O2_DIR = "fitbit_data/new_data/estimated_oxygen_variation/"
NEW_MENST_DIR = "fitbit_data/new_data/menstrual_cycles/"

# Single daily data
RHR = {"orig": ORIG_HEART_DIR + "resting_heart_rate/resting_heart_rate-*.json",
       "new": NEW_HEART_DIR + "resting_heart_rate.csv"}
DRS = {"orig": ORIG_PH_DIR + "daily_readiness/Daily Readiness Score - *.csv",
       "new": NEW_PH_DIR + "daily_readiness.csv"}
VO2_MAX = {"orig": ORIG_PH_DIR + "demographic_vo2_max/demographic_vo2_max-*.json",
           "new": NEW_PH_DIR + "demographic_vo2_max.csv"}
RR = {"orig": ORIG_SLEEP_DIR + "respiratory_rate/Respiratory Rate Summary - *.csv",
       "new": NEW_SLEEP_DIR + "respiratory_rate.csv"}
HRV_DAILY = {"orig": ORIG_SLEEP_DIR + "heart_rate_variability/daily/Daily Heart Rate Variability Summary - *.csv",
             "new": NEW_SLEEP_DIR + "heart_rate_variability_daily.csv"}
HRV_HIST = {"orig": ORIG_SLEEP_DIR + "heart_rate_variability/histogram/Heart Rate Variability Histogram - *.csv",
            "new": NEW_SLEEP_DIR + "heart_rate_variability_histogram.csv"}
SLEEP_SCORE = {"orig": ORIG_SLEEP_DIR + "sleep/sleep_score.csv",
               "new": NEW_SLEEP_DIR + "sleep_score.csv"}
STRESS_SCORE = {"orig": ORIG_STRESS_DIR + "stress_score/Stress Score.csv",
                "new": NEW_STRESS_DIR + "stress_score.csv"}
COMP_TEMP = {"orig": ORIG_SLEEP_DIR + "temperature/computed/Computed Temperature - *.csv",
             "new": NEW_SLEEP_DIR + "computed_temperature.csv"}
TIME_IN_HR_ZONES = {"orig": ORIG_PH_DIR + "time_in_heart_rate_zones/time_in_heart_rate_zones-*.json",
                    "new": NEW_PH_DIR + "time_in_heart_rate_zones.csv"}

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
HRV_DETAILED = {"orig": ORIG_SLEEP_DIR + "heart_rate_variability/details/Heart Rate Variability Details - *.csv",
                "new": NEW_SLEEP_DIR + "heart_rate_variability_details.csv"}
WRIST_TEMP = {"orig": ORIG_SLEEP_DIR + "temperature/wrist/Wrist Temperature - *.csv",
              "new": NEW_SLEEP_DIR + "wrist_temperature.csv"}
MIN_SPO2 = {"orig": ORIG_SLEEP_DIR + "minute_spo2/Minute SpO2 - *.csv",
            "new": NEW_SLEEP_DIR + "minute_spo2.csv"}

# Recorded activity and signals
ECG = {"orig": ORIG_HEART_DIR + "ecg/afib_ecg_reading_*.csv",
       "new": NEW_HEART_DIR + "ecg.csv"}
EDA = {"orig": ORIG_STRESS_DIR + "eda/mindfulness_eda_data_sessions.csv",
       "new": NEW_STRESS_DIR + "eda_data.csv"}
SNORE = {"orig": ORIG_SLEEP_DIR + "snore/Snore Details - *.csv",
         "new": NEW_SLEEP_DIR + "snore_data.csv"}

# Other
MENST = {"orig": ORIG_MENST_DIR + "menstrual_health_cycles.csv",
         "new": NEW_MENST_DIR + "menstrual_cycles.csv"}


# Missing
SLEEP = {"orig": ORIG_SLEEP_DIR + "sleep/sleep-*.json",
         "new": NEW_SLEEP_DIR + "sleep_data.csv"}

AZM = {"orig": ORIG_PH_DIR + "active_minutes/active_zone_minutes/Active Zone Minutes - *.csv",
       "new": NEW_PH_DIR + "active_zone_minutes.csv"}

AZM_LIGHT = {"orig": ORIG_PH_DIR + "active_minutes/lightly_active_minutes/lightly_active_minutes-*.json",
             "new": NEW_PH_DIR + "lightly_active_minutes.csv"}

AZM_MODERATE = {"orig": ORIG_PH_DIR + "active_minutes/moderately_active_minutes/moderately_active_minutes-*.json",
                "new": NEW_PH_DIR + "moderately_active_minutes.csv"}

AZM_SEDENTARY = {"orig": ORIG_PH_DIR + "active_minutes/sedentary_minutes/sedentary_minutes-*.json",
                 "new": NEW_PH_DIR + "sedentary_minutes.csv"}

AZM_VERY_ACTIVE = {"orig": ORIG_PH_DIR + "active_minutes/very_active_minutes/very_active_minutes-*.json",
                   "new": NEW_PH_DIR + "very_active_minutes.csv"}

EXERCISE = {"orig": ORIG_PH_DIR + "exercise/exercise-*.json",
            "new": NEW_PH_DIR + "exercise_data.csv"}







