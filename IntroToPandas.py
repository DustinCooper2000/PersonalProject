############
# Dustin Cooper
# This will be me playing around wih the pandas and nunmpy libraries of python
############
import numpy as np
import pandas as pd

xlsx = pd.ExcelFile(r"C:\Users\cooperd\Downloads\Stats\CRP_database_master.xlsx")
Df1 = pd.read_excel(xlsx, "Sheet1")
print(Df1.head())
print(Df1["Activity"])