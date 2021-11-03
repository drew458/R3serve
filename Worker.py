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
        reserve_another = input("Do you want to insert another course? [Y/n]...\n")
        if reserve_another.casefold() in ("y", "yes", "si", "s"):
            another_course_name = IOConsole.insertNewCourse()
            reserve(driver, another_course_name)
        else:
            logging.info('Quitting the program...')
            driver.quit()
            logging.info("Driver thrown away, I'm gonna die")
            sys.exit()
    else:
        logging.info('Here it is!')

    return driver


def reserve(driver, selected_course):
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
            time.sleep(1.5)
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
                return
                # logging.info('Quitting the program...')
                # driver.quit()
                # logging.info("Driver thrown away, I'm gonna die")
                # sys.exit()
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
                time.sleep(1.5)
                if driver3.find_element_by_xpath("//h1[contains(text(), 'Dettagli prenotazione')]").is_displayed():
                    reserve_another = input("Done!\n"
                                            "Do you want to reserve another lesson for this course? [Y/n]...\n")
                    if reserve_another.casefold() in ("y", "yes", "si", "s"):
                        WebDriverWait(driver3, 20).until(EC.element_to_be_clickable((
                            By.ID, "backArrowReservs"))).click()
                        # driver3.find_element_by_id("backArrowReservs").click()
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
                            # driver3.find_element_by_id("backArrowReservs").click()
                        except Exception:
                            continue
                    else:
                        break


def reserveBiblio(driver, biblioHour):
    driver.refresh()
    time.sleep(random.uniform(0.3, 1.3))

    # GO TO COURSE RESERVATION LIST
    driver.get("https://gomp.uniroma3.it/StudentSpaceReserv")
    # driver2 = goToCourseReservationList(driver)
    time.sleep(random.uniform(0.3, 1.3))

    while True:
        try:
            biblioHourParsed = IOConsole.biblioParsing(biblioHour)
        except IOError:
            print("No matching library time slot for the hour you inserted")
            return
        break

    biblioReservationCycle(driver, biblioHourParsed)


def biblioReservationCycle(driver, biblioHour):
    driver.refresh()
    time.sleep(random.uniform(0.3, 1.3))

    # CLICK ON THE DROPDOWN MENU
    select = Select(WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'courseSelector'))))
    select.select_by_visible_text("BIBLIOTECA - PRENOTAZIONE POSTO ALL'INTERNO DELLA BIBLIOTECA")

    biblioHourString = str(biblioHour)

    time.sleep(random.uniform(0.3, 1.3))
    # CLICK ON THE TIME SLOT
    # WebDriverWait(driver2, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='courseBody']/tr[" + biblioHourString + "]"))).click()
    driver.find_element_by_xpath("//*[@id='courseBody']/tr[" + biblioHourString + "]").click()

    time.sleep(random.uniform(0.3, 1.3))
    # CLICK ON THE ENGINEERING DEPARTMENT LIBRARY
    WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((
            By.XPATH, "//*[contains(text(), 'BIBLIOTECA SCIENTIFICA TECNOLOGICA SEDE CENTRALE - via della Vasca"
                      " Navale, 79-81 - Uniroma3')]"))).click()

    # CLICK ON THE MODAL "YES" BUTTON
    try:
        WebDriverWait(driver, 2).until(EC.element_to_be_clickable((
            By.ID, "partialQuestionYesNoConfirmButton"))).click()
    except Exception:
        if driver.find_element_by_xpath("//h1[contains(text(), 'Dettagli prenotazione')]").is_displayed():
            print("Library time slot already reserved!")
            biblioHour += 1
            biblioReservationCycle(driver, biblioHour)

    time.sleep(random.uniform(0.5, 1.3))
    if driver.find_element_by_xpath("//h1[contains(text(), 'Dettagli prenotazione')]").is_displayed():
        print("Done!")
    else:
        print("Reservation cannot be completed. It is possible that the library is full at this time slot or there's"
              " an overlapping reservation of a lesson.\n"
              "Now I'll try to reserve the next time slot...")
        biblioHour += 1
        biblioReservationCycle(driver, biblioHour)
