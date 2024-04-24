import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
x=[51, 62, 69, 64, 65, 56, 58, 57, 55, 54]
y=[167, 182, 176, 173, 172, 174, 169, 173, 170, 174]
classes = ['red', 'blue', 'blue', 'blue', 'blue', 'red', 'blue', 'blue', 'blue', 'red']
classes1 = ['U', 'N', 'N', 'N', 'N', 'U', 'N', 'N', 'N', 'U']
plt.scatter(x, y, c=classes)
#plt.show()
data1 = list(zip(x,y))
#print(data1)
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(data1,classes1)
newx =50
newy =182
prediction = knn.predict([(newx, newy)])
print(prediction)