import numpy as np
from sklearn import preprocessing
import pandas as pd

pricing  = pd.read_csv('D:/repository/python_example/AI/assignments/assignment4/data.csv')
Price_array = np.array(pricing['price'])
normalized_price = preprocessing.normalize([Price_array])
print(normalized_price)

# without array

data_top = pricing.head(7)
print(data_top)
names = pricing.columns
d = preprocessing.normalize(pricing)
scalted_df =pd.DataFrame(d,columns=names)
print(scalted_df.head(10))