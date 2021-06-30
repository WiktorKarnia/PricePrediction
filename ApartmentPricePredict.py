import pandas
from sklearn.linear_model import LinearRegression

data = pandas.read_csv('ApartmentPrice.csv')
model = LinearRegression()
model.fit(data[['year']], data[['price']])
print(model.predict([[2045]]))