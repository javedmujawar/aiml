import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
print(plt.style.available)
style.use('ggplot')
x = ["Kolhapur","Pune","Mumbai","Nagpur","Sangli","Nanded","Amravati"]
y = [18,45,55,40,15,20,17]

cols = ['c','m','r','b','y','k','g']

plt.pie(y,labels=x, colors=cols, startangle=90, shadow=True, autopct='%1.1f%%')
plt.title("Houses for sale")
plt.show()