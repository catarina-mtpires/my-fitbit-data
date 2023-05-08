# Main Directories
HEART_MAIN_DIR = "fitbit_data/heart/"
STRESS_MAIN_DIR = "fitbit_data/stress/"
PHYSICAL_ACTIVITY_MAIN_DIR = "fitbit_data/physical_activity/"
SLEEP_MAIN_DIR = "fitbit_data/sleep/"
O2_VAR_MAIN_DIR = "fitbit_data/estimated_oxygen_variation/"

# Single daily data
RHR_DIR = HEART_MAIN_DIR + "resting_heart_rate/*.json"
AZM_DIR = PHYSICAL_ACTIVITY_MAIN_DIR + "active_minutes/active_zone_minutes/*.csv"
AZM_LIGHT_DIR = PHYSICAL_ACTIVITY_MAIN_DIR + "active_minutes/lightly_active_minutes/*.json"
AZM_MODERATE_DIR = PHYSICAL_ACTIVITY_MAIN_DIR + "active_minutes/moderately_active_minutes/*.json"
AZM_SEDENTARY_DIR = PHYSICAL_ACTIVITY_MAIN_DIR + "active_minutes/sedentary_minutes/*.json"
AZM_VERY_ACTIVE_DIR = PHYSICAL_ACTIVITY_MAIN_DIR + "active_minutes/very_active_minutes/*.json"
DRS_DIR = PHYSICAL_ACTIVITY_MAIN_DIR + "daily_readiness/*.csv"
VO2_MAX_DIR = PHYSICAL_ACTIVITY_MAIN_DIR + "demographic_vo2_max/*.json"
DRR_DIR = SLEEP_MAIN_DIR + "respiratory_rate/*.csv"
HRV_DAILY_DIR = SLEEP_MAIN_DIR + "heart_rate_variability/daily/*.csv"
HRV_HIST_DIR = SLEEP_MAIN_DIR + "heart_rate_variability/histogram/*.csv"
SLEEP_DIR = SLEEP_MAIN_DIR + "sleep/*.json"
SLEEP_SCORE_DIR = SLEEP_MAIN_DIR + "sleep/*.csv"
COMP_TEMP_DIR = SLEEP_MAIN_DIR + "temperature/computed/Computed Temperature - *.csv"
STRESS_SCORE_DIR = STRESS_MAIN_DIR + "stress_score/*.csv"
TIME_IN_HR_ZONES_DIR = PHYSICAL_ACTIVITY_MAIN_DIR + "time_in_heart_rate_zones/*.json"

# Multiple daily data
O2_VAR_DIR = O2_VAR_MAIN_DIR + "*.csv"
HR_DIR = HEART_MAIN_DIR + "heart_rate/*.json"
STEPS_DIR = PHYSICAL_ACTIVITY_MAIN_DIR + "steps/*.json"
DISTANCE_DIR = PHYSICAL_ACTIVITY_MAIN_DIR + "distance/*.json"
ALTITUDE_DIR = PHYSICAL_ACTIVITY_MAIN_DIR + "altitude/*json"
CALORIES_DIR = PHYSICAL_ACTIVITY_MAIN_DIR + "calories/*.json"
HRV_DIR = SLEEP_MAIN_DIR + "heart_rate_variability/details/*.csv"
WRIST_TEMP_DIR = SLEEP_MAIN_DIR + "temperature/wrist/*.csv"

# Recorded activity and signals
EXERCISE_DIR = PHYSICAL_ACTIVITY_MAIN_DIR + "exercise/*.json"
ECG_DIR = HEART_MAIN_DIR + "ecg/*.csv"
SNORE_DIR = SLEEP_MAIN_DIR + "snore/*.csv"
EDA_DIR = STRESS_MAIN_DIR + "eda/*.csv"




