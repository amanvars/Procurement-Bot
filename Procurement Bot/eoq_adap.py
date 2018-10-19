import sqlite3
import math

conn = sqlite3.connect('eoq.db')

cur = conn.execute("SELECT * from eoq_analyse where PROD_ID=?",(4,))

for row in cur:
    pid = row[0]
    nm = row[1]
    demand = row[2]
    ocost = row[3]
    hcost = row[4]

eoq = math.sqrt((2*demand*ocost)/hcost)

eoq = int(round(eoq))

conn.execute("UPDATE eoq_analyse SET EOQ=?,ORD_COST=? WHERE PROD_ID=?",(eoq,4))
conn.commit()
conn.close()


#conn.close()