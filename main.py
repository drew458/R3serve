import argparse
import logging
from threading import Thread

import Automation
import CourseNames
import Login
import Worker

"""def argumentEvaluation():
    # create the top-level parser
    parser = argparse.ArgumentParser(description='Enter the working mode of the script')
    parser.add_argument("-M", "--manual", help="Manual mode", action="store_true")
    subparsers = parser.add_subparsers(help='sub-command help')

    # create the parser for the "a" command
    parser_a = subparsers.add_parser('a', help='Automatic mode')
    parser_a.add_argument('bar', type=int, help='bar help')

    # Read arguments from the command line
    args = parser.parse_args()

    # Check for --automatic or -A
    if args.automatic:
        logging.info("Automatic mode selected...")

    # Check for --manual or -M
    if args.manual:
        logging.info("Manual mode selected...") """


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
    parser.add_argument("-H", "-hl", "-headless", "--headless", action="store_true",
                        help="Don't open the browser for the whole task"
                             "(Headless mode)")

    args = parser.parse_args()

    # Initialize loggin format
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

    # Perform the log in
    driver = Login.login(args.username, args.password, args.headless)

    # Insert the course
    selected_course = CourseNames.insertCourse(args.course)

    # Start the automatic reserve thread
    automatic_reservations = Thread(target=Automation.scheduler, args=(args.username, args.password,
                                                                       args.headless))
    automatic_reservations.start()

    # Reserve the lesson
    Worker.reserve(driver, selected_course)


# Press the green button on the left side to run the script
if __name__ == '__main__':
    main()
