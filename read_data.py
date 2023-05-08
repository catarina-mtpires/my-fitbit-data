import glob
import json
import datetime
import pandas as pd
import utils.constants as c


hr_files = glob.glob(c.HR_DIR)

hr_df = pd.DataFrame({"datetime": [], "bpm": [], "confidence": []})
minute_int = 1

for f_name in hr_files:
    print(f_name)
    with open(f_name, 'r') as f:
        hr_json = json.load(f)

    dt, bpm, confidence = [], [], []
    for hr in hr_json:
        dt_var = datetime.datetime.strptime(hr["dateTime"], "%m/%d/%y %H:%M:%S")
        minute = round(dt_var.minute / minute_int) * minute_int
        if minute == 60:
            dt_var += datetime.timedelta(hours=1)
            minute = 0
        dt.append(dt_var.replace(second=0, minute=minute))
        bpm.append(hr["value"]["bpm"])
        confidence.append(hr["value"]["confidence"])

    df = pd.DataFrame({"datetime": dt, "bpm": bpm, "confidence": confidence})
    frames = [hr_df, df.groupby("datetime").agg("mean").reset_index().round()]
    hr_df = pd.concat(frames)

hr_df = hr_df.reset_index(drop=True)
hr_df.to_csv("fitbit_data/new_data/heart_rate.csv", index=False)
