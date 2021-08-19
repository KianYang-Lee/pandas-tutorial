# pandas-tutorial
Tutorial on using Pandas, a popular data analysis framework in Python, to perform data analysis tasks on structured data.

## Contents

- [Repository Structure](#repository-structure)
- [Dependencies](#dependencies)

## Repository Structure

This repository is structured as follow:

```
contents/   : contains Python scripts for instructor's demonstration purposes during training session
exercises/  : contains Python scripts with instructions for participants to practice
```

Class contents are structured in such a way that core functionalities of `pandas` are exposed to participants in a step-by-step and functional manner. Following contains  short description of subject covered for each scripts:

- `01_intro.py`: Introduces `Series` and `DataFrame`, two core data structures of `pandas`
- `02_load_and_save.py`: Importing and exporting files/datasets
- `03_data_manipulation.py`: Indexing and slicing data, `loc` and `iloc` methods
- `04_EDA.py`: General methods to perform exploratory data analysis
- `05_data_cleaning.py`: Performing missing data identification and imputation
- `06_data_analysis.py`: Performing more in-depth data analysis using rolling window, grouping method and more
- `07_data_visualization.py`: Depicting data in various visualizations

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

