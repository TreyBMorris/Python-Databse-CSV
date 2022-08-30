import pyodbc 

server = 'localhost\SCHWARZ'
database = 'Courses' 
username = 'Laptop\SCHWARZ'
password = '' 
conn = pyodbc.connect('DSN=trey;Trusted_Connection=yes;')
cursor = conn.cursor()
cursor.execute("SELECT name FROM sys.columns WHERE object_id = OBJECT_ID('dbo.Classes')")
columns = cursor.fetchall()
cursor.execute("SELECT * FROM Classes WHERE course_id<10")
rows = cursor.fetchall()


for column in columns:
    print(column)

for row in rows:
    print(row)



