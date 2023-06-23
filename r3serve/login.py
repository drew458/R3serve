import logging
import os
import sys
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def login(inputUsername, inputPassword, isHeadless, isHeroku, isLogging, result):
    """
    Performs the login into the website
    :param inputUsername: the website username
    :param inputPassword: the website password
    :param isHeadless: headless mode boolean condition
    :param isHeroku: heroku mode boolean condition
    :param isLogging: logging mode boolean condition
    :param result: the array containing the logged-in driver in position [0]
    """
    if isLogging is False:
        logger = logging.getLogger()
        logger.disabled = True

    logging.info('Opening the login page...')

    # DEFINE WEB DRIVER
    options = webdriver.ChromeOptions()
    options.add_argument('--log-level=3')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    if isHeadless is True:
        options.add_argument('--headless')

    if sys.platform.startswith('linux'):
        driver = webdriver.Chrome(chrome_options=options, executable_path='/usr/lib/chromium-browser/chromedriver')
    else:
        driver = webdriver.Chrome(chrome_options=options)

    logging.info("Browser initialized. Reaching the website...")

    # TARGET THE FIRST PAGE
    driver.get("https://gomp.uniroma3.it/Login?ReturnUrl=%2f")

    logging.info("Entering username and password...")

    # Prioritize username and password passed as argument. If we are in heroku mode, then search them in environment
    # variables. If they aren't found in environment variables, then ask for it to the user
    username = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'userName')))
    username.clear()
    if inputUsername is not None:
        logging.info("Log in via input username...")
        username.send_keys(inputUsername)
    elif isHeroku is True:
        try:
            pathUsername = os.environ["USERNAME"]
            pathUsernameString = str(pathUsername)
            username.send_keys(pathUsernameString)
        except KeyError or pathUsernameString is None:
            logging.info("Username environment variable not found!")
    else:
        logging.info("Log in via user prompted username")
        promptedUsername = input("Insert you username...\n")
        username.send_keys(promptedUsername)

    password = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'password')))
    password.clear()
    if inputPassword is not None:
        logging.info("Log in via input password...")
        password.send_keys(inputPassword)
    elif isHeroku is True:
        try:
            pathPassword = os.environ["PASSWORD"]
            pathPasswordString = str(pathPassword)
            password.send_keys(pathPasswordString)
        except KeyError or pathPasswordString is None:
            logging.info("Password environment variable not found!")
    else:
        logging.info("Log in via user prompted password")
        promptedPassword = input("Insert you password...\n")
        password.send_keys(promptedPassword)

    # CLICK THE LOGIN BUTTON
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'loginButton'))).click()

    logging.info("Login done!")
    time.sleep(0.5)

    result[0] = driver
