"""
Copyright (C) 2023 Dave Walsh

Codes sourced from

Bateman BT, Mhyre JM, Hernandez-Diaz S, Huybrechts KF,
    Fischer MA, Creanga AA, Callaghan WM, Gagne JJ.
    Development of a comorbidity index for use in obstetric
    patients. Obstet Gynecol. 2013 Nov;122(5):957-965.
    doi: 10.1097/AOG.0b013e3182a603bb. PMID: 24104771;
    PMCID: PMC3829199
Leonard SA, Kennedy CJ, Carmichael SL, Lyell DJ, Main EK.
    An Expanded Obstetric Comorbidity Scoring System for
    Predicting Severe Maternal Morbidity. Obstet Gynecol.
    2020 Sep;136(3):440-449. doi: 10.1097/AOG.0000000000004022.
    PMID: 32769656; PMCID: PMC7523732
"""
import pandas as pd

GDM = dict()

CODE_TYPE = 'DX'
VERSION = 'ICD9'
CODE = 'code'

GDM[CODE_TYPE] = dict()
GDM[CODE_TYPE][VERSION] = dict()
GDM[CODE_TYPE][VERSION][CODE] = (
    "^6488.*",
)

VERSION = 'ICD10'
GDM[CODE_TYPE][VERSION] = dict()
GDM[CODE_TYPE][VERSION][CODE] = (
    "^O244.*",
    "^O9981.*",
)


GDM = pd.DataFrame.from_dict(GDM, orient='index').stack().to_frame()
GDM = pd.DataFrame(GDM[0].values.tolist(), index=GDM.index)
GDM = pd.DataFrame(GDM[CODE].values.tolist(),
                   index=GDM.index).stack().reset_index().drop('level_2', axis=1)

GDM.columns = ['code_type', 'version', 'code']
