import datetime
import pandas as pd
import utils.constants as c
from classes.base_class import DataClass


class StressScoreClass(DataClass):
    def __init__(self, initialize_df=True, name="stress_score"):
        directory = c.STRESS_SCORE
        orig_dir = directory["orig"]
        new_dir = directory["new"]
        self.max_sleep_points = 30
        self.max_responsiveness_points = 30
        self.max_exertion_points = 40
        super().__init__(orig_dir=orig_dir, new_dir=new_dir, initialize_df=initialize_df, name=name)

    def create_df(self):
        df = self.read_csv()
        df = df[df["STATUS"] == "READY"]
        df = df.drop(columns=["UPDATED_AT", "MAX_SLEEP_POINTS", "MAX_RESPONSIVENESS_POINTS", "MAX_EXERTION_POINTS",
                              "STATUS", "CALCULATION_FAILED"], axis=1)
        df = df.rename(columns={"DATE": self.dt_col, "STRESS_SCORE": self.value_col, "SLEEP_POINTS": "sleep_value",
                                "RESPONSIVENESS_POINTS": "responsiveness_value", "EXERTION_POINTS": "exertion_value"})
        df[self.dt_col] = pd.to_datetime(df[self.dt_col]).dt.date

        return df


class EDAClass(DataClass):
    def __init__(self, initialize_df=True, name="eda"):
        directory = c.EDA
        orig_dir = directory["orig"]
        new_dir = directory["new"]
        self.id_col = "id"
        super().__init__(orig_dir=orig_dir, new_dir=new_dir, initialize_df=initialize_df, sort_values=False, name=name)

    def create_df(self):
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
        df = df.sort_values(by=[self.id_col, self.dt_col]).reset_index(drop=True)

        return df

