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

# endregion

dataframe = pd.read_csv("../datasets/Pokemon.csv")
# print(dataframe.head())
# print(dataframe.describe())
# print(dataframe["Type 1"].value_counts())
# dataframe["Type 1"].value_counts().plot(kind="barh")
# plt.show()

# region Analysing by ascending/descending order
dataframe.sort_values(by="Attack", ascending=False)
dataframe.sort_values(by="Attack", ascending=True)
# endregion

# region Analysing by Single Group
dataframe.groupby("Type 1").head()
dataframe.groupby("Type 1").count()
dataframe.groupby("Type 1").HP.mean().sort_values(ascending=False)
dataframe.groupby("Type 1").HP.median().sort_values(ascending=False)
dataframe.groupby("Type 1").HP.max().sort_values(ascending=False)

# GroupByObject can be thought as a resemblance to DataFrame
# and certain functions can be applied on it by using apply method
dataframe.groupby("Type 1").apply(lambda x: x.loc[:, "Name"])
dataframe.groupby("Type 1").apply(np.sum, axis=0)

# endregion

# region Analysing by Multiple Groups
dataframe.groupby(["Type 1", "Type 2"]).head()
dataframe.groupby(["Type 1", "Type 2"]).Defense.describe()
dataframe.groupby(["Type 1", "Type 2"]).HP.mean().sort_values(ascending=True)

# endregion
