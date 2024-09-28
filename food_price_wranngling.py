import pandas as pd
import re

df = pd.read_csv("Food Prices.csv")

# Splitting "Products" column into product and quantity
df[['Product', 'Quantity']] = df['Products'].str.extract(r'(.+), per (.+)', expand=True)
df['YEAR'] = pd.to_datetime(df['REF_DATE']).dt.year


# Generalising products
def g_products(product):
    if isinstance(product, str):
        product = product.lower()
        if "beef" in product:
            return "Beef"
        elif "chicken" in product:
            return "Chicken"
        elif any(p in product for p in ["pork", "bacon", "wieners"]):
            return "Pork"
        elif any(p in product for p in ["salmon", "tuna", "shrimp"]):
            return "Sea Food"
        elif any(p in product for p in ["milk", "cream", "butter", "margarine", "cheese", "yogurt"]):
            return "Dairy Products"
        elif "potatoes" in product:
            return "Potatoes"
        elif "onions" in product:
            return "Onions"
        elif "lettuce" in product:
            return "Lettuce"
        elif "bread" in product:
            return "Bread"
        elif "peas" in product:
            return "Peas"
        elif "strawberries" in product:
            return "Strawberries"
        elif "spinach" in product:
            return "Spinach"
        elif "broccoli" in product:
            return "Broccoli"
        elif "corn" in product:
            return "Corn"
        elif "pasta" in product:
            return "Pasta"
        elif "rice" in product:
            return "Rice"
        elif "flour" in product:
            return "Flour"
        elif "sugar" in product:
            return "Sugar"
        elif "oil" in product:
            return "Oil"
        elif "juice" in product:
            return "Juice"
        elif "beans" in product:
            return "Beans"
    return None


# using the g_products function
df['Product'] = df['Product'].apply(g_products)

# Dropping None/Nan/other rows
df = df.dropna(subset=['Product'])


# Converting quantity and price adjustment
def convert_quantity(row):
    quantity = row['Quantity'].lower()
    value = row['VALUE']

    # extracting number from string. \d+\.?\d* this part is called regex you can look it up on google
    num = float(re.findall(r'\d+\.?\d*', quantity)[0]) if re.search(r'\d+\.?\d*', quantity) else 1

    # Conversion based on units
    if 'kg' in quantity or 'kilogram' in quantity:
        return value / num, '1 kg'
    elif 'gram' in quantity:
        return value * (1000 / num), '1 kg'
    elif 'litre' in quantity or 'ml' in quantity:
        if 'ml' in quantity:
            return value * (1000 / num), '1 litre'
        else:
            return value / num, '1 litre'
    else:
        return value / num, '1 unit'


# quantity conversion using defined fun
df[['VALUE', 'Quantity']] = df.apply(convert_quantity, axis=1, result_type='expand')

# Grouping by product, GEO, and year, and calculating the average value
df_grouped = df.groupby(['YEAR', 'GEO', 'Product']).agg({'VALUE': 'mean'}).reset_index()

df_grouped.to_csv('Cleaned_Food_Prices.csv', index=False)

print(df_grouped)