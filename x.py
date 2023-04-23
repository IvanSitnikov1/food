from app import create_product_base
import sqlite3

con = sqlite3.connect('./instance/product_base.db')
cursor = con.cursor()
cursor.execute('select * from product where "Продукты" = "Крупа овсяная"')
print(cursor.fetchall())