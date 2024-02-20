import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
dataset=pd.read_csv('food_dataset.csv')

dataset.shape

X=np.array(dataset.iloc[:,:-1])
X=X.astype(dtype='int')
Y=np.array(dataset.iloc[:,-1])
Y=Y.reshape(-1,)

X_train, X_test, y_train, y_test =train_test_split(X,Y,test_size=0.25,
                                                   random_state=42)

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix, accuracy_score

import seaborn as sb
import joblib
print(X_train.shape)
model_food=RandomForestClassifier(n_estimators=100,criterion='entropy',)
model_food.fit(X_train,y_train)
X_test=[1,0,0,0,1,0,0]



y_predicted=model_food.predict(np.asarray(X_test).reshape(1,-1))
print(y_predicted)
# joblib.dump(model_food, "RF_food_model.joblib")

