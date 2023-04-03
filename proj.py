import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Creates dataframe based off of superstore.xls and formats floats
fileloc = 'data/superstore.xls'
df = pd.read_excel(fileloc)

df.Profit = df.Profit.round(2)
df.Sales = df.Sales.round(2)
#Creates Pandas series for valuable calculations
df['Profit Margin'] = ( (df.Profit / df.Sales) * 100 ).round(2)
df['Lead Time'] = df['Ship Date'] - df['Order Date']

def profit_chart():
    plt.subplot(2,2,1)
    x = df.groupby(by='Sub-Category').Sales.mean()
    sns.barplot(data=df, x='Sales', y='Sub-Category', hue='Category')

    plt.subplot(2,2,2)
    sns.barplot(data=df, x='Profit', y='Sub-Category', hue='Category')

    plt.subplot(2,1,2)
    sns.barplot(data=df, x='Profit Margin', y='Sub-Category', hue='Category')
if __name__ == '__main__':
    profit_chart()##