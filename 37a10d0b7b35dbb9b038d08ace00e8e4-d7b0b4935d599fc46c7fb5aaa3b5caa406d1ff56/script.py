import codecademylib3_seaborn
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
from sklearn.neighbors import KNeighborsClassifier
from matplotlib import pyplot as plt

breast_cancer_data = load_breast_cancer()

#print(breast_cancer_data.data[0])
#print(breast_cancer_data.feature_names)
#print(breast_cancer_data.target)
#print(breast_cancer_data.target_names)

training_data, validation_data, training_labels, validation_labels= train_test_split(breast_cancer_data.data, breast_cancer_data.target, test_size = 0.2, random_state = 100)


print(len(training_data), len(training_labels))


score_list = []
for i in range(1,100):
  classifier = KNeighborsClassifier(n_neighbors = i)
  classifier.fit(training_data, training_labels)
  score = classifier.score(validation_data, validation_labels)
  score_list.append(score)

print(score_list)
plt.plot(range(1,100),score_list)
plt.xlabel('K')
plt.ylabel('Validation Accuracy')
plt.title('Breast Cancer Classifier Accuracy')
plt.show()