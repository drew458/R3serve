ANALISI = "ANALISI MATEMATICA I"
GEOMETRIA_COMBINATORIA = "GEOMETRIA E COMBINATORIA"
ELETTRONICA_ELETTROTECNICA = "ELETTROTECNICA ED ELETTRONICA"
TELECOMUNICAZIONI = "FONDAMENTI DI TELECOMUNICAZIONE"
ANALISI_SISTEMI_EVENTI = "ANALISI DI SISTEMI AD EVENTI"
ALGORITMI_STRUTTURE_DATI = "ALGORITMI E STRUTTURE DATI"
BASI_DATI = "BASI DI DATI I"
SISTEMI_OPERATIVI = "SISTEMI OPERATIVI"
PROGRAMMAZIONE_FUNZIONALE = "PROGRAMMAZIONE FUNZIONALE"
RETI_CALCOLATORI = "RETI DI CALCOLATORI"
MOBILE_COMPUTING = "MOBILE COMPUTING"


def insertClass():
    inserted_class = input("Please insert the class you want to reserve...\n")

    # ANALISI I
    if inserted_class == "analisi" or inserted_class == "Analisi" or inserted_class == "Analisi I" \
            or inserted_class == "Analisi 1" or inserted_class == "analisi 1" \
            or inserted_class == "Analisi matematica 1" or inserted_class == "Analisi Matematica 1"\
            or inserted_class == "analisi Matematica 1" or inserted_class == "analisi Matematica I":
        selected_class = ANALISI
        return selected_class

    # GEOMETRIA E COMBINATORIA
    elif inserted_class == "geometria" or inserted_class == "Geometria" or inserted_class == "geometria e combinatoria" \
            or inserted_class == "Geometria e Combinatoria" or inserted_class == "Geometria e combinatoria"\
            or inserted_class == "geometria e Combinatoria" or inserted_class == "Geometria E Combinatoria":
        selected_class = GEOMETRIA_COMBINATORIA
        return selected_class

    # ELETTRONICA
    elif inserted_class == "elettronica" or inserted_class == "Elettronica" or inserted_class == "Elettronica ed Elettrotecnica" \
            or inserted_class == "Elettronica ed Elettrotecnica" or inserted_class == "Elettrotecnica"\
            or inserted_class == "elettrotecnica":
        selected_class = ELETTRONICA_ELETTROTECNICA
        return selected_class

    # FONDAMENTI DI TELECOMUNICAZIONI
    elif inserted_class == "telecomunicazioni" or inserted_class == "Telecomunicazioni" \
            or inserted_class == "Fondamenti di Telecomunicazioni" or inserted_class == "Fondamenti di telecomunicazioni"\
            or inserted_class == "tlc" or inserted_class == "TLC":
        selected_class = TELECOMUNICAZIONI
        return selected_class

    # ANALISI DI SISTEMI AD EVENTI
    elif inserted_class == "analisi di sistemi ad eventi" or inserted_class == "ASE" or inserted_class == "ase" \
            or inserted_class == "Analisi di sistemi ad eventi" or inserted_class == "Analisi Di Sistemi Ad Eventi"\
            or inserted_class == "Analisi di Sistemi ad Eventi":
        selected_class = ANALISI_SISTEMI_EVENTI
        return selected_class

    # ALGORITMI E STRUTTURE DATI
    elif inserted_class == "algoritmi e strutture dati" or inserted_class == "Algoritmi e strutture dati"\
            or inserted_class == "asd" or inserted_class == "ASD" or inserted_class == "Algoritmi e Strutture Dati":
        selected_class = ALGORITMI_STRUTTURE_DATI
        return selected_class

    # BASI DI DATI
    elif inserted_class == "basi di dati" or inserted_class == "Basi Di Dati" or inserted_class == "Basi di dati"\
            or inserted_class == "basi di dati 1" or inserted_class == "Basi Di Dati 1" or inserted_class == "Basi di dati 1"\
            or inserted_class == "Basi di Dati I" or inserted_class == "Basi di dati I" or inserted_class == "Basi Di Dati I":
        selected_class = BASI_DATI
        return selected_class

    # SISTEMI OPERATIVI
    elif inserted_class == "sistemi operativi" or inserted_class == "Sistemi operativi" \
            or inserted_class == "Sistemi Operativi" or inserted_class == "so" or inserted_class == "SO":
        selected_class = SISTEMI_OPERATIVI
        return selected_class

    # RETI DI CALCOLATORI
    elif inserted_class == "reti di calcolatori" or inserted_class == "Reti di calcolatori" or inserted_class == "Reti Di Calcolatori"\
            or inserted_class == "reti" or inserted_class == "Reti":
        selected_class = RETI_CALCOLATORI
        return selected_class

    # PROGRAMMAZIONE FUNZIONALE
    elif inserted_class == "programmazione funzionale" or inserted_class == "Programmazione funzionale" \
            or inserted_class == "Programmazione Funzionale" or inserted_class == "pf" or inserted_class == "PF":
        selected_class = PROGRAMMAZIONE_FUNZIONALE
        return selected_class

    # MOBILE COMPUTING
    elif inserted_class == "mobile computing" or inserted_class == "Mobile computing" \
            or inserted_class == "Mobile Computing" or inserted_class == "MC" or inserted_class == "mc":
        selected_class = MOBILE_COMPUTING
        return selected_class

    else:
        return IOError


def composeClassXPath(selected_class):
    a = "//tr/td[contains(text(), "
    b = "'" + selected_class + "'"
    c = ")]"

    z = a + b + c
    return z
