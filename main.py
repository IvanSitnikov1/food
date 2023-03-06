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
    name = []
    num = []
    for i in table_products.loc[product]:
        try:
            num.append(int(i) / 100 * weight)
        except ValueError:
            num.append(0)
    for i in table_products.columns:
        name.append(i)
    print(product)
    for i in range(len(name)):
        print(f'{name[i]} = {num[i]}')
        d[name[i]] += num[int(i)]
for k, v in d.items():
    print(k)
    print(v)

