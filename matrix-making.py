# Install packages

# ! pip install pandas
# ! pip install numpy

# Import packages

import numpy as np
import pandas as pd

df = pd.read_csv('collabs.csv', names=['login_1', 'last_name_1', 'first_name_1', 'orgu_1', 'publication_id', 'login_2', 'last_name_2', 'first_name_2', 'cat', 'orgu_2', 'organisation'])

series = df.groupby(['last_name_1','last_name_2']).size()

matrix = series.unstack()

# TODO: Can't remember if the D3 function requires 0 or nulls or whatever...0
matrix = matrix.fillna(0)

#  Trying with crosstab function
ct = pd.crosstab(index=df['last_name_1'], columns = df['last_name_2'])
