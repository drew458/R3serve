import logging
import time

import selenium

import ClassNames


def goToClassReservationList(driver):
    logging.info('Going to the class reservation list...')

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
        logging.info('Landend on the class reservation list!')
    else:
        time.sleep(5)
        logging.info('Landend on the class reservation list!')

    return driver


def clickOnClass(driver, selected_class):
    logging.info('Reaching the inserted class reservation to click on...')

    # get the table
    table = driver.find_element_by_xpath("//*[@id='studyPlanBody']")

    # find the row
    try:
        class_xpath = ClassNames.composeClassXPath(selected_class)
        table.find_element_by_xpath(class_xpath).click()
    except IOError:
        print("No such class found!")
        reserve_another = input("Do you want to insert another class? [Y/n]...\n")
        if reserve_another == "y" or reserve_another == "Y":
            another_class_name = ClassNames.insertClass()
            reserve(driver, another_class_name)
        else:
            driver.quit()
            quit()
    else:
        time.sleep(3)
        logging.info('Here it is!')

    return driver


def reserve(driver, selected_class):
    driver.refresh()
    time.sleep(3)

    # GO TO CLASS RESERVATION LIST
    driver2 = goToClassReservationList(driver)

    # CLICK ON THE CLASS
    driver3 = clickOnClass(driver2, selected_class)

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
            print("No more lessons available for this class!")
            reserve_another = input("Do you want to reserve another class? [Y/n]...\n")
            if reserve_another == "y" or reserve_another == "Y":
                another_class_name = ClassNames.insertClass()
                reserve(driver, another_class_name)
            else:
                driver.quit()
                quit()
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
                    print("Class at line " + iString + " already reserved")
                    continue
                else:
                    calendar.click()
                    time.sleep(3)
                    modal = driver3.find_element_by_xpath("//*[@id='partialQuestionYesNo']")
                    modal.find_element_by_xpath("//*[@id='partialQuestionYesNoConfirmButton']").click()
                    time.sleep(10)

                if driver3.find_element_by_xpath("//h1[contains(text(), 'Dettagli prenotazione')]").is_displayed():
                    reserve_another = input("Done!\n"
                                            "Do you want to reserve another lesson for this class? [Y/n]...\n")
                    if reserve_another == "y" or reserve_another == "Y":
                        driver3.find_element_by_xpath("//*[@id='backArrowReservs']").click()
                        continue
                    else:
                        driver.quit()
                        quit()
                else:
                    print("This reservation overlaps with another one in the same time slot, "
                          "hence it cannot be completed.\n"
                          "It's devstating, I know.")
