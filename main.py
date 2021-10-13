import argparse
import logging
from threading import Thread

import Automation
import ClassNames
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

    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

    # Perform the log in
    driver = Login.login()

    # Insert the class
    selected_class = ClassNames.insertClass()

    automatic_reservations = Thread(target=Automation.scheduler)
    automatic_reservations.start()

    # Reserve the lesson
    Worker.reserve(driver, selected_class)


# Press the green button on the left side to run the script
if __name__ == '__main__':
    main()
