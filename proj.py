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

def endlabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2, height + 1,
        height,
        ha='center', va='bottom', color='white')


def profit_chart():
    fig, ax = plt.subplots(2,2)
    #x = df.groupby(by='Sub-Category').Sales.mean()
    ax[0,0] = sns.barplot(
    data=df, x='Sales', y='Sub-Category', hue='Category',
    estimator='sum', errorbar=None,
    dodge=False)
    plt.xlabel('Sales (in USD)')

    #plt.subplot(2,2,2)
    ax[0,1] = sns.barplot(data=df, x='Profit', y='Sub-Category', hue='Category',
    estimator='sum', errorbar=None,
    dodge=False)
    plt.xlabel('Profit (in USD)')

    fig.subplots(2,1,2)
    ax[1, 0:] = sns.barplot(data=df, x='Profit Margin', y='Sub-Category', hue='Category',
    errorbar=None, estimator='mean',
    dodge=False)
    plt.xlabel('Profit Margins (Percent)')
    
    plt.show()
if __name__ == '__main__':
    profit_chart()