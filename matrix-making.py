# Data preparation for using CSCollab D3 code

# Rodeo commands to install packages

! pip install pandas
! pip install numpy

# Import packages
import numpy as np
import pandas as pd

# Make a dataframe from the rows containing each collaboration.  Each row has two authors in it
df = pd.read_csv('collabs.csv', names=['last_name_1', 'first_name_1', 'orgu_1', 'publication_id', 'login_2', 'last_name_2', 'first_name_2', 'cat', 'orgu_2', 'organisation'])

# series = df.groupby(['last_name_1','last_name_2']).size()

#  Crosstab function
ct = pd.crosstab(index=df['last_name_1'], columns = df['last_name_2'])

# Write out to JSON without the indices/headers
# Looks like the correct matrix as referenced in collab/graphs/*-matrix.json
matrix_json = ct.to_json('matrix.json', orient = 'values')

# Get the authors in a list for the 'nodes.csv' file as required
df_node = pd.read_csv('collabs.csv', names=['last_name_1', 'first_name_1', ])

# Write out to CSV, similar with to_json just adding orient='values'. TODO: Needs to be amended to match
nodes_csv = df_node.to_csv('nodes.csv', index = False)
