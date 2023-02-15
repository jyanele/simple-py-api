import psycopg2

conn = psycopg2.connect(
    "dbname=rectrackv3_uat user=bfifarms password=superpw64 host=94.237.65.245 port=5432")

cursor = conn.cursor

cursor.execute("""SELECT * FROM roles""")
roles = cursor.fetchall()

print(roles)

cursor.close()
conn.close()
