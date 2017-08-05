def scroll(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


"""
def executeThread():
    crawler.start_crawler(URL, Email, Password, depth)
    try:
        crawler.start_crawler(URL, Email, Password, depth)
    except:
        try:
            crawler.start_crawler(URL, Email, Password, depth)
        except:
            pass

for index in range(1, 2):
    thread = threading.Thread(target=executeThread, args=())
    thread.start()
    time.sleep(60)

"""
