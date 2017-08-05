from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup

import getpass
import time
import utils
import models
from random import shuffle

def start_crawler(url, email, password, depth):


    #Check if page has loaded
    def page_loaded(driver):
        return driver.find_element_by_tag_name("body") != None

    # Log and sign into twitter - definde or redefine driver
    def log_in():
        # Opening the web browser and the twitter page
        driver = webdriver.Chrome(executable_path=r'F:\Dokumentation\Programme\ChromeDriver\chromedriver.exe')
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
        return driver


    # Opening the web browser and the twitter page
    driver = log_in()

    # Get first node
    html_doc = driver.page_source
    soup = BeautifulSoup(html_doc, 'html.parser')

    # Create Anchor
    id = len(models.GephiNode.objects.all()) + 1
    print("id: ", id)
    label = soup.find("a", {"class":"ProfileHeaderCard-nameLink u-textInheritColor js-nav"}).get_text()
    print("label: ", label)
    try:
        fan_count = soup.findAll("span", {"class":"ProfileNav-value"})[2].get_text()
    except:
        fan_count = 0

    print("fan_count: ", fan_count)
    handle = soup.find("b", {"class":"u-linkComplex-target"}).get_text()
    print("handle: ", handle)
    Anchor = models.GephiNode(id=id, label=label, fan_count=fan_count, handle=handle)
    Anchor.create()
    print("Anchor: ", Anchor.id, Anchor.label)

    # Go to following following
    driver.get(url+"/following")
    wait = ui.WebDriverWait(driver, 10)
    wait.until(page_loaded)

    try:
        lnks_cnt = int(soup.findAll("span", {"class":"ProfileNav-value"})[1].get_text().replace(".", ""))
    except:
        lnks_cnt = 1500
    print(lnks_cnt)
    links = driver.find_elements_by_xpath("//a[@class='ProfileCard-bg js-nav']")
    print(len(links))

    test = 1
    while len(links) < lnks_cnt - 2 and test < 1500:
        utils.scroll(driver)
        links = driver.find_elements_by_xpath("//a[@class='ProfileCard-bg js-nav']")
        print("following: ", lnks_cnt)
        print("links: ", len(links))
        test += 1
    utils.scroll(driver)
    links = driver.find_elements_by_xpath("//a[@class='ProfileCard-bg js-nav']")

    newUrlList = list()
    for lnk in links:
        newUrlList.append(lnk.get_attribute("href"))

    print("links unshuffeld: ", newUrlList)
    shuffle(newUrlList)
    print("links shuffeld: ", newUrlList)

    # Check everyone the Anchor follows
    print("link count: ", len(links))
    print("edge count: ", len(models.GephiEdge.objects.filter(source=Anchor.id)))
    if len(newUrlList) > len(models.GephiEdge.objects.filter(source=Anchor.id)):

        #First Followed
        for link in newUrlList:
            if link == "https://twitter.com/account/suspended":
                newUrlList = [x for x in newUrlList if x != "https://twitter.com/account/suspended"]
            else:
                try:
                    driver.get(link)
                except:
                    driver = log_in()
                    driver.get(link)

                # Get HTML
                wait = ui.WebDriverWait(driver, 10)
                wait.until(page_loaded)
                html_doc = driver.page_source
                soup = BeautifulSoup(html_doc, 'html.parser')

                #Create Node
                id = len(models.GephiNode.objects.all()) + 1
                print("id: ", id)
                label = soup.find("a", {"class":"ProfileHeaderCard-nameLink u-textInheritColor js-nav"}).get_text()
                print("label: ", label)
                try:
                    fan_count = soup.findAll("span", {"class":"ProfileNav-value"})[2].get_text()
                except:
                    fan_count = 0
                print("fan_count: ", fan_count)
                handle = soup.find("b", {"class":"u-linkComplex-target"}).get_text()
                print("handle: ", handle)
                tempNode = models.GephiNode(id=id, label=label, fan_count=fan_count, handle=handle)
                tempNode.create()

                #Create Edge
                print("source: ", Anchor.id)
                print("target: ", tempNode.id)
                print("type: ", "Directed")
                edge_id = len(models.GephiEdge.objects.all())
                print("id: ", edge_id)

                firstEdge = models.GephiEdge(source=Anchor.id, target=tempNode.id, type="Directed", id=edge_id, weight=1)
                firstEdge.create()

                # Break if list is complete in DB
                print("link count: ", len(links))
                print("edge count: ", len(models.GephiEdge.objects.filter(source=Anchor.id)))
                if len(newUrlList) == len(models.GephiEdge.objects.filter(source=Anchor.id)):
                    break

            print("Nodes: ", len(models.GephiNode.objects.all()))
            print("Edges: ", len(models.GephiEdge.objects.all()))
            print("Difference: ", len(models.GephiEdge.objects.all()) - len(models.GephiNode.objects.all()))

    driver.close()

    # Rekcursion

    print("depth: ", depth)
    if depth > 0:
        for uri in newUrlList:
            try:
                start_crawler(uri, email, password, depth-1)
            except:
                try:
                    start_crawler(uri, email, password, depth-1)
                except:
                    pass
