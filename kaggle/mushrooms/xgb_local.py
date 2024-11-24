import xgboost as xgb
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd
import time

# load data
FILENAME = "mushroom_vertical_trim"
df = pd.read_csv("./"+FILENAME+".csv")

# split data into X and y
X = df[df.columns[1:-1]]
Y = df[df.columns[0]]
# split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
# fit model no training data
start = time.time()
eval_set = [(X_train, y_train), (X_test, y_test)]
model = xgb.XGBClassifier(max_depth=8, eta=0.1, objective="binary:logistic", eval_metric="auc", tree_method="hist", nthread=16, verbose=True, early_stopping_rounds=2)
model.fit(X_train, y_train, eval_set=eval_set)
end = time.time()
print("Time Elapsed: "+str(end-start))
results = model.evals_result()
epochs = len(results['validation_0']['auc'])
x_axis = range(0, epochs)

fig, ax = plt.subplots()
ax.plot(x_axis, results['validation_0']['auc'], label='Train')
ax.plot(x_axis, results['validation_1']['auc'], label='Test')
ax.legend()
plt.ylabel('AUC')
plt.title('XGBoost AUC')
plt.savefig("XGBoost AUC.png")

xgb.plot_importance(model)
plt.rcParams['figure.figsize'] = [12,9]
plt.savefig("f_score_"+FILENAME+".png")

#          max_depth = 8
 #         eta = 0.1
  #        objective = "binary:logistic"
   #       eval_metric = "auc"
    #      tree_method ="hist"
     #     nthread = 16
