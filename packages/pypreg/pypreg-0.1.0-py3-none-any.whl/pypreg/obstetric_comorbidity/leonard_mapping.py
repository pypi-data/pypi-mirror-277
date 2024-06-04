"""
Copyright (C) 2023 Dave Walsh

Source material codes have been translated into regex.
They include the top-level CODE where feasible to account for
idiosyncracies in different secondary data sources.

Codes are sourced from:
Leonard SA, Kennedy CJ, Carmichael SL, Lyell DJ, Main EK.
    An Expanded Obstetric Comorbidity Scoring System for
    Predicting Severe Maternal Morbidity. Obstet Gynecol.
    2020 Sep;136(3):440-449. doi: 10.1097/AOG.0000000000004022.
    PMID: 32769656; PMCID: PMC7523732.
"""

import pandas as pd

VERSION = 'ICD10'

# ======================
# Gestational diabetes
# ======================
GEST_DM = dict()
GEST_DM[VERSION] = (
    "O244.*",
)

# ======================
# HIV / AIDS
# ======================
HIV = dict()
HIV[VERSION] = (
    "O987.*",
    "B20",
)

# ======================
# Preexisting diabetes mellitus
# ======================
DIABETES = dict()
DIABETES[VERSION] = (
    "E(0[8-9]|1[0,1,3]).*",
    "O24[0,1,3,8,9].*",
    "Z794.*",
)

# ======================
# Previous cesarean birth
# ======================
CESAREAN = dict()
CESAREAN[VERSION] = (
    "O3421.*",
)

# ======================
# Pulmonary hypertension
# ======================
PULM_HT = dict()
PULM_HT[VERSION] = (
    "I27[0,2].*",
)

# ======================
# Twin/multiple pregnancy
# ======================
MULTIPLE_GEST = dict()
MULTIPLE_GEST[VERSION] = (
    "O3[0-1].*",
    "Z37[2-7].*",
)

# ======================
# Asthma
# ======================
ASTHMA = dict()
ASTHMA[VERSION] = (
    "O995.*",
    "J45([2-3][1-2]|[4-5]|90[1-2]).*",
)

# ======================
# Bleeding disorder
# ======================
BLEEDING = dict()
BLEEDING[VERSION] = (
    "D6[6-9].*",
)

# ======================
# Obesity
# ======================
OBESITY = dict()
OBESITY[VERSION] = (
    "Z684.*",
)

# ======================
# Cardiac disease
# ======================
CARDIAC_DISEASE = dict()
CARDIAC_DISEASE[VERSION] = (
    "I(0[5-9]|1[1-3,5,6]|2[0,5]|278|3[0-9]|4[1,4-9]|50[2-4][2-3]|5081[2-3]).*",
    "O994[1-2].*",
    "Q2[0-4].*",
)

# ======================
# Chronic hypertension
# ======================
HYPERTENSION = dict()
HYPERTENSION[VERSION] = (
    "O1[0-1].*",
    "I10.*",
)

# ======================
# Chronic RENAL disease
# ======================
RENAL = dict()
RENAL[VERSION] = (
    "O2683.*",
    "I1[2-3].*",
    "N(0[3-5,7,8]|11[1,8,9]|18|25[0-1,9]|258[1,9]|269).*",
)

# ======================
# Connective tissue or autoimmune disease
# ======================
AUTOIMMUNE = dict()
AUTOIMMUNE[VERSION] = (
    "M3[0-6].*",
)

# ======================
# Placenta previa
# ======================
PLACENTA_PREVIA = dict()
PLACENTA_PREVIA[VERSION] = (
    "O44[0-3]3",
)

# ======================
# Preeclampsia
# ======================
PREECLAMPSIA = dict()
PREECLAMPSIA[VERSION] = (
    "O1(1|4[1-2]).*",
)

# ======================
# Mild preeclampsia
# ======================
MILD_PREECLAMPSIA = dict()
MILD_PREECLAMPSIA[VERSION] = (
    "O1(3|4[0,9]).*",
)

# ======================
# Substance use disorder
# ======================
SUBSTANCE_USE = dict()
SUBSTANCE_USE[VERSION] = (
    "F1[0-9].*",
    "O993[1-2].*",
)

# ======================
# Anemia
# ======================
ANEMIA = dict()
ANEMIA[VERSION] = (
    "O990[1-2].*",
    "D5([0,5,6,8,9]|7[1,3]|7[2,4,8]0).*",
)

# ======================
# Bariatric surgery
# ======================
BARIATRIC = dict()
BARIATRIC[VERSION] = (
    "O9984.*",
)

# ======================
# Gastrointestinal disease
# ======================
GI_DISEASE = dict()
GI_DISEASE[VERSION] = (
    "K.*",
    "O996.*",
    "O266.*"
)

# ======================
# Mental health disorder
# ======================
MENTAL_HEALTH = dict()
MENTAL_HEALTH[VERSION] = (
    "O9934.*",
    "F[2-3][0-9].*",
)

# ======================
# Neuromuscular disease
# ======================
NEUROMUSCULAR = dict()
NEUROMUSCULAR[VERSION] = (
    "O9935.*",
    "G[4,7]0.*",
)

# ======================
# Placental abruption
# ======================
ABRUPTION = dict()
ABRUPTION[VERSION] = (
    "O45.*",
)

# ======================
# Placental accreta spectrum
# ======================
ACCRETA = dict()
ACCRETA[VERSION] = (
    "O432.*",
)

# ======================
# Preterm birth
# ======================
PRETERM = dict()
PRETERM[VERSION] = (
    "Z3A(2[0-9]|3[0-6]).*",
)

# ======================
# Thyrotoxicosis
# ======================
THYROTOXICOSIS = dict()
THYROTOXICOSIS[VERSION] = (
    "E05.*",
)

# ======================
# Convert to Pandas
# ======================
GEST_DM = pd.DataFrame.from_dict(GEST_DM, orient='index').stack().to_frame()
GEST_DM = GEST_DM.reset_index().drop('level_1', axis=1)
GEST_DM['indicator'] = 'gestational diabetes'

HIV = pd.DataFrame.from_dict(HIV, orient='index').stack().to_frame()
HIV = HIV.reset_index().drop('level_1', axis=1)
HIV['indicator'] = 'hiv'

DIABETES = pd.DataFrame.from_dict(DIABETES, orient='index').stack().to_frame()
DIABETES = DIABETES.reset_index().drop('level_1', axis=1)
DIABETES['indicator'] = 'preexisting diabetes'

CESAREAN = pd.DataFrame.from_dict(CESAREAN, orient='index').stack().to_frame()
CESAREAN = CESAREAN.reset_index().drop('level_1', axis=1)
CESAREAN['indicator'] = 'previous cesarean'

PULM_HT = pd.DataFrame.from_dict(PULM_HT, orient='index').stack().to_frame()
PULM_HT = PULM_HT.reset_index().drop('level_1', axis=1)
PULM_HT['indicator'] = 'pulmonary hypertension'

MULTIPLE_GEST = pd.DataFrame.from_dict(MULTIPLE_GEST, orient='index').stack().to_frame()
MULTIPLE_GEST = MULTIPLE_GEST.reset_index().drop('level_1', axis=1)
MULTIPLE_GEST['indicator'] = 'multiple gestation'

ASTHMA = pd.DataFrame.from_dict(ASTHMA, orient='index').stack().to_frame()
ASTHMA = ASTHMA.reset_index().drop('level_1', axis=1)
ASTHMA['indicator'] = 'asthma'

BLEEDING = pd.DataFrame.from_dict(BLEEDING, orient='index').stack().to_frame()
BLEEDING = BLEEDING.reset_index().drop('level_1', axis=1)
BLEEDING['indicator'] = 'bleeding disorder'

OBESITY = pd.DataFrame.from_dict(OBESITY, orient='index').stack().to_frame()
OBESITY = OBESITY.reset_index().drop('level_1', axis=1)
OBESITY['indicator'] = 'obesity'

CARDIAC_DISEASE = pd.DataFrame.from_dict(CARDIAC_DISEASE, orient='index').stack().to_frame()
CARDIAC_DISEASE = CARDIAC_DISEASE.reset_index().drop('level_1', axis=1)
CARDIAC_DISEASE['indicator'] = 'cardiac disease'

HYPERTENSION = pd.DataFrame.from_dict(HYPERTENSION, orient='index').stack().to_frame()
HYPERTENSION = HYPERTENSION.reset_index().drop('level_1', axis=1)
HYPERTENSION['indicator'] = 'chronic hypertension'

RENAL = pd.DataFrame.from_dict(RENAL, orient='index').stack().to_frame()
RENAL = RENAL.reset_index().drop('level_1', axis=1)
RENAL['indicator'] = 'renal disease'

AUTOIMMUNE = pd.DataFrame.from_dict(AUTOIMMUNE, orient='index').stack().to_frame()
AUTOIMMUNE = AUTOIMMUNE.reset_index().drop('level_1', axis=1)
AUTOIMMUNE['indicator'] = 'autoimmune disease'

PLACENTA_PREVIA = pd.DataFrame.from_dict(PLACENTA_PREVIA, orient='index').stack().to_frame()
PLACENTA_PREVIA = PLACENTA_PREVIA.reset_index().drop('level_1', axis=1)
PLACENTA_PREVIA['indicator'] = 'placenta previa'

PREECLAMPSIA = pd.DataFrame.from_dict(PREECLAMPSIA, orient='index').stack().to_frame()
PREECLAMPSIA = PREECLAMPSIA.reset_index().drop('level_1', axis=1)
PREECLAMPSIA['indicator'] = 'preeclampsia'

MILD_PREECLAMPSIA = pd.DataFrame.from_dict(MILD_PREECLAMPSIA, orient='index').stack().to_frame()
MILD_PREECLAMPSIA = MILD_PREECLAMPSIA.reset_index().drop('level_1', axis=1)
MILD_PREECLAMPSIA['indicator'] = 'mild preeclampsia'

SUBSTANCE_USE = pd.DataFrame.from_dict(SUBSTANCE_USE, orient='index').stack().to_frame()
SUBSTANCE_USE = SUBSTANCE_USE.reset_index().drop('level_1', axis=1)
SUBSTANCE_USE['indicator'] = 'substance use disorder'

ANEMIA = pd.DataFrame.from_dict(ANEMIA, orient='index').stack().to_frame()
ANEMIA = ANEMIA.reset_index().drop('level_1', axis=1)
ANEMIA['indicator'] = 'anemia'

BARIATRIC = pd.DataFrame.from_dict(BARIATRIC, orient='index').stack().to_frame()
BARIATRIC = BARIATRIC.reset_index().drop('level_1', axis=1)
BARIATRIC['indicator'] = 'bariatric surgery'

GI_DISEASE = pd.DataFrame.from_dict(GI_DISEASE, orient='index').stack().to_frame()
GI_DISEASE = GI_DISEASE.reset_index().drop('level_1', axis=1)
GI_DISEASE['indicator'] = 'gastrointestinal disease'

MENTAL_HEALTH = pd.DataFrame.from_dict(MENTAL_HEALTH, orient='index').stack().to_frame()
MENTAL_HEALTH = MENTAL_HEALTH.reset_index().drop('level_1', axis=1)
MENTAL_HEALTH['indicator'] = 'mental health disorder'

NEUROMUSCULAR = pd.DataFrame.from_dict(NEUROMUSCULAR, orient='index').stack().to_frame()
NEUROMUSCULAR = NEUROMUSCULAR.reset_index().drop('level_1', axis=1)
NEUROMUSCULAR['indicator'] = 'neuromuscular disease'

ABRUPTION = pd.DataFrame.from_dict(ABRUPTION, orient='index').stack().to_frame()
ABRUPTION = ABRUPTION.reset_index().drop('level_1', axis=1)
ABRUPTION['indicator'] = 'placental abruption'

ACCRETA = pd.DataFrame.from_dict(ACCRETA, orient='index').stack().to_frame()
ACCRETA = ACCRETA.reset_index().drop('level_1', axis=1)
ACCRETA['indicator'] = 'placenta accreta spectrum'

PRETERM = pd.DataFrame.from_dict(PRETERM, orient='index').stack().to_frame()
PRETERM = PRETERM.reset_index().drop('level_1', axis=1)
PRETERM['indicator'] = 'preterm birth'

THYROTOXICOSIS = pd.DataFrame.from_dict(THYROTOXICOSIS, orient='index').stack().to_frame()
THYROTOXICOSIS = THYROTOXICOSIS.reset_index().drop('level_1', axis=1)
THYROTOXICOSIS['indicator'] = 'thyrotoxicosis'

# Fix column names
SCORE_COLUMNS = ['version', 'code', 'indicator']
GEST_DM.columns = SCORE_COLUMNS
HIV.columns = SCORE_COLUMNS
DIABETES.columns = SCORE_COLUMNS
CESAREAN.columns = SCORE_COLUMNS
PULM_HT.columns = SCORE_COLUMNS
MULTIPLE_GEST.columns = SCORE_COLUMNS
ASTHMA.columns = SCORE_COLUMNS
BLEEDING.columns = SCORE_COLUMNS
OBESITY.columns = SCORE_COLUMNS
CARDIAC_DISEASE.columns = SCORE_COLUMNS
HYPERTENSION.columns = SCORE_COLUMNS
RENAL.columns = SCORE_COLUMNS
AUTOIMMUNE.columns = SCORE_COLUMNS
PLACENTA_PREVIA.columns = SCORE_COLUMNS
PREECLAMPSIA.columns = SCORE_COLUMNS
MILD_PREECLAMPSIA.columns = SCORE_COLUMNS
SUBSTANCE_USE.columns = SCORE_COLUMNS
ANEMIA.columns = SCORE_COLUMNS
BARIATRIC.columns = SCORE_COLUMNS
GI_DISEASE.columns = SCORE_COLUMNS
MENTAL_HEALTH.columns = SCORE_COLUMNS
NEUROMUSCULAR.columns = SCORE_COLUMNS
ABRUPTION.columns = SCORE_COLUMNS
ACCRETA.columns = SCORE_COLUMNS
PRETERM.columns = SCORE_COLUMNS
THYROTOXICOSIS.columns = SCORE_COLUMNS

# Add an age category to the map
AGE_CATEGORY = ['<35', '>=35']

# Assign weights for each condition for SMM and non-TRANSFUSION SMM
WEIGHTS = {GEST_DM['indicator'][0]: (1, 1),
           HIV['indicator'][0]: (30, 13),
           DIABETES['indicator'][0]: (9, 6),
           CESAREAN['indicator'][0]: (4, 0),
           PULM_HT['indicator'][0]: (50, 32),
           MULTIPLE_GEST['indicator'][0]: (20, 8),
           ASTHMA['indicator'][0]: (11, 9),
           BLEEDING['indicator'][0]: (34, 23),
           OBESITY['indicator'][0]: (5, 4),
           CARDIAC_DISEASE['indicator'][0]: (31, 22),
           HYPERTENSION['indicator'][0]: (10, 7),
           RENAL['indicator'][0]: (38, 26),
           AUTOIMMUNE['indicator'][0]: (10, 7),
           PLACENTA_PREVIA['indicator'][0]: (27, 13),
           PREECLAMPSIA['indicator'][0]: (26, 16),
           MILD_PREECLAMPSIA['indicator'][0]: (11, 6),
           SUBSTANCE_USE['indicator'][0]: (10, 5),
           ANEMIA['indicator'][0]: (20, 7),
           BARIATRIC['indicator'][0]: (0, 0),
           GI_DISEASE['indicator'][0]: (12, 8),
           MENTAL_HEALTH['indicator'][0]: (7, 4),
           NEUROMUSCULAR['indicator'][0]: (9, 8),
           ABRUPTION['indicator'][0]: (18, 7),
           ACCRETA['indicator'][0]: (59, 36),
           PRETERM['indicator'][0]: (18, 12),
           THYROTOXICOSIS['indicator'][0]: (6, 0),
           AGE_CATEGORY[1]: (2, 1)
           }

WEIGHTS = pd.DataFrame.from_dict(WEIGHTS,
                                 orient='index',
                                 columns=['smm score', 'non-transfusion smm score'])

# Consolidate the map
LEONARD_MAP = pd.concat([
    GEST_DM,
    HIV,
    DIABETES,
    CESAREAN,
    PULM_HT,
    MULTIPLE_GEST,
    ASTHMA,
    BLEEDING,
    OBESITY,
    CARDIAC_DISEASE,
    HYPERTENSION,
    RENAL,
    AUTOIMMUNE,
    PLACENTA_PREVIA,
    PREECLAMPSIA,
    MILD_PREECLAMPSIA,
    SUBSTANCE_USE,
    ANEMIA,
    BARIATRIC,
    GI_DISEASE,
    MENTAL_HEALTH,
    NEUROMUSCULAR,
    ABRUPTION,
    ACCRETA,
    PRETERM,
    THYROTOXICOSIS,
])

# Attach weights to the codes
LEONARD_MAP = LEONARD_MAP.merge(WEIGHTS,
                                how='right',
                                left_on='indicator',
                                right_index=True)
