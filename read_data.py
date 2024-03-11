import classes.hr_class as hr_class
import classes.o2_var_class as o2_var_class
import classes.physical_activity_class as ph_class
import classes.sleep_class as sleep_class
import classes.stress_class as stress_class
import classes.m_cycles_class as m_cycles_class

done = True
if done:
    hr = hr_class.HeartRateClass()
    rhr = hr_class.RestingHeartRateClass()
    ecg = hr_class.ECGClass()
    hr_complete = hr_class.HeartRateCompleteClass(year=2023, month=5, day=13)

    o2_var = o2_var_class.O2VarClass()

    steps = ph_class.StepsClass()
    distance = ph_class.DistanceClass()
    altitude = ph_class.AltitudeClass()
    calories = ph_class.CaloriesClass()
    drs = ph_class.DailyReadinessClass()
    vo2_max = ph_class.Vo2MaxClass()
    time_hr_zones = ph_class.TimeHRZonesClass()
    azm = ph_class.ActiveZoneMinClass()
    sedentary_am = ph_class.SedentaryClass()
    lightly_am = ph_class.LightlyActiveClass()
    moderately_am = ph_class.ModeratelyActiveClass()
    very_am = ph_class.VeryActiveClass()
    exercise = ph_class.ExerciseClass()

    hrv = sleep_class.HeartRateVariabilityClass()
    wrist_temp = sleep_class.WristTemperatureClass()
    rr = sleep_class.RespiratoryRateClass()
    dhrv = sleep_class.DailyHeartRateVariabilityClass()
    hist_hrv = sleep_class.HeartRateVariabilityHistClass()
    sleep_score = sleep_class.SleepScoreClass()
    comp_temp = sleep_class.ComputedTemperatureClass()
    min_spo2 = sleep_class.MinSPO2Class()
    snore = sleep_class.SnoreClass()
    sleep = sleep_class.DailySleepClass()
    detailed_sleep = sleep_class.DetailedSleepClass()

    stress_score = stress_class.StressScoreClass()
    eda = stress_class.EDAClass()

    menstrual_cycles = m_cycles_class.MenstrualCycleClass()

else:
    pass
