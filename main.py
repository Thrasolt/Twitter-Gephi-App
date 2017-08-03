import dbMethods
import crawler
import models

# Definitions
URL = "https://twitter.com/ibdeutschland"

Email = ""
Password = ""

dbMethods.create_table()

crawler.start_crawler(URL, Email, Password, 3)

dbMethods.close_connection()
