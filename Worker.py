import datetime
import logging
import random
import sys
import time

import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import IOConsole

from difflib import SequenceMatcher


# def similar(a, b):
#    return SequenceMatcher(None, a, b).ratio()


def goToCourseReservationList(driver):
    logging.info('Going to the course reservation list...')

    try:
        # Click on prenotazione posto in aula, biblioteca, sala studio
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((
                By.XPATH, "//*[contains(text(), 'Prenota il posto in aula, biblioteca, sala studio')]"))).click()
    except selenium.common.exceptions.NoSuchElementException:
        # Click on carriera
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((
                By.XPATH, "//*[contains(text(), 'Carriera, Piano di Studi, Esami')]"))).click()

        # Click on prenotazione posto in aula, biblioteca, sala studio
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((
                By.XPATH, "//*[contains(text(), 'Prenota il posto in aula, biblioteca, sala studio')]"))).click()
        logging.info('Landend on the course reservation list!')
    else:
        logging.info('Landend on the course reservation list!')

    return driver


def clickOnCourse(driver, selected_course):
    logging.info('Reaching the inserted course reservation to click on...')

    # get the table
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'studyPlanBody')))

    # find the row
    try:
        course_xpath = IOConsole.composeCourseXPath(selected_course)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, course_xpath))).click()
        # table.find_element_by_xpath(course_xpath).click()
    except IOError:
        print("No such course found!")
        another_course_name = IOConsole.insertNewCourse()
        reserve(driver, another_course_name)
    else:
        logging.info('Here it is!')

    return driver


def reserve(driver, selected_course):
    try:
        driver.refresh()

        # GO TO COURSE RESERVATION LIST
        # driver2 = goToCourseReservationList(driver)
        driver.get("https://gomp.uniroma3.it/StudentSpaceReserv")

        # CLICK ON THE COURSE
        driver3 = clickOnCourse(driver, selected_course)

        # CHECK IF SEATS ARE STILL AVAILABLE
        WebDriverWait(driver3, 20).until(EC.presence_of_element_located((By.ID, 'slotListBody')))

        # tr[n]/td[m] are row and column of the element in the matrix
        # n parameter in tr[n] depends on the specific lesson, m parameter in td[m] is fixed at 7
        for i in range(1, 10):
            iString = str(i)

            try:
                # TODO: find a way to remove time.sleep()
                time.sleep(random.uniform(0.7, 1.5))
                # remainingSeatsString = WebDriverWait(driver3, 20).until(EC.presence_of_element_located((
                #    By.XPATH, "//*[@id='slotListBody']/tr[" + iString + "]/td[7]"))).text
                remainingSeats = driver3.find_element_by_xpath(
                    "//*[@id='slotListBody']/tr[" + iString + "]/td[7]").text
            except selenium.common.exceptions.NoSuchElementException:
                print("No more lessons available for this course")
                reserve_another = input("Do you want to reserve another course? [Y/n]...\n")
                if reserve_another.casefold() in ("y", "yes", "si", "s"):
                    another_course_name = IOConsole.insertNewCourse()
                    reserve(driver, another_course_name)
                else:
                    logging.info('Quitting the program...')
                    driver.quit()
                    logging.info("Driver thrown away, I'm gonna die")
                    sys.exit()
            else:
                if remainingSeats in ("0"):
                    print("No more seats available")
                    continue
                else:
                    # tr[n]/td[m] are row and column of the element in the matrix
                    # n parameter in tr[n] depends on the specific lesson, m parameter in td[m] is fixed at 8, that is
                    # the location of calendar icon
                    WebDriverWait(driver3, 20).until(EC.visibility_of_element_located((
                        By.XPATH, "//*[@id='slotListBody']/tr[" + iString + "]/td[8]")))
                    calendar = driver3.find_element_by_xpath("//*[@id='slotListBody']/tr[" + iString + "]/td[8]")
                    calendarAttribute = calendar.get_attribute("title")
                    if calendarAttribute == "Annulla la prenotazione per questa erogazione ":
                        print("Course at line " + iString + " already reserved")
                        continue
                    else:
                        calendar.click()
                        # modal = driver3.find_element_by_id("partialQuestionYesNo")
                        WebDriverWait(driver3, 20).until(EC.element_to_be_clickable((
                            By.ID, "partialQuestionYesNoConfirmButton"))).click()
                        # modal.find_element_by_id("partialQuestionYesNoConfirmButton").click()

                    # TODO: find a way to incorporate is_displayed() function into WebDriverWait, so time.sleep()
                    #   can be removed
                    time.sleep(random.uniform(1, 1.5))
                    if driver3.find_element_by_xpath("//h1[contains(text(), 'Dettagli prenotazione')]").is_displayed():
                        reserve_another = input("Done!\n"
                                                "Do you want to reserve another lesson for this course? [Y/n]...\n")
                        if reserve_another.casefold() in ("y", "yes", "si", "s"):
                            WebDriverWait(driver3, 20).until(EC.element_to_be_clickable((
                                By.ID, "backArrowReservs"))).click()
                            continue
                        else:
                            break
                    else:
                        print("This reservation overlaps with another one in the same time slot, "
                              "hence it cannot be completed")
                        reserve_another2 = input("Do you want to reserve another lesson for this course? [Y/n]...\n")
                        if reserve_another2.casefold() in ("y", "yes", "si", "s"):
                            try:
                                WebDriverWait(driver3, 2).until(EC.element_to_be_clickable((
                                    By.ID, "backArrowReservs"))).click()
                            except Exception:
                                continue
                        else:
                            break
    except AttributeError:
        print("There was an error during the login process. Please start the script again and retry.")
        logging.info("Driver thrown away, I'm gonna die")
        sys.exit()


def reserveBiblio(driver, biblioDay, biblioHour):
    driver.refresh()
    time.sleep(random.uniform(0.3, 1.3))

    # GO TO COURSE RESERVATION LIST
    driver.get("https://gomp.uniroma3.it/StudentSpaceReserv")
    # driver2 = goToCourseReservationList(driver)
    time.sleep(random.uniform(0.3, 2))

    try:
        biblioHourParsed = IOConsole.biblioParsing(biblioHour)
    except IOError:
        print("No matching library time slot for the hour you inserted")
        return

    if biblioDay is not None:
        try:
            biblioDayParsed = IOConsole.userInsertedDayParsing(biblioDay)

            # CLICK ON THE DROPDOWN MENU
            select = Select(WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'courseSelector'))))
            select.select_by_visible_text("BIBLIOTECA - PRENOTAZIONE POSTO ALL'INTERNO DELLA BIBLIOTECA")

            biblioReservationCycle(driver, biblioDayParsed, biblioHourParsed)
        except IOError:
            print("Wrong day to reserve the library inserted!")
            return
    else:
        # CLICK ON THE DROPDOWN MENU
        select = Select(WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'courseSelector'))))
        select.select_by_visible_text("BIBLIOTECA - PRENOTAZIONE POSTO ALL'INTERNO DELLA BIBLIOTECA")

        biblioReservationCycle(driver, biblioDay, biblioHourParsed)


def biblioReservationCycle(driver, biblioDay, biblioHour):
    global reservationRow
    biblioHourString = str(biblioHour)

    time.sleep(random.uniform(0.3, 1.3))
    # CLICK ON THE TIME SLOT
    driver.find_element_by_xpath("//*[@id='courseBody']/tr[" + biblioHourString + "]").click()

    # If the user has inserted a day for the library reservation, use it; otherwise reserve the next day from now
    if biblioDay is not None:
        dayName = biblioDay
    else:
        dayName = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%A")

    # Find all the rows with the desired day of reservation
    nextDayXPath = IOConsole.composeDayXPath(dayName)
    desiredDayRows = WebDriverWait(driver, 3).until(
        EC.visibility_of_any_elements_located((By.XPATH, nextDayXPath)))

    # Find the rows with desired day and library
    desiredDayAndLibraryRows = list()

    for element in desiredDayRows:
        try:
            parentRow = element.find_element_by_xpath('..')
            parentRowText = parentRow.text
            rowTextRatio = SequenceMatcher(None, parentRowText, 'BIBLIOTECA SCIENTIFICA TECNOLOGICA SEDE CENTRALE - '
                                                                'via della Vasca Navale, 79-81 - Uniroma3').ratio()
            if 0.55 < rowTextRatio < 0.75:
                desiredDayAndLibraryRows.append(parentRow)
        except Exception:
            logging.info("Error occurred when trying to match day and library!")
            pass

    # Take the first row
    try:
        reservationRow = desiredDayAndLibraryRows.pop(0)
    except IndexError:
        logging.info("Empty list for matching day and library reservation!")
        print("No reservation option for " + dayName + "!")
        driver.quit()
        logging.info("Day to reserve library not found. Exiting the program...")
        sys.exit()

    # Check if the reservation row matches the desired day of the week
    try:
        logging.info("Looking for turn " + biblioHourString + " on " + dayName)
        WebDriverWait(reservationRow, 3).until(
            EC.element_to_be_clickable((
                By.XPATH, "//*[contains(text(), 'BIBLIOTECA SCIENTIFICA TECNOLOGICA SEDE CENTRALE - via della Vasca"
                          " Navale, 79-81 - Uniroma3')]"))).click()
    except Exception:
        print("No reservation option for " + dayName + "!")
        driver.quit()
        logging.info("Day to reserve library not found. Exiting the program...")
        sys.exit()


    # CLICK ON THE MODAL "YES" BUTTON
    try:
        WebDriverWait(driver, 2).until(EC.element_to_be_clickable((
            By.ID, "partialQuestionYesNoConfirmButton"))).click()
        time.sleep(random.uniform(1.5, 3))
    except Exception:
        logging.info("No modal with 'yes' and 'no' button shown")
        pass

    if driver.find_element_by_xpath("//h1[contains(text(), 'Dettagli prenotazione')]").is_displayed():
        reserve_another = input("Done!\n"
                                "Do you want to reserve the next time slot? [Y/n]...\n")
        temp = biblioHour + 1
        if reserve_another.casefold() in ("y", "yes", "si", "s") and temp < 10:
            logging.info("Trying to reserve the next time slot...")
            biblioHour += 1
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((
                By.ID, "backArrowReservs"))).click()
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((
                By.ID, "backArrow"))).click()
            biblioReservationCycle(driver, biblioDay, biblioHour)
        else:
            print("Nothing more to reserve. I'm gonna die...")
            driver.quit()
            logging.info("Library time slot reservation done. Exiting the program...")
            sys.exit()
    else:
        reserve_another = input(
            "Reservation of turn " + biblioHourString + " cannot be completed. It is possible that the library is full at "
                                                        "this time slot or there's an overlapping reservation of a lesson.\n"
                                                        "Do you want to reserve the next time slot? [Y/n]...\n")
        temp = biblioHour + 1
        if reserve_another.casefold() in ("y", "yes", "si", "s") and temp < 10:
            logging.info("Trying to reserve the next time slot...")
            biblioHour += 1
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((
                By.ID, "backArrow"))).click()
            biblioReservationCycle(driver, biblioDay, biblioHour)
        else:
            print("I'm gonna die...")
            driver.quit()
            logging.info('Quitting the program...')
            sys.exit()
