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