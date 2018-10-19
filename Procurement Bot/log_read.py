import sqlite3

#con1 = sqlite3.connect('item_list.db')
con1 = sqlite3.connect('order_list.db')

#cur1 = con1.execute("SELECT strftime('%m',PLACED_AT) as mon, FROM USER_ORDER GROUP BY mon");
cur1 = con1.execute("SELECT strftime('%y',a.PLACED_AT) as yr,strftime('%m',a.PLACED_AT) as mon,a.PROD_ID,a.PROD, sum(b.QTY)"
                    " FROM USER_ORDER a INNER JOIN USER_ORDER b on a.PROD_ID=b.PROD_ID GROUP BY a.PROD_ID, a.PROD order by yr,mon");


for row in cur1:
    x = row[0]
    y = row[1]
    z = row[2]
    a = row[3]
    b = row[4]
    print(str(y)+" "+str(z)+" "+str(a)+" "+str(b))