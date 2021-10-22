import argparse
import logging
from configparser import ConfigParser
from threading import Thread

import Automation
import IOConsole
import Login
import Worker


def main():

    # this allows to insert the course full name (even with whitespaces) without need to add ""
    # the course name is inferred from the argument between two options (e.g. -c)
    class MyAction(argparse.Action):
        def __call__(self, parser, namespace, values, option_string=None):
            setattr(namespace, self.dest, ' '.join(values))

    # COMMAND LINE ARGUMENTS
    parser = argparse.ArgumentParser(description='Your username and passworda are needed to perform log-in')
    parser.add_argument("-U", "-u", "-username", "--username", default=None, type=str, help="The GOMP username")
    parser.add_argument("-P", "-p", "-password", "--password", default=None, type=str, help="The GOMP password")
    parser.add_argument("-C", "-c", "-course", "--course", default=None, type=str,
                        help="The course you want to reserve",
                        nargs="+", action=MyAction)
    parser.add_argument("-A", "-a", "-auto", "-automatic", "--automatic", action="store_true",
                        help="Run the program only in Automatic Course Reserve mode")
    parser.add_argument("-hl", "-headless", "--headless", action="store_true",
                        help="Don't open the browser for the whole task "
                             "(Headless mode)")
    parser.add_argument("-L", "-l", "-logging", "--logging", action="store_true",
                        help="Enable logging")
    parser.add_argument("-heroku", "--heroku", action="store_true",
                        help="Run the program in Heroku mode (see for login credentials in the "
                             "environment variables")

    args = parser.parse_args()

    # If no args are provided (checking if all the arguments are in their default state), take parameters from config file
    if args.username is None and args.password is None and args.course is None and args.automatic is False \
            and args.headless is False and args.logging is False and args.heroku is False:

        # CONFIG FILE (config.ini)
        config = ConfigParser(allow_no_value=True)
        config.read('config.ini')

        usernameConfigFile = config.get('main', 'username')
        passwordConfigFile = config.get('main', 'password')
        courseConfigFile = config.get('main', 'course')
        autoModeConfigFile = config.getboolean('main', 'autoMode')
        headlessModeConfigFile = config.getboolean('main', 'headless')
        loggingModeConfigFile = config.getboolean('main', 'logging')
        herokuModeConfigFile = config.getboolean('main', 'heroku')

        if autoModeConfigFile is True:
            mainAutomatic(usernameConfigFile, passwordConfigFile, courseConfigFile, headlessModeConfigFile,
                          herokuModeConfigFile, loggingModeConfigFile)
        else:
            mainManual(usernameConfigFile, passwordConfigFile, courseConfigFile, headlessModeConfigFile,
                       loggingModeConfigFile, herokuModeConfigFile)
    else:
        if args.automatic is True:
            mainAutomatic(args.username, args.password, args.course, args.headless, args.heroku, args.logging)
        else:
            mainManual(args.username, args.password, args.course, args.headless, args.logging, args.heroku)


def mainManual(inputUsername, inputPassword, inputCourse, isHeadless, isLogging, isHeroku):
    """
    The main function of the Manual Mode. In this mode, the user can insert the course to reserve, or pass it as an
    argument, and the reservation is then made and program exited.
    :param inputUsername: the website username
    :param inputPassword: the website password
    :param inputCourse: the course to reserve
    :param isHeadless: headless mode boolean condition
    :param isLogging: logging mode boolean condition
    :param isHeroku: heroku mode boolean condition
    """
    # Initialize loggin format
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

    # Start the login thread
    results = [None] * 2
    login_thread = Thread(target=Login.login, args=(inputUsername, inputPassword, isHeadless,
                                                    isHeroku, isLogging, results))
    login_thread.start()

    # Insert the course
    while True:
        try:
            selected_course = IOConsole.insertCourse(inputCourse)
        except IOError:
            if inputCourse is not None:
                print("The course passed as argument does not exist")
                inputCourse = None
                continue
            else:
                print("No matching course for what you inserted.")
                continue
        break

    # retrieve result from the login thread
    login_thread.join()
    driver = results[0]

    # Reserve the lesson
    Worker.reserve(driver, selected_course)

    # Quit the program
    logging.info('Quitting the program...')
    driver.quit()
    logging.info("Driver thrown away, I'm gonna die")


def mainAutomatic(inputUsername, inputPassword, inputCourse, isHeadless, isHeroku, isLogging):
    """
    The main function of the Automatic Mode. In this mode, course reservations are performed automatically on a specific
    date and time (like Friday at 08:00). The course to reserve is already specified in the schedule() function
    :param inputUsername: the website username
    :param inputPassword: the website password
    :param inputCourse: the course to reserve
    :param isHeadless: headless mode boolean condition
    :param isHeroku: heroku mode boolean condition
    :param isLogging: logging mode boolean condition
    """
    # Initialize loggin format
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

    # Start the automatic reserve thread
    automatic_reservations = Thread(target=Automation.scheduler, args=(inputUsername, inputPassword,
                                                                       isHeadless, isHeroku, isLogging))
    automatic_reservations.start()


# Press the green button on the left side to run the script
if __name__ == '__main__':
    main()
