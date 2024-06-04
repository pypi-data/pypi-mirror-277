"""
Copyright (C) 2023 Dave Walsh

Process the weights by patient and pregnancy number.
"""
import pandas as pd


def get_score(df: pd.DataFrame,
              method: str,
              patient_col: str,
              pregnancy_col: str):
    """
    Entry point to the scoring section that directs the inputs to the appropriate version.

    :param df: pandas dataframe containing patient and pregnancy identifiers
        with comorbidity indicators and weights
    :param method: Choice of 'leonard' or 'bateman' for obstetric index
    :param patient_col: column that gives the patient identifier
    :param pregnancy_col:column that gives the pregnancy identifier

    :return: Pandas dataframe with total comorbidity score for the
        chosen method by patient and pregnancy

    :raises: ValueError
        -Patient or Pregnancy ID columns are not in the data
        -Given method does not exist
    """

    methods = ['leonard', 'bateman']
    method = method.lower()

    if method not in methods:
        raise ValueError(f'Method must be one of {methods}')

    if patient_col not in df.columns:
        raise ValueError(f'Patient ID column {patient_col} not in dataframe.')

    if pregnancy_col not in df.columns:
        raise ValueError(f'Pregnancy ID column {pregnancy_col} not in dataframe.')

    if method == methods[0]:
        return leonard_score(df, patient_col=patient_col, pregnancy_col=pregnancy_col)

    if method == methods[1]:
        return bateman_score(df, patient_col=patient_col, pregnancy_col=pregnancy_col)


def bateman_score(df: pd.DataFrame,
                  patient_col: str,
                  pregnancy_col: str):

    """
    Totals up the score for the Batemen obstetric index. More severe
    preeclampsia and eclampsia preclude mild preeclampsia. Pre-existing
    hypertension and/or preeclampsia/eclampsia precludes gestational hypertension.

    :param df: pandas dataframe containing patient and pregnancy identifiers
        with comorbidity indicators and weights
    :param patient_col: column that gives the patient identifier
    :param pregnancy_col: column that gives the pregnancy identifier

    -mild preeclampsia is only included if severe preeclampsia/eclampsia is absent
    -gestational hypertension is only included if there is no
        pre-existing hypertension nor preeclampsia/eclampsia

    :return: Pandas dataframe containing patient and pregnancy
        identifiers with the total score

    :raises: ValueError is thrown when the provided patient or
        pregnancy columns are not present in the data

    """

    from .bateman_mapping import BATEMAN_MAP

    # error checking for column names
    if patient_col not in df.columns:
        raise ValueError(f'Patient identifier column {patient_col} '
                         f'is not in the provided dataframe.')

    if pregnancy_col not in df.columns:
        raise ValueError(f'Pregnancy identifier column {pregnancy_col} '
                         f'is not in the provided dataframe.')

    # Set up search terms for indicators for hypertension, can be reused for eclampsia exclusions
    # terms should be for eclampsia/preeclampsia and preexisting hypertension
    terms = [BATEMAN_MAP.indicator.iloc[5],
             BATEMAN_MAP.indicator.iloc[4],
             BATEMAN_MAP.indicator.iloc[8]]

    # Reference the weight column name
    weight_col = BATEMAN_MAP.columns[3]

    # Reference the indicator column name
    indicator_col = BATEMAN_MAP.columns[2]

    # Only keep 1 copy of each indicator per patient per pregnancy
    df = df[[patient_col, pregnancy_col, indicator_col, weight_col]].drop_duplicates().copy()

    # Collect the data that matches the search terms, reference the
    # gestation hypertension indicator directly
    eclampsia_df = df[df.indicator == terms[0]]
    preeclampsia_df = df[df.indicator == terms[1]]
    hypertension_df = df[df.indicator.isin(terms)]
    gest_ht_df = df[df.indicator == BATEMAN_MAP.indicator.iloc[3]]

    # Identify the preeclampsia rows for which an eclampsia indicator
    # is present for the same patient and pregnancy
    preeclampsia_df = preeclampsia_df.merge(eclampsia_df[[patient_col, pregnancy_col]],
                                            how='inner',
                                            left_on=[patient_col, pregnancy_col],
                                            right_on=[patient_col, pregnancy_col]).drop_duplicates()

    # Identify the gestational hypertension rows for which an exclusion
    # is present for the same patient and pregnancy
    gest_ht_df = gest_ht_df.merge(hypertension_df[[patient_col, pregnancy_col]],
                                  how='inner',
                                  left_on=[patient_col, pregnancy_col],
                                  right_on=[patient_col, pregnancy_col]).drop_duplicates()

    # The adjusted weights are 0 when more severe, or pre-existing hypertension exists
    preeclampsia_df[weight_col] = 0
    gest_ht_df[weight_col] = 0

    # Correct the weights for preeclampsia
    output = df.merge(preeclampsia_df[[patient_col, pregnancy_col, indicator_col, weight_col]],
                      how='left',
                      left_on=[patient_col, pregnancy_col, indicator_col],
                      right_on=[patient_col, pregnancy_col, indicator_col],
                      suffixes=('_x', ''))
    output.fillna({'weight': output[f'{weight_col}_x']}, inplace=True)
    output.drop(columns=[f'{weight_col}_x'], inplace=True)

    # Correct the weights for gestational hypertension
    output = output.merge(gest_ht_df[[patient_col, pregnancy_col, indicator_col, weight_col]],
                          how='left',
                          left_on=[patient_col, pregnancy_col, indicator_col],
                          right_on=[patient_col, pregnancy_col, indicator_col],
                          suffixes=('_x', ''))
    output.fillna({'weight': output[f'{weight_col}_x']}, inplace=True)
    output.drop(columns=[f'{weight_col}_x'], inplace=True)

    # Sum the weights to get the score
    output = output.groupby([patient_col, pregnancy_col])[weight_col].sum().reset_index()

    # Convert the score to an integer
    output[weight_col] = output[weight_col].astype(int)

    # Rename the column to something explicit
    output.rename(columns={weight_col: 'bateman_score'},
                  inplace=True)

    return output


def leonard_score(df: pd.DataFrame,
                  patient_col: str,
                  pregnancy_col: str):
    """
    Totals up the two Leonard scores. There are no caveats with this method
    like there are with Bateman

    :param df: pandas dataframe containing patient and pregnancy identifiers
        with comorbidity indicators and weights
    :param patient_col: column that gives the patient identifier
    :param pregnancy_col: column that gives the pregnancy identifier

    :return: Pandas dataframe containing patient and pregnancy identifiers
        with the score for SMM and non-Transfusion SMM
    """
    from .leonard_mapping import LEONARD_MAP

    # error checking for column names
    if patient_col not in df.columns:
        raise ValueError(f'Patient identifier column {patient_col} '
                         f'is not in the provided dataframe.')

    if pregnancy_col not in df.columns:
        raise ValueError(f'Pregnancy identifier column {pregnancy_col} '
                         f'is not in the provided dataframe.')

    # Get reference to the leonard score column names
    score_col = [LEONARD_MAP.columns[3],
                 LEONARD_MAP.columns[4]]

    # Get reference to the leonard indicator column
    indicator_col = LEONARD_MAP.columns[2]

    # Sum up the scores
    output = df[[patient_col,
                 pregnancy_col,
                 indicator_col,
                 score_col[0],
                 score_col[1]]].fillna(0).drop_duplicates()
    output = output.groupby([patient_col, pregnancy_col])[[score_col[0], score_col[1]]]\
        .apply(lambda x: x.astype(int).sum())\
        .reset_index()

    # Rename the scoring columns to be more explicit
    output.rename(columns={score_col[0]: 'leonard_smm_score',
                           score_col[1]: 'leonard_nontransfusion_smm_score'},
                  inplace=True)

    return output
