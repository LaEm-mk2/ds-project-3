import pandas as pd
import sqlite3

cons = sqlite3.connect('./samsung.db')
cursor = cons.cursor()

query = cursor.execute("SELECT * FROM samsung;")
cols = [column[0] for column in query.description]
df = pd.DataFrame.from_records(data=query.fetchall(),columns=cols)

target = 'Price'
features = df.drop(['Date''Price'],axis=1)

df_target = df[target]

cursor.close()
cons.close()

from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score

X_train = features[:814]
y_train = df_target[:814]
X_test = features[814:]
y_test = df_target[814:]

pipe_linear = Pipeline([('scl',StandardScaler()),
                        ('fit',LinearRegression())])

pipe_linear.fit(X_train,y_train)

y_preds = pipe_linear.predict(X_test)

import pickle

with open('./flask_app/model/model.pkl','wb') as pickle_file:
    pickle.dump(pipe_linear,pickle_file)