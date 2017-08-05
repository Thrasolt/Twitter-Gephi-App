import dbMethods
import crawler
import models

# Definitions
URL = "https://twitter.com/ibdeutschland"

Email = ""
Password = ""
depth = 1

dbMethods.create_table()

for index in range(1, 10):
    try:
        crawler.start_crawler(URL, Email, Password, depth)
    except:
        pass

print("finished")
dbMethods.close_connection()
