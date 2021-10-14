import logging
import sys
import time

import selenium

import CourseNames


def goToCourseReservationList(driver):
    logging.info('Going to the course reservation list...')

    try:
        # Click on prenotazione posto in aula, biblioteca, sala studio
        # listPrenotazione = driver.find_element_by_xpath("//*[@id='homeIconList']")
        driver.find_element_by_xpath(
            "//*[contains(text(), 'Prenota il posto in aula, biblioteca, sala studio')]").click()
    except selenium.common.exceptions.NoSuchElementException:
        # Click on carriera
        # listCarriera = driver.find_element_by_xpath("//*[@id='homeIconList']")
        driver.find_element_by_xpath("//*[contains(text(), 'Carriera, Piano di Studi, Esami')]").click()
        time.sleep(5)
        # Click on prenotazione posto in aula, biblioteca, sala studio
        # listPrenotazione = driver.find_element_by_xpath("//*[@id='homeIconList']")
        driver.find_element_by_xpath(
            "//*[contains(text(), 'Prenota il posto in aula, biblioteca, sala studio')]").click()
        time.sleep(5)
        logging.info('Landend on the course reservation list!')
    else:
        time.sleep(5)
        logging.info('Landend on the course reservation list!')

    return driver


def clickOnCourse(driver, selected_course):
    logging.info('Reaching the inserted course reservation to click on...')

    # get the table
    table = driver.find_element_by_xpath("//*[@id='studyPlanBody']")

    # find the row
    try:
        course_xpath = CourseNames.composeCourseXPath(selected_course)
        table.find_element_by_xpath(course_xpath).click()
    except IOError:
        print("No such course found!")
        reserve_another = input("Do you want to insert another course? [Y/n]...\n")
        if reserve_another in ("y", "Y", "yes", "Yes", "si", "Si"):
            another_course_name = CourseNames.insertNewCourse()
            reserve(driver, another_course_name)
        else:
            logging.info('Quitting the program...')
            driver.quit()
            logging.info('Driver thrown away, addios!')
            sys.exit()
    else:
        time.sleep(3)
        logging.info('Here it is!')

    return driver


def reserve(driver, selected_course):
    driver.refresh()
    time.sleep(3)

    # GO TO course RESERVATION LIST
    driver2 = goToCourseReservationList(driver)

    # CLICK ON THE course
    driver3 = clickOnCourse(driver2, selected_course)

    # CHECK IF SEATS ARE STILL AVAILABLE
    table2 = driver3.find_element_by_xpath("//*[@id='slotListBody']")

    # tr[n]/td[m] are row and column of the element in the matrix
    # n parameter in tr[n] depends on the specific lesson, m parameter in td[m] is fixed at 7
    for i in range(1, 10):
        iString = str(i)

        try:
            remainingSeatsString = table2.find_element_by_xpath(
                "//*[@id='slotListBody']/tr[" + iString + "]/td[7]").text
        except selenium.common.exceptions.NoSuchElementException:
            print("No more lessons available for this course!")
            reserve_another = input("Do you want to reserve another course? [Y/n]...\n")
            if reserve_another in ("y", "Y", "yes", "Yes", "si", "Si"):
                another_course_name = CourseNames.insertNewCourse()
                reserve(driver, another_course_name)
            else:
                logging.info('Quitting the program...')
                driver.quit()
                logging.info('Driver thrown away, addios!')
                sys.exit()
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
                    modal = driver3.find_element_by_xpath("//*[@id='partialQuestionYesNo']")
                    modal.find_element_by_xpath("//*[@id='partialQuestionYesNoConfirmButton']").click()
                    time.sleep(10)

                if driver3.find_element_by_xpath("//h1[contains(text(), 'Dettagli prenotazione')]").is_displayed():
                    reserve_another = input("Done!\n"
                                            "Do you want to reserve another lesson for this course? [Y/n]...\n")
                    if reserve_another in ("y", "Y", "yes", "Yes", "si", "Si"):
                        driver3.find_element_by_xpath("//*[@id='backArrowReservs']").click()
                        continue
                    else:
                        logging.info('Quitting the program...')
                        driver.quit()
                        logging.info('Driver thrown away, addios!')
                        sys.exit()
                else:
                    print("This reservation overlaps with another one in the same time slot, "
                          "hence it cannot be completed.\n"
                          "It's devstating, I know.")
