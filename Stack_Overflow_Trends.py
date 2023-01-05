#Stack Overflow Trends

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.model_selection import train_test_split

#Import Dataset
df = pd.read_csv('developer_dataset.csv')
#Print Columns Names
print(df.columns)
# count the data in each column
print(df.count())

#Find the Average Min, Max of the number of null points
print(df.describe())

# Find the Percentage of Missing Data in Each Column
maxRows = df['RespondentID'].count()
print('%of Mising Data:')
print((1-df.count()/maxRows)*100)
# Remove Columns with Lots of Missing Data
#We are going to Remove the NEWJobHunt, NEWJobHuntResearch, NEWLearn columsn because they have too many data points missing
df.drop(['NEWJobHunt','NEWJobHuntResearch','NEWLearn'], axis = 1, inplace = True)

# Check to see if the rows Dropped
print(df.head())
# Determine Missing Data for Each Country
df[['RespondentID','Country']].groupby('Country').count()

missingdata= df[['Employment','DevType']].isnull().groupby(df['Country']).sum().reset_index()
print("Missing Values in Employment and DevType by Country")
print(missingdata)
#Create a BarChar for Employment and DevType missing Data
#A=sns.catplot(data= missingdata, kind ='bar',x="Country", y = "Employment",height = 6, aspect = 2)
#B = sns.catplot(data = missingdata, kind = 'bar', x="Country",y = 'DevType', height = 6, aspect= 2)
#plt.show()
# Delete subsets of data using listwise Deletion
df.dropna(subset = ['Employment','DevType'],inplace = True, how = 'any')
print(df.head())
# Create a series of Bar Charts describing the breakdwon of each developer role for each country
empfig = sns.catplot(x = 'Country', col= 'Employment',data = df, kind = 'count', height = 6, aspect = 1.5)

devdf = df[['Country','DevType']]
devdf.loc[devdf['DevType'].str.contains('back-end'), 'BackEnd'] = True
devdf.loc[devdf['DevType'].str.contains('front-end'), 'FrontEnd'] = True
devdf.loc[devdf['DevType'].str.contains('full-stack'),'FullStack'] = True
devdf.loc[devdf['DevType'].str.contains('mobile'),'Mobile']=True
devdf.loc[devdf['DevType'].str.contains('administrator'),"Admin"]=True

devdf = devdf.melt(id_vars = ['Country'],value_vars=['BackEnd','FrontEnd','FullStack','Mobile','Admin'],var_name = 'DevCat',value_name = 'DevFlage')

devdf.dropna(how='any',inplace =True)

devFig = sns.catplot(x="Country", col = 'DevCat',data = devdf, kind = 'count', height = 6, aspect = 1.5)
plt.show()

# Take a Look at the Distribution of majors each year

# use NOCB to fill in the gaps for missing data

# Analyze the distrubtion for each year for each major

# Create a new data frame with the Year, YearsCodePro, and CovertedComp

# Create a box plot for YearsCoded and One for Converted Comp

# Use Multiple Imputation to fill in missing data

# Then create a boxplot with converted comp (y), Years Coded (x)


