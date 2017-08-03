import dbMethods
import crawler
import models

# Definitions
URL = "https://twitter.com/ibdeutschland"

Email = ""
Password = ""

dbMethods.create_table()

for index in range(1, 10):
    try:
        crawler.start_crawler(URL, Email, Password, 3)
    except:
        pass

print("finished")
dbMethods.close_connection()
