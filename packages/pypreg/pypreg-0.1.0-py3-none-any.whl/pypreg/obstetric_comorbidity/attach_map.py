"""
Copyright (C) 2023 Dave Walsh

Utility functions to process a pandas dataframe of codes and
attach the comorbidity scores from one of the maps.
"""
import pandas as pd


def assign_weights(df: pd.DataFrame,
                   patient_col: str,
                   pregnancy_col: str,
                   code_col: str,
                   version_col: str,
                   method: str,
                   age_col: str = None):
    """
    Entry method to attach weights to diagnosis codes and age categories based on the method chosen.

    :param df: pandas dataframe containing diagnostic codes and the CODE versions
    :param patient_col: column that gives the patient identifier
    :param pregnancy_col: column that gives the pregnancy identifier
    :param code_col: Column containing diagnostic codes
    :param version_col: Column containing VERSION info about the CODE (ICD9/ICD10)
    :param method: Choice of 'bateman' or 'leonard' for the index
    :param age_col: Optional, column that gives the patient age

    :return: Returns the original dataframe with the indicator
        classification and the weight for the CODE class
    """

    from .bateman_mapping import BATEMAN_MAP
    from .leonard_mapping import LEONARD_MAP

    map_df = None
    versions = ['ICD9',
                'ICD10']

    # Select the map based on the method chosen
    if method == 'bateman':
        map_df = BATEMAN_MAP
        df = df[df[version_col] == versions[0]]
    elif method == 'leonard':
        map_df = LEONARD_MAP
        df = df[df[version_col] == versions[1]]

    # Remove . from the codes to make regex matching easier
    df[code_col] = df[code_col].str.replace('.', '', regex=False)

    # Rename the CODE column
    df.rename(columns={code_col: 'code'}, inplace=True)

    # Set up the regex match
    df['join'] = df[code_col].replace(map_df['code'].to_list(),
                                      map_df['code'].to_list(), regex=True)

    # Join on the matching regex pattern
    output = df.merge(map_df,
                      how='left',
                      left_on='join',
                      right_on='code',
                      suffixes=('', '_y')).drop(columns=['join', 'code_y'])

    # If the age column is given, include the age category in the score
    if age_col:
        age_df = age_category(df, patient_col, pregnancy_col, age_col, method)
        age_df = age_weights(age_df, map_df)
        output = pd.concat([output, age_df])

    return output


def age_category(df: pd.DataFrame,
                 patient_col: str,
                 pregnancy_col: str,
                 age_col: str,
                 method: str):
    """
    Utility to classify the age category by method. Bateman uses the
    age at LMP, so the minimum age captured during a pregnancy will be used.
    Leonard uses the age at delivery, so the maximum age captured during delivery will be used.

    :param df: pandas dataframe containing patient and pregnancy identifiers with age
    :param patient_col: column that gives the patient identifier
    :param pregnancy_col: column that gives the pregnancy identifier
    :param age_col: column that gives the patient age
    :param method: Choice of 'bateman' or 'leonard' for the index

    :return: Returns a pandas dataframe with the age category
    """

    from .bateman_mapping import AGE_CATEGORY as bateman_categories
    from .leonard_mapping import AGE_CATEGORY as leonard_categories

    # Set up the age bins for each method
    bateman_bins = [0, 34, 39, 44, 110]
    leonard_bins = [0, 34, 110]

    methods = {'leonard', 'bateman'}
    method = method.lower()

    if method not in methods:
        raise ValueError(f'Method must be one of {methods}')

    if age_col not in df.columns:
        raise ValueError(f'Age column {age_col} is not in dataframe.')

    bins = None
    labels = None

    if method == 'leonard':
        labels = leonard_categories
        bins = leonard_bins
        df = df.groupby([patient_col, pregnancy_col])[age_col].max().reset_index()

    if method == 'bateman':
        labels = bateman_categories
        bins = bateman_bins
        df = df.groupby([patient_col, pregnancy_col])[age_col].min().reset_index()

    df['age_category'] = pd.cut(df[age_col], bins, labels=labels, include_lowest=False)

    return df


def age_weights(df: pd.DataFrame,
                map_df: pd.DataFrame):

    """
    Attach the weights for age categories.

    :param df: pandas dataframe containing the age category as assigned in the age_category method
    :param map_df: pandas dataframe of the index method's CODE map

    :return: returns the original dataframe with the weights assigned to the age category
    """

    output = df.merge(map_df,
                      how='inner',
                      left_on='age_category',
                      right_on='indicator')

    return output
