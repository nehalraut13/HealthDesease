import pandas as pd
from sklearn.linear_model import LogisticRegression

file_path = "C:\\Users\\Shreyas\\Desktop\\Resume\\ha.xlsx"

data = pd.read_excel(file_path)

X = data[['age','ch']]
y = data['attack']

model = LogisticRegression();
model.fit(X,y)

print(model.predict([[99,220]]))