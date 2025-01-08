import pandas as pd
import re

df = pd.read_csv("Food Prices.csv")

df[['pn', 'quantity']] = df['Products'].str.extract(r'(.+), per (.+)', expand=True)
df['year'] = pd.to_datetime(df['REF_DATE']).dt.year

df = df[df['year'] == 2023]

def cp(pn):
    if isinstance(pn, str):
        pn = pn.lower().strip()
        if any(keyword in pn for keyword in ['beef', 'chicken', 'pork', 'salmon', 'tuna', 'shrimp']):
            return "Meat"
        categories = {
            "Dairy products": ["milk", "cream", "butter", "margarine", "cheese", "yogurt", "whipping", "sour cream",
                               "skim milk"],
            "Vegetables": ["potato", "onion", "lettuce", "peas", "spinach", "broccoli", "beans", "corn", "tomato",
                           "cabbage", "pepper"],
            "Bread": ["bread"],
            "Eggs": ["eggs"],
            "Pasta": ["pasta"],
            "Rice": ["rice"],
            "Wheat": ["flour", "wheat"],
            "Sugar": ["sugar"],
            "Oil": ["oil"],
            "Fruits": ["strawberries", "juice", "squash", "apple", "orange", "banana", "pear", "grape"],
        }
        for category, keywords in categories.items():
            if any(re.search(r'\b' + re.escape(k) + r'\b', pn) for k in keywords):
                return category
    return "Other"

df['product_category'] = df['pn'].apply(cp)
df_cleaned = df.dropna(subset=['product_category']).copy()

def convert_quantity(row):
    quantity = row['quantity']
    if isinstance(quantity, str):
        quantity = quantity.lower()
    else:
        return None

    value = row['VALUE']
    num = float(re.findall(r'\d+\.?\d*', quantity)[0]) if re.search(r'\d+\.?\d*', quantity) else 1

    if 'kg' in quantity or 'kilogram' in quantity:
        return value / num
    elif 'gram' in quantity:
        return value * (1000 / num)
    elif 'litre' in quantity or 'ml' in quantity:
        return value * (1000 / num) if 'ml' in quantity else value / num
    return value / num

df_cleaned['VALUE'] = df_cleaned.apply(convert_quantity, axis=1)
df_cleaned.drop(columns=['quantity'], inplace=True)

df_cleaned = df_cleaned[df_cleaned['GEO'] != 'Canada']

df_health_diet = df_cleaned.groupby('product_category').agg(VALUE=('VALUE', 'mean')).reset_index()

df_health_diet['VALUE'] = df_health_diet['VALUE'].round(2)

df_health_diet = df_health_diet.rename(columns={'product_category': 'Product'})

df_health_diet.to_csv('health_diet_price.csv', index=False)

print(df_health_diet)
