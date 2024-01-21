import classes.hr_class as hr_class
import classes.o2_var_class as o2_var_class
import classes.physical_activity_class as ph_class
import classes.sleep_class as sleep_class
import classes.stress_class as stress_class
import classes.m_cycles_class as m_cycles_class

done = False
if done:
    hr = hr_class.HeartRateClass()
    rhr = hr_class.RestingHeartRateClass()
    ecg = hr_class.ECGClass()
    hr_complete = hr_class.HeartRateCompleteClass(year=2023, month=5, day=13)

    hr.initialize_df()
    rhr.initialize_df()
    ecg.initialize_df()
    hr_complete.initialize_df()

    o2_var = o2_var_class.O2VarClass()
    o2_var.initialize_df()

    steps = ph_class.StepsClass()
    distance = ph_class.DistanceClass()
    altitude = ph_class.AltitudeClass()
    calories = ph_class.CaloriesClass()
    drs = ph_class.DailyReadinessClass()
    vo2_max = ph_class.Vo2MaxClass()
    time_hr_zones = ph_class.TimeHRZonesClass()

    steps.initialize_df()
    distance.initialize_df()
    altitude.initialize_df()
    calories.initialize_df()
    drs.initialize_df()
    vo2_max.initialize_df()
    time_hr_zones.initialize_df()

    hrv = sleep_class.HeartRateVariabilityClass()
    wrist_temp = sleep_class.WristTemperatureClass()
    rr = sleep_class.RespiratoryRateClass()
    dhrv = sleep_class.DailyHeartRateVariabilityClass()
    hist_hrv = sleep_class.HeartRateVariabilityHistClass()
    sleep_score = sleep_class.SleepScoreClass()
    comp_temp = sleep_class.ComputedTemperatureClass()
    min_spo2 = sleep_class.MinSPO2Class()
    snore = sleep_class.SnoreClass()

    hrv.initialize_df()
    wrist_temp.initialize_df()
    rr.initialize_df()
    dhrv.initialize_df()
    hist_hrv.initialize_df()
    sleep_score.initialize_df()
    comp_temp.initialize_df()
    min_spo2.initialize_df()
    snore.initialize_df()

    stress_score = stress_class.StressScoreClass()
    eda = stress_class.EDAClass()

    stress_score.initialize_df()
    eda.initialize_df()

    menstrual_cycles = m_cycles_class.MenstrualCycleClass()
    menstrual_cycles.initialize_df()

else:
    pass

