import classes.hr_class as hr_class
import classes.o2_var_class as o2_var_class
import classes.physical_activity_class as ph_class
import classes.sleep_class as sleep_class


hr = hr_class.HeartRateClass()
rhr = hr_class.RestingHeartRateClass()
ecg = hr_class.ECGClass()
hr_complete = hr_class.HeartRateCompleteClass(year=2022, month=5, day=13)

o2_var = o2_var_class.O2VarClass()

steps = ph_class.StepsClass()
distance = ph_class.DistanceClass()
altitude = ph_class.AltitudeClass()
calories = ph_class.CaloriesClass()
drs = ph_class.DailyReadinessClass()
vo2_max = ph_class.Vo2MaxClass()

hrv = sleep_class.HeartRateVariabilityClass()
wrist_temp = sleep_class.WristTemperatureClass()
drr = sleep_class.RespiratoryRateClass()
dhrv = sleep_class.DailyHeartRateVariabilityClass()
hist_hrv = sleep_class.HeartRateVariabilityHistClass()
sleep_score = sleep_class.SleepScoreClass()



