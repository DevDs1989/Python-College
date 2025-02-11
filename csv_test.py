import csv

import pandas as pd
from tabulate import tabulate

pd.set_option("display.max_columns", None)
df = pd.read_csv("customers-100.csv")
data = df.values.tolist()
headers = df.columns.tolist()

print(tabulate(data, headers=headers, tablefmt="grid"))
