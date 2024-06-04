"""
Copyright (C) 2023 Dave Walsh

Source material codes have been translated into regex.
They include the top-level CODE where feasible to account for
idiosyncracies in different secondary data sources.

Codes are sourced from:
Bateman BT, Mhyre JM, Hernandez-Diaz S, Huybrechts KF, Fischer MA,
    Creanga AA, Callaghan WM, Gagne JJ. Development of a comorbidity index
    for use in obstetric patients. Obstet Gynecol. 2013 Nov;122(5):957-965.
    doi: 10.1097/AOG.0b013e3182a603bb. PMID: 24104771; PMCID: PMC3829199.
"""

import pandas as pd

VERSION = 'ICD9'

# ======================
# Pulmonary hypertension
# ======================
PULM_HT = dict()
PULM_HT[VERSION] = (
    "416[0,8,9].*",
)

# ======================
# Placenta previa
# ======================
PLACENTA_PREV = dict()
PLACENTA_PREV[VERSION] = (
    "641[0,1].*",
)

# ======================
# Sickle cell
# ======================
SICKLE_CELL = dict()
SICKLE_CELL[VERSION] = (
    "282[4,6].*",
)

# ======================
# Gestational hypertension
# ======================
GEST_HT = dict()
GEST_HT[VERSION] = (
    "6423.*",
)

# ======================
# Mild preeclampsia or unspecified preeclampsia
# ======================
MILD_PE = dict()
MILD_PE[VERSION] = (
    "642[4,7].*",
)

# ======================
# Severe preeclampsia / ECLAMPSIA
# ======================
ECLAMPSIA = dict()
ECLAMPSIA[VERSION] = (
    "642[5,6].*",
)

# ======================
# Chronic RENAL disease
# ======================
RENAL_DISEASE = dict()
RENAL_DISEASE[VERSION] = (
    "58[1-3,5,7,8].*",
    "6462.*",
)

# ======================
# Preexisting hypertension
# ======================
HYPERTENSION = dict()
HYPERTENSION[VERSION] = (
    "40[1-5].*",
    "642[0-2,7].*",
)

# ======================
# Chronic ischemic heart disease
# ======================
ISCHEMIC_HD = dict()
ISCHEMIC_HD[VERSION] = (
    "41[2-4].*",
)

# ======================
# Congenital heart disease
# ======================
CONGENITAL_HD = dict()
CONGENITAL_HD[VERSION] = (
    "74([5-6]|7[0-4]).*",
)

# ======================
# Systemic lupus erythematosus
# ======================
LUPUS = dict()
LUPUS[VERSION] = (
    "7100.*",
)

# ======================
# Human immunodeficiency virus
# ======================
HIV = dict()
HIV[VERSION] = (
    "042.*",
    "V08.*",
)

# ======================
# Multiple gestation
# ======================
MULTIPLE_GEST = dict()
MULTIPLE_GEST[VERSION] = (
    "V27[2-8].*",
    "651.*",
)

# ======================
# Drug abuse
# ======================
DRUG_ABUSE = dict()
DRUG_ABUSE[VERSION] = (
    "30(4|5[2-9]).*",
    "6483.*",
)

# ======================
# Alcohol abuse
# ======================
ALCOHOL_ABUSE = dict()
ALCOHOL_ABUSE[VERSION] = (
    "291.*",
    "30(3|50).*",
)

# ======================
# Tobacco abuse
# ======================
TOBACCO_ABUSE = dict()
TOBACCO_ABUSE[VERSION] = (
    "3051.*",
    "6490.*",
)

# ======================
# Cardiac valvular disease
# ======================
CARD_VALV = dict()
CARD_VALV[VERSION] = (
    "39[4-7].*",
    "424.*",
)

# ======================
# Chronic congestive heart failure
# ======================
CONGESTIVE_HF = dict()
CONGESTIVE_HF[VERSION] = (
    "428[2-4][2-3].*",
)

# ======================
# Asthma
# ======================
ASTHMA = dict()
ASTHMA[VERSION] = (
    "493.*",
)

# ======================
# Preexisting diabetes mellitus
# ======================
DIABETES = dict()
DIABETES[VERSION] = (
    "250.*",
    "6480.*",
)

# ======================
# Gestational diabetes mellitus
# ======================
GEST_DM = dict()
GEST_DM[VERSION] = (
    "6488.*",
)

# ======================
# Obesity
# ======================
OBESITY = dict()
OBESITY[VERSION] = (
    "2780.*",
    "6491.*",
    "V85[3-4].*",
)

# ======================
# Cystic fibrosis
# ======================
CYSTIC_FIBROSIS = dict()
CYSTIC_FIBROSIS[VERSION] = (
    "2770.*",
)

# ======================
# Previous cesarean delivery
# ======================
PREVIOUS_CSEC = dict()
PREVIOUS_CSEC[VERSION] = (
    "6542.*",
)

# ======================
# Convert to Pandas
# ======================
PULM_HT = pd.DataFrame.from_dict(PULM_HT, orient='index').stack().to_frame()
PULM_HT = PULM_HT.reset_index().drop('level_1', axis=1)
PULM_HT['indicator'] = 'pulmonary hypertension'

PLACENTA_PREV = pd.DataFrame.from_dict(PLACENTA_PREV, orient='index').stack().to_frame()
PLACENTA_PREV = PLACENTA_PREV.reset_index().drop('level_1', axis=1)
PLACENTA_PREV['indicator'] = 'placenta previa'

SICKLE_CELL = pd.DataFrame.from_dict(SICKLE_CELL, orient='index').stack().to_frame()
SICKLE_CELL = SICKLE_CELL.reset_index().drop('level_1', axis=1)
SICKLE_CELL['indicator'] = 'sickle cell disease'

GEST_HT = pd.DataFrame.from_dict(GEST_HT, orient='index').stack().to_frame()
GEST_HT = GEST_HT.reset_index().drop('level_1', axis=1)
GEST_HT['indicator'] = 'gestational hypertension'

MILD_PE = pd.DataFrame.from_dict(MILD_PE, orient='index').stack().to_frame()
MILD_PE = MILD_PE.reset_index().drop('level_1', axis=1)
MILD_PE['indicator'] = 'mild preeclampsia'

ECLAMPSIA = pd.DataFrame.from_dict(ECLAMPSIA, orient='index').stack().to_frame()
ECLAMPSIA = ECLAMPSIA.reset_index().drop('level_1', axis=1)
ECLAMPSIA['indicator'] = 'eclampsia'

RENAL_DISEASE = pd.DataFrame.from_dict(RENAL_DISEASE, orient='index').stack().to_frame()
RENAL_DISEASE = RENAL_DISEASE.reset_index().drop('level_1', axis=1)
RENAL_DISEASE['indicator'] = 'chronic renal disease'

HYPERTENSION = pd.DataFrame.from_dict(HYPERTENSION, orient='index').stack().to_frame()
HYPERTENSION = HYPERTENSION.reset_index().drop('level_1', axis=1)
HYPERTENSION['indicator'] = 'preexisting hypertension'

ISCHEMIC_HD = pd.DataFrame.from_dict(ISCHEMIC_HD, orient='index').stack().to_frame()
ISCHEMIC_HD = ISCHEMIC_HD.reset_index().drop('level_1', axis=1)
ISCHEMIC_HD['indicator'] = 'chronic ischemic heart disease'

CONGENITAL_HD = pd.DataFrame.from_dict(CONGENITAL_HD, orient='index').stack().to_frame()
CONGENITAL_HD = CONGENITAL_HD.reset_index().drop('level_1', axis=1)
CONGENITAL_HD['indicator'] = 'congenital heart disease'

LUPUS = pd.DataFrame.from_dict(LUPUS, orient='index').stack().to_frame()
LUPUS = LUPUS.reset_index().drop('level_1', axis=1)
LUPUS['indicator'] = 'lupus'

HIV = pd.DataFrame.from_dict(HIV, orient='index').stack().to_frame()
HIV = HIV.reset_index().drop('level_1', axis=1)
HIV['indicator'] = 'hiv'

MULTIPLE_GEST = pd.DataFrame.from_dict(MULTIPLE_GEST, orient='index').stack().to_frame()
MULTIPLE_GEST = MULTIPLE_GEST.reset_index().drop('level_1', axis=1)
MULTIPLE_GEST['indicator'] = 'multiple gestation'

DRUG_ABUSE = pd.DataFrame.from_dict(DRUG_ABUSE, orient='index').stack().to_frame()
DRUG_ABUSE = DRUG_ABUSE.reset_index().drop('level_1', axis=1)
DRUG_ABUSE['indicator'] = 'drug abuse'

ALCOHOL_ABUSE = pd.DataFrame.from_dict(ALCOHOL_ABUSE, orient='index').stack().to_frame()
ALCOHOL_ABUSE = ALCOHOL_ABUSE.reset_index().drop('level_1', axis=1)
ALCOHOL_ABUSE['indicator'] = 'alcohol abuse'

TOBACCO_ABUSE = pd.DataFrame.from_dict(TOBACCO_ABUSE, orient='index').stack().to_frame()
TOBACCO_ABUSE = TOBACCO_ABUSE.reset_index().drop('level_1', axis=1)
TOBACCO_ABUSE['indicator'] = 'tobacco use'

CARD_VALV = pd.DataFrame.from_dict(CARD_VALV, orient='index').stack().to_frame()
CARD_VALV = CARD_VALV.reset_index().drop('level_1', axis=1)
CARD_VALV['indicator'] = 'cardiac valvular disease'

CONGESTIVE_HF = pd.DataFrame.from_dict(CONGESTIVE_HF, orient='index').stack().to_frame()
CONGESTIVE_HF = CONGESTIVE_HF.reset_index().drop('level_1', axis=1)
CONGESTIVE_HF['indicator'] = 'chronic congestive heart failure'

ASTHMA = pd.DataFrame.from_dict(ASTHMA, orient='index').stack().to_frame()
ASTHMA = ASTHMA.reset_index().drop('level_1', axis=1)
ASTHMA['indicator'] = 'asthma'

DIABETES = pd.DataFrame.from_dict(DIABETES, orient='index').stack().to_frame()
DIABETES = DIABETES.reset_index().drop('level_1', axis=1)
DIABETES['indicator'] = 'preexisting diabetes'

GEST_DM = pd.DataFrame.from_dict(GEST_DM, orient='index').stack().to_frame()
GEST_DM = GEST_DM.reset_index().drop('level_1', axis=1)
GEST_DM['indicator'] = 'gestational diabetes'

OBESITY = pd.DataFrame.from_dict(OBESITY, orient='index').stack().to_frame()
OBESITY = OBESITY.reset_index().drop('level_1', axis=1)
OBESITY['indicator'] = 'obesity'

CYSTIC_FIBROSIS = pd.DataFrame.from_dict(CYSTIC_FIBROSIS, orient='index').stack().to_frame()
CYSTIC_FIBROSIS = CYSTIC_FIBROSIS.reset_index().drop('level_1', axis=1)
CYSTIC_FIBROSIS['indicator'] = 'cystic fibrosis'

PREVIOUS_CSEC = pd.DataFrame.from_dict(PREVIOUS_CSEC, orient='index').stack().to_frame()
PREVIOUS_CSEC = PREVIOUS_CSEC.reset_index().drop('level_1', axis=1)
PREVIOUS_CSEC['indicator'] = 'previous cesarean'


SCORE_COLUMNS = ['version', 'code', 'indicator']
PULM_HT.columns = SCORE_COLUMNS
PLACENTA_PREV.columns = SCORE_COLUMNS
SICKLE_CELL.columns = SCORE_COLUMNS
GEST_HT.columns = SCORE_COLUMNS
MILD_PE.columns = SCORE_COLUMNS
ECLAMPSIA.columns = SCORE_COLUMNS
RENAL_DISEASE.columns = SCORE_COLUMNS
HYPERTENSION.columns = SCORE_COLUMNS
ISCHEMIC_HD.columns = SCORE_COLUMNS
CONGENITAL_HD.columns = SCORE_COLUMNS
LUPUS.columns = SCORE_COLUMNS
HIV.columns = SCORE_COLUMNS
MULTIPLE_GEST.columns = SCORE_COLUMNS
DRUG_ABUSE.columns = SCORE_COLUMNS
ALCOHOL_ABUSE.columns = SCORE_COLUMNS
TOBACCO_ABUSE.columns = SCORE_COLUMNS
CARD_VALV.columns = SCORE_COLUMNS
CONGESTIVE_HF.columns = SCORE_COLUMNS
ASTHMA.columns = SCORE_COLUMNS
DIABETES.columns = SCORE_COLUMNS
GEST_DM.columns = SCORE_COLUMNS
OBESITY.columns = SCORE_COLUMNS
CYSTIC_FIBROSIS.columns = SCORE_COLUMNS
PREVIOUS_CSEC.columns = SCORE_COLUMNS

AGE_CATEGORY = ['<35',
                '35-39',
                '40-44',
                '>44']

WEIGHTS = {PULM_HT['indicator'][0]: 4,
           PLACENTA_PREV['indicator'][0]: 2,
           SICKLE_CELL['indicator'][0]: 3,
           GEST_HT['indicator'][0]: 1,
           MILD_PE['indicator'][0]: 2,
           ECLAMPSIA['indicator'][0]: 5,
           RENAL_DISEASE['indicator'][0]: 1,
           HYPERTENSION['indicator'][0]: 1,
           ISCHEMIC_HD['indicator'][0]: 3,
           CONGENITAL_HD['indicator'][0]: 4,
           LUPUS['indicator'][0]: 2,
           HIV['indicator'][0]: 2,
           MULTIPLE_GEST['indicator'][0]: 2,
           DRUG_ABUSE['indicator'][0]: 2,
           ALCOHOL_ABUSE['indicator'][0]: 1,
           TOBACCO_ABUSE['indicator'][0]: 0,
           CARD_VALV['indicator'][0]: 2,
           CONGESTIVE_HF['indicator'][0]: 5,
           ASTHMA['indicator'][0]: 1,
           DIABETES['indicator'][0]: 1,
           GEST_DM['indicator'][0]: 0,
           OBESITY['indicator'][0]: 0,
           CYSTIC_FIBROSIS['indicator'][0]: 0,
           PREVIOUS_CSEC['indicator'][0]: 1,
           AGE_CATEGORY[1]: 1,
           AGE_CATEGORY[2]: 2,
           AGE_CATEGORY[3]: 3,
           }

WEIGHTS = pd.DataFrame.from_dict(WEIGHTS, orient='index', columns=['weight'])

BATEMAN_MAP = pd.concat([
    PULM_HT,
    PLACENTA_PREV,
    SICKLE_CELL,
    GEST_HT,
    MILD_PE,
    ECLAMPSIA,
    RENAL_DISEASE,
    HYPERTENSION,
    ISCHEMIC_HD,
    CONGENITAL_HD,
    LUPUS,
    HIV,
    MULTIPLE_GEST,
    DRUG_ABUSE,
    ALCOHOL_ABUSE,
    TOBACCO_ABUSE,
    CARD_VALV,
    CONGESTIVE_HF,
    ASTHMA,
    DIABETES,
    GEST_DM,
    OBESITY,
    CYSTIC_FIBROSIS,
    PREVIOUS_CSEC
])

BATEMAN_MAP = BATEMAN_MAP.merge(WEIGHTS,
                                how='right',
                                left_on='indicator',
                                right_index=True)
