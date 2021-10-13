import logging
from threading import Thread

import Automation
import ClassNames
import Login
import Worker


def main():
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
