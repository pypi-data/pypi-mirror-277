"""
Copyright (C) 2023 Dave Walsh

Codes identified through code search of ICD-10 and crosswalk to ICD-9
"""

import pandas as pd

FG = dict()

CODE_TYPE = 'DX'
VERSION = 'ICD9'
CODE = 'code'

FG[CODE_TYPE] = dict()
FG[CODE_TYPE][VERSION] = dict()
FG[CODE_TYPE][VERSION][CODE] = (
    "^6565.*",
)

VERSION = 'ICD10'
FG[CODE_TYPE][VERSION] = dict()
FG[CODE_TYPE][VERSION][CODE] = (
    "^O3659.*",
)


FG = pd.DataFrame.from_dict(FG, orient='index').stack().to_frame()
FG = pd.DataFrame(FG[0].values.tolist(), index=FG.index)
FG = pd.DataFrame(FG[CODE].values.tolist(),
                  index=FG.index).stack().reset_index().drop('level_2', axis=1)

FG.columns = ['code_type', 'version', 'code']
