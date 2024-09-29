import pandas as pd

df = pd.read_csv('health_diet_price.csv')

proportions = {
    'Meat': 0.15,
    'Vegetables': 0.30,
    'Fruits': 0.20,
    'Other': 0.35
}
total_daily_consumption = 1.5

df['Avg_consumption'] = df['Product'].map(proportions) * total_daily_consumption

df['per_day_cost'] = df['Avg_consumption'] * df['VALUE']
df['per_day_cost'] = df['per_day_cost'].round(2)

df['per_day_cost'] = df['per_day_cost'].apply(lambda x: f'${x:.2f}')

df['Product'] = df['Product'].replace("Other", "Other (Cereals & Dairy)")

df.to_csv('health_diet_cost.csv', index=False)

print(df)
