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

PE = dict()

CODE_TYPE = 'DX'
VERSION = 'ICD9'
CODE = 'code'

PE[CODE_TYPE] = dict()
PE[CODE_TYPE][VERSION] = dict()
PE[CODE_TYPE][VERSION][CODE] = (
    "^642[4-7].*",
)

VERSION = 'ICD10'
PE[CODE_TYPE][VERSION] = dict()
PE[CODE_TYPE][VERSION][CODE] = (
    "^O1[145].*",
)


PE = pd.DataFrame.from_dict(PE, orient='index').stack().to_frame()
PE = pd.DataFrame(PE[0].values.tolist(), index=PE.index)
PE = pd.DataFrame(PE[CODE].values.tolist(),
                  index=PE.index).stack().reset_index().drop('level_2', axis=1)

PE.columns = ['code_type', 'version', 'code']
