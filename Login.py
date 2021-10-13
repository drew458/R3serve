import time

from selenium import webdriver

import Resources.Cred as Cred


def login():
    # browser = webdriver.Firefox()
    # browser.get('https://website.com/Home')
    # emailElem = browser.find_element_by_id('UserName') #finds login username field
    # emailElem.send_keys('username') #enter the username
    # passwordElem = browser.find_element_by_id('UserPassword') #finds pw field
    # passwordElem.send_keys('password') #enters pw
    # passwordElem.submit() #presses submit button

    # DEFINE WEB DRIVER
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options, executable_path="Resources/chromedriver.exe")

    # TARGET THE FIRST PAGE
    # Give the driver the starting URL and check you've landed where you should
    # by running an assertion on the text in the title of the page:
    driver.get("https://gomp.uniroma3.it/Login?ReturnUrl=%2f")
    time.sleep(3)
    assert "smart_edu" in driver.title

    # COMPLETE THE USERNAME AND PASSWORD FIELDS
    # Find the username field by its id in the HTML markup (e.g. id="uid) and the password
    # by the name attribute (e.g. name="pwd")
    username = driver.find_element_by_xpath("//*[@id='userName']")
    username.clear()
    username.send_keys(Cred.username)

    password = driver.find_element_by_xpath("//*[@id='password']")
    password.clear()
    password.send_keys(Cred.password)

    # CLICK THE LOGIN BUTTON
    # Now we need to submit the login credentials by clicking the submit button
    driver.find_element_by_xpath("//*[@id='loginButton']").click()

    return driver
