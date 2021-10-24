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
    Determines thwe course via user input
    :return: the course
    """
    inserted_course = input("Please insert the course you want to reserve...\n")

    parsed_course = courseParsing(inserted_course)
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
        logging.info("course parsing completed! I'mma look for " + selected_course + "...")
        return selected_course

    # GEOMETRIA E COMBINATORIA
    elif inserted_course.casefold() in ("geometria", "geometria e combinatoria"):
        selected_course = Courses.GEOMETRIA_COMBINATORIA
        logging.info("course parsing completed! I'mma look for " + selected_course + "...")
        return selected_course

    # FISICA I
    elif inserted_course.casefold() in ("fisica", "fisica 1", "fisica i"):
        selected_course = Courses.FISICA
        logging.info("course parsing completed! I'mma look for " + selected_course + "...")
        return selected_course

    # CHIMICA
    elif inserted_course.casefold() in ("chimica", "chimica 1", "chimica i"):
        selected_course = Courses.CHIMICA
        logging.info("course parsing completed! I'mma look for " + selected_course + "...")
        return selected_course

    # FONDAMENTI INFORMATICA
    elif inserted_course.casefold() in ("fondamenti di informatica", "informatica", "fdi", "fond inf",
                                        "fondamenti informatica"):
        selected_course = Courses.FONDAMENTI_INFORMATICA
        logging.info("course parsing completed! I'mma look for " + selected_course + "...")
        return selected_course

    # ELETTRONICA
    elif inserted_course.casefold() in ("elettronica", "elettronica ed elettrotecnica", "elettrotecnica ed elettronica",
                                        "elettronica e elettrotecnica", "elettrotecnica e elettronica",
                                        "elettrotecnica"):
        selected_course = Courses.ELETTRONICA_ELETTROTECNICA
        logging.info("course parsing completed! I'mma look for " + selected_course + "...")
        return selected_course

    # FONDAMENTI DI TELECOMUNICAZIONI
    elif inserted_course.casefold() in ("telecomunicazioni", "fondamenti di telecomunicazioni", "fondamenti tlc",
                                        "fondamenti di tlc", "tlc"):
        selected_course = Courses.TELECOMUNICAZIONI
        logging.info("course parsing completed! I'mma look for " + selected_course + "...")
        return selected_course

    # ANALISI DI SISTEMI AD EVENTI
    elif inserted_course.casefold() in ("analisi di sistemi ad eventi", "ase"):
        selected_course = Courses.ANALISI_SISTEMI_EVENTI
        logging.info("course parsing completed! I'mma look for " + selected_course + "...")
        return selected_course

    # ALGORITMI E STRUTTURE DATI
    elif inserted_course.casefold() in ("algoritmi e strutture dati", "asd"):
        selected_course = Courses.ALGORITMI_STRUTTURE_DATI
        logging.info("course parsing completed! I'mma look for " + selected_course + "...")
        return selected_course

    # RICERCA OPERATIVA
    elif inserted_course.casefold() in ("ricerca operativa", "ricerca operativa 1", "ricerca operativa i",
                                        "ro", "ro1", "roi"):
        selected_course = Courses.RICERCA_OPERATIVA
        logging.info("course parsing completed! I'mma look for " + selected_course + "...")
        return selected_course

    # PROGRAMMAZIONE ORIENTATA AGLI OGGETTI
    elif inserted_course.casefold() in ("programmazione orientata agli oggetti", "programmazione ad oggetti",
                                        "programmazione a oggetti", "poo"):
        selected_course = Courses.PROGRAMMAZIONE_AD_OGGETTI
        logging.info("course parsing completed! I'mma look for " + selected_course + "...")
        return selected_course

    # CALCOLATORI ELETTRONICI
    elif inserted_course.casefold() in ("calcolatori elettronici", "calcolatori"):
        selected_course = Courses.CALCOLATORI_ELETTRONICI
        logging.info("course parsing completed! I'mma look for " + selected_course + "...")
        return selected_course

    # BASI DI DATI
    elif inserted_course.casefold() in ("basi di dati", "basi di dati 1", "basi di dati i", "bd"):
        selected_course = Courses.BASI_DATI
        logging.info("course parsing completed! I'mma look for " + selected_course + "...")
        return selected_course

    # ECONOMIA
    elif inserted_course.casefold() in ("economia applicata all'ingegneria", "economia", "eai"):
        selected_course = Courses.ECONOMIA
        logging.info("course parsing completed! I'mma look for " + selected_course + "...")
        return selected_course

    # SISTEMI OPERATIVI
    elif inserted_course.casefold() in ("sistemi operativi", "so"):
        selected_course = Courses.SISTEMI_OPERATIVI
        logging.info("course parsing completed! I'mma look for " + selected_course + "...")
        return selected_course

    # RETI DI CALCOLATORI
    elif inserted_course.casefold() in ("reti di calcolatori", "reti"):
        selected_course = Courses.RETI_CALCOLATORI
        logging.info("course parsing completed! I'mma look for " + selected_course + "...")
        return selected_course

    # PROGRAMMAZIONE FUNZIONALE
    elif inserted_course.casefold() in ("programmazione funzionale", "funzionale", "pf"):
        selected_course = Courses.PROGRAMMAZIONE_FUNZIONALE
        logging.info("course parsing completed! I'mma look for " + selected_course + "...")
        return selected_course

    # MOBILE COMPUTING
    elif inserted_course.casefold() in ("mobile computing", "mc", "mobile"):
        selected_course = Courses.MOBILE_COMPUTING
        logging.info("course parsing completed! I'mma look for " + selected_course + "...")
        return selected_course

    # ANALISI E PROGETTAZIONE DEL SOFTWARE
    elif inserted_course.casefold() in ("analisi e progettazione del software",
                                        "analisi e progettazione software", "aps"):
        selected_course = Courses.ANALISI_PROGETTAZIONE_SOFTWARE
        logging.info("course parsing completed! I'mma look for " + selected_course + "...")
        return selected_course

    # SISTEMI INFORMATIVI SU WEB
    elif inserted_course.casefold() in ("sistemi informativi su web",
                                        "sistemi informativi sul web", "siw"):
        selected_course = Courses.SISTEMI_INFORMATIVI_WEB
        logging.info("course parsing completed! I'mma look for " + selected_course + "...")
        return selected_course

    else:
        raise IOError


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
