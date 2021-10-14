import logging
import os
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

try:
    import static.Cred as Cred
except ModuleNotFoundError:
    pass


def login(inputUsername, inputPassword, isHeadless, isHeroku, result):
    # browser = webdriver.Firefox()
    # browser.get('https://website.com/Home')
    # emailElem = browser.find_element_by_id('UserName') #finds login username field
    # emailElem.send_keys('username') #enter the username
    # passwordElem = browser.find_element_by_id('UserPassword') #finds pw field
    # passwordElem.send_keys('password') #enters pw
    # passwordElem.submit() #presses submit button

    logging.info('Opening the login page...')

    # DEFINE WEB DRIVER
    options = webdriver.ChromeOptions()
    options.add_argument('--log-level=3')
    if isHeadless is True:
        options.add_argument('--headless')

    # TODO: remove all kind of logging from Webdriver Manager
    driver = webdriver.Chrome(chrome_options=options, executable_path=ChromeDriverManager(log_level=0,
                                                                                          print_first_line=False).install())

    logging.info("Browser initialized. Reaching the website...")

    # TARGET THE FIRST PAGE
    # Give the driver the starting URL and check you've landed where you should
    # by running an assertion on the text in the title of the page:
    driver.get("https://gomp.uniroma3.it/Login?ReturnUrl=%2f")
    time.sleep(3)

    logging.info("Entering username and password...")

    # Prioritize input username and password. If we are in heroku mode, then search them in environment
    # variables. If they aren't found in environment variables, then look for them in the Cred.py file
    username = driver.find_element_by_xpath("//*[@id='userName']")
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
        logging.info("Log in via default username")
        username.send_keys(Cred.username)

    password = driver.find_element_by_xpath("//*[@id='password']")
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
        logging.info("Log in via default password...")
        password.send_keys(Cred.password)

    # CLICK THE LOGIN BUTTON
    driver.find_element_by_xpath("//*[@id='loginButton']").click()

    logging.info("Login done!")
    time.sleep(0.5)

    result[0] = driver
