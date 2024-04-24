import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
print(plt.style.available)
style.use('ggplot')
x = ["Kolhapur","Pune","Mumbai","Nagpur","Sangli","Nanded","Amravati"]
y1 = [18,45,55,40,15,20,17]
y2 = [22,55,75,50,25,25,28]
xPoints = np.array(x)
y1Points = np.array(y1)
y2Points = np.array(y2)
plt.scatter(xPoints,y1Points, color="g", label="house value")
plt.scatter(xPoints,y2Points, color="r", label="prime location value")
plt.xlabel("City")
plt.ylabel("value of house in lakh")
plt.title("Houses for sale")
plt.legend()
plt.show()