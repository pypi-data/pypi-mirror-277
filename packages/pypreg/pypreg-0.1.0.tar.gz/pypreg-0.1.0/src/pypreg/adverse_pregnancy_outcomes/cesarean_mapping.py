"""
Copyright (C) 2023 Dave Walsh

Codes sourced from:

Agency for Healthcare Research and Quality:
https://qualityindicators.ahrq.gov/Downloads/Modules/IQI/V50-ICD10/TechSpecs/IQI%2021%20Cesarean%20Delivery%20Rate,%20Uncomplicated.pdf

Castillo, Wendy Camelo / Boggess, Kim / Stürmer, Til / Brookhart, M. Alan /
    Benjamin, Daniel K. / Funk, Michele Jonsson. Trends in Glyburide Compared
    With Insulin Use for Gestational Diabetes Treatment in the United States, 2000-2011
    Obstetrics & Gynecology , Vol. 123, No. 6 Ovid Technologies (Wolters Kluwer Health) p. 1177-1184

And code search using keyword "cesar" and including any procedure
which indicates cesarean was performed
"""

import pandas as pd

CESAREAN = dict()

CODE_TYPE = 'PX'
VERSION = 'ICD9'
CODE = 'code'

CESAREAN[CODE_TYPE] = dict()
CESAREAN[CODE_TYPE][VERSION] = dict()
CESAREAN[CODE_TYPE][VERSION][CODE] = (
    #74.9 excluded as child CODE should be used (could also describe hysterotomy 74.91
    "^74([0-24]|99)$",
)

VERSION = 'ICD10'
CESAREAN[CODE_TYPE][VERSION] = dict()
CESAREAN[CODE_TYPE][VERSION][CODE] = (
    "^10D00Z[0-2]$",
)

VERSION = 'CPT4'
CESAREAN[CODE_TYPE][VERSION] = dict()
CESAREAN[CODE_TYPE][VERSION][CODE] = (
    "^00857$",
    "^58611$",
    "^5950[01]$",
    "^5951[0-5]$",
    "^5952[015]$",
    "^5954[01]$",
    "^59618$",
    "^5962[02]$",
    "^0196[1389]$",
)

CODE_TYPE = 'DX'
CESAREAN[CODE_TYPE] = dict()
VERSION = 'ICD9'
CESAREAN[CODE_TYPE][VERSION] = dict()
CESAREAN[CODE_TYPE][VERSION][CODE] = (
    "^6498.*",
    "^6697.*",
    "^6741.*",
    "^V3[0-79]01$",
    "^7634$",
)

VERSION = 'ICD10'
CESAREAN[CODE_TYPE][VERSION] = dict()
CESAREAN[CODE_TYPE][VERSION][CODE] = (
    "^O82$",
    "^O7582$",
    "^Z38([03]1|6[2469])$",
    "^O900$",
    "^P034$",
)

CODE_TYPE = 'DRG'
CESAREAN[CODE_TYPE] = dict()
VERSION = 'DRG'
CESAREAN[CODE_TYPE][VERSION] = dict()
CESAREAN[CODE_TYPE][VERSION][CODE] = (
    "^37[01]$",
    "^76[56]$",
)

CESAREAN = pd.DataFrame.from_dict(CESAREAN, orient='index').stack().to_frame()
CESAREAN = pd.DataFrame(CESAREAN[0].values.tolist(), index=CESAREAN.index)
CESAREAN = pd.DataFrame(CESAREAN[CODE].values.tolist(),
                        index=CESAREAN.index).stack().reset_index().drop('level_2',
                                                                         axis=1)

CESAREAN.columns = ['code_type', 'version', 'code']
