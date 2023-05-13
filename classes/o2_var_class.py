import datetime
import utils.constants as c
from classes.base_class import DataClass


class O2VarClass(DataClass):

    def __init__(self):
        super().__init__()
        self.orig_dir = c.ORIG_O2_VAR_DIR
        self.new_dir = c.O2_VAR_DIR
        self.dt_col = "datetime"
        self.df = self.get_df()

    def create_csv(self):
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
        df = df.rename(columns={"timestamp": "datetime", "Infrared to Red Signal Ratio": "value"})
        df.to_csv(self.new_dir)