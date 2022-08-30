import pyodbc
import csv

filename = "c:/Users/Laptop/Documents/Coding/Python/Database/classes.csv"
server = 'localhost\SCHWARZ'
database = 'Courses'
username = 'Laptop\SCHWARZ'
password = ''
conn = pyodbc.connect('DSN=trey;Trusted_Connection=yes;')
cursor = conn.cursor()
cursor.execute(
	"SELECT name FROM sys.columns WHERE object_id = OBJECT_ID('dbo.Classes')")
columns = cursor.fetchall()
cursor.execute("SELECT * FROM Classes WHERE course_id<10")
rows = cursor.fetchall()


with open(filename, 'w') as csvfile:
	
	csvwriter = csv.writer(csvfile)
	csvwriter.writerow(columns)
	csvwriter.writerows(rows)
	