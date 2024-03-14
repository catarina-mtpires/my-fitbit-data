import pandas as pd
import utils.constants as c
from classes.base_class import DataClass


class MenstrualCycleClass(DataClass):
    def __init__(self, initialize_df=True, name="menstrual_cycle"):
        directory = c.MENST
        orig_dir = directory["orig"]
        new_dir = directory["new"]
        super().__init__(orig_dir=orig_dir, new_dir=new_dir, initialize_df=initialize_df, name=name)

    def create_df(self):
        df = self.read_csv()
        df = df[df["period_source"] == "manual"]
        df = df.drop(columns=["id", "cycle_start_date", "cycle_end_date", "ovulation_start_date", "ovulation_end_date",
                              "ovulation_source", "period_end_date", "period_source", "fertile_start_date",
                              "fertile_end_date", "fertile_source"], axis=1)
        df = df.rename(columns={"period_start_date": self.dt_col})
        df[self.dt_col] = pd.to_datetime(df[self.dt_col])

        return df
