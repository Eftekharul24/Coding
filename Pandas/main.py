import pandas

mydataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2]
}

myvar = pandas.DataFrame(mydataset)

print(myvar)

import pandas as pd

mydataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)

# Create a simple Pandas Series from a list:

import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)

# Create your own labels:

import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a, index=["x", "y", "z"])

print(myvar)

# Create a simple Pandas Series from a dictionary:

import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)

# Create a DataFrame from two Series:

import pandas as pd

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)

print(myvar)
# refer to the row index:
print(myvar.loc[0])
# use a list of indexes:
print(myvar.loc[[0, 1]])

# Add a list of names to give each row a name:
import pandas as pd

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index=["day1", "day2", "day3"])

print(df)

# Load a comma separated file (CSV file) into a DataFrame:
import pandas as pd

df = pd.read_csv('Data.csv')

print(df)

# Load the CSV into a DataFrame:

import pandas as pd

df = pd.read_csv('Data.csv')

print(df.to_string())
# Check the number of maximum returned rows:
print(pd.options.display.max_rows)
# Increase the maximum number of rows to display the entire DataFrame:
import pandas as pd

pd.options.display.max_rows = 9999

df = pd.read_csv('Data.csv')

print(df)

# Load the JSON file into a DataFrame:
import pandas as pd

df = pd.read_json('Data.json')

print(df.to_string())

# Get a quick overview by printing the first 10 rows of the DataFrame:

import pandas as pd

df = pd.read_csv('Data.csv')

print(df.head(10))
print(df.head())  # Print the first 5 rows of the DataFrame:
print(df.tail())  # Print the last 5 rows of the DataFrame:
print(df.info())

# Return a new Data Frame with no empty cells:
import pandas as pd

df = pd.read_csv('Data.csv')

new_df = df.dropna()

print(new_df.to_string())

# emove all rows with NULL values:
import pandas as pd

df = pd.read_csv('Data.csv')

df.dropna(inplace=True)

print(df.to_string())

# Replace NULL values in the "Calories" columns with the number 130:
import pandas as pd

df = pd.read_csv('Data.csv')

df["Calories"].fillna(130, inplace=True)

# Calculate the MEAN, and replace any empty values with it:
import pandas as pd

df = pd.read_csv('Data.csv')

x = df["Calories"].mean()

df["Calories"].fillna(x, inplace=True)

# Calculate the MEDIAN, and replace any empty values with it:

import pandas as pd

df = pd.read_csv('data.csv')

x = df["Calories"].median()

df["Calories"].fillna(x, inplace=True)

# Calculate the MODE, and replace any empty values with it:
import pandas as pd

df = pd.read_csv('data.csv')

x = df["Calories"].mode()[0]

df["Calories"].fillna(x, inplace=True)

df.loc[7, 'Duration'] = 45

# Delete rows where "Duration" is higher than 120:
for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.drop(x, inplace=True)

# Returns True for every row that is a duplicate, othwerwise False:
print(df.duplicated())
df.drop_duplicates(inplace=True)  # To remove duplicates, use the drop_duplicates() method.

# Show the relationship between the columns:
#import pandas as pd

#df = pd.read_csv('Data.csv')

#print(df.corr())

#Three lines to make our compiler able to draw:
import sys
import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Data.csv')

df.plot()

plt.show()

#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()


#Scatter Plot
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Data.csv')

df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')

plt.show()

#A scatterplot where there are no relationship between the columns:
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df.plot(kind = 'scatter', x = 'Duration', y = 'Maxpulse')

plt.show()

#Histogram
df["Duration"].plot(kind = 'hist')