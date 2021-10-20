import logging

from static import Courses


def insertCourse(input_course):
    if input_course is None:
        inserted_course = input("Please insert the course you want to reserve...\n")
    else:
        inserted_course = input_course

    parsed_course = courseParsing(inserted_course)
    return parsed_course


def insertNewCourse():
    inserted_course = input("Please insert the course you want to reserve...\n")

    parsed_course = courseParsing(inserted_course)
    return parsed_course


def courseParsing(inserted_course):
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
        selected_course = ELETTRONICA_ELETTROTECNICA
        logging.info("course parsing completed! I'mma look for " + selected_course + "...")
        return selected_course

    # FONDAMENTI DI TELECOMUNICAZIONI
    elif inserted_course.casefold() in ("telecomunicazioni", "fondamenti di telecomunicazioni", "fondamenti tlc",
                                        "fondamenti di tlc", "tlc"):
        selected_course = TELECOMUNICAZIONI
        logging.info("course parsing completed! I'mma look for " + selected_course + "...")
        return selected_course

    # ANALISI DI SISTEMI AD EVENTI
    elif inserted_course.casefold() in ("analisi di sistemi ad eventi", "ase"):
        selected_course = ANALISI_SISTEMI_EVENTI
        logging.info("course parsing completed! I'mma look for " + selected_course + "...")
        return selected_course

    # ALGORITMI E STRUTTURE DATI
    elif inserted_course.casefold() in ("algoritmi e strutture dati", "asd"):
        selected_course = ALGORITMI_STRUTTURE_DATI
        logging.info("course parsing completed! I'mma look for " + selected_course + "...")
        return selected_course

    # RICERCA OPERATIVA
    elif inserted_course.casefold() in ("ricerca operativa", "ricerca operativa 1", "ricerca operativa i",
                                        "ro", "ro1", "roi"):
        selected_course = RICERCA_OPERATIVA
        logging.info("course parsing completed! I'mma look for " + selected_course + "...")
        return selected_course

    # PROGRAMMAZIONE ORIENTATA AGLI OGGETTI
    elif inserted_course.casefold() in ("programmazione orientata agli oggetti", "programmazione ad oggetti",
                                        "programmazione a oggetti", "poo"):
        selected_course = PROGRAMMAZIONE_AD_OGGETTI
        logging.info("course parsing completed! I'mma look for " + selected_course + "...")
        return selected_course

    # CALCOLATORI ELETTRONICI
    elif inserted_course.casefold() in ("calcolatori elettronici", "calcolatori"):
        selected_course = CALCOLATORI_ELETTRONICI
        logging.info("course parsing completed! I'mma look for " + selected_course + "...")
        return selected_course

    # BASI DI DATI
    elif inserted_course.casefold() in ("basi di dati", "basi di dati 1", "basi di dati i", "bd"):
        selected_course = BASI_DATI
        logging.info("course parsing completed! I'mma look for " + selected_course + "...")
        return selected_course

    # ECONOMIA
    elif inserted_course.casefold() in ("economia applicata all'ingegneria", "economia", "eai"):
        selected_course = ECONOMIA
        logging.info("course parsing completed! I'mma look for " + selected_course + "...")
        return selected_course

    # SISTEMI OPERATIVI
    elif inserted_course.casefold() in ("sistemi operativi", "so"):
        selected_course = SISTEMI_OPERATIVI
        logging.info("course parsing completed! I'mma look for " + selected_course + "...")
        return selected_course

    # RETI DI CALCOLATORI
    elif inserted_course.casefold() in ("reti di calcolatori", "reti"):
        selected_course = RETI_CALCOLATORI
        logging.info("course parsing completed! I'mma look for " + selected_course + "...")
        return selected_course

    # PROGRAMMAZIONE FUNZIONALE
    elif inserted_course.casefold() in ("programmazione funzionale", "funzionale", "pf"):
        selected_course = PROGRAMMAZIONE_FUNZIONALE
        logging.info("course parsing completed! I'mma look for " + selected_course + "...")
        return selected_course

    # MOBILE COMPUTING
    elif inserted_course.casefold() in ("mobile computing", "mc"):
        selected_course = MOBILE_COMPUTING
        logging.info("course parsing completed! I'mma look for " + selected_course + "...")
        return selected_course

    # ANALISI E PROGETTAZIONE DEL SOFTWARE
    elif inserted_course.casefold() in ("analisi e progettazione del software",
                                        "analisi e progettazione software", "aps"):
        selected_course = ANALISI_PROGETTAZIONE_SOFTWARE
        logging.info("course parsing completed! I'mma look for " + selected_course + "...")
        return selected_course

    # SISTEMI INFORMATIVI SU WEB
    elif inserted_course.casefold() in ("sistemi informativi su web",
                                        "sistemi informativi sul web", "siw"):
        selected_course = SISTEMI_INFORMATIVI_WEB
        logging.info("course parsing completed! I'mma look for " + selected_course + "...")
        return selected_course

    else:
        return IOError


def composeCourseXPath(selected_course):
    a = "//tr/td[contains(text(), "
    b = "'" + selected_course + "'"
    c = ")]"

    z = a + b + c
    return z
