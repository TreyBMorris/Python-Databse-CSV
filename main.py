#Importing libraries
import pyodbc
import csv

#Connecting to Database
filename = "filename.csv"
server = 'servername'
database = 'database_name'
username = 'username'
password = 'password'
conn = pyodbc.connect('DSN=dsn;Trusted_Connection=yes;')
cursor = conn.cursor()

#SQL Queries retrieving Information from the Database
cursor.execute("SELECT name FROM sys.columns WHERE object_id = OBJECT_ID('dbo.tablename')")
columns = cursor.fetchall()
cursor.execute("SELECT * FROM TableName")
rows = cursor.fetchall()

#Writing to CSV File
with open(filename, 'w') as csvfile:
	
	csvwriter = csv.writer(csvfile)
	csvwriter.writerow(columns)
	csvwriter.writerows(rows)
	