import logging
import time

import schedule
import selenium

import CourseNames
import Login
import Worker


def reserveCourse(driver, course_to_reserve):
    driver.refresh()
    time.sleep(3)

    # GO TO COURSE RESERVATION LIST
    driver2 = Worker.goToCourseReservationList(driver)

    # CLICK ON THE COURSE
    driver3 = Worker.clickOnCourse(driver2, course_to_reserve)

    # CHECK IF SEATS ARE STILL AVAILABLE
    table2 = driver3.find_element_by_id("slotListBody")

    # tr[n]/td[m] are row and column of the element in the matrix
    # n parameter in tr[n] depends on the specific lesson, m parameter in td[m] is fixed at 7
    for i in range(1, 10):
        iString = str(i)

        try:
            remainingSeatsString = table2.find_element_by_xpath(
                "//*[@id='slotListBody']/tr[" + iString + "]/td[7]").text
        except selenium.common.exceptions.NoSuchElementException:
            print("No more lessons available for this course! I'll continue my mission...")
            driver3.quit()
            break
        else:
            remainingSeatsInt = int(remainingSeatsString)
            if remainingSeatsInt == 0:
                print("No more seats available, I'm sorry bro")
                continue
            else:
                # tr[n]/td[m] are row and column of the element in the matrix
                # n parameter in tr[n] depends on the specific lesson, m parameter in td[m] is fixed at 8, that is
                # the location of calendar icon
                calendar = driver3.find_element_by_xpath("//*[@id='slotListBody']/tr[" + iString + "]/td[8]")
                calendarAttribute = calendar.get_attribute("title")
                if calendarAttribute == "Annulla la prenotazione per questa erogazione ":
                    print("Course at line " + iString + " already reserved")
                    continue
                else:
                    calendar.click()
                    time.sleep(3)
                    modal = driver3.find_element_by_id("partialQuestionYesNo")
                    modal.find_element_by_id("partialQuestionYesNoConfirmButton").click()
                    time.sleep(10)

                if driver3.find_element_by_xpath("//h1[contains(text(), 'Dettagli prenotazione')]").is_displayed():
                    print("Done!\n")
                    driver3.find_element_by_id("backArrowReservs").click()
                    continue
                else:
                    print("This reservation overlaps with another one in the same time slot, "
                          "hence it cannot be completed.\n"
                          "It's devstating, I know.")


def launcher(course_to_reserve, inputUsername, inputPassword, isHeadless, isHeroku):
    results = [None] * 2
    Login.login(inputUsername, inputPassword, isHeadless, isHeroku, results)
    driver = results[0]
    parsed_course_to_reserve = CourseNames.courseParsing(course_to_reserve)
    reserveCourse(driver, parsed_course_to_reserve)


def scheduler(inputUsername, inputPassword, isHeadless, isHeroku):

    logging.info('Starting automatic reserve threads...')

    schedule.every().monday.at("00:07").do(launcher, course_to_reserve="basi di dati",
                                           inputUsername=inputUsername, inputPassword=inputPassword,
                                           isHeadless=isHeadless, isHeroku=isHeroku)
    schedule.every().monday.at("00:08").do(launcher, course_to_reserve="reti di calcolatori",
                                           inputUsername=inputUsername, inputPassword=inputPassword,
                                           isHeadless=isHeadless, isHeroku=isHeroku)
    schedule.every().monday.at("00:06").do(launcher, course_to_reserve="mobile computing",
                                           inputUsername=inputUsername, inputPassword=inputPassword,
                                           isHeadless=isHeadless, isHeroku=isHeroku)
    schedule.every().monday.at("00:09").do(launcher, course_to_reserve="programmazione funzionale",
                                           inputUsername=inputUsername, inputPassword=inputPassword,
                                           isHeadless=isHeadless, isHeroku=isHeroku)

    schedule.every().tuesday.at("00:07").do(launcher, course_to_reserve="mobile computing",
                                            inputUsername=inputUsername, inputPassword=inputPassword,
                                            isHeadless=isHeadless, isHeroku=isHeroku)
    schedule.every().tuesday.at("00:08").do(launcher, course_to_reserve="programmazione funzionale",
                                            inputUsername=inputUsername, inputPassword=inputPassword,
                                            isHeadless=isHeadless, isHeroku=isHeroku)
    schedule.every().tuesday.at("00:06").do(launcher, course_to_reserve="sistemi operativi",
                                            inputUsername=inputUsername, inputPassword=inputPassword,
                                            isHeadless=isHeadless, isHeroku=isHeroku)

    schedule.every().wednesday.at("00:07").do(launcher, course_to_reserve="sistemi operativi",
                                              inputUsername=inputUsername, inputPassword=inputPassword,
                                              isHeadless=isHeadless, isHeroku=isHeroku)

    schedule.every().thursday.at("00:07").do(launcher, course_to_reserve="basi di dati",
                                             inputUsername=inputUsername, inputPassword=inputPassword,
                                             isHeadless=isHeadless, isHeroku=isHeroku)
    schedule.every().thursday.at("00:08").do(launcher, course_to_reserve="reti di calcolatori",
                                             inputUsername=inputUsername, inputPassword=inputPassword,
                                             isHeadless=isHeadless, isHeroku=isHeroku)

    logging.info('Automatic reserve threads started!')

    while True:
        schedule.run_pending()
        time.sleep(1)
        # logging.info("AUTOMATIC reserve thread running...")
