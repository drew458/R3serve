import logging
import time

import schedule
import selenium

import r3serve.io_console as io_console
import login
import worker


def reserveCourse(driver, course_to_reserve):
    """
    Performs the whole course reservation process
    :param driver: the already logged-in driver
    :param course_to_reserve: the already parsed course name
    """
    driver.refresh()
    time.sleep(3)

    # GO TO COURSE RESERVATION LIST
    driver = worker.goToCourseReservationList(driver)

    # CLICK ON THE COURSE
    driver = worker.clickOnCourse(driver, course_to_reserve)

    # CHECK IF SEATS ARE STILL AVAILABLE
    table = driver.find_element_by_id("slotListBody")

    # tr[n]/td[m] are row and column of the element in the matrix
    # n parameter in tr[n] depends on the specific lesson, m parameter in td[m] is fixed at 7
    # TODO: implement WebDriverWait just like in worker.py
    for i in range(1, 10):
        iString = str(i)

        try:
            # TODO: find a way to remove time.sleep(3)
            time.sleep(1.5)
            remainingSeatsString = table.find_element_by_xpath(
                "//*[@id='slotListBody']/tr[" + iString + "]/td[7]").text
        except selenium.common.exceptions.NoSuchElementException:
            print("No more lessons available for this course! I'll continue my mission...")
            driver.quit()
            break
        else:
            remainingSeatsInt = int(remainingSeatsString)
            if remainingSeatsInt == 0:
                print("No more seats available")
                continue
            else:
                # tr[n]/td[m] are row and column of the element in the matrix
                # n parameter in tr[n] depends on the specific lesson, m parameter in td[m] is fixed at 8, that is
                # the location of calendar icon
                calendar = driver.find_element_by_xpath("//*[@id='slotListBody']/tr[" + iString + "]/td[8]")
                calendarAttribute = calendar.get_attribute("title")
                if calendarAttribute == "Annulla la prenotazione per questa erogazione ":
                    print("Course at line " + iString + " already reserved")
                    continue
                else:
                    calendar.click()
                    time.sleep(3)
                    modal = driver.find_element_by_id("partialQuestionYesNo")
                    modal.find_element_by_id("partialQuestionYesNoConfirmButton").click()
                    time.sleep(3)

                if driver.find_element_by_xpath("//h1[contains(text(), 'Dettagli prenotazione')]").is_displayed():
                    print("Done!\n")
                    driver.find_element_by_id("backArrowReservs").click()
                    continue
                else:
                    print("This reservation overlaps with another one in the same time slot, "
                          "hence it cannot be completed")


def launcher(course_to_reserve, inputUsername, inputPassword, isHeadless, isHeroku, isLogging):
    """
    Launches the login, course name parsing and reservation functions
    :param course_to_reserve:
    :param inputUsername: the website username
    :param inputPassword: the website password
    :param isHeadless: headless mode boolean condition
    :param isHeroku: heroku mode boolean condition
    :param isLogging: logging mode boolean condition
    """
    results = [None] * 2
    login.login(inputUsername, inputPassword, isHeadless, isHeroku, isLogging, results)
    driver = results[0]
    parsed_course_to_reserve = io_console.courseParsing(course_to_reserve)
    reserveCourse(driver, parsed_course_to_reserve)


def scheduler(inputUsername, inputPassword, isHeadless, isHeroku, isLogging):
    """
    Schedules all the courses reservations
    :param inputUsername: the website username
    :param inputPassword: the website password
    :param isHeadless: headless mode boolean condition
    :param isHeroku: heroku mode boolean condition
    :param isLogging: logging mode boolean condition
    """
    if isLogging is False:
        logger = logging.getLogger()
        logger.disabled = True

    logging.info('Starting automatic reserve threads...')

    schedule.every().monday.at("00:12").do(launcher, course_to_reserve="basi di dati",
                                           inputUsername=inputUsername, inputPassword=inputPassword,
                                           isHeadless=isHeadless, isHeroku=isHeroku, isLogging=isLogging)
    schedule.every().monday.at("00:07").do(launcher, course_to_reserve="reti di calcolatori",
                                           inputUsername=inputUsername, inputPassword=inputPassword,
                                           isHeadless=isHeadless, isHeroku=isHeroku, isLogging=isLogging)
    schedule.every().monday.at("00:05").do(launcher, course_to_reserve="mobile computing",
                                           inputUsername=inputUsername, inputPassword=inputPassword,
                                           isHeadless=isHeadless, isHeroku=isHeroku, isLogging=isLogging)
    schedule.every().monday.at("00:09").do(launcher, course_to_reserve="programmazione funzionale",
                                           inputUsername=inputUsername, inputPassword=inputPassword,
                                           isHeadless=isHeadless, isHeroku=isHeroku, isLogging=isLogging)

    schedule.every().tuesday.at("00:10").do(launcher, course_to_reserve="mobile computing",
                                            inputUsername=inputUsername, inputPassword=inputPassword,
                                            isHeadless=isHeadless, isHeroku=isHeroku, isLogging=isLogging)
    schedule.every().tuesday.at("00:07").do(launcher, course_to_reserve="programmazione funzionale",
                                            inputUsername=inputUsername, inputPassword=inputPassword,
                                            isHeadless=isHeadless, isHeroku=isHeroku, isLogging=isLogging)
    schedule.every().tuesday.at("00:05").do(launcher, course_to_reserve="sistemi operativi",
                                            inputUsername=inputUsername, inputPassword=inputPassword,
                                            isHeadless=isHeadless, isHeroku=isHeroku, isLogging=isLogging)

    schedule.every().wednesday.at("00:07").do(launcher, course_to_reserve="sistemi operativi",
                                              inputUsername=inputUsername, inputPassword=inputPassword,
                                              isHeadless=isHeadless, isHeroku=isHeroku, isLogging=isLogging)

    schedule.every().thursday.at("00:05").do(launcher, course_to_reserve="basi di dati",
                                             inputUsername=inputUsername, inputPassword=inputPassword,
                                             isHeadless=isHeadless, isHeroku=isHeroku, isLogging=isLogging)
    schedule.every().thursday.at("00:08").do(launcher, course_to_reserve="reti di calcolatori",
                                             inputUsername=inputUsername, inputPassword=inputPassword,
                                             isHeadless=isHeadless, isHeroku=isHeroku, isLogging=isLogging)

    logging.info('Automatic reserve threads started!')

    while True:
        schedule.run_pending()
        time.sleep(1)
        # logging.info("AUTOMATIC reserve thread running...")
