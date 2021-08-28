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

# region Every DataFrame at least has one row index and
# one column index
dataframe.columns
dataframe.index

# endregion

# region Accessing column(s)
# dot notation to access attribute of object
dataframe.Name

# similar operation but using indexing operator - square bracket
dataframe["Name"]

# select multiple columns
dataframe[["Name", "HP", "Attack", "Defense"]]

# drilling down
dataframe["Name"][0]
# endregion

# region Indexing
# index-based selection - based on index position
# select first row
dataframe.iloc[1, :]

# select last column
dataframe.iloc[:, -1]

# label-based selection - based on index value
# select Name column
dataframe.loc[:, "Name"]

# select second row
dataframe.loc[1, :]

# select multiple columns
dataframe.loc[:, ["Name", "HP", "Attack", "Defense"]]

# endregion

# region Index can be changes, like everything else in life
df_with_name_index = dataframe.set_index("Name", drop=True)
df_with_name_index.loc["Charizard"]

# endregion

# region Conditional selection that fulfills certain criteria
# setting a condition to return a Boolean Series
min_HP_condition = dataframe.HP > 200

# this line will not work, do you know why?
# dataframe.iloc[min_HP_condition]

# conditional selection of rows that satisfies the condition
dataframe.loc[min_HP_condition]

# conditional selection on multiple criteria
min_attack_condition = dataframe.Attack > 100
min_defense_condition = dataframe.Defense > 100
dataframe.loc[min_attack_condition & min_defense_condition]
dataframe.loc[min_attack_condition | min_defense_condition]

# endregion

# region Changing a value
# able to access specific value in the DataFrame means that
# you can also change the value
dataframe.loc[0, "Name"] = "Rilakuma"

# endregion

# region Changing multiple values at once
# mapping from one value to another for a Series
dataframe.HP.map(lambda x: 0)

# applying a transformation on a DataFrame
# transform each column by passing "columns" or 1 argument to axis parameter
dataframe.apply(lambda x: x * 2, axis="columns")

# endregion
