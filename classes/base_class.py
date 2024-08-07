import os
import glob
import json
import pandas as pd


class DataClass:
    def __init__(self, directory=None, orig_dir=None, new_dir=None, dt_col="datetime", value_col="value", initialize_df=True,
                 name=None, sort_values=True, additional_dt_cols=None):
        if directory is None:
            self.orig_dir = orig_dir
            self.new_dir = new_dir
        else:
            self.orig_dir = directory["orig"]
            self.new_dir = directory["new"]
        self.dt_col = dt_col
        self.value_col = value_col
        self.df = None
        self.name = name
        dt_cols = [self.dt_col]
        if additional_dt_cols:
            dt_cols += additional_dt_cols
        self.dt_cols = dt_cols
        if initialize_df:
            self.initialize_df(sort_values=sort_values)

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

    def initialize_df(self, sort_values=True):
        if self.df is None:
            files_dir = self.new_dir
            if not os.path.exists(files_dir):
                self.create_csv(sort_values=sort_values)
            df = pd.read_csv(files_dir)
            for col in self.dt_cols:
                df[col] = pd.to_datetime(df[col])
            self.df = df

    def create_csv(self, sort_values=True):
        df = self.create_df()
        df = df.drop_duplicates()
        if sort_values:
            df = df.sort_values(self.dt_col)
        df.to_csv(self.new_dir, index=False)

    def create_df(self):
        pass
