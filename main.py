import argparse
import logging
from threading import Thread

import Automation
import CourseNames
import Login
import Worker


def main():
    # argumentEvaluation()

    # this allows to insert the course full name (even with whitespaces) without need to add ""
    # the course name is inferred from the argument between two options (e.g. -c)
    class MyAction(argparse.Action):
        def __call__(self, parser, namespace, values, option_string=None):
            setattr(namespace, self.dest, ' '.join(values))

    # COMMAND LINE ARGUMENTS
    parser = argparse.ArgumentParser(description='Your username and passworda are needed to perform log-in')
    parser.add_argument("-U", "-u", "-username", "--username", default=None, type=str, help="The username")
    parser.add_argument("-P", "-p", "-password", "--password", default=None, type=str, help="The password")
    parser.add_argument("-C", "-c", "-course", "--course", default=None, type=str,
                        help="The course you want to reserve",
                        nargs="+", action=MyAction)
    parser.add_argument("-A", "-a", "-auto", "-automatic", "--automatic", action="store_true",
                        help="Run the program only in Automatic Course Reserve mode")
    parser.add_argument("-H", "-hl", "-headless", "--headless", action="store_true",
                        help="Don't open the browser for the whole task"
                             "(Headless mode)")

    args = parser.parse_args()

    if args.automatic is True:
        mainAutomatic(args.username, args.password, args.course, args.headless)
    else:
        mainManual(args.username, args.password, args.course, args.headless)


def mainManual(inputUsername, inputPassword, inputCourse, isHeadless):
    # Initialize loggin format
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

    # Perform the log in
    driver = Login.login(inputUsername, inputPassword, isHeadless)

    # Insert the course
    selected_course = CourseNames.insertCourse(inputCourse)

    # Reserve the lesson
    Worker.reserve(driver, selected_course)


def mainAutomatic(inputUsername, inputPassword, inputCourse, isHeadless):
    # Initialize loggin format
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

    # Start the automatic reserve thread
    automatic_reservations = Thread(target=Automation.scheduler, args=(inputUsername, inputPassword,
                                                                       isHeadless))
    automatic_reservations.start()


# Press the green button on the left side to run the script
if __name__ == '__main__':
    main()
