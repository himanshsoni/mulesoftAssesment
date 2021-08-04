import sqlite3
connection=sqlite3.connect('Movies.db')
cursor=connection.cursor()

#command to create table
command1=""" CREATE TABLE IF NOT EXISTS Movies(name TEXT PRIMARY KEY,actor TEXT,actress TEXT, director TEXT,year INTEGER) """

cursor.execute(command1)

#command to insert into the table
cursor.execute(" INSERT INTO Movies VALUES ('Sholay','Amitabh Bachchan','Hema Malini','Ramesh Sippy',1975)")
cursor.execute(" INSERT INTO Movies VALUES ('Don','Amitabh Bachchan','Zeenat Aman','Chandra Barot',1978)")
cursor.execute(" INSERT INTO Movies VALUES ('Swades','Sharukh Khan','Gayatri Joshi','Ashutosh Gowariker',2004)")
cursor.execute(" INSERT INTO Movies VALUES ('Main Hoon Na','Sharukh Khan','Sushmita Sen','Farah Khan',2004)")


#command to select all the row from the table
cursor.execute("SELECT * FROM Movies")
results=cursor.fetchall()

#command to select all the rows from the table with WHERE clause
cursor.execute("SELECT * FROM Movies WHERE actor='Amitabh Bachchan' ")
results2=cursor.fetchall()

#orint the results
print(results)

print(results2)