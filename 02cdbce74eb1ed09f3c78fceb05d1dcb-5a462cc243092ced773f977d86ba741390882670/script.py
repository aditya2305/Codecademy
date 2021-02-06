import codecademylib3_seaborn
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

flags = pd.read_csv('flags.csv', header = 0)

labels = flags['Landmass']
data = flags[["Red","Green","Blue","Gold","White","Black","Orange"]]
train_data, test_data, train_labels, test_labels = train_test_split(data, labels, random_state = 1)

scores = []
for i in range(1,21):
 tree = DecisionTreeClassifier(random_state =1, max_depth =i)
 tree.fit(train_data, train_labels)
 scores.append(tree.score(test_data, test_labels))

#To improve performance we include all the characterstics of a flag in data

data_1 = flags[["Red", "Green", "Blue", "Gold",
 "White", "Black", "Orange",
 "Circles",
"Crosses","Saltires","Quarters","Sunstars",
"Crescent","Triangle"]]

train_data, test_data, train_labels, test_labels = train_test_split(data_1, labels, random_state = 1)

scores_1 = []
for i in range(1,21):
 classifier = DecisionTreeClassifier(max_depth =i)
 classifier.fit(train_data, train_labels)
 scores_1.append(classifier.score(test_data, test_labels))

plt.plot(range(1,21), scores_1)
plt.plot(range(1,21), scores)
plt.xlabel('Depth Of Tree')
plt.ylabel('Accuracy')
plt.title('Accuracy Of A Tree On Different Features')
plt.legend(['14 Features','7 Features'])
plt.show()