import pyodbc

server = 'KLBLRLP1868\SQLEXPRESS'
database = 'master'
username = 'sa'
password = 'root@123'

# Establishing a connection to the SQL Server
def connect_to_server():
    try:
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};\
                            SERVER='+server+';\
                            DATABASE='+database+';\
                            UID='+username+';\
                            PWD='+ password)
        cursor = cnxn.cursor()
        print("Connection to database is successful!")
    except:
        print("Problem while connecting to database!")
    return cursor