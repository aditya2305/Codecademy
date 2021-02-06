import codecademylib3_seaborn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('passengers.csv')
#print(df.head())

df['Sex'] = df['Sex'].apply(lambda x : 1 if x=='male' else 0)
df['FirstClass'] = df.Pclass.apply(lambda x: 1 if x==1 else 0) 
df['SecondClass'] = df.Pclass.apply(lambda x: 1 if x==2 else 0) 
df['ThirdClass'] = df.Pclass.apply(lambda x: 1 if x==3 else 0) 
df.Age = df.Age.fillna(np.mean(df.Age))

features = df[['Sex','Age','FirstClass','SecondClass']]
survival = df.Survived

train_1, test_1, train_2, test_2 = train_test_split(features, survival, test_size =0.2)

new = StandardScaler()
train_1 = new.fit_transform(train_1)
test_1 = new.transform(test_1)

model = LogisticRegression()
model.fit(train_1, train_2)

print(model.score(train_1, train_2))
print(model.score(test_1,test_2))

Jack = np.array([0.0,20.0,0.0,0.0])
Rose = np.array([1.0,17.0,1.0,0.0])
Me = np.array([1.0,20.0,0.0,0.0])

sample_passengers = np.array([Jack, Rose, Me])
sample_passengers = new.transform(sample_passengers)
print(model.predict(sample_passengers))

