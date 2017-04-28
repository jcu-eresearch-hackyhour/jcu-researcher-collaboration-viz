# Data preparation for using CSCollab D3 code

# Rodeo commands to install packages

# ! pip install pandas
# ! pip install numpy

# Import packages
import numpy as np
import pandas as pd

# Make a dataframe from the rows containing each collaboration.  Each row has two authors in it
df1 = pd.read_csv('input/collabs.csv', usecols=['Family Name 1', 'Given Name 1', 'ORGU 1', 'Pub ID', 'Login 2', 'Family Name 2', 'Given Name 2', 'Cat', 'ORGU 2', 'Organisation'])
df2 = pd.read_csv('input/collabs.csv', usecols=['Family Name 1', 'Given Name 1', 'ORGU 1', 'Pub ID', 'Login 2', 'Family Name 2', 'Given Name 2', 'Cat', 'ORGU 2', 'Organisation'])

df2['orig-fn1'] = df2['Family Name 1']
df2['Family Name 1'] = df2['Family Name 2']
df2['Family Name 2'] = df2['orig-fn1']

df = pd.concat([df1, df2], ignore_index=True)

#  Crosstab function
ct = pd.crosstab(index=df['Family Name 1'], columns = df['Family Name 2'])

# Write out to JSON without the indices/headers
# Looks like the correct matrix as referenced in collab/graphs/*-matrix.json
matrix_json = ct.to_json('James Cook University-graph-matrix.json', orient = 'values')

# Get the authors in a list for the 'nodes.csv' file as required
df_node = pd.read_csv('input/collabs.csv', usecols=['Family Name 1', 'Given Name 1', 'ORGU 1'])

df_node['name'] = df_node['Given Name 1'] + df_node['Family Name 1']
df_node['abbrv'] = df_node['Family Name 1']
df_node['color'] = '#cc3333'
# df_node['color'] = '#' + df_node['ORGU 1'].astype(str)
df_node['coauthored'] = 1

del df_node['Given Name 1']
del df_node['Family Name 1']
del df_node['ORGU 1']

# another try at making df_node -------=-=---

df_node = df[['Family Name 1']].copy()
df_node['name'] = df_node['Family Name 1']
df_node['abbrv'] = df_node['Family Name 1']
df_node['color'] = '#cc3333'

del df_node['Family Name 1']

# Write out to CSV, similar with to_json just adding orient='values'. TODO: Needs to be amended to match
nodes_csv = df_node.to_csv('James Cook University-graph-nodes.csv', index = False)
