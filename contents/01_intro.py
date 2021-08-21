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

print("Hello pandas")

# region Import package as pandas does not ship along as native package
# use pip install pandas if not installed yet, or follow setup guide
# import matplotlib

# matplotlib.use("TkAgg")
import pandas as pd

# import matplotlib.pyplot as plt

# endregion

# dataframe = pd.read_csv("../datasets/Pokemon.csv")
# print(dataframe.head())
# print(dataframe.describe())
# print(dataframe["Type 1"].value_counts())
# dataframe["Type 1"].value_counts().plot(kind="barh")


# region Introducing primitive Python data types
integers = 2
floats = 1.11
string = "This is a string."

# endregion

# region Introducing Series
# DESC: a Series is similar to a fixed-size dict that has key-value pairs (index and values)
a = pd.Series([1, 2, 3])
print("a: ", a, sep="\n")
b = pd.Series(range(3))
print("b: ", b, sep="\n")

# Series only can consists of one type of primitive Python data type
c = pd.Series([1, 2, "a"])
print("c: ", c, sep="\n")

# some useful attributes
a.dtype
a.values
print(b)
b.index
b.index = ["apple", "banana", "coconut"]
b.index
b.name
b.name = "Quantity of Food"
b.index.name = "Food index"
print(b)

# simple indexing
b[1]
b["apple"]
b[["apple", "coconut"]]

# some useful methods
b.get("apple")
b.to_numpy()
b.drop("banana")
b.rename("Renamed quantity of food")
print(b)
pointer_to_b = b
assert pointer_to_b is b, "pointer_to_b is b"
copy_of_b = b.copy()
assert copy_of_b is b, "copy_of_b is not b"

# endregion

# region Introducting DataFrame
# DESC: A 2D labeled data structure which can consist of diverse data types
# (akin to spreadsheet or SQL table or a dict of Series objects)
# some of the accepted inputs as below:
# - Dict of 1D ndarrays, lists, dicts, or Series
# - 2-D numpy.ndarray
# - Structured or record ndarray
# - A Series
# - Another DataFrame

# creating DataFrame
e = {
    "first_col": pd.Series([1, 2], index=["a", "b"]),
    "second_col": pd.Series([1.0, 2.0, 3.0], index=["a", "b", "c"]),
    "third_col": pd.Series(range(3), index=["a", "b", "c"]),
}

dataframe_from_e = pd.DataFrame(e)

# useful DataFrame attributes
dataframe_from_e.index
dataframe_from_e.columns

# DataFrame indexing
dataframe_from_e["first_col"]
dataframe_from_e["fourth_col"] = True

# useful DataFrame methods
dataframe_from_e.info()
dataframe_from_e.drop("second_col")

# endregion

# region Useful resources
# - https://pandas.pydata.org/community/ecosystem.html
# - https://pandas.pydata.org/pandas-docs/stable/user_guide/dsintro.html
# endregion
