import glob
import json
import pandas as pd

from datetime import datetime


hr_dir = "fitbit_data/heart/heart_rate/heart_rate-*.json"
hr_files = glob.glob(hr_dir)

hr_df = pd.DataFrame({"datetime": [], "bpm": [], "confidence": []})
minute_int = 5

for f_name in hr_files:
    print(f_name)
    with open(f_name, 'r') as f:
        hr_json = json.load(f)

    dt, bpm, confidence = [], [], []
    for hr in hr_json:
        dt_var = datetime.strptime(hr["dateTime"], "%m/%d/%y %H:%M:%S")
        minute = round(dt_var.minute / minute_int) * minute_int
        if minute == 60:
            minute -= 1
        dt.append(dt_var.replace(second=0, minute=minute))
        bpm.append(hr["value"]["bpm"])
        confidence.append(hr["value"]["confidence"])

    df = pd.DataFrame({"datetime": dt, "bpm": bpm, "confidence": confidence})
    frames = [hr_df, df.groupby("datetime").agg("mean").reset_index().round()]
    hr_df = pd.concat(frames)

hr_df = hr_df.reset_index()

