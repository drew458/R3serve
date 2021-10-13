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


def insertClass():
    inserted_class = input("Please insert the class you want to reserve...\n")

    logging.info("Started class parsing...")

    # ANALISI I
    if inserted_class in ("analisi", "Analisi", "Analisi I", "Analisi 1", "analisi 1", "Analisi matematica 1",
                          "Analisi Matematica 1", "analisi Matematica 1", "analisi Matematica I"):
        selected_class = ANALISI
        logging.info("Class parsing completed! I'mma look for " + selected_class + "...")
        return selected_class

        # GEOMETRIA E COMBINATORIA
    elif inserted_class in ("geometria", "Geometria", "geometria e combinatoria", "Geometria e Combinatoria",
                            "Geometria e combinatoria", "geometria e Combinatoria", "Geometria E Combinatoria"):
        selected_class = GEOMETRIA_COMBINATORIA
        logging.info("Class parsing completed! I'mma look for " + selected_class + "...")
        return selected_class

    # ELETTRONICA
    elif inserted_class in (
            "elettronica", "Elettronica", "Elettronica ed Elettrotecnica", "Elettronica ed Elettrotecnica",
            "Elettrotecnica", "elettrotecnica"):
        selected_class = ELETTRONICA_ELETTROTECNICA
        logging.info("Class parsing completed! I'mma look for " + selected_class + "...")
        return selected_class

    # FONDAMENTI DI TELECOMUNICAZIONI
    elif inserted_class in ("telecomunicazioni", "Telecomunicazioni", "Fondamenti di Telecomunicazioni",
                            "Fondamenti di telecomunicazioni", "tlc", "TLC"):
        selected_class = TELECOMUNICAZIONI
        logging.info("Class parsing completed! I'mma look for " + selected_class + "...")
        return selected_class

    # ANALISI DI SISTEMI AD EVENTI
    elif inserted_class in ("analisi di sistemi ad eventi", "ASE", "ase", "Analisi di sistemi ad eventi",
                            "Analisi Di Sistemi Ad Eventi", "Analisi di Sistemi ad Eventi"):
        selected_class = ANALISI_SISTEMI_EVENTI
        logging.info("Class parsing completed! I'mma look for " + selected_class + "...")
        return selected_class

    # ALGORITMI E STRUTTURE DATI
    elif inserted_class in ("algoritmi e strutture dati", "Algoritmi e strutture dati", "asd", "ASD",
                            "Algoritmi e Strutture Dati"):
        selected_class = ALGORITMI_STRUTTURE_DATI
        logging.info("Class parsing completed! I'mma look for " + selected_class + "...")
        return selected_class

    # BASI DI DATI
    elif inserted_class in ("basi di dati", "Basi Di Dati", "Basi di dati", "basi di dati 1", "Basi Di Dati 1",
                            "Basi di dati 1", "Basi di Dati I", "Basi di dati I", "Basi Di Dati I"):
        selected_class = BASI_DATI
        logging.info("Class parsing completed! I'mma look for " + selected_class + "...")
        return selected_class

    # SISTEMI OPERATIVI
    elif inserted_class in ("sistemi operativi", "Sistemi operativi", "Sistemi Operativi" "so" "SO"):
        selected_class = SISTEMI_OPERATIVI
        logging.info("Class parsing completed! I'mma look for " + selected_class + "...")
        return selected_class

    # RETI DI CALCOLATORI
    elif inserted_class in ("reti di calcolatori", "Reti di calcolatori", "Reti Di Calcolatori", "reti", "Reti"):
        selected_class = RETI_CALCOLATORI
        logging.info("Class parsing completed! I'mma look for " + selected_class + "...")
        return selected_class

    # PROGRAMMAZIONE FUNZIONALE
    elif inserted_class in ("programmazione funzionale", "Programmazione funzionale", "Programmazione Funzionale",
                            "pf", "PF"):
        selected_class = PROGRAMMAZIONE_FUNZIONALE
        logging.info("Class parsing completed! I'mma look for " + selected_class + "...")
        return selected_class

    # MOBILE COMPUTING
    elif inserted_class in ("mobile computing", "Mobile computing", "Mobile Computing", "MC", "mc"):
        selected_class = MOBILE_COMPUTING
        logging.info("Class parsing completed! I'mma look for " + selected_class + "...")
        return selected_class

    else:
        return IOError


def composeClassXPath(selected_class):
    a = "//tr/td[contains(text(), "
    b = "'" + selected_class + "'"
    c = ")]"

    z = a + b + c
    return z
