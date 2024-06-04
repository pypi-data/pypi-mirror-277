# pypreg
pypreg is a collection of packages that classifies pregnancy outcome types from health data, identifies severe maternal 
morbidity, adverse pregnancy outcomes, and calculates obstetric comorbidity scores.

## Features

This package makes available several methods to support pregnancy research:
 - [Pregnancy Outcome Classification](#pregnancy-outcome-classification):
   - Classify pregnancies by their outcome (Live birth, Stillbirth, etc.)
 - [Adverse Pregnancy Outcomes](#adverse-pregnancy-outcomes):
   - Identify the presence of indicators for Cesarean section, Preeclampsia, Gestational Diabetes, Gestational Hypertension, and Fetal Growth Restriction
 - [Severe Maternal Morbidity](#severe-maternal-morbidity):
   - Identify the presence of SMM and non-Transfusion SMM
   - Get individual flags for each of 21 indicators that make up the SMM definition
 - [Obstetric Comorbidity Index](#obstetric-comorbidity-index):
   - Get a numeric obstetric comorbidity index consistent with methods published by Bateman or Leonard

## General Usage Data Format

The methods in this package rely on diagnostic, procedure, and/or diagnostic related group (DRG) codes. These codes should be organized rowwise with the relevant patient identifiers in the context of a pandas dataframe.

## Pregnancy Outcome Classification
This module is an implementation of the obstetric classification algorithm given by Moll(2020).

### Data Requirements
A Pandas dataframe with the following elements is required to begin using this package: 

| Column       | Description                                                    | Notes                                                                                                |
|--------------|----------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| Patient ID   | Unique patient identifier                                      |                                                                                                      |
| Encounter ID | Encounter identifier                                           |                                                                                                      |
| Admit date   | Date of encounter admission                                    | Date or datetime                                                                                     |
| Code type    | Describes if the given code is a procedure, diagnostic, or DRG | Accepts 'dx', 'diagnosis', 'diagnostic', 'px', 'procedure', 'drg', 'diagnostic related group'        |
| Code version | Describes the coding system of the given code                  | Accepts '9', 'ICD9', '10', 'ICD10', 'ICD10-CM', 'ICD10-PCS', 'CPT', 'CPT4', 'HCPCS', 'DRG', 'MS-DRG' |
| Code         | The procedure, diagnostic, or DRG code                         |                                                                                                      |

The dataframe may contain multiple instances of a single encounter with a variety of codes. The data should be presented 
rowwise where the codes are differentiated by the **_Code type_** and **_Code version_** columns.

### Code selection

#### Crosswalk
The codes given by Moll(2020) are primarily in the ICD10 coding system and are crosswalked to ICD9 for broader use.
Crosswalked codes are retrieved via General Equivalence Mappings. ICD10 codes are mapped back to ICD9, and ICD9 codes
are mapped forward to ICD10. The resulting codes are reviewed and kept if they are related to an obstetric outcome, and,
if the original ICD10 code broadly refers to labor and delivery, then the mapped codes may also. 

#### Change to Moll codes
ICD10 procedure codes 10D17ZZ and 10D18ZZ refer to extraction of retained products of conception. These codes describe
a dilation and curettage procedure which is more frequently, though not exclusively, performed on abortive outcomes. 
These codes lead to misclassification of abortive outcomes as unknown deliveries and were removed from this 
implementation.

#### Expanded codes
Expanded codes are added based upon a review of ICD9 and ICD10 codes for other obstetric outcomes not captured.
This primarily captures codes where episode of care indicates _delivered_ in ICD9.

### Algorithm
The specifics of the algorithm are contained within Moll(2020). In short, each code provided is classified by regular 
expression matching. Each individual patient is then processed independently to prioritize certain outcomes. The 
outcomes are then checked to ensure that the spacing between different pregnancy outcome types is sensible. Outcome 
types that do not fit the spacing are dropped from consideration. A pregnancy start window is estimated based on the 
outcome type. The start of this window is then adjusted if needed so that it is not overlapping a previous pregnancy.

### Usage

Four processes are exposed and available to be imported:

1. `process_outcomes`
  - the entry into the classifcation algorithm. All parameters are required except for the `expanded` 
flag which indicates if you would like to use the Moll codes or an expanded list of codes identified by this author
  - the dataframe need not have the columns in a standardized order, instead the required column names must be passed 
as strings

```python
from pypreg import process_outcomes

process_outcomes(df: pd.DataFrame,
                 patient_col: str,
                 encounter_col: str,
                 admit_date_col: str,
                 version_col: str,
                 type_col: str,
                 code_col: str,
                 expanded: bool = False)
```
#### Output
This process will produce a pandas dataframe with the following data (column names that are reflexive of provided data 
will use the originally provided column name): 


| Column       |Description|Notes|
|--------------|----|----|
| Patient ID   |Unique patient identifier|Will be the same as originally provided|
| Preg_num     |Pregnancy identifier per patient|Synonomous with gravida, but only relevant to the provided data (uncaptured pregnancies cannot be counted)|
| Encounter ID |Encounter identifier belonging to the outcome encounter|Will be the same as originally provided|
| Admit        |Date of admission for the outcome encounter|Formatted as date, not datetime||
|Event_date|Date of admission for the outcome encounter|Formatted as date, not datetime||
|Outcome|String classification of the pregnancy outcome| live_birth, stillbirth, delivery, trophoblastic, ectopic, therapeutic_abortion, spontaneous_abortion|
|Start_window|Date that delineates the beginning of the pregnancy start window||
|End_window|Date that delineates the end of the pregnancy start window||

2. `OUTCOME_LIST`
  - exports the list of pregnancy outcomes in hierarchical order
```python
from pypreg import OUTCOME_LIST

print(OUTCOME_LIST)
['LIVE_BIRTH', 'STILLBIRTH', 'DELIVERY', 'TROPHOBLASTIC', 'ECTOPIC', 'THERAPEUTIC_ABORTION', 'SPONTANEOUS_ABORTION']
```
3. `OUTCOMES`
  - exports the full list of codes, the code type, the code version, and the association outcome classification
  - codes are given as a regular expression
```python
from pypreg import OUTCOMES

print(OUTCOMES.head())
  code_type version     schema                      code  outcome
0        DX   ICD10       MOLL                 ^O0[08].*  ECTOPIC
1        DX    ICD9  CROSSWALK                    ^633.*  ECTOPIC
2        PX   ICD10       MOLL  ^10(D2[78]|T2[03478])ZZ$  ECTOPIC
3        PX    ICD9  CROSSWALK                     ^743$  ECTOPIC
4        PX    ICD9  CROSSWALK                 ^66[06]2$  ECTOPIC

```
4. `map_version_split`
  - splits `OUTCOMES` into 4 subcategories
    - ICD9 Diagnostic codes
    - ICD10 Diagnositc codes
    - Procedure codes
    - Diagnostic Related Group (DRG) codes
  - default behavior is to not include the expanded code list
```python
from pypreg import map_version_split

map_version_split(expanded: bool = False)
```

## Adverse Pregnancy Outcomes
This package is an implementation to identify adverse pregnancy outcomes from longitudinal data. This implementation 
covers cesarean section, fetal growth restriction, gestational diabetes, gestational hypertension, and preeclampsia. 
Pre-term birth is not included in this package as it relies on gestational age which is not covered in this work.

### Code selection

#### Cesarean section
Codes were sourced from a variety of authors. Additional codes were added by this author after review that indicated a 
cesarean section had been performed. These include anesthesia for c-section as they should appear alongside the 
cesarean section code anyway, and disruption of cesarean wound as this indicates a cesarean section had been recently 
performed.

### Usage
#### Data requirement
A Pandas dataframe with the following elements is required to begin using this package: 

| Column       | Description                                                    | Notes                                                                                                  |
|--------------|----------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| Patient ID   | Unique patient identifier                                      |                                                                                                        |
| Pregnancy ID | Pregnancy identifier                                           |                                                                                                        | 
| Code type    | Describes if the given code is a procedure, diagnostic, or DRG | Accepts 'dx', 'diagnosis', 'px', 'procedure', 'drg', 'diagnostic related group', 'diagnostic grouping' |
| Code version | Describes the coding system of the given code                  | Accepts '9', 'ICD9', '10', 'ICD10', 'ICD10-CM', 'ICD10-PCS', 'CPT', 'CPT4', 'HCPCS', 'DRG', 'DIAGNOSTIC RELATED GROUP', 'DIAGNOSTIC GROUPING', 'MS-DRG' |
| Code         | The procedure, diagnostic, or DRG code                         |                                                                                                        |

The dataframe may contain multiple instances of a single encounter with a variety of codes. The data should be presented 
rowwise.

#### Process outcomes
```python
from pypreg import apo

apo_df = apo(data_df,
             patient_id='patient_id',
             preg_id='preg_id',
             code_type='code_type',
             version='code_version',
             code='code')
```

#### Output
This process will produce a pandas dataframe with the following data:

| Column                   | Description                                                            | Notes   |
|--------------------------|------------------------------------------------------------------------|---------|
| Patient ID               | Unique patient identifier                                              |         |
| Pregnancy ID             | Pregnancy identifier                                                   |         | 
| cesarean                 | Indicates if a cesarean section was recorded for the pregnancy         | Boolean |                                                                                                                                                 |
| fetal growth restriction | Indicates if a fetal growth restriction was recorded for the pregnancy | Boolean |
| gest diabetes mellitus   | Indicates if gestational diabetes was recorded for the pregnancy       | Boolean |
| gest hypertension        | Indicates if gestational hypertension was recorded for the pregnancy   | Boolean |
| preeclampsia             | Indicates if preeclampsia was recorded for the pregnancy               | Boolean |


## Severe Maternal Morbidity
This package is an implementation of Severe Maternal Mordbidity(SMM) classification defined by the Centers for Disease 
Control and Prevention (CDC).

### Code selection
Codes are as provided by the [CDC](https://www.cdc.gov/maternal-infant-health/php/severe-maternal-morbidity/icd.html). 
Where all child codes are indicated, the top-level codes are also included. All codes have been translated into regular 
expressions.

### Usage
#### Data requirement
A Pandas dataframe with the following elements is required to begin using this package: 

| Column       | Description                                                    | Notes                                                                                                |
|--------------|----------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| Encounter ID | Encounter identifier of the pregnancy outcome                  | SMM definition requires using the delivery encounter                                                 |
| Code type| Describes if the given code is a procedure, diagnostic, or DRG | Accepts 'dx', 'diagnosis', 'px', 'procedure'       |
| Code version| Describes the coding system of the given code                  | Accepts '9', 'ICD9', '10', 'ICD10', 'ICD10-CM', 'ICD10-PCS' |
| Code | The procedure or diagnostic code                       |                                                                                                      |

The dataframe may contain multiple instances of a single encounter with a variety of codes. The data should be presented 
rowwise where the codes are differentiated by the _Code type_ and _Code version_ columns.

#### Process SMM
```python
from pypreg import smm

smm_df = smm(data_df,
             enc_id='encounter_id',
             code_type='code_type',
             version='code_version',
             code='code',
             indicators=True)
```

##### Output
This process will produce a pandas dataframe with the following data:

| Column       | Description                                                                                         | Notes                                                |
|--------------|-----------------------------------------------------------------------------------------------------|------------------------------------------------------|
| Encounter ID | Encounter identifier of the pregnancy outcome                                                       | SMM definition requires using the delivery encounter |
| smm | Indicates the delivery encounter qualifies as SMM                                                   | Boolean                                              |
|transfusion| Indicates the delivery encounter recorded a transfusion procedure                                   | Boolean                                              |
| Others | If `indicators = TRUE` every condition class that makes up SMM will be included | Boolean                                              |



## Obstetric Comorbidity Index
This module is an implementation of both the Bateman(2013) and Leonard(2020) obstetric comorbidity indices.

### Codes
Codes are given by Bateman(2013) and Leonard(2020). This author has adapted them as regular expressions to include the
top-level code where appropriate, as some secondary databases include these codes.

### Scoring
Scores are assigned by comorbidity. Comorbidity classifications are matched to codes using regular expressions. Weights 
assigned to each comorbidity vary depending on the scoring method chosen. Refer to Bateman(2013) and Leonard(2020) for 
information on the weights assigned.

#### Ranges
 - Bateman
   - 0-45
 - Leonard
   - non-transfusion SMM
     - 0-281
   - transfusion SMM
     - 0-478

### Usage
#### Data requirement
A Pandas dataframe with the following elements is required to begin using this package: 

| Column       | Description                                                    | Notes                                                                                        |
|--------------|----------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| Patient ID   | Unique patient identifier                                      |                                                                                              |
| Pregnancy ID | Pregnancy identifier                                           |                                                                                              |
| Code version | Describes the coding system of the given code                  | Accepts '9', 'ICD9', '10', 'ICD10', 'ICD10-CM'|
| Code         | The diagnostic code                         ||
|Method|String choice to select the method| Accepts 'bateman', 'leonard'|
|Age column| Optional parameter to provide the column containing patient age| Bateman needs the patient age at the beginning of the pregnancy, Leonard needs the age at the outcome|

The dataframe may contain multiple instances of a single pregnancy with a variety of codes. The data should be presented 
rowwise.

#### Calculate index
Two different scoring methods can be selected:
1. Bateman
```python
from pypreg import calc_index

calc_index(df,
           patient_col='patient_id',
           pregnancy_col='preg_id',
           code_col='code',
           version_col='code_version',
           method='bateman',
           age_col='age'):
```
Bateman asks for patient age at the Last Menstrual Period (LMP). If you've given an age column, the method assumes that 
the patient can age during the course of pregnancy and thus the minimum age is selected.

2. Leonard
```python
from pypreg import calc_index

calc_index(df,
           patient_col='patient_id',
           pregnancy_col='preg_id',
           code_col='code',
           version_col='code_version',
           method='leonard',
           age_col='age'):
```
Leonard asks for patient age at the outcome. If you've given an age column, the method assumes that the patient can age 
during the course of pregnancy and thus the maximum age is selected.

#### Output
This process will produce a pandas dataframe with the following data:

| Column                           | Description                           | Notes                   |
|----------------------------------|---------------------------------------|-------------------------|
| Patient ID                       | Unique patient identifier             |                         |
| Pregnancy ID                     | Pregnancy identifier                  |                         |
| bateman_score                    | When the 'bateman' method is selected | Scores range from 0-5   |
| leonard_smm_score                | When the 'leonard' method is selected | Scores range from 0-478 |
| leonard_nontransfucion_smm_score | When the 'leonard' method is selected | Scores range from 0-281 |

## References
 - Centers for Disease Control and Prevention. How does CDC identify severe maternal morbidity? 
    https://www.cdc.gov/reproductivehealth/maternalinfanthealth/smm/severe-morbidity-ICD.htm. Accessed 2023.
   - Updated link: https://www.cdc.gov/maternal-infant-health/php/severe-maternal-morbidity/icd.html
 - Moll K FK Wong H-L. Task order HHSF22301001T: Pregnancy outcomes validation final report. U.S. Food and Drug 
    Administration; 2020. Available at: https://www.bestinitiative.org/wp-content/uploads/2020/08/Validating_Pregnancy_Outcomes_Linked_Database_Report_2020-1.pdf
 - Agency for Healthcare Research and Quality U.S. Department of Health and Human Services. AHRQ Quality Indicators™ 
    (AHRQ QI™)ICD-9-CM and ICD-10-CM/PCSSpecification Enhanced Version 5.0: Inpatient Quality Indicators #21 
    (IQI #21)Cesarean Delivery Rate, Uncomplicated 2015: https://qualityindicators.ahrq.gov/Downloads/Modules/IQI/V50-ICD10/TechSpecs/IQI%2021%20Cesarean%20Delivery%20Rate,%20Uncomplicated.pdf
 - Castillo WC, Boggess K, Stürmer T, Brookhart MA, Benjamin DK, Funk MJ.
    Trends in Glyburide Compared With Insulin Use for Gestational Diabetes Treatment in the United States, 2000-2011
    (Supplemental Materials) Obstetrics & Gynecology , Vol. 123, No. 6 Ovid Technologies (Wolters Kluwer Health) p. 1177-1184
 - Bateman BT, Mhyre JM, Hernandez-Diaz S, Huybrechts KF, Fischer MA, Creanga AA, Callaghan WM, Gagne JJ.
    Development of a comorbidity index for use in obstetric patients. Obstet Gynecol. 2013 Nov;122(5):957-965.
    doi: 10.1097/AOG.0b013e3182a603bb. PMID: 24104771; PMCID: PMC3829199
 - Leonard SA, Kennedy CJ, Carmichael SL, Lyell DJ, Main EK.
    An Expanded Obstetric Comorbidity Scoring System for Predicting Severe Maternal Morbidity. Obstet Gynecol.
    2020 Sep;136(3):440-449. doi: 10.1097/AOG.0000000000004022. PMID: 32769656; PMCID: PMC7523732
 