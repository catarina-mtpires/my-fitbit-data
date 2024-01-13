import os
import glob
import json
import pandas as pd


class DataClass:
    def __init__(self):
        self.orig_dir = None
        self.new_dir = None
        self.df = None
        self.dt_col = "datetime"
        self.value_col = "value"

    def read_json(self):
        data = []
        files = glob.glob(self.orig_dir)
        for f_name in files:
            with open(f_name, 'r') as f:
                data += json.load(f)
        return data

    def read_csv(self):
        data = []
        files = glob.glob(self.orig_dir)
        for f_name in files:
            data += [pd.read_csv(f_name)]
        data_df = pd.concat(data).drop_duplicates().reset_index(drop=True)
        return data_df

    def initialize_df(self):
        if self.df is None:
            files_dir = self.new_dir
            if not os.path.exists(files_dir):
                self.create_csv()
            df = pd.read_csv(files_dir)
            df[self.dt_col] = pd.to_datetime(df[self.dt_col])
            self.df = df

    def create_csv(self):
        pass
