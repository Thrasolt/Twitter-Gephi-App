from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.action_chains import ActionChains
import getpass
import time


def start_crawler(url, email, password):


    #Definitions
    def page_loaded(driver):
        return driver.find_element_by_tag_name("body") != None

    # Opening the web browser and the twitter page
    driver = webdriver.Firefox(executable_path=r'F:\Dokumentation\Programme\Geckodriver\geckodriver.exe')
    driver.get(url)
    wait = ui.WebDriverWait(driver, 10)
    wait.until(page_loaded)

    #Signing in
    actions = ActionChains(driver)
    actions.send_keys(email)
    actions.send_keys(Keys.TAB)
    actions.send_keys(password)
    actions.send_keys(Keys.ENTER)
    actions.perform()
    time.sleep(5)

    # following
    driver.get(url+"/following")





    '''
    # print(driver.page_source)

    # Finding email and password fields and sending the keys
    email = driver.find_element_by_id("email")
    email.send_keys(input_email_id)
    pwd = driver.find_element_by_id("pass")
    pwd.send_keys(input_pwd)
    pwd.send_keys(Keys.RETURN)

    time.sleep(5)

    driver.get("https://www.facebook.com/groups/464961190503556/")
    time.sleep(5)
    #text_box = driver.find_element_by_xpath("/html/body/div[@id='composer_text_input_box']")
    text_box = driver.find_element_by_id('rc.u_0_2f')
    #text_box = driver.find_element_by_id('composer_text_input_box')
    #text_box = driver.find_element_by_css_selector(".uiTextareaAutogrow._552m")
    text_box.click()
    time.sleep(5)
    actions = ActionChains(driver)
    actions.send_keys(post)
    actions.send_keys(Keys.RETURN)
    actions.perform()
    time.sleep(5)
    button = driver.find_element_by_xpath('//button[@type="submit" and @value="1" and @class="_1mf7 _4jy0 _4jy3 _4jy1 _51sy selected _42ft"]')
    button.click()
    time.sleep(5)
    driver.close()


    driver.get("https://www.facebook.com/events/birthdays")

    box_count = len(driver.find_elements_by_class_name("innerWrap"))

    for x in range(0, box_count):
    	text_box = driver.find_element_by_tag_name('textarea')
    	text_box.send_keys("Happy Birthday!! \n")
    	# The birthday message

'''
