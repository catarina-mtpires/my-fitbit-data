import datetime
import utils.constants as c
from classes.base_class import DataClass


class O2VarClass(DataClass):
    def __init__(self, initialize_df=True):
        directory = c.O2_VAR
        orig_dir = directory["orig"]
        new_dir = directory["new"]
        super().__init__(orig_dir=orig_dir, new_dir=new_dir, initialize_df=initialize_df)

    def create_df(self):
        df = self.read_csv()
        dts = df.timestamp
        dts_var = []
        for dt in dts:
            dt_var = datetime.datetime.strptime(dt, "%m/%d/%y %H:%M:%S")
            seconds = round(dt_var.second / 60) * 60
            if seconds == 60:
                dt_var += datetime.timedelta(minutes=1)
            dts_var.append(dt_var.replace(second=0))
        df["timestamp"] = dts_var
        df = df.rename(columns={"timestamp": self.dt_col, "Infrared to Red Signal Ratio": self.value_col})

        return df
