# Making the app, Project Exercise with Mysql and python with english dictionary
import mysql.connector

con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)

cursor = con.cursor()
query = cursor.execute("SeLECT * FROM Dictionary")
results = cursor.fetchall()

print(results)