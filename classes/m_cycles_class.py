import pandas as pd
import utils.constants as c
from classes.base_class import DataClass


class MenstrualCycleClass(DataClass):
    def __init__(self):
        super().__init__()
        directory = c.MENST
        self.orig_dir = directory["orig"]
        self.new_dir = directory["new"]

    def create_csv(self):
        df = self.read_csv()
        df = df[df["period_source"] == "manual"]
        df = df.drop(columns=["id", "cycle_start_date", "cycle_end_date", "ovulation_start_date", "ovulation_end_date",
                              "ovulation_source", "period_end_date", "period_source", "fertile_start_date",
                              "fertile_end_date", "fertile_source"], axis=1)
        df = df.rename(columns={"period_start_date": self.dt_col})
        df[self.dt_col] = pd.to_datetime(df[self.dt_col])
        df.to_csv(self.new_dir, index=False)
