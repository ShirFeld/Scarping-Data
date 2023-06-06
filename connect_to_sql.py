import mysql.connector
import os, json

# read JSON file which is in the next parent folder
file = os.path.abspath('') + "/json_data"
json_data=open(file).read()
json_obj = json.loads(json_data)
# print(json_obj)


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Scraping"
)

mycursor = db.cursor()  #cursor object

# mycursor.execute("DESCRIBE jobs")
# for x in mycursor:
#     print(x)


def validate_string(value):
   if value != None:
       return value


# parse json data to SQL insert
for i, item in enumerate(json_obj):
    Title = validate_string(item.get("Title", None))
    Country = validate_string(item.get("Country", None))
    City = validate_string(item.get("City", None))
    job_description = validate_string(item.get("job_description", None))

    mycursor.execute("INSERT INTO jobs (job_title,country,city,job_description) VALUES (%s,	%s,	%s,	%s)", (Title,Country,City,job_description))
    db.commit()



mycursor.execute("SELECT * FROM jobs")
for x in mycursor:
    print(x)

# db.close()