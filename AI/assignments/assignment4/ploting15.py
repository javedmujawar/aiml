import numpy as np
from sklearn import preprocessing

House_prices = [18,45,55,40,15,20,17]
Price_array = np.array(House_prices)
normalized_price = preprocessing.normalize([Price_array])
print(normalized_price)