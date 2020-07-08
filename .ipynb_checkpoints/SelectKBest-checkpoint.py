# import packages
from sklearn import datasets
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
# load dataset
data = datasets.load_iris()
# separate features and target
X = data.data
y = data.target
# display first 5 rows
X[0:5,:]
# feature engineering. Let's see the best 3 features by setting k = 3
kBest_chi = SelectKBest(score_func=chi2, k=3)
fit_test = kBest_chi.fit(X, y)

# print test scores
fit_test.scores_

adjusted_features = fit_test.transform(X)
adjusted_features[0:5,:]
