import mysql.connector
print("IMPORT OK")
from db import get_conn
conn = get_conn()
print(conn.is_connected())
conn.close()