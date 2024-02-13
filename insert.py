import sqlite3

conn = sqlite3.connect('example.db')
print("Opened database successfully")

conn.execute("INSERT INTO EMPLOYEES VALUES (1,'CYNTHIA CROUSE',23,463255.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (2,'MATHIAS JAMES',29,122223.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (3,'CRISPINE YEGO',35,32344.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (4,'ANNA MICHAEL',33,324434.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (5,'JAMES THOMPSON',45,343255.00)")

conn.commit()
print("Records inserted successfully")
conn.close()
