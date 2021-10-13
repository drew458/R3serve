import logging
import time

import schedule
import selenium

import Login
import Worker


def reserveClass(driver, class_to_reserve):
    driver.refresh()
    time.sleep(3)

    # GO TO CLASS RESERVATION LIST
    driver2 = Worker.goToClassReservationList(driver)

    # CLICK ON THE CLASS
    driver3 = Worker.clickOnClass(driver2, class_to_reserve)

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
                    print("Class at line " + iString + " already reserved")
                    continue
                else:
                    calendar.click()
                    time.sleep(3)
                    modal = driver3.find_element_by_xpath("//*[@id='partialQuestionYesNo']")
                    modal.find_element_by_xpath("//*[@id='partialQuestionYesNoConfirmButton']").click()
                    time.sleep(10)

                if driver3.find_element_by_xpath("//h1[contains(text(), 'Dettagli prenotazione')]").is_displayed():
                    print("Done!\n")
                    driver3.find_element_by_xpath("//*[@id='backArrowReservs']").click()
                    continue
                else:
                    print("This reservation overlaps with another one in the same time slot, "
                          "hence it cannot be completed.\n"
                          "It's devstating, I know.")


def launcher(class_to_reserve, inputUsername, inputPassword, headlessMode):
    driver = Login.login(inputUsername, inputPassword, headlessMode)
    reserveClass(driver, class_to_reserve)


def scheduler(inputUsername, inputPassword, headlessMode):
    """

    """

    logging.info('Starting automatic reserve threads...')

    schedule.every().monday.at("00:07").do(launcher, class_to_reserve="basi di dati",
                                           inputUsername=inputUsername, inputPassword=inputPassword,
                                           headlessMode=headlessMode)
    schedule.every().monday.at("00:08").do(launcher, class_to_reserve="reti di calcolatori",
                                           inputUsername=inputUsername, inputPassword=inputPassword,
                                           headlessMode=headlessMode)
    schedule.every().monday.at("00:06").do(launcher, class_to_reserve="mobile computing",
                                           inputUsername=inputUsername, inputPassword=inputPassword,
                                           headlessMode=headlessMode)
    schedule.every().monday.at("00:09").do(launcher, class_to_reserve="programmazione funzionale",
                                           inputUsername=inputUsername, inputPassword=inputPassword,
                                           headlessMode=headlessMode)

    schedule.every().tuesday.at("00:07").do(launcher, class_to_reserve="mobile computing",
                                            inputUsername=inputUsername, inputPassword=inputPassword,
                                            headlessMode=headlessMode)
    schedule.every().tuesday.at("00:08").do(launcher, class_to_reserve="programmazione funzionale",
                                            inputUsername=inputUsername, inputPassword=inputPassword,
                                            headlessMode=headlessMode)
    schedule.every().tuesday.at("00:06").do(launcher, class_to_reserve="sistemi operativi",
                                            inputUsername=inputUsername, inputPassword=inputPassword,
                                            headlessMode=headlessMode)

    schedule.every().wednesday.at("00:07").do(launcher, class_to_reserve="sistemi operativi",
                                              inputUsername=inputUsername, inputPassword=inputPassword,
                                              headlessMode=headlessMode)

    schedule.every().thursday.at("00:07").do(launcher, class_to_reserve="basi di dati",
                                             inputUsername=inputUsername, inputPassword=inputPassword,
                                             headlessMode=headlessMode)
    schedule.every().thursday.at("00:08").do(launcher, class_to_reserve="reti di calcolatori",
                                             inputUsername=inputUsername, inputPassword=inputPassword,
                                             headlessMode=headlessMode)

    logging.info('Automatic reserve threads started!')

    while True:
        schedule.run_pending()
        time.sleep(1)
        logging.info("AUTOMATIC reserve thread running...")
