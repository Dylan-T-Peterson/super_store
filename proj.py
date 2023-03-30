import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Creates dataframe based off of superstore.xls
fileloc = 'data/superstore.xls'
df = pd.read_excel(fileloc)
