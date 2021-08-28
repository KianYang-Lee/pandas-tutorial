# region License

# Copyright (C) 2021  Lee Kian Yang

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# endregion

# region Import package as pandas does not ship along as native package
# use pip install pandas if not installed yet, or follow setup guide

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(123)

# endregion

dataframe = pd.read_csv("../datasets/Pokemon.csv")
# print(dataframe.head())
# print(dataframe.describe())
# print(dataframe["Type 1"].value_counts())
# dataframe["Type 1"].value_counts().plot(kind="barh")
# plt.show()

# region Injecting missing values
dataframe.Generation = dataframe.Generation.map(lambda x: np.nan)
dataframe.Attack = dataframe.Attack.map(
    lambda x: np.nan if np.random.rand() < 0.5 else x
)

# region Checking for missing values
dataframe.isnull()
dataframe.isnull().sum()

# endregion

# region Missing value imputation using specific values
df_filled_with_1 = dataframe.fillna(999)
df_filled_with_1.isnull().sum()

df_impute_string = dataframe.fillna("Null")
df_impute_string.isnull().sum()

df_mean_imputation = dataframe.Attack.fillna(dataframe.Attack.mean())
df_median_imputation = dataframe.Attack.fillna(dataframe.Attack.median())


# endregion

# region Missing value imputation using different values
# propagate non-null values forward
df_ffill = dataframe.fillna(method="ffill")
df_bfill = dataframe.fillna(method="bfill")

# endregion
