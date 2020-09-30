import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import plotly.graph_objects as go

# Read the dataset
df = pd.read_csv('covid_19_data.csv')

#df.head()
#df.describe()
#df.info()

# Dropping 2 columns
df = df.drop(['SNo','Last Update'],axis=1)

# Renaming
df = df.rename(columns={'ObservationDate':'Date','Province/State':'State','Country/Region':'Country'})

#df.head()
#df.tail()

# Getting the order of countries wrt the confirmed cases
confirmed = df.groupby(['Country']).sum()[['Confirmed']].sort_values(by=['Confirmed'], ascending=False)
confirmed.head()

