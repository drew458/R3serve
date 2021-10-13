import time

import selenium.common.exceptions
from selenium import webdriver
import pickle

import Cred


def login():
    try:
        # Login using the stored cookies for automatic authentication:

        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options)
        driver.get('https://gomp.uniroma3.it/Login?ReturnUrl=%2f')
        cookies = pickle.load(open("Resources/cookies.pkl", "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.get('https://gomp.uniroma3.it/Login?ReturnUrl=%2f')
    except Exception:
        # Login and store the cookies

        # options = webdriver.ChromeOptions()
        # driver = webdriver.Chrome(options=options)
        driver.get('https://gomp.uniroma3.it/Login?ReturnUrl=%2f')
        driver.find_element_by_xpath("//*[@id='userName']").send_keys(Cred.username)
        driver.find_element_by_xpath("//*[@id='password']").send_keys(Cred.password)
        driver.find_element_by_xpath("//*[@id='loginButton']").click()
        pickle.dump(driver.get_cookies(), open("Resources/cookies.pkl", "wb"))

    time.sleep(2)
    try:
        driver.find_element_by_xpath("//*[@id='userName']")
    except selenium.common.exceptions.NoSuchElementException:
        return driver

    # Login and store the cookies
    # options = webdriver.ChromeOptions()
    # driver = webdriver.Chrome(options=options)
    driver.get('https://gomp.uniroma3.it/Login?ReturnUrl=%2f')
    driver.find_element_by_xpath("//*[@id='userName']").send_keys("AND.MARINI4")
    driver.find_element_by_xpath("//*[@id='password']").send_keys("Canino?1963")
    driver.find_element_by_xpath("//*[@id='loginButton']").click()
    pickle.dump(driver.get_cookies(), open("Resources/cookies.pkl", "wb"))

    return driver
