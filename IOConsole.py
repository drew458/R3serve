import logging

from static import Courses


def insertCourse(input_course):
    """
    Determines the course, passed as program argument or requested as user input
    :param: the course passed as an argumente when launching the program
    :return: the course
    """
    if input_course is None:
        inserted_course = input("Please insert the course you want to reserve...\n")
    else:
        inserted_course = input_course

    parsed_course = courseParsing(inserted_course)
    return parsed_course


def insertNewCourse():
    """
    Determines the course via user input
    :return: the course
    """
    while True:
        inserted_course = input("Please insert the course you want to reserve...\n")

        try:
            parsed_course = courseParsing(inserted_course)
        except IOError:
            print("No matching course for what you inserted")
            continue
        else:
            return parsed_course


def courseParsing(inserted_course):
    """
    Assings the user inserted course to the corrisponding course, as GOMP formats its name.
    :param: inserted_course: the user-typed course name
    :return: the GOMP-compatible course name
    """
    logging.info("Started course parsing...")

    # ANALISI I
    if inserted_course.casefold() in ("analisi", "analisi 1", "analisi matematica 1", "analisi matematica i"):
        selected_course = Courses.ANALISI
        logging.info("Course parsing completed! I'mma look for " + selected_course + "...")
        return selected_course

    # GEOMETRIA E COMBINATORIA
    elif inserted_course.casefold() in ("geometria", "geometria e combinatoria"):
        selected_course = Courses.GEOMETRIA_COMBINATORIA
        logging.info("Course parsing completed! I'mma look for " + selected_course + "...")
        return selected_course

    # FISICA I
    elif inserted_course.casefold() in ("fisica", "fisica 1", "fisica i"):
        selected_course = Courses.FISICA
        logging.info("Course parsing completed! I'mma look for " + selected_course + "...")
        return selected_course

    # CHIMICA
    elif inserted_course.casefold() in ("chimica", "chimica 1", "chimica i"):
        selected_course = Courses.CHIMICA
        logging.info("Course parsing completed! I'mma look for " + selected_course + "...")
        return selected_course

    # FONDAMENTI INFORMATICA
    elif inserted_course.casefold() in ("fondamenti di informatica", "informatica", "fdi", "fond inf",
                                        "fondamenti informatica"):
        selected_course = Courses.FONDAMENTI_INFORMATICA
        logging.info("Course parsing completed! I'mma look for " + selected_course + "...")
        return selected_course

    # ELETTRONICA
    elif inserted_course.casefold() in ("elettronica", "elettronica ed elettrotecnica", "elettrotecnica ed elettronica",
                                        "elettronica e elettrotecnica", "elettrotecnica e elettronica",
                                        "elettrotecnica"):
        selected_course = Courses.ELETTRONICA_ELETTROTECNICA
        logging.info("Course parsing completed! I'mma look for " + selected_course + "...")
        return selected_course

    # FONDAMENTI DI TELECOMUNICAZIONI
    elif inserted_course.casefold() in ("telecomunicazioni", "fondamenti di telecomunicazioni", "fondamenti tlc",
                                        "fondamenti di tlc", "tlc"):
        selected_course = Courses.TELECOMUNICAZIONI
        logging.info("Course parsing completed! I'mma look for " + selected_course + "...")
        return selected_course

    # ANALISI DI SISTEMI AD EVENTI
    elif inserted_course.casefold() in ("analisi di sistemi ad eventi", "ase"):
        selected_course = Courses.ANALISI_SISTEMI_EVENTI
        logging.info("Course parsing completed! I'mma look for " + selected_course + "...")
        return selected_course

    # ALGORITMI E STRUTTURE DATI
    elif inserted_course.casefold() in ("algoritmi e strutture dati", "asd"):
        selected_course = Courses.ALGORITMI_STRUTTURE_DATI
        logging.info("Course parsing completed! I'mma look for " + selected_course + "...")
        return selected_course

    # RICERCA OPERATIVA
    elif inserted_course.casefold() in ("ricerca operativa", "ricerca operativa 1", "ricerca operativa i",
                                        "ro", "ro1", "roi"):
        selected_course = Courses.RICERCA_OPERATIVA
        logging.info("Course parsing completed! I'mma look for " + selected_course + "...")
        return selected_course

    # PROGRAMMAZIONE ORIENTATA AGLI OGGETTI
    elif inserted_course.casefold() in ("programmazione orientata agli oggetti", "programmazione ad oggetti",
                                        "programmazione a oggetti", "poo"):
        selected_course = Courses.PROGRAMMAZIONE_AD_OGGETTI
        logging.info("Course parsing completed! I'mma look for " + selected_course + "...")
        return selected_course

    # CALCOLATORI ELETTRONICI
    elif inserted_course.casefold() in ("calcolatori elettronici", "calcolatori"):
        selected_course = Courses.CALCOLATORI_ELETTRONICI
        logging.info("Course parsing completed! I'mma look for " + selected_course + "...")
        return selected_course

    # BASI DI DATI
    elif inserted_course.casefold() in ("basi di dati", "basi di dati 1", "basi di dati i", "bd"):
        selected_course = Courses.BASI_DATI
        logging.info("Course parsing completed! I'mma look for " + selected_course + "...")
        return selected_course

    # ECONOMIA
    elif inserted_course.casefold() in ("economia applicata all'ingegneria", "economia", "eai"):
        selected_course = Courses.ECONOMIA
        logging.info("Course parsing completed! I'mma look for " + selected_course + "...")
        return selected_course

    # SISTEMI OPERATIVI
    elif inserted_course.casefold() in ("sistemi operativi", "so"):
        selected_course = Courses.SISTEMI_OPERATIVI
        logging.info("Course parsing completed! I'mma look for " + selected_course + "...")
        return selected_course

    # RETI DI CALCOLATORI
    elif inserted_course.casefold() in ("reti di calcolatori", "reti"):
        selected_course = Courses.RETI_CALCOLATORI
        logging.info("Course parsing completed! I'mma look for " + selected_course + "...")
        return selected_course

    # PROGRAMMAZIONE FUNZIONALE
    elif inserted_course.casefold() in ("programmazione funzionale", "funzionale", "pf"):
        selected_course = Courses.PROGRAMMAZIONE_FUNZIONALE
        logging.info("Course parsing completed! I'mma look for " + selected_course + "...")
        return selected_course

    # MOBILE COMPUTING
    elif inserted_course.casefold() in ("mobile computing", "mc", "mobile"):
        selected_course = Courses.MOBILE_COMPUTING
        logging.info("Course parsing completed! I'mma look for " + selected_course + "...")
        return selected_course

    # ANALISI E PROGETTAZIONE DEL SOFTWARE
    elif inserted_course.casefold() in ("analisi e progettazione del software",
                                        "analisi e progettazione software", "aps"):
        selected_course = Courses.ANALISI_PROGETTAZIONE_SOFTWARE
        logging.info("Course parsing completed! I'mma look for " + selected_course + "...")
        return selected_course

    # SISTEMI INFORMATIVI SU WEB
    elif inserted_course.casefold() in ("sistemi informativi su web",
                                        "sistemi informativi sul web", "siw"):
        selected_course = Courses.SISTEMI_INFORMATIVI_WEB
        logging.info("Course parsing completed! I'mma look for " + selected_course + "...")
        return selected_course

    else:
        raise IOError


def biblioParsing(biblioHour):
    if biblioHour in ("09.00", "9.00", "09,00", "9,00", "09", "9"):
        i = 1
        return i
    elif biblioHour in ("10.00", "10,00", "10"):
        i = 2
        return i
    elif biblioHour in ("11.00", "11,00", "11"):
        i = 3
        return i
    elif biblioHour in ("12.00", "12,00", "12"):
        i = 4
        return i
    elif biblioHour in ("14.00", "14,00", "14", "2"):
        i = 5
        return i
    elif biblioHour in ("15.00", "15,00", "15", "3"):
        i = 6
        return i
    elif biblioHour in ("16.00", "16,00", "16", "4"):
        i = 7
        return i
    elif biblioHour in ("17.00", "17,00", "17", "5"):
        i = 8
        return i
    elif biblioHour in ("18.00", "18,00", "18", "6"):
        i = 9
        return i
    else:
        return IOError


def composeCourseXPath(selected_course):
    """
    Composes the XPATH of the course in the reservation list
    :param selected_course: the course name
    :return: the XPATH
    """
    a = "//tr/td[contains(text(), "
    b = "'" + selected_course + "'"
    c = ")]"

    z = a + b + c
    return z
