
import re
import time


from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from RandomWordGenerator import RandomWord
import random


def account_details():

    username_and_password = {}
    #url for the first site 
    url1 = "https://login.systemxlite.com/register/"


    #url for temporary email
    url2 = "https://10minutemail.com/"

    driver = webdriver.Firefox(executable_path="./geckodriver")
    driver.get(url1)

    #tab switching
    driver.execute_script("window.open('about:blank','secondtab');") 
    driver.switch_to.window("secondtab") 
    driver.get(url2)

    #hold to let email to generate
    time.sleep(6)
    a = ActionChains(driver)

    #ctrl+c to copy email which is already highlited
    a.key_down(Keys.CONTROL).send_keys('C').key_up(Keys.CONTROL).perform()

    


    driver.switch_to.window(driver.window_handles[0])
    time.sleep(2)

    # initial_signup_page input locations
    ids = driver.find_elements_by_xpath(f'//*[@id]')
    id1 = ids[1].get_attribute('id')
    id2 = ids[2].get_attribute('id')
    id3 = ids[3].get_attribute('id')
    id4 = ids[4].get_attribute('id')

    #inputing the valuers in the field
    driver.find_element_by_xpath(f'//*[@id="{id1}"]').click()
    a.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
    time.sleep(3)

    driver.find_element_by_xpath(f'//*[@id="{id2}"]').click()
    rw = RandomWord(max_word_size=5)
    first_name = rw.generate()
    last_name = rw.generate()

    input2=driver.find_element_by_id(id2)
    input2.send_keys(first_name)
    time.sleep(2)
    driver.find_element_by_xpath(f'//*[@id="{id3}"]').click()
    input3=driver.find_element_by_id(id3)
    input3.send_keys(last_name)
    phone_number = int(str(98)+ str(random.randint(10000000,99999999)))

    driver.find_element_by_xpath(f'//*[@id="{id4}"]').click()
    input4=driver.find_element_by_id(id4)
    input4.send_keys(phone_number)

    driver.find_element_by_xpath("/html/body/div/div[2]/div/form/div[6]/button").click()


   
    #back to the temp email tab
    driver.switch_to.window(driver.window_handles[1])

    #
    time.sleep(20)

    driver.find_element_by_xpath("//*[@class='small_message_icon']").click()
    time.sleep(10)
    message = driver.find_element_by_xpath("//*[@class='message_bottom']")

    text_ele = message.text

    email = re.search("Username : .*com",text_ele)[0].split(" : ")[1]
    if not email:
        email = re.search("Username : .*online",text_ele)[0].split(" : ")[1]
    password = re.search("Password : ..........",text_ele)[0].split(" : ")[1]
    username_and_password["email"] = email
    username_and_password["password"] = password



    return username_and_password

    
