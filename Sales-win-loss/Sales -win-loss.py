from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn import preprocessing


Sales_Win_Loss_data=pd.read_csv("E:\msc AI\SEM -II\AP\Prac2\Sales-Win-Loss.csv")
le = preprocessing.LabelEncoder()


Sales_Win_Loss_data['Route To Market'] = le.fit_transform(Sales_Win_Loss_data['Route To Market'])
Sales_Win_Loss_data['Opportunity Result'] = le.fit_transform(Sales_Win_Loss_data['Opportunity Result'])
Sales_Win_Loss_data['Competitor Type'] = le.fit_transform(Sales_Win_Loss_data['Competitor Type'])
Sales_Win_Loss_data['Supplies Group'] = le.fit_transform(Sales_Win_Loss_data['Supplies Group'])
Sales_Win_Loss_data['Region'] = le.fit_transform(Sales_Win_Loss_data['Region'])
Sales_Win_Loss_data['Supplies Subgroup'] = le.fit_transform(Sales_Win_Loss_data['Supplies Subgroup'])

Sales_Win_Loss_data.head()
cols = [col for col in Sales_Win_Loss_data.columns if col not in ['Opportunity Number','Opportunity Result']]
data = Sales_Win_Loss_data[cols]
target = Sales_Win_Loss_data['Opportunity Result']


data_train, data_test, target_train, target_test = train_test_split(data,target, test_size = 0.30, random_state = 10)

neigh = KNeighborsClassifier(n_neighbors=3)

neigh.fit(data_train, target_train)

pred = neigh.predict(data_test)
a=le.inverse_transform(pred[:20])
print("Predicted target name: {}".format(a))


print ("KNeighbors accuracy score : ",accuracy_score(target_test, pred))
