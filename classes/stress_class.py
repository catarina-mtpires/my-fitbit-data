import datetime
import pandas as pd
import utils.constants as c
from classes.base_class import DataClass


class StressScoreClass(DataClass):
    def __init__(self):
        super().__init__()
        directory = c.STRESS_SCORE
        self.orig_dir = directory["orig"]
        self.new_dir = directory["new"]
        self.max_sleep_points = 30
        self.max_responsiveness_points = 30
        self.max_exertion_points = 40

    def create_csv(self):
        df = self.read_csv()
        df = df[df["STATUS"] == "READY"]
        df = df.drop(columns=["UPDATED_AT", "MAX_SLEEP_POINTS", "MAX_RESPONSIVENESS_POINTS", "MAX_EXERTION_POINTS",
                              "STATUS", "CALCULATION_FAILED"], axis=1)
        df = df.rename(columns={"DATE": self.dt_col, "STRESS_SCORE": self.value_col, "SLEEP_POINTS": "sleep_value",
                                "RESPONSIVENESS_POINTS": "responsiveness_value", "EXERTION_POINTS": "exertion_value"})
        df[self.dt_col] = pd.to_datetime(df[self.dt_col]).dt.date
        df.to_csv(self.new_dir, index=False)


class EDAClass(DataClass):
    def __init__(self):
        super().__init__()
        directory = c.EDA
        self.orig_dir = directory["orig"]
        self.new_dir = directory["new"]
        self.id_col = "id"

    def create_csv(self):
        df = self.read_csv()
        df = df.rename(columns={"session_id": self.id_col, "timestamp": self.dt_col, "scl_avg": self.value_col})
        set_ts = set(df[self.dt_col])
        for ts in set_ts:
            df_id = df[df[self.dt_col] == ts]
            i = 0
            for index in df_id.index:
                df.loc[index, self.dt_col] = ts + i
                i += 1

        df[self.dt_col] = [datetime.datetime.fromtimestamp(ts) for ts in df[self.dt_col]]
        df.to_csv(self.new_dir, index=False)

