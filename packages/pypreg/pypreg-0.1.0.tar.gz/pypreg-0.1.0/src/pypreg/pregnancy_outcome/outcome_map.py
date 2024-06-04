"""
Source material codes have been translated into regex and crosswalked to ICD-9 by David Walsh.
They include the top-level CODE to account for idiosyncracies in different secondary data sources.

Copyright (C) 2023 Dave Walsh

Original codes are sourced from:
    Moll K FK Wong H-L. Task order HHSF22301001T: Pregnancy OUTCOMES
validation final report. U.S. Food; Drug Administration; 2020. Available at:
https://www.bestinitiative.org/wp-content/uploads/2020/08/Validating_
Pregnancy_Outcomes_Linked_Database_Report_2020-1.pdf

Crosswalked codes are retrieved via General Equivalence Mappings.
ICD10 codes are mapped back to ICD9, and ICD9 codes are mapped forward
to ICD10. The resulting codes were reviewed and kept if they are related
to an obstetric outcome, and if the original ICD10 CODE broadly refers
to labor and DELIVERY, then the mapped codes may also.

Expanded codes were added based upon a review of ICD9 and ICD10 codes
for other obstetric OUTCOMES not captured, specifically the delivered
episode of care codes contained in ICD9.
"""

import pandas as pd

PROCEDURE = 'PX'
DIAGNOSIS = 'DX'
ICD9 = 'ICD9'
ICD10 = 'ICD10'
CPT = 'CPT'
DRG = 'DRG'
MOLL = 'MOLL'
CROSSWALK = 'CROSSWALK'
EXPANDED = 'EXPANDED'
OUTCOME_LIST = ['LIVE_BIRTH',
                'STILLBIRTH',
                'DELIVERY',
                'TROPHOBLASTIC',
                'ECTOPIC',
                'THERAPEUTIC_ABORTION',
                'SPONTANEOUS_ABORTION']
OUTCOME_COL = 'outcome'

# ======================
# Ectopic
# ======================
ECTOPIC = dict()
ECTOPIC[DIAGNOSIS] = dict()
ECTOPIC[DIAGNOSIS][ICD10] = dict()
ECTOPIC[DIAGNOSIS][ICD10][MOLL] = (
    r"^O0[08].*",
)

ECTOPIC[DIAGNOSIS][ICD9] = dict()
ECTOPIC[DIAGNOSIS][ICD9][CROSSWALK] = (
    r"^633.*",
)

ECTOPIC[PROCEDURE] = dict()
ECTOPIC[PROCEDURE][ICD9] = dict()
ECTOPIC[PROCEDURE][ICD9][CROSSWALK] = (
    r"^743$",
    r"^66[06]2$",
)

ECTOPIC[PROCEDURE][ICD10] = dict()
ECTOPIC[PROCEDURE][ICD10][MOLL] = (
    r"^10(D2[78]|T2[03478])ZZ$",
)

ECTOPIC[PROCEDURE][CPT] = dict()
ECTOPIC[PROCEDURE][CPT][MOLL] = (
    r"^591([04]0|[25][01]|3[056])$",
)

ECTOPIC[DRG] = dict()
ECTOPIC[DRG][DRG] = dict()
ECTOPIC[DRG][DRG][MOLL] = (
    r"^777$",
)

ECTOPIC[DRG][DRG][EXPANDED] = (
    r"^378$",
)

# ======================
# Trophoblastic
# ======================
TROPHOBLASTIC = dict()
TROPHOBLASTIC[DIAGNOSIS] = dict()
TROPHOBLASTIC[DIAGNOSIS][ICD10] = dict()
TROPHOBLASTIC[DIAGNOSIS][ICD10][MOLL] = (
    r"^O0(1|2([09]|89)).*",
)

TROPHOBLASTIC[DIAGNOSIS][ICD9] = dict()
TROPHOBLASTIC[DIAGNOSIS][ICD9][CROSSWALK] = (
    r"^63(0|18).*",
)

TROPHOBLASTIC[PROCEDURE] = dict()
TROPHOBLASTIC[PROCEDURE][CPT] = dict()
TROPHOBLASTIC[PROCEDURE][CPT][MOLL] = (
    r"^59870$",
)

# ======================
# Spontaneous Abortion
# ======================
SPONTANEOUS_ABORTION = dict()
SPONTANEOUS_ABORTION[DIAGNOSIS] = dict()
SPONTANEOUS_ABORTION[DIAGNOSIS][ICD10] = dict()
SPONTANEOUS_ABORTION[DIAGNOSIS][ICD10][MOLL] = (
    r"^O0(21|3).*",
)

SPONTANEOUS_ABORTION[DIAGNOSIS][ICD9] = dict()
SPONTANEOUS_ABORTION[DIAGNOSIS][ICD9][CROSSWALK] = (
    r"^63[24].*",
)

SPONTANEOUS_ABORTION[PROCEDURE] = dict()
SPONTANEOUS_ABORTION[PROCEDURE][CPT] = dict()
SPONTANEOUS_ABORTION[PROCEDURE][CPT][MOLL] = (
    r"^01965$",
    r"^598(12|2[01]|30)$"
)

# ======================
# Elective/Therapeutic Abortion
# ======================
THERAPEUTIC_ABORTION = dict()
THERAPEUTIC_ABORTION[DIAGNOSIS] = dict()
THERAPEUTIC_ABORTION[DIAGNOSIS][ICD10] = dict()
THERAPEUTIC_ABORTION[DIAGNOSIS][ICD10][MOLL] = (
    r"^O04.*",
    r"^Z332.*",
)

THERAPEUTIC_ABORTION[DIAGNOSIS][ICD9] = dict()
THERAPEUTIC_ABORTION[DIAGNOSIS][ICD9][CROSSWALK] = (
    r"^63[5-7].*",
)

THERAPEUTIC_ABORTION[PROCEDURE] = dict()
THERAPEUTIC_ABORTION[PROCEDURE][ICD10] = dict()
THERAPEUTIC_ABORTION[PROCEDURE][ICD10][MOLL] = (
    r"^10A0([03478]ZZ|7Z[6WX])$",
)

THERAPEUTIC_ABORTION[PROCEDURE][ICD9] = dict()
THERAPEUTIC_ABORTION[PROCEDURE][ICD9][CROSSWALK] = (
    r"^7(491|50)$",
    r"^69([05]1|93)$"
)

THERAPEUTIC_ABORTION[PROCEDURE][CPT] = dict()
THERAPEUTIC_ABORTION[PROCEDURE][CPT][MOLL] = (
    r"^0196[46]$",
    r"^598(4[01]|5[0-25-7])$",
    r"^S(0199|226[025-7])$",
)

THERAPEUTIC_ABORTION[DRG] = dict()
THERAPEUTIC_ABORTION[DRG][DRG] = dict()
THERAPEUTIC_ABORTION[DRG][DRG][MOLL] = (
    r"^77[09]$",
)

THERAPEUTIC_ABORTION[DRG][DRG][EXPANDED] = (
    r"^38[01]$",
)

# ======================
# Stillbirth
# ======================
STILLBIRTH = dict()
STILLBIRTH[DIAGNOSIS] = dict()
STILLBIRTH[DIAGNOSIS][ICD10] = dict()
STILLBIRTH[DIAGNOSIS][ICD10][MOLL] = (
    r"^Z37[147].*",
    r"^O364XX[0-59]$",
)

STILLBIRTH[DIAGNOSIS][ICD9] = dict()
STILLBIRTH[DIAGNOSIS][ICD9][CROSSWALK] = (
    r"^6564[013]$",
    r"^V27[147].*",
)

# ======================
# Live birth
# ======================
LIVE_BIRTH = dict()
LIVE_BIRTH[DIAGNOSIS] = dict()
LIVE_BIRTH[DIAGNOSIS][ICD10] = dict()
LIVE_BIRTH[DIAGNOSIS][ICD10][MOLL] = (
    r"^Z37([023]|[56][0-49]).*",
    r"^O80.*",
)

LIVE_BIRTH[DIAGNOSIS][ICD10][EXPANDED] = (
    r"^Z38[036].*",
)

LIVE_BIRTH[DIAGNOSIS][ICD9] = dict()
LIVE_BIRTH[DIAGNOSIS][ICD9][CROSSWALK] = (
    r"^650$",
    r"^V27[02356]$",
)

LIVE_BIRTH[DIAGNOSIS][ICD9][EXPANDED] = (
    r"^V3[0-9]0.*",
)

# ======================
# Delivery of Unknown code_type
# ======================
DELIVERY = dict()
DELIVERY[DIAGNOSIS] = dict()
DELIVERY[DIAGNOSIS][ICD10] = dict()
DELIVERY[DIAGNOSIS][ICD10][MOLL] = (
    r"^Z3(79|90)$",
    r"^O420.*",
    r"^O6([3-57-9]|0[12]|6[0-35689]).*",
    r"^O7([0467]|[12]1|5[023589]).*",
    r"^O8(2|8[0-3,8]2)$",
    r"^O9(8[0-9]2|9([014-7]2|2[18]4|3[1-5]4|8[1-4]4)|A[1-5]2).*",
)

DELIVERY[DIAGNOSIS][ICD10][EXPANDED] = (
    r"^O(151|62).*",
)

DELIVERY[DIAGNOSIS][ICD9] = dict()
DELIVERY[DIAGNOSIS][ICD9][CROSSWALK] = (
    r"^V2(40|79).*",
    r"^64(1[389]1|421|681|7[0-689]1|8[1-689]1|9([0-4]1|8)).*",
    r'^65(2[24689]1|3[0-5]1|491|6[38]1|8[13]1|9([2389][013]?|71))$',
    r"^66(0[0-57-9]|[23]|4[0-46]|[56]1|8[0-289][12]|9[05-9]).*",
    r"^67([49]0[12]|3[0-38][12]).*",
)

DELIVERY[DIAGNOSIS][ICD9][EXPANDED] = (
    r"^64(0[089]1|1[0-2]1|2[0-79][12]|3[0-289]1|5[12]1|6([0379]1|[124-6][12]|82)|"
    r"7[0-689]2|8([1-689]2|[07][12])|9([0-4]2|6[12]|[57]1)).*",
    r"^65([15][0-9]1|2[01357]1|3[6-9]1|4([013-8][12]|21|92)|"
    r"6[0-25-79]1|701|8[02489]1|9[014-6]1).*",
    r"^66(061|1[0-49]1|4[589]|5([03-6]1|22|[7-9][12])|"
    r"6(0|[23]2)|7[01]2|9([124][12]|32)).*",
    r"^67(0[0-38]2|1([0-2589][12]|31|42)|202|4([1-489]2|5[12])|"
    r"5[0-289][12]|6[0-689][12]|8[01]1|91[12]).*",
)

DELIVERY[PROCEDURE] = dict()
DELIVERY[PROCEDURE][ICD10] = dict()
DELIVERY[PROCEDURE][ICD10][MOLL] = (
    r"^0W8NXZZ$",
    r"^10(D(0|1[78]Z9)|E0).*",
)

DELIVERY[PROCEDURE][ICD9] = dict()
DELIVERY[PROCEDURE][ICD9][CROSSWALK] = (
    r'^7(2[0-35-9][0-9]?|3(22|[569][0-9]?)|4([0-4]|99)|54)$',
)

DELIVERY[PROCEDURE][CPT] = dict()
DELIVERY[PROCEDURE][CPT][MOLL] = (
    r"^0196[0-37-9]$",
    r"^59(05[01]|4(09|1[04])|5(1[45]|25)|6(1[24]|2[02]))$",
    r"^994(36|6[45])$",
    r"^G9356$",
)

DELIVERY[DRG] = dict()
DELIVERY[DRG][DRG] = dict()
DELIVERY[DRG][DRG][MOLL] = (
    r"^37[0-5]$",
    r"^7(6[5-8]|7[45])$",
)

# ======================
# Convert to Pandas
# ======================
ECTOPIC = pd.DataFrame.from_dict(ECTOPIC, orient='index').stack().to_frame()
ECTOPIC = pd.DataFrame(ECTOPIC[0].values.tolist(),
                       index=ECTOPIC.index)
ECTOPIC = ECTOPIC.stack().to_frame()
ECTOPIC = pd.DataFrame(ECTOPIC[0].values.tolist(),
                       index=ECTOPIC.index).stack().reset_index().drop('level_3', axis=1)
ECTOPIC['outcome'] = OUTCOME_LIST[4]

TROPHOBLASTIC = pd.DataFrame.from_dict(TROPHOBLASTIC,
                                       orient='index').stack().to_frame()
TROPHOBLASTIC = pd.DataFrame(TROPHOBLASTIC[0].values.tolist(),
                             index=TROPHOBLASTIC.index)
TROPHOBLASTIC = TROPHOBLASTIC.stack().to_frame()
TROPHOBLASTIC = pd.DataFrame(TROPHOBLASTIC[0].values.tolist(),
                             index=TROPHOBLASTIC.index)\
    .stack().reset_index().drop('level_3', axis=1)
TROPHOBLASTIC['outcome'] = OUTCOME_LIST[3]

SPONTANEOUS_ABORTION = pd.DataFrame.from_dict(SPONTANEOUS_ABORTION,
                                              orient='index').stack().to_frame()
SPONTANEOUS_ABORTION = pd.DataFrame(SPONTANEOUS_ABORTION[0].values.tolist(),
                                    index=SPONTANEOUS_ABORTION.index)
SPONTANEOUS_ABORTION = SPONTANEOUS_ABORTION.stack().to_frame()
SPONTANEOUS_ABORTION = pd.DataFrame(SPONTANEOUS_ABORTION[0].values.tolist(),
                                    index=SPONTANEOUS_ABORTION.index)\
    .stack().reset_index().drop('level_3', axis=1)
SPONTANEOUS_ABORTION['outcome'] = OUTCOME_LIST[6]

THERAPEUTIC_ABORTION = pd.DataFrame.from_dict(THERAPEUTIC_ABORTION,
                                              orient='index').stack().to_frame()
THERAPEUTIC_ABORTION = pd.DataFrame(THERAPEUTIC_ABORTION[0].values.tolist(),
                                    index=THERAPEUTIC_ABORTION.index)
THERAPEUTIC_ABORTION = THERAPEUTIC_ABORTION.stack().to_frame()
THERAPEUTIC_ABORTION = pd.DataFrame(THERAPEUTIC_ABORTION[0].values.tolist(),
                                    index=THERAPEUTIC_ABORTION.index)\
    .stack().reset_index().drop('level_3', axis=1)
THERAPEUTIC_ABORTION['outcome'] = OUTCOME_LIST[5]

STILLBIRTH = pd.DataFrame.from_dict(STILLBIRTH, orient='index').stack().to_frame()
STILLBIRTH = pd.DataFrame(STILLBIRTH[0].values.tolist(),
                          index=STILLBIRTH.index)
STILLBIRTH = STILLBIRTH.stack().to_frame()
STILLBIRTH = pd.DataFrame(STILLBIRTH[0].values.tolist(),
                          index=STILLBIRTH.index).stack().reset_index().drop('level_3', axis=1)
STILLBIRTH['outcome'] = OUTCOME_LIST[1]

LIVE_BIRTH = pd.DataFrame.from_dict(LIVE_BIRTH, orient='index').stack().to_frame()
LIVE_BIRTH = pd.DataFrame(LIVE_BIRTH[0].values.tolist(),
                          index=LIVE_BIRTH.index)
LIVE_BIRTH = LIVE_BIRTH.stack().to_frame()
LIVE_BIRTH = pd.DataFrame(LIVE_BIRTH[0].values.tolist(),
                          index=LIVE_BIRTH.index).stack().reset_index().drop('level_3', axis=1)
LIVE_BIRTH['outcome'] = OUTCOME_LIST[0]

DELIVERY = pd.DataFrame.from_dict(DELIVERY, orient='index').stack().to_frame()
DELIVERY = pd.DataFrame(DELIVERY[0].values.tolist(),
                        index=DELIVERY.index)
DELIVERY = DELIVERY.stack().to_frame()
DELIVERY = pd.DataFrame(DELIVERY[0].values.tolist(),
                        index=DELIVERY.index).stack().reset_index().drop('level_3', axis=1)
DELIVERY['outcome'] = OUTCOME_LIST[2]

OUTCOMES_COLUMNS = ['code_type', 'version', 'schema', 'code', 'outcome']
ECTOPIC.columns = OUTCOMES_COLUMNS
TROPHOBLASTIC.columns = OUTCOMES_COLUMNS
SPONTANEOUS_ABORTION.columns = OUTCOMES_COLUMNS
THERAPEUTIC_ABORTION.columns = OUTCOMES_COLUMNS
STILLBIRTH.columns = OUTCOMES_COLUMNS
LIVE_BIRTH.columns = OUTCOMES_COLUMNS
DELIVERY.columns = OUTCOMES_COLUMNS

OUTCOMES = pd.concat([
    ECTOPIC,
    TROPHOBLASTIC,
    SPONTANEOUS_ABORTION,
    THERAPEUTIC_ABORTION,
    STILLBIRTH,
    LIVE_BIRTH,
    DELIVERY,
])
