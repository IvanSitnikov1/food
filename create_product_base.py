import pandas as pd
import sqlite3


con = sqlite3.connect('./instance/product_base.db')
df = pd.read_excel('table_products.xlsx')
df.to_sql('product', con=con, if_exists='append')
pd.read_sql('select * from product', con)
print(df)