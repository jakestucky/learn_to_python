import psycopg2
#connect to the db
con = psycopg2.connect(
     host="localhost",
     database="Bank",
     user="jakestucky",
     password="",
     port = "5432",
)

cur = con.cursor()

cur.execute('select "id", "username" from accounts')

rows = cur.fetchall()

for r in rows:
    print(r)

cur.close()


#close db connection
con.close()