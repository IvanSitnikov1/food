import pandas as pd


table_products = pd.read_excel('table_products.xlsx').set_index('Продукты')
#print(table_products.loc[a])
d = {}
for i in table_products.columns:
    d[i] = 0

while True:
    try:
        product, weight = input().split()
        weight = int(weight)
    except ValueError:
        break
    df = {}
    for column in table_products.columns:
        try:
            df[column] = int(table_products.loc[product, column]) / 100 * weight
            d[column] += int(table_products.loc[product, column]) / 100 * weight
        except ValueError:
            df[column] = 0
    print(product)
    for k,  v in df.items():
        print(k, '=', v)

for k, v in d.items():
    print(k)
    print(v)

