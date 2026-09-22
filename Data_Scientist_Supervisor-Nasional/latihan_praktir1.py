import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    'Hours_Studied': [1, 2, 3, 4, 5],
    'Final_Score': [50, 55, 60, 65, 70]
}
df = pd.DataFrame(data)

X = df[['Hours_Studied']] 
y = df['Final_Score']

model = LinearRegression()
model.fit(X, y)

print(f"Intercept (a): {model.intercept_}")
print(f"Slope (b): {model.coef_[0]}")
print(f"R-squared: {model.score(X, y)}")

prediksi = model.predict([[6]])
print(f"Prediksi nilai jika belajar 6 jam: {prediksi[0]}")