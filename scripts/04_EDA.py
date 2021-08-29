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

# endregion

dataframe = pd.read_csv("../datasets/Pokemon.csv")
# print(dataframe.head())
# print(dataframe.describe())
# print(dataframe["Type 1"].value_counts())
# dataframe["Type 1"].value_counts().plot(kind="barh")
# plt.show()

# region Checking for overview of DataFrame
dataframe.info()

# endregion

# region Checking for structure of DataFrame
# number of rows and columns
dataframe.shape

# number of elements in total
dataframe.size

# number of dimension
dataframe.ndim

# endregion

# region Checking for data types
dataframe.dtypes
dataframe.HP.dtype
dataframe["HP"].dtype
dataframe.HP.astype("float64")

# endregion

# region Checking first and last n rows
dataframe.head(10)
dataframe.tail()
# endregion

# region Checking for indices
dataframe.index
dataframe.columns

# endregion

# region Validating uniqueness
dataframe.duplicated()
dataframe.nunique()
dataframe.Name.unique()

# endregion

# region Fast counting
dataframe["Type 1"].value_counts()

# endregion

# region Checking for missing values
dataframe.isnull()
dataframe.isnull().sum()

# endregion

# region Compute descriptive statistics
dataframe.describe()
dataframe.Name.describe()

# endregion

# region Compute correlation matrix
dataframe.corr()

# endregion

# region Getting n-largest values for a column
dataframe.nlargest(10, "Attack")

# endregion

# region Getting specific summative value on a Series
dataframe.Attack.mean()
dataframe.HP.median()
dataframe.Defense.max()

# endregion
