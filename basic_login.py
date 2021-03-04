import time
import re
import pprint


import requests
from lxml import html 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



def web_browsing(url):
    username = "qvvhozvcgpnsejwqks@wqcefp.com"
    password = "jbc0wgw9f1"
    driver = webdriver.Firefox(executable_path="./geckodriver")
    driver.get(url)

    ids = driver.find_elements_by_xpath(f'//*[@id]')
    id1 = ids[1].get_attribute('id')
    id2 = ids[2].get_attribute('id')


    driver.find_element_by_xpath(f'//*[@id="{id1}"]').click()
    input1=driver.find_element_by_id(id1)
    input1.send_keys(username)
    time.sleep(3)
    driver.find_element_by_xpath(f'//*[@id="{id2}"]').click()
    input2=driver.find_element_by_id(id2)
    input2.send_keys(password)
    time.sleep(3)
    driver.find_element_by_xpath("/html/body/div/div[2]/div/form/div[4]/button").click()

    time.sleep(3)

    driver.switch_to_window(driver.current_window_handle)
    page2 = driver.page_source

    tree = html.fromstring(page2)
    path_required = tree.xpath("/html/body/div/nav/div[1]/a[7]")[0]
    final_url = path_required.get("href")

    driver.close()

    return final_url


next_target = web_browsing("https://login.systemxlite.com/login/")
print(next_target)