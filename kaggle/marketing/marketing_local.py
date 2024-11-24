import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_auc_score, roc_curve
import matplotlib.pyplot as plt
from sklearn.linear_model import SGDClassifier, LogisticRegression

from subprocess import check_output
from datetime import time

df = pd.read_csv("./marketing_campaign.csv", sep='\t')

#print(df.shape)

#df.head()
#print(df.describe())

#drop NaN lines
df = df.dropna(subset=["Income"])
df = df.drop(['ID', 'Year_Birth', 'Education', 'Marital_Status', 'Dt_Customer'], axis=1)



#drop Irrelevant collumns
X = df[df.columns[4:-1]]
#X = df.drop(['ID', 'Year_Birth', 'Education', 'Marital_Status', 'Dt_Customer', 'Response'], axis=1)
y = df[df.columns[-1]]
#y = df['Response']
#print(df)
#Label encoding instead of drop

scaler = StandardScaler()
X = scaler.fit_transform(X)

#df = scaler.fit_transform(df)
#data = df.values
#X = data[:, 1:] # all rows, no label
#y = data[:, 0]  # all rows, label only

#print(df)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, shuffle=True, random_state=2200)

#scaler = StandardScaler()
#scaler.fit(X_train)
#X_train = scaler.transform(X_train)
#X_test = scaler.transform(X_test)


print(X_test.shape)
print(y_test.shape)

print(X_train.shape)
print(y_train.shape)

#print(X_train)


#model = SGDClassifier(loss="log_loss", penalty="l2", learning_rate="constant", eta0=0.0001, fit_intercept=True)
model = LogisticRegression()
model.fit(X_train, y_train)
y_results = model.predict(X_test)
print("Accuracy: ", model.score(X_test, y_test))


clf = model
#auc = roc_auc_score(y_test, clf.decision_function(X_test))
auc = roc_auc_score(y_results, y_test)
print("AUC Score: ", auc)
#print("AUC Score: ", roc_auc_score(y_test, y_results))

#code from stack overflow for roc
y_pred_proba = clf.predict_proba(X_test)[::,1]
fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
plt.plot(fpr, tpr, label="AUC = "+str(auc))
plt.ylabel("True Positive Rate")
plt.xlabel("False Positive Rate")
plt.legend(loc=4)
plt.savefig("auc_fig.png")

#from sklearn import metrics
#print("AUC method: ", str(metrics.auc(fpr,tpr)))