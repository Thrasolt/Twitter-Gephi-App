def scroll(driver, count):

    index = 1
    while index <= count:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        index += 1
