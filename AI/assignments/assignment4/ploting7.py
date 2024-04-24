import numpy as np
import matplotlib.pyplot as plt

x = ["Kolhapur","Pune","Mumbai","Nagpur","Sangli","Nanded","Amravati"]
y = [18,45,55,40,15,20,17]
xPoints = np.array(x)
yPoints = np.array(y)
plt.plot(xPoints,yPoints, color="g", linewidth="10.5")
plt.xlabel("City")
plt.ylabel("value of house in lakh")
plt.title("Houses for sale")
plt.show()