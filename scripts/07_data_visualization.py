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
# plt.show()

# region Plotting bar chart
# vertical bar chart
dataframe["Type 1"].value_counts().plot(kind="bar")
plt.show()

dataframe.groupby("Type 1")["Attack"].max().plot(kind="bar")
plt.show()

# horizontal bar chart
dataframe["Type 1"].value_counts().plot(kind="barh")
plt.show()

# clustered bar chart
dataframe.nlargest(10, columns="Attack").plot(kind="bar")
plt.show()

# endregion

# region Plotting line chart
# spotted anything awkward with this line chart?
dataframe.nlargest(10, columns="Attack").Attack.plot(kind="line")
plt.show()

dataframe.set_index("Name").nlargest(10, columns="Attack").Attack.sort_values().plot(
    kind="line"
)
plt.show()

# endregion

# region Plotting boxplots
dataframe.Attack.plot(kind="box")
plt.show()

# endregion

# region Styling
dataframe.Attack.plot(
    kind="box", xlabel="Metric", ylabel="Value", title="Distribution of Attack"
)
plt.show()

dataframe.nlargest(10, columns="Attack").plot(
    kind="bar",
    title="Metrics for top 10 Pokemon with Highest Attack",
    xlabel="Metrics",
    ylabel="Value",
)
plt.show()

# endregion
