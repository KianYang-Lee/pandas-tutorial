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
print(dataframe.head())
print(dataframe.describe())
print(dataframe["Type 1"].value_counts())
dataframe["Type 1"].value_counts().plot(kind="barh")
plt.show()

# region Importing data
# pandas provide API calls to easily load almost any format
# of file into pandas DataFrame
csv_df = pd.read_csv(
    "https://raw.githubusercontent.com/pandas-dev/pandas/master/doc/data/titanic.csv"
)
excel_df = pd.read_excel("../datasets/airline.xls")
json_df = pd.read_json(
    "../datasets/ct.json",
    lines=True,
)

# endregion

# region Exporting data
# exporting data into respective file format
csv_df.to_csv("../datasets/Titanic_extracted.csv")
csv_df.to_excel(
    "../datasets/Titanic_extracted.xlsx", sheet_name="passengers", index=False
)
excel_df.to_csv("../datasets/airlines_extracted.csv")
json_df.to_json("../datasets/ct_extracted.json")

# read .xlsx file
excelx_df = pd.read_excel("../datasets/Titanic_extracted.xlsx", sheet_name="passengers")

# endregion

# region Useful resources
# - https://www.kdnuggets.com/datasets/index.html
# - https://github.com/awesomedata/awesome-public-datasets
# - ct.json dataset source: https://www.bmc.com/blogs/pandas-read-json-csv-files/
# - airlines.csv dataset source: http://www.principlesofeconometrics.com/excel.htm
# - Pokemon.csv dataset source: https://www.kaggle.com/abcsds/pokemon
# - Titanic.csv dataset source: https://github.com/pandas-dev/pandas/blob/master/doc/data/titanic.csv
# - Financial Sample.xlsx dataset source: https://docs.microsoft.com/en-us/power-bi/create-reports/sample-financial-download
# endregion
