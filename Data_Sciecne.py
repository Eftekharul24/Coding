import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

full_health_data = pd.read_csv("data.csv", header=0, sep=",")

x = full_health_data["Average_Pulse"]
y = full_health_data["Calorie_Burnage"]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
 return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.ylim(ymin=0, ymax=2000)
plt.xlim(xmin=0, xmax=200)
plt.xlabel("Average_Pulse")
plt.ylabel ("Calorie_Burnage")
plt.show()

Average_pulse_max = max(80, 85, 90, 95, 100, 105, 110, 115, 120, 125)

print (Average_pulse_max)

import pandas as pd

health_data = pd.read_csv("data.csv", header=0, sep=",")

health_data.dropna(axis=0,inplace=True)

print(health_data)

import pandas as pd

health_data = pd.read_csv("data.csv", header=0, sep=",")

pd.set_option('display.max_columns',None)

print(health_data.describe())

import pandas as pd
import matplotlib.pyplot as plt

health_data = pd.read_csv("data.csv", header=0, sep=",")

health_data.plot(x ='Average_Pulse', y='Calorie_Burnage', kind='line')
plt.ylim(ymin=0)
plt.xlim(xmin=0)

plt.show()

import pandas as pd
import matplotlib.pyplot as plt

health_data = pd.read_csv("data.csv", header=0, sep=",")

health_data.plot(x ='Average_Pulse', y='Calorie_Burnage', kind='scatter'),

plt.show()

import pandas as pd
import matplotlib.pyplot as plt

full_health_data = pd.read_csv("data.csv", header=0, sep=",")

full_health_data.plot(x ='Duration', y='Max_Pulse', kind='scatter')

plt.show()


import pandas as pd
import matplotlib.pyplot as plt

negative_corr = {'Hours_Work_Before_Training': [10,9,8,7,6,5,4,3,2,1],
'Calorie_Burnage': [220,240,260,280,300,320,340,360,380,400]}
negative_corr = pd.DataFrame(data=negative_corr)

negative_corr.plot(x ='Hours_Work_Before_Training', y='Calorie_Burnage', kind='scatter')
plt.show()

full_health_data = pd.read_csv("data.csv", header=0, sep=",")
Corr_Matrix = round(full_health_data.corr(),2)

print(Corr_Matrix)


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

full_health_data = pd.read_csv("data.csv", header=0, sep=",")
correlation_full_health = full_health_data.corr()

axis_corr = sns.heatmap(
correlation_full_health,
vmin=-1, vmax=1, center=0,
cmap=sns.diverging_palette(50, 500, n=500),
square=True)

plt.show()


import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

full_health_data = pd.read_csv("data.csv", header=0, sep=",")

x = full_health_data["Average_Pulse"]
y = full_health_data["Calorie_Burnage"]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
 return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.ylim(ymin=0, ymax=2000)
plt.xlim(xmin=0, xmax=200)
plt.xlabel("Average_Pulse")
plt.ylabel ("Calorie_Burnage")
plt.show()

import pandas as pd
import statsmodels.formula.api as smf

full_health_data = pd.read_csv("data.csv", header=0, sep=",")

model = smf.ols('Calorie_Burnage ~ Average_Pulse', data = full_health_data)
results = model.fit()
print(results.summary())

import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

full_health_data = pd.read_csv("data.csv", header=0, sep=",")

x = full_health_data["Duration"]
y = full_health_data["Calorie_Burnage"]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
 return slope * x + intercept

mymodel = list(map(myfunc, x))

print(mymodel)

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.ylim(ymin=0, ymax=2000)
plt.xlim(xmin=0, xmax=200)
plt.xlabel("Duration")
plt.ylabel ("Calorie_Burnage")
plt.show()


import pandas as pd
import statsmodels.formula.api as smf

full_health_data = pd.read_csv("data.csv", header=0, sep=",")

model = smf.ols('Calorie_Burnage ~ Average_Pulse + Duration', data = full_health_data)
results = model.fit()
print(results.summary())