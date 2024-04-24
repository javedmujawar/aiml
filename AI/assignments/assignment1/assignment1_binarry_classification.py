# Import section
from sklearn import preprocessing 
from sklearn.neighbors import KNeighborsClassifier 

# data collection
fever =[102,103,101,99.9,100,100,102,100,99.9,102,99.9,101,103,103,102]
sore_throat=['yes','yes','no','yes','yes','no','no','no','yes','yes','yes','yes','no','no','no']
cold =['yes','yes','yes','no','no','yes','yes','no','yes','no','no','yes','yes','yes','no']
covid_check=['yes','yes','no','no','yes','yes','yes','no','no','yes','no','yes','yes','yes','no']

# create label encoder object
ln = preprocessing.LabelEncoder()

# Converting string labels into numberical values
sore_throat = ln.fit_transform(sore_throat)
cold = ln.fit_transform(cold)
covid_check = ln.fit_transform(covid_check)

#print encoded values
print("Sore throat encoded values: ", sore_throat)
print("Cold encoded values: ", cold)
print("Covid check encoded values: ", covid_check)

# Combine multiple columns or features into a single set of data using "zip" function 
feature = list(zip(fever,sore_throat,cold))

# Model object creation
knModel = KNeighborsClassifier(n_neighbors=3)

# train model
knModel.fit(feature,covid_check)

# Predict based on user input
print("================== User Input ======================")
iFever = float(input("Please enter fever: "))
iSoreThroat = int(input("Do you have sore throat? (Yes = 1 / No = 0): "))
iCold = int(input("Do you have cold? (Yes = 1 / No = 0): "))
# Predict 
prediction = knModel.predict([[iFever,iSoreThroat,iCold]])

#print predicted values
print("================== Result ======================")

print("Prediction value is:", prediction)
if(prediction):
    print("You should test covid.")
else:
    print("No need to test covid.")
