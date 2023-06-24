import argparse
import logging
from configparser import ConfigParser
from threading import Thread

import r3serve.automation as automation
import r3serve.io_console as io_console
import login
import worker
import stats


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

        username_config_file = config.get('main', 'username')
        password_config_file = config.get('main', 'password')
        course_config_file = config.get('main', 'course')
        auto_mode_config_file = config.getboolean('main', 'autoMode')
        headless_mode_config_file = config.getboolean('main', 'headless')
        logging_mode_config_file = config.getboolean('main', 'logging')
        heroku_mode_config_file = config.getboolean('main', 'heroku')

        if auto_mode_config_file is True:
            main_automatic(username_config_file, password_config_file, course_config_file, headless_mode_config_file,
                          heroku_mode_config_file, logging_mode_config_file)
        else:
            main_manual(username_config_file, password_config_file, course_config_file, headless_mode_config_file,
                       logging_mode_config_file, heroku_mode_config_file)
    else:
        if args.automatic is True:
            main_automatic(args.username, args.password, args.course, args.headless, args.heroku, args.logging)
        else:
            main_manual(args.username, args.password, args.course, args.headless, args.logging, args.heroku)


def main_manual(input_username, input_password, input_course, is_headless, is_logging, is_heroku):
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
    # start the timer for the execution statistics 
    timer_start = stats.performance_counter()

    # Initialize loggin format
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

    # Start the login thread
    results = [None] * 2
    login_thread = Thread(target=login.login, args=(input_username, input_password, is_headless,
                                                    is_heroku, is_logging, results))
    login_thread.start()

    # Insert the course
    while True:
        try:
            selected_course = io_console.insert_course(input_course)
        except IOError:
            if input_course is not None:
                print("The course passed as argument does not exist")
                input_course = None
                continue
            else:
                print("No matching course for what you inserted.")
                continue
        break

    # retrieve result from the login thread
    login_thread.join()
    driver = results[0]

    # Reserve the lesson
    worker.reserve(driver, selected_course)

    # finish the timer for execution statistics and print result
    timer_finish = stats.performance_counter()
    stats.printPerformanceResult(stats.getResult(timer_start, timer_finish))

    # Quit the program
    logging.info('Quitting the program...')
    driver.quit()
    logging.info("Driver thrown away, I'm gonna die")


def main_automatic(input_username, input_password, input_course, is_headless, is_heroku, is_logging):
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
    automatic_reservations = Thread(target=automation.scheduler, args=(input_username, input_password,
                                                                       is_headless, is_heroku, is_logging))
    automatic_reservations.start()


if __name__ == '__main__':
    main()
