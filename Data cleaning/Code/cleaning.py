import numpy as np
import pandas as pd

df = pd.read_csv("F://Data-Preprocessing//Data//NFL Play by Play 2009-2017 (v4).csv")

print(df.head(5))

total_missing = df.isnull().sum()
total_values = np.prod(df.shape)

missing_percent = (total_missing / total_values) * 100

dataset_without_null_rows = df.dropna()
dataset_without_null_coloumns = df.dropna(axis=1)

dataset_with_filled_missing_values = df.fillna(0)

df_nan_with_previous_value = df.bfill().fillna(0)