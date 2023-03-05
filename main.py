import pandas as pd


table_products = pd.read_excel('table_products.xlsx').set_index('Продукты')
#print(table_products.loc[a])
d = {}
for i in table_products.columns:
    d[i] = 0

a = input()
while a != '0':
    name = []
    num = []
    for i in table_products.loc[a]:
        num.append(i)
    for i in table_products.columns:
        name.append(i)
    print(a)
    for i in range(len(name)):
        print(f'{name[i]} = {num[i]}')
        try:
            d[name[i]] += num[int(i)]
        except:
            pass
    a = input()
for k, v in d.items():
    print(k)
    print(v)

