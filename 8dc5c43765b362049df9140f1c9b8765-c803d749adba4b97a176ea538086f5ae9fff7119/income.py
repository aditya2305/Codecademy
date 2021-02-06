def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier

income = pd.read_csv('income.csv', header = 0, delimiter =', ')

income['sex-int'] = income['sex'].apply(lambda x : 0 if x=='Male' else 1 )

income['country-int'] = income['native-country'].apply(lambda x: 0 if x=='United-States' else 1)

print(income.iloc[0])
labels = income['income']
data = income[['age', 'capital-gain', 'capital-loss', 'hours-per-week', 'sex-int', 'country-int']]

train_data, test_data, train_labels, test_labels = train_test_split(data, labels, random_state =1)

forest = RandomForestClassifier(random_state =1)
forest.fit(train_data, train_labels)

print(forest.score(test_data, test_labels))
