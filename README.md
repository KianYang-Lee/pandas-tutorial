# pandas-tutorial
Tutorial on using Pandas, a popular data analysis framework in Python, to perform data analysis tasks on structured data.

## Contents

- [Repository Structure](#repository-structure)
- [Dependencies](#dependencies)
- [Disclaimer](#disclaimer)

## Repository Structure

This repository is structured as follow:

```
contents/   : contains Python scripts for instructor's demonstration purposes during training session
exercises/  : contains Python scripts with instructions for participants to practice
```

Class contents are structured in such a way that core functionalities of `pandas` are exposed to participants in a step-by-step and functional manner. Following contains  short description of subject covered for each scripts:


- `01_intro.ipynb`: Introduces `Series` and `DataFrame`, two core data structures of `pandas` [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/KianYang-Lee/pandas-tutorial/blob/main/contents/01_intro.ipynb)
- `02_load_and_save.ipynb`: Importing and exporting files/datasets [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/KianYang-Lee/pandas-tutorial/blob/main/contents/02_load_and_save.ipynb)
- `03_data_manipulation.ipynb`: Indexing and slicing data, `loc` and `iloc` methods [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/KianYang-Lee/pandas-tutorial/blob/main/contents/03_data_manipulation.ipynb)
- `04_EDA.ipynb`: General methods to perform exploratory data analysis [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/KianYang-Lee/pandas-tutorial/blob/main/contents/04_EDA.ipynb)
- `05_data_cleaning.ipynb`: Performing missing data identification and imputation [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/KianYang-Lee/pandas-tutorial/blob/main/contents/05_data_cleaning.ipynb)
- `06_data_analysis.ipynb`: Performing more in-depth data analysis using rolling window, grouping method and more [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/KianYang-Lee/pandas-tutorial/blob/main/contents/06_data_analysis.ipynb)
- `07_data_visualization.ipynb`: Depicting data in various visualizations [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/KianYang-Lee/pandas-tutorial/blob/main/contents/07_data_visualization.ipynb)

## Dependencies

Isolating each environment for different projects is the best practice. One of the way you can create virtual environment is by using Python's native `virtualenv` module. At this directory's root, execute the following to create a virtual environment:

```sh
python3 -m venv venv
```

Commands to activate virtual environment varies according to your OS. Use the following for Linux:

```sh
source venv/bin/activate
```

Use the following for Windows:

```cmd
venv\Scripts\activate
```

A `(venv)` appearing in front of your system path indicates that the virtual environment is successfully activated, as shown below:

`(venv) C:\Users\User\pandas-tutorial>`

Finally, execute the following to install the dependencies for this lab into your activated virtual environment:

```sh
pip install -r requirements.txt
```

## Disclaimer

All the dataset used in this repository does not belong to the authors but rather are open-sourced datasets found online. Attached are the URLs for each and every dataset:

* `ct.json` dataset [source](https://www.bmc.com/blogs/pandas-read-json-csv-files/)
* `airlines.csv` dataset [source](http://www.principlesofeconometrics.com/excel.htm)
* `Pokemon.csv` dataset [source](https://www.kaggle.com/abcsds/pokemon)
* `Titanic.csv` dataset [source](https://github.com/pandas-dev/pandas/blob/master/doc/data/titanic.csv) 