import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score
# Importing the dataset
dataset = pd.read_csv('diabetes.csv')

X = dataset.iloc[:, 0:8].values
X = pd.DataFrame(X)
Y = dataset.iloc[:, 8].values
Y = pd.DataFrame(Y)


X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=7)

scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)

lrc = LogisticRegression(C=100000, fit_intercept=False,solver='lbfgs').fit(X_train, Y_train.values.ravel())
Y_pred = lrc.predict(X_test)
acc = accuracy_score(Y_test,Y_pred)
print("Logistic regression accuracy: "+ str(acc))