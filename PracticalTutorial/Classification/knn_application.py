'''
Benign = class 2 = good
Malignant = class 4 = bad
'''

import numpy as np
from sklearn import preprocessing, cross_validation, neighbors
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('breast-cancer-wisconsin.data')
df.replace('?', -99999, inplace=True)
df.drop(['id'], 1, inplace=True)

X = np.array(df.drop(['class'], 1))
X = StandardScaler().fit_transform(X)
y = np.array(df['class'])

# Lets visualize entire dataset to get better view of data
# This code based on this tutorial
# https://towardsdatascience.com/pca-using-python-scikit-learn-e653f8989e60

pca = PCA(n_components=2)
principalComponents = pca.fit_transform(X)
principalDf = pd.DataFrame(data = principalComponents
             , columns = ['principal component 1', 'principal component 2'])
print('Variance ratio: ', pca.explained_variance_ratio_)

finalDf = pd.concat([principalDf, df['class']], axis = 1)

print(finalDf.head())


fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(1,1,1)
ax.set_xlabel('Principal Component 1', fontsize = 15)
ax.set_ylabel('Principal Component 2', fontsize = 15)
ax.set_title('2 Component PCA', fontsize = 20)

classes = [2, 4]
colors = ['r', 'b']
for target, color in zip(classes,colors):
    indicesToKeep = finalDf['class'] == target
    ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1']
               , finalDf.loc[indicesToKeep, 'principal component 2']
               , c = color
               , s = 50)
ax.legend(classes)
ax.grid()
plt.show()

# ==========

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X,y, test_size=0.2)

clf = neighbors.KNeighborsClassifier()
clf.fit(X_train, y_train)

accuracy = clf.score(X_test, y_test)
print('Accuracy:', accuracy)

# EXAMPLE PREDICTION
# example_measures = np.array([4,2,1,1,1,2,3,2,1])
#
# prediction = clf.predict(example_measures.reshape(1, -1))
# print(prediction)