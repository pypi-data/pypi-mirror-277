"""
Obstetric Comorbidity Index

Copyright (C) 2023 Dave Walsh
Department of Biomedical and Health Informatics
UMKC

Looks at a pandas dataframe containing patient and pregnancy
identifiers with diagnostic codes. Diagnostic codes must be
labeled as ICD9 or ICD10. User indicates the desired comorbidity index.
Returns the total score for each patient/pregnancy.

Codes and scores are attributable to:
    Bateman BT, Mhyre JM, Hernandez-Diaz S, Huybrechts KF, Fischer MA,
        Creanga AA, Callaghan WM, Gagne JJ. Development of a comorbidity
        index for use in obstetric patients. Obstet Gynecol.
        2013 Nov;122(5):957-965. doi: 10.1097/AOG.0b013e3182a603bb.
        PMID: 24104771; PMCID: PMC3829199.

    Leonard SA, Kennedy CJ, Carmichael SL, Lyell DJ, Main EK.
        An Expanded Obstetric Comorbidity Scoring System for
        Predicting Severe Maternal Morbidity. Obstet Gynecol.
        2020 Sep;136(3):440-449. doi: 10.1097/AOG.0000000000004022.
        PMID: 32769656; PMCID: PMC7523732.

"""

import pandas as pd


def calc_index(df: pd.DataFrame,
               patient_col: str,
               pregnancy_col: str,
               code_col: str,
               version_col: str,
               method: str,
               age_col: str = None):
    """
    Main function. Accepts a pandas dataframe of patient encounter data.
    Only ICD9/ICD10 diagnostic codes are accepted. Appends the Leonard or
    Bateman score as chosen by the user. Bateman returns a single score,
    Leonard returns both a transfusion and non-transfusion score.

    :param df: Pandas dataframe containing patient and pregnancy identifiers
        with ICD9/10 diagnostic codes
    :param patient_col: column that gives the patient identifier
    :param pregnancy_col: column that gives the pregnancy identifier
    :param code_col: column that gives the diagnostic codes
    :param version_col: column that indicates if the given diagnostic code is ICD9 or ICD10.
    Accepts 9, ICD9, 10, ICD10, and ICD10-CMS
    :param method: Choice of 'leonard' or 'bateman' for obstetric index scores
    :param age_col: Optional column that gives the age of the patient
    :return: Pandas dataframe containing the total index score for each patient's pregnancy
    """

    # Error checking to ensure the reported columns are contained in the dataframe
    if not {patient_col, pregnancy_col, code_col, version_col}.issubset(df.columns):
        raise KeyError(f"Ensure that columns "
                       f"{[patient_col, pregnancy_col, code_col, version_col]} "
                       f"are present in the data.")

    package_cols = {patient_col: 'group_id',
                    pregnancy_col: 'preg_num',
                    version_col: 'version',
                    code_col: 'code'
                    }
    restore_cols = {i: j for j, i in package_cols.items()}

    # Refactor the passed column names
    patient_col = package_cols[patient_col]
    pregnancy_col = package_cols[pregnancy_col]
    version_col = package_cols[version_col]
    code_col = package_cols[code_col]

    df.rename(columns=package_cols, inplace=True)

    # Ignore SettingWithCopyWarning
    pd.options.mode.chained_assignment = None

    methods = ['leonard', 'bateman']
    method = method.lower()

    # Versions can accept different coding systems: 9/ICD9, 10/ICD10/ICD10-CM/ICD10-PCS
    versions = dict()
    versions['ICD9'] = ("9",
                        "ICD9")
    versions['ICD10'] = ("10",
                         "ICD10",
                         "ICD10-CM",
                         "ICD10-PCS")

    if method not in methods:
        raise ValueError(f'Method must be one of {methods}')

    if patient_col not in df.columns:
        raise ValueError(f'Patient ID column {patient_col} not in dataframe.')

    if pregnancy_col not in df.columns:
        raise ValueError(f'Pregnancy ID column {pregnancy_col} not in dataframe.')

    if code_col not in df.columns:
        raise ValueError(f'Code column {code_col} not in dataframe.')

    # Create a copy to avoid warnings from pandas
    if age_col:
        df = df[[patient_col, pregnancy_col, version_col, code_col, age_col]].copy()
    else:
        df = df[[patient_col, pregnancy_col, version_col, code_col]].copy()

    # Check the contents of the Version column and warn user if
    # the contents don't match the expected. This doesn't constitute
    # an error as the dataset could contain valid codes from other
    # systems for other uses
    df[version_col] = df[version_col].astype(str)
    df[version_col] = df[version_col].str.upper()
    df_versions = set(df[version_col].unique().flat)
    this_versions = set([val for value in versions.values() for val in value])

    import warnings

    if not df_versions.issubset(this_versions):
        warnings.warn(f"Some code versions ({df_versions - this_versions})"
                      f" do not match {this_versions}."
                      f" Ensure these are not in error.", stacklevel=2)

    # Convert dictionary to dataframe
    versions = pd.DataFrame.from_dict(versions, orient='index').stack().to_frame()
    versions = pd.DataFrame(versions[0].values.tolist(),
                            index=versions.index).reset_index().drop('level_1', axis=1)
    versions.columns = ['version', 'version_match']

    # Replace Version in the provided dataframe with a standard form
    df = df.merge(versions,
                  how='inner',
                  left_on=version_col,
                  right_on='version_match',
                  suffixes=('_x', '')) \
        .drop(columns=['version_x', 'version_match'])

    # Process comorbidity scoring
    from .attach_map import assign_weights
    from .score import get_score

    output = assign_weights(df, patient_col, pregnancy_col, code_col, version_col, method, age_col)
    output = get_score(output, method, patient_col=patient_col, pregnancy_col=pregnancy_col)

    # Restore SettingWithCopyWarning
    pd.options.mode.chained_assignment = 'warn'

    output.rename(columns=restore_cols, inplace=True)

    return output
