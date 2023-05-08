# Main Directories
ORIG_DIR = "fitbit_data/original_data/"
NEW_DIR = "fitbit_data/new_data/"

# Single daily data
RHR_DIR = ORIG_DIR + "heart/resting_heart_rate/*.json"
AZM_DIR = ORIG_DIR + "physical_activity/active_minutes/active_zone_minutes/*.csv"
AZM_LIGHT_DIR = ORIG_DIR + "physical_activity/active_minutes/lightly_active_minutes/*.json"
AZM_MODERATE_DIR = ORIG_DIR + "physical_activity/active_minutes/moderately_active_minutes/*.json"
AZM_SEDENTARY_DIR = ORIG_DIR + "physical_activity/active_minutes/sedentary_minutes/*.json"
AZM_VERY_ACTIVE_DIR = ORIG_DIR + "physical_activity/active_minutes/very_active_minutes/*.json"
DRS_DIR = ORIG_DIR + "physical_activity/daily_readiness/*.csv"
VO2_MAX_DIR = ORIG_DIR + "physical_activity/demographic_vo2_max/*.json"
DRR_DIR = ORIG_DIR + "sleep/respiratory_rate/*.csv"
HRV_DAILY_DIR = ORIG_DIR + "sleep/heart_rate_variability/daily/*.csv"
HRV_HIST_DIR = ORIG_DIR + "sleep/heart_rate_variability/histogram/*.csv"
SLEEP_DIR = ORIG_DIR + "sleep/sleep/*.json"
SLEEP_SCORE_DIR = ORIG_DIR + "sleep/sleep/*.csv"
COMP_TEMP_DIR = ORIG_DIR + "sleep/temperature/computed/Computed Temperature - *.csv"
STRESS_SCORE_DIR = ORIG_DIR + "stress/stress_score/*.csv"
TIME_IN_HR_ZONES_DIR = ORIG_DIR + "physical_activity/time_in_heart_rate_zones/*.json"

# Multiple daily data
O2_VAR_DIR = ORIG_DIR + "estimated_oxygen_variation/*.csv"
HR_DIR = ORIG_DIR + "heart/heart_rate/*.json"
STEPS_DIR = ORIG_DIR + "physical_activity/steps/*.json"
DISTANCE_DIR = ORIG_DIR + "physical_activity/distance/*.json"
ALTITUDE_DIR = ORIG_DIR + "physical_activity/altitude/*json"
CALORIES_DIR = ORIG_DIR + "physical_activity/calories/*.json"
HRV_DIR = ORIG_DIR + "sleep/heart_rate_variability/details/*.csv"
WRIST_TEMP_DIR = ORIG_DIR + "sleep/temperature/wrist/*.csv"

# Recorded activity and signals
EXERCISE_DIR = ORIG_DIR + "physical_activity/exercise/*.json"
ECG_DIR = ORIG_DIR + "heart/ecg/*.csv"
SNORE_DIR = ORIG_DIR + "sleep/snore/*.csv"
EDA_DIR = ORIG_DIR + "stress/eda/*.csv"
