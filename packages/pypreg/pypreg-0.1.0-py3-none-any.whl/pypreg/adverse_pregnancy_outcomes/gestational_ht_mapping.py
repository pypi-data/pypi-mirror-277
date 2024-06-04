"""
Copyright (C) 2023 Dave Walsh

Codes sourced from

Bateman BT, Mhyre JM, Hernandez-Diaz S, Huybrechts KF, Fischer MA,
    Creanga AA, Callaghan WM, Gagne JJ. Development of a comorbidity
    index for use in obstetric patients. Obstet Gynecol. 2013 Nov;122(5):957-965.
    doi: 10.1097/AOG.0b013e3182a603bb. PMID: 24104771; PMCID: PMC3829199
Leonard SA, Kennedy CJ, Carmichael SL, Lyell DJ, Main EK.
    An Expanded Obstetric Comorbidity Scoring System for
    Predicting Severe Maternal Morbidity. Obstet Gynecol.
    2020 Sep;136(3):440-449. doi: 10.1097/AOG.0000000000004022.
    PMID: 32769656; PMCID: PMC7523732
"""

import pandas as pd

GHT = dict()

CODE_TYPE = 'DX'
VERSION = 'ICD9'
CODE = 'code'

GHT[CODE_TYPE] = dict()
GHT[CODE_TYPE][VERSION] = dict()
GHT[CODE_TYPE][VERSION][CODE] = (
    "^6423.*",
)

VERSION = 'ICD10'
GHT[CODE_TYPE][VERSION] = dict()
GHT[CODE_TYPE][VERSION][CODE] = (
    "^O13.*",
)


GHT = pd.DataFrame.from_dict(GHT, orient='index').stack().to_frame()
GHT = pd.DataFrame(GHT[0].values.tolist(), index=GHT.index)
GHT = pd.DataFrame(GHT[CODE].values.tolist(),
                   index=GHT.index).stack().reset_index().drop('level_2', axis=1)

GHT.columns = ['code_type', 'version', 'code']
