import warnings
warnings.filterwarnings("ignore")

import pandas
import sklearn
import xgboost
import sklearn.linear_model
import random
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import KBinsDiscretizer
from datetime import datetime
from scipy.io.arff import loadarff

customer = pandas.read_csv("./marketing_campaign.csv", sep="\t")
customer = customer.drop(columns = ["Z_CostContact", "Z_Revenue", "Dt_Customer"])
customer

#woe coding
def woe(data):
    import math
    large1, large0 = sum(data[data.columns[-1]]), sum(data[data.columns[-1]] == False)
    for column in data.columns[:-1]:
        local = {}
        for unique in set(data[column].unique()):
            local_1, local_0 = sum(data[data[column] == unique][data.columns[-1]]), sum(data[data[column] == unique][data.columns[-1]] == False)
            if local_1 == 0:
                local[unique] = 0
            elif local_0 != 0:
                local[unique] = (
                                    math.log(
                                            (local_1/large1)/(local_0/large0)  
                                            )
                                )
            else:
                local[unique] = (
                                (local_1/large1)
                                )
        temp = []
        for row in data[column]:
            temp.append(local[row])
        data[column] = temp
    return data

#woe coding
processed = woe(customer[["Education", "Marital_Status", "Response"]])
customer[["Education", "Marital_Status", "Response"]] = processed

#filling missing value
customer["Income"] = customer["Income"].fillna(customer["Income"].mean())

#standardization
numf = [i for i in customer.columns if i not in ["ID", "Education", "Marital_Status", "Response"]]
standardize = customer[numf]
ss = StandardScaler()
standardize = ss.fit_transform(standardize)
customer[numf] = standardize

#data split
x = customer[customer.columns[1:-1]]
y = customer[customer.columns[-1]]
train_x, test_x, train_y, test_y = train_test_split(x, y, test_size = 0.3, random_state = 2200)

#LR
lr_cls = sklearn.linear_model.LogisticRegression()
lr_clf = lr_cls.fit(train_x, train_y)

#prediction, print evaluation results
lr_predict_y = lr_clf.predict(test_x)
fpr, tpr, threshold = sklearn.metrics.roc_curve(lr_predict_y, test_y)
print("\nLR accuracy: {}\nLR auc: {}\nKS: {}".format(sum(lr_predict_y == test_y)/len(lr_predict_y), 
                                             sklearn.metrics.roc_auc_score(lr_predict_y, test_y),
                                                    max(tpr-fpr)))