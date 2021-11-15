import logging
import os
import sys
import time
import random
import getpass
from threading import Thread

from webdriver_manager.chrome import ChromeDriverManager

import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def initializeWebDriverThread(isHeadless, isHeroku, driverResult):
    """
    Initializes the WebDriver and navigates to the login page.
    :param isHeadless: headless mode boolean condition
    :param isHeroku: heroku mode boolean condition
    :param driverResult: the array containing the initialized driver in position [0]
    """
    # DEFINE WEB DRIVER
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--log-level=3')  # hide logs
    dir_path = os.getcwd()
    chrome_options.add_argument(f'user-data-dir={dir_path}/driver_user_data')   # to save the login session
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    if isHeadless is True:
        chrome_options.add_argument('--headless')

    if isHeroku is False:
        driver = webdriver.Chrome(ChromeDriverManager(log_level=0, print_first_line=False, cache_valid_range=10).install(),
                                  options=chrome_options)

    else:
        driver = webdriver.Chrome(chrome_options=chrome_options)

    logging.info("Browser initialized. Reaching the website...")

    # TARGET THE FIRST PAGE
    driver.get("https://gomp.uniroma3.it/Login?ReturnUrl=%2f")

    driverResult[0] = driver


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

    # Initialize the webdriver thread
    driverResult = [None] * 2
    webdriver_init_thread = Thread(target=initializeWebDriverThread, args=(isHeadless, isHeroku, driverResult))
    webdriver_init_thread.start()

    # Prioritize username and password passed as argument. If we are in heroku mode, then search them in environment
    # variables. If they aren't found in environment variables, then ask for it to the user
    if inputUsername is None or inputPassword is None:
        tempUsername = input("Insert your username...\n")
        promptedUsername = tempUsername.upper()

        try:
            promptedPassword = getpass.getpass(prompt="Insert your password... (Note: it will not be shown while "
                                                      "you're inserting it)\n")
        except getpass.GetPassWarning:
            pass

        webdriver_init_thread.join()
        driver = driverResult[0]

        # If we're already logged in via the previous session cookies, return the driver and exit the login process
        try:
            if driver.find_element_by_id("homeIconList").is_displayed():
                logging.info("Already logged in via the previous session cookies!")
                result[0] = driver
                return
        except selenium.common.exceptions.NoSuchElementException:
            logging.info("Proceding with normal login...")
            pass

        logging.info("Entering username and password...")
        username = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'userName')))
        username.clear()
        logging.info("Log in via user prompted username")
        username.send_keys(promptedUsername)

        password = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'password')))
        password.clear()
        logging.info("Log in via user prompted password")
        password.send_keys(promptedPassword)

    else:
        webdriver_init_thread.join()
        driver = driverResult[0]

        # If we're already logged in via the previous session cookies, return the driver and exit the login process
        try:
            if driver.find_element_by_id("homeIconList").is_displayed():
                logging.info("Already logged in via the previous session cookies!")
                result[0] = driver
                return
        except selenium.common.exceptions.NoSuchElementException:
            logging.info("Proceding with normal login...")
            pass

        logging.info("Entering username and password...")
        username = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'userName')))
        username.clear()
        if inputUsername is not None:
            logging.info("Log in via input username...")
            username.send_keys(inputUsername)
        if isHeroku is True and inputUsername is None:
            try:
                pathUsername = os.environ["USERNAME"]
                pathUsernameString = str(pathUsername)
                username.send_keys(pathUsernameString)
            except KeyError or pathUsernameString is None:
                logging.info("Username environment variable not found!")

        password = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'password')))
        password.clear()
        if inputPassword is not None:
            logging.info("Log in via input password...")
            password.send_keys(inputPassword)
        if isHeroku is True and inputPassword is None:
            try:
                pathPassword = os.environ["PASSWORD"]
                pathPasswordString = str(pathPassword)
                password.send_keys(pathPasswordString)
            except KeyError or pathPasswordString is None:
                logging.info("Password environment variable not found!")

    # CLICK THE LOGIN BUTTON
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'loginButton'))).click()
    time.sleep(random.uniform(0.6, 1.2))

    try:
        if driver.find_element_by_id("errorAlert").is_displayed():
            logging.info("Wrong username or password inserted")
            print("Wrong username or password inserted! Now I'm gonna die...")
            driver.quit()
            logging.info("Driver thrown away, I'm gonna die")
            sys.exit()
    except selenium.common.exceptions.NoSuchElementException:
        pass

    result[0] = driver
