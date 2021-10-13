import logging

ANALISI = "ANALISI MATEMATICA I"
GEOMETRIA_COMBINATORIA = "GEOMETRIA E COMBINATORIA"
FISICA = "FISICA I"  # TODO: implementare nel parsing sotto
CHIMICA = "CHIMICA"  # TODO: implementare nel parsing sotto
FONDAMENTI_INFORMATICA = "FONDAMENTI DI INFORMATICA"  # TODO: implementare nel parsing sotto
ELETTRONICA_ELETTROTECNICA = "ELETTROTECNICA ED ELETTRONICA"
TELECOMUNICAZIONI = "FONDAMENTI DI TELECOMUNICAZIONE"
ANALISI_SISTEMI_EVENTI = "ANALISI DI SISTEMI AD EVENTI"
ALGORITMI_STRUTTURE_DATI = "ALGORITMI E STRUTTURE DATI"
RICERCA_OPERATIVA = "RICERCA OPERATIVA"  # TODO: implementare nel parsing sotto
FONDAMENTI_AUTOMATICA = "FONDAMENTI DI AUTOMATICA"  # TODO: implementare nel parsing sotto
PROGRAMMAZIONE_AD_OGGETTI = "PROGRAMMAZIONE ORIENTATA AGLI OGGETTI"  # TODO: implementare nel parsing sotto
CALCOLATORI_ELETTRONICI = "CALCOLATORI ELETTRONICI"  # TODO: implementare nel parsing sotto
BASI_DATI = "BASI DI DATI I"
ECONOMIA = "ECONOMIA APPLICATA ALL'INGEGNERIA"  # TODO: implementare nel parsing sotto
SISTEMI_OPERATIVI = "SISTEMI OPERATIVI"
PROGRAMMAZIONE_FUNZIONALE = "PROGRAMMAZIONE FUNZIONALE"
RETI_CALCOLATORI = "RETI DI CALCOLATORI"
MOBILE_COMPUTING = "MOBILE COMPUTING"
ANALISI_PROGETTAZIONE_SOFTWARE = "ANALISI E PROGETTAZIONE DEL SOFTWARE"  # TODO: implementare nel parsing sotto
SISTEMI_INFORMATIVI_WEB = "SISTEMI INFORMATIVI SU WEB"  # TODO: implementare nel parsing sotto


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
    if inserted_course in ("analisi", "Analisi", "Analisi I", "Analisi 1", "analisi 1", "Analisi matematica 1",
                           "Analisi Matematica 1", "analisi Matematica 1", "analisi Matematica I"):
        selected_course = ANALISI
        logging.info("course parsing completed! I'mma look for " + selected_course + "...")
        return selected_course

        # GEOMETRIA E COMBINATORIA
    elif inserted_course in ("geometria", "Geometria", "geometria e combinatoria", "Geometria e Combinatoria",
                             "Geometria e combinatoria", "geometria e Combinatoria", "Geometria E Combinatoria"):
        selected_course = GEOMETRIA_COMBINATORIA
        logging.info("course parsing completed! I'mma look for " + selected_course + "...")
        return selected_course

    # ELETTRONICA
    elif inserted_course in (
            "elettronica", "Elettronica", "Elettronica ed Elettrotecnica", "Elettronica ed Elettrotecnica",
            "Elettrotecnica", "elettrotecnica"):
        selected_course = ELETTRONICA_ELETTROTECNICA
        logging.info("course parsing completed! I'mma look for " + selected_course + "...")
        return selected_course

    # FONDAMENTI DI TELECOMUNICAZIONI
    elif inserted_course in ("telecomunicazioni", "Telecomunicazioni", "Fondamenti di Telecomunicazioni",
                             "Fondamenti di telecomunicazioni", "tlc", "TLC"):
        selected_course = TELECOMUNICAZIONI
        logging.info("course parsing completed! I'mma look for " + selected_course + "...")
        return selected_course

    # ANALISI DI SISTEMI AD EVENTI
    elif inserted_course in ("analisi di sistemi ad eventi", "ASE", "ase", "Analisi di sistemi ad eventi",
                             "Analisi Di Sistemi Ad Eventi", "Analisi di Sistemi ad Eventi"):
        selected_course = ANALISI_SISTEMI_EVENTI
        logging.info("course parsing completed! I'mma look for " + selected_course + "...")
        return selected_course

    # ALGORITMI E STRUTTURE DATI
    elif inserted_course in ("algoritmi e strutture dati", "Algoritmi e strutture dati", "asd", "ASD",
                             "Algoritmi e Strutture Dati"):
        selected_course = ALGORITMI_STRUTTURE_DATI
        logging.info("course parsing completed! I'mma look for " + selected_course + "...")
        return selected_course

    # BASI DI DATI
    elif inserted_course in ("basi di dati", "Basi Di Dati", "Basi di dati", "basi di dati 1", "Basi Di Dati 1",
                             "Basi di dati 1", "Basi di Dati I", "Basi di dati I", "Basi Di Dati I"):
        selected_course = BASI_DATI
        logging.info("course parsing completed! I'mma look for " + selected_course + "...")
        return selected_course

    # SISTEMI OPERATIVI
    elif inserted_course in ("sistemi operativi", "Sistemi operativi", "Sistemi Operativi" "so" "SO"):
        selected_course = SISTEMI_OPERATIVI
        logging.info("course parsing completed! I'mma look for " + selected_course + "...")
        return selected_course

    # RETI DI CALCOLATORI
    elif inserted_course in ("reti di calcolatori", "Reti di calcolatori", "Reti Di Calcolatori", "reti", "Reti"):
        selected_course = RETI_CALCOLATORI
        logging.info("course parsing completed! I'mma look for " + selected_course + "...")
        return selected_course

    # PROGRAMMAZIONE FUNZIONALE
    elif inserted_course in ("programmazione funzionale", "Programmazione funzionale", "Programmazione Funzionale",
                             "pf", "PF"):
        selected_course = PROGRAMMAZIONE_FUNZIONALE
        logging.info("course parsing completed! I'mma look for " + selected_course + "...")
        return selected_course

    # MOBILE COMPUTING
    elif inserted_course in ("mobile computing", "Mobile computing", "Mobile Computing", "MC", "mc"):
        selected_course = MOBILE_COMPUTING
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
