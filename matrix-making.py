# Install packages

# ! pip install pandas
# ! pip install numpy

# Import packages

import numpy as np
import pandas as pd

df = pd.read_csv('collabs.csv', names=['login_1', 'last_name_1', 'first_name_1', 'orgu_1', 'publication_id', 'login_2', 'last_name_2', 'first_name_2', 'cat', 'orgu_2', 'organisation'])

# N = 100
# df = pd.DataFrame({
#     'A': pd.date_range(start='2016-01-01',periods=N,freq='D'),
#     'x': np.linspace(0,stop=N-1,num=N),
#     'y': np.random.rand(N),
#     'C': np.random.choice(['Low','Medium','High'],N).tolist(),
#     'D': np.random.normal(100, 10, size=(N)).tolist()
#     })
# df.head()

# Another example of making a plot:

# from matplotlib import pyplot as plt
# x=df.x
# with plt.style.context('fivethirtyeight'):
#     plt.plot(x, np.sin(x*5) + x + np.random.randn(N)*15)
#     plt.plot(x, np.sin(x*5) + 0.5 * x + np.random.randn(N)*5)
#     plt.plot(x, np.sin(x) + 2 * x + np.random.randn(N)*20)

# plt.title('Counting ')
# plt.show()
