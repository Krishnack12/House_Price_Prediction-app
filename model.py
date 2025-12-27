import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib


data = pd.read_csv("BHP.csv")

print("Original Columns:")
print(data.columns)


data = data.drop(columns=[
    'area_type',
    'availability',
    'location',
    'society'
], errors='ignore')


data['size'] = data['size'].str.split().str[0]
data['size'] = pd.to_numeric(data['size'], errors='coerce')


def convert_sqft(value):
    try:
        if '-' in str(value):
            a, b = value.split('-')
            return (float(a) + float(b)) / 2
        return float(value)
    except:
        return None

data['total_sqft'] = data['total_sqft'].apply(convert_sqft)


print("\nNull values before cleaning:")
print(data.isnull().sum())

data = data.dropna()

print("\nNull values after cleaning:")
print(data.isnull().sum())

X = data[['total_sqft', 'bath', 'balcony', 'size']]
y = data['price']


model = LinearRegression()
model.fit(X, y)


joblib.dump(model, "house_model.pkl")

print("\n✅ Model trained and saved successfully!")
