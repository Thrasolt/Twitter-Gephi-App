import dbMethods
import crawler

# Definitions
URL = "https://twitter.com/ibdeutschland"

Email = ""
Password = ""

dbMethods.create_table()

crawler.start_crawler(URL, Email, Password)

dbMethods.close_connection()
