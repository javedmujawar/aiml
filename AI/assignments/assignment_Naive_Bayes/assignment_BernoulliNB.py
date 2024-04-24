# import lib. section
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import confusion_matrix,accuracy_score
# import dataset
df = pd.read_csv('maharashtrian.csv')
# data mapping
d = {'regularly': 0, 'occasionaly': 1, 'no': 2}
e = {'no': 0, 'yes': 1}
f = {'no': 0, 'yes': 1}
g = {'no': 0, 'yes': 1}

df['saree-or-pheta'] = df['saree-or-pheta'].map(d)
df['misal'] = df['misal'].map(e)
df['vada-pav'] = df['vada-pav'].map(f)
df['puran-poli'] = df['puran-poli'].map(g)

features = ['saree-or-pheta', 'misal', 'vada-pav', 'puran-poli']
X = df[features]
Y = df['Maharashtrian']
print("===============================")
print(X)
print("===============================")
print(Y)

# split data for traing 
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.20, random_state=0)
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
clf = BernoulliNB()
clf.fit(X_train, Y_train)

print("===============================")
print(X_train)
print("===============================")
print(X_test)
Y_pred = clf.predict(X_test)
print("===============================")

print(Y_pred)
print(Y_test)
cm = confusion_matrix(Y_test,Y_pred)
ac = accuracy_score(Y_test,Y_pred)
print(cm)
print(ac)
