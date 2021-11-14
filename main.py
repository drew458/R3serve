import logging
from threading import Thread

import ArgumentParser
import Automation
import IOConsole
import Login
import Worker
import Stats


def mainManual(inputUsername, inputPassword, inputCourse, biblioHour, isHeadless, isLogging, isHeroku):
    """
    The main function of the Manual Mode. In this mode, the user can insert the course to reserve, or pass it as an
    argument, and the reservation is then made and program exited.
    :param inputUsername: the website username
    :param inputPassword: the website password
    :param inputCourse: the course to reserve
    :param biblioHour: the library hour to reserve
    :param isHeadless: headless mode boolean condition
    :param isLogging: logging mode boolean condition
    :param isHeroku: heroku mode boolean condition
    """

    # start the timer for the execution statistics 
    timer_start = Stats.performanceCounter()

    # Define logging format
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

    # Initialize the login thread
    results = [None] * 2
    login_thread = Thread(target=Login.login, args=(inputUsername, inputPassword, isHeadless,
                                                    isHeroku, isLogging, results))

    # If the user wants to reserve only the library
    if biblioHour is not None:
        login_thread.start()
        login_thread.join()
        driver = results[0]

        # Reserve the library time slot
        Worker.reserveBiblio(driver, biblioHour)

        # finish the timer for execution statistics and print result
        timer_finish = Stats.performanceCounter()
        Stats.printPerformanceResult(Stats.getResult(timer_start, timer_finish))

        # Quit the program
        logging.info('Quitting the program...')
        driver.quit()
        logging.info("Driver thrown away, I'm gonna die")
        return

    # If the user doesn't provide username or password, the course input needs to be done AFTER the input for username
    # and password, otherwise they'll overlap
    if (inputUsername is None or inputPassword is None) and inputCourse is None:
        login_thread.start()
        login_thread.join()

        # retrieve result from the login thread
        driver = results[0]

        # Ask the user to insert the course
        while True:
            try:
                selected_course = IOConsole.insertCourse(inputCourse)
            except IOError:
                if inputCourse is not None:
                    print("The course passed as argument does not exist")
                    inputCourse = None
                    continue
                else:
                    print("No matching course for what you inserted")
                    continue
            break
    else:
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
                    print("No matching course for what you inserted")
                    continue
            break

        # retrieve result from the login thread
        login_thread.join()
        driver = results[0]

    # Reserve the lesson
    Worker.reserve(driver, selected_course)

    # Stop the timer for execution statistics and print result
    timer_finish = Stats.performanceCounter()
    Stats.printPerformanceResult(Stats.getResult(timer_start, timer_finish))

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

    # Start the automatic reserve thread
    automatic_reservations = Thread(target=Automation.scheduler, args=(inputUsername, inputPassword,
                                                                       isHeadless, isHeroku, isLogging))
    automatic_reservations.start()


def main():
    ArgumentParser.parse()


# Press the green button on the left side to run the script
if __name__ == '__main__':
    main()
