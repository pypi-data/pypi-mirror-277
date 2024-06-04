"""
SMM Severe Maternal Morbidity

Copyright (C) 2023 Dave Walsh
Department of Biomedical and Health Informatics
UMKC

Looks at a pandas dataframe containing ICD9 and IC10 diagnostic and procedure
codes to report out the presence of Severe Maternal Morbidity (SMM) and TRANSFUSION.
The function includes an option to report out the subgroups making up an SMM
determination. The function can also accept codes in other systems, but will ignore them.

Since SMM is only defined in the context of a delivery encounter,
the user should ensure that they are only processing data from delivery/outcome encounters.

SMM definition is based on the CDC definition:
https://www.cdc.gov/reproductivehealth/maternalinfanthealth/smm/severe-morbidity-ICD.htm

The codes used in the module are derived from the updated CODE list provided
by the Alliance for Innovation on Maternal Health:
https://saferbirth.org/aim-resources/implementation-resources/
https://saferbirth.org/wp-content/uploads/Updated-AIM-SMM-Code-List_10152021.xlsx

"""

import warnings
import pandas as pd
from .smm_mapping import _SMM, TRANSFUSION, ICD9, ICD10


def smm(df: pd.DataFrame,
        enc_id: str,
        code_type: str,
        version: str,
        code: str,
        indicators: bool = False):
    """
    Processes a pandas dataframe to indicate if an encounter contained codes consistent with
    Severe Maternal Morbidity(SMM).

    :param df: A pandas dataframe that contains at least 4 columns to identify
    the delivery encounter, the code_type of code, the version of the code,
    and the code itself - encounters may exist on multiple lines to account
    for multiple codes
    :param enc_id: Encounter identifier that contains the pregnancy outcome
    :param code_type: One of either DX - Diagnosis or PX - Procedure
    :param version:  Only accepts CODE versions for ICD9 or ICD10
    (9/ICD9, 10/ICD10/ICD10-CM/ICD10-PCS)
    :param code: The DX or PX CODE assigned during that encounter
    :param indicators: Optional boolean to return the full slate of indicators
    and not only SMM and transfusion columns

    :return: Returns a condensed pandas dataframe with the delivery
    encounter identifier and indicators for SMM and transfusion.
    Optionally returned individualized indicators for each of the 20 other classes that make up SMM.

    """

    # Error checking to ensure the reported columns are contained in the dataframe
    if not {enc_id, code_type, version, code}.issubset(df.columns):
        raise KeyError(f"Ensure that columns {[enc_id, code_type, version, code]}"
                       f" are present in the data.")

    package_cols = {enc_id: 'encounter_id',
                    version: 'version',
                    code_type: 'code_type',
                    code: 'code'
                    }
    restore_cols = {i: j for j, i in package_cols.items()}

    # Refactor the passed column names
    enc_id = package_cols[enc_id]
    version = package_cols[version]
    code_type = package_cols[code_type]
    code = package_cols[code]

    df.rename(columns=package_cols, inplace=True)

    # Types can accept a CODE label as dx/diagnosis or px/procedure
    types = dict()
    types['DX'] = ('dx',
                   'diagnosis')
    types['PX'] = ('px',
                   'procedure')

    # Versions can accept different coding systems: 9/ICD9, 10/ICD10/ICD10-CM/ICD10-PCS
    versions = dict()
    versions['ICD9'] = ("9",
                        "ICD9")
    versions['ICD10'] = ("10",
                         "ICD10",
                         "ICD10-CM",
                         "ICD10-PCS")

    # Make a copy of the dataframe to avoid warnings about working on the original
    df = df[[enc_id, code_type, version, code]].copy()

    # Check the contents of the Type column and warn user if
    # the contents don't match the expected types. This doesn't
    # constitute an error as the dataset could contain valid
    # codes from other systems for other uses.
    df[code_type] = df[code_type].str.lower()
    df_types = set(df[code_type].unique().flat)
    this_types = set([val for value in types.values() for val in value])
    if not df_types.issubset(this_types):
        warnings.warn(f"Some code types ({df_types-this_types}) do not match {this_types}."
                      f" Ensure these are not in error.", stacklevel=2)

    # Check the contents of the Version column and warn user
    # if the contents don't match the expected. This doesn't
    # constitute an error as the dataset could contain valid
    # codes from other systems for other uses
    df[version] = df[version].str.upper()
    df_versions = set(df[version].unique().flat)
    this_versions = set([val for value in versions.values() for val in value])
    if not df_versions.issubset(this_versions):
        warnings.warn(f"Some code versions ({df_versions-this_versions})"
                      f" do not match {this_versions}."
                      f" Ensure these are not in error.", stacklevel=2)

    # Convert dictionary to dataframe
    types = pd.DataFrame.from_dict(types, orient='index').stack().to_frame()
    types = pd.DataFrame(types[0].values.tolist(),
                         index=types.index).reset_index().drop('level_1', axis=1)
    types.columns = [code_type, 'type_match']

    # Convert dictionary to dataframe
    versions = pd.DataFrame.from_dict(versions, orient='index').stack().to_frame()
    versions = pd.DataFrame(versions[0].values.tolist(),
                            index=versions.index).reset_index().drop('level_1', axis=1)
    versions.columns = [version, 'version_match']

    # Replace Type and Version in the provided dataframe with standard forms
    df = df.merge(types,
                  how='inner',
                  left_on=code_type,
                  right_on='type_match',
                  suffixes=('_x', ''))\
        .merge(versions,
               how='inner',
               left_on=version,
               right_on='version_match',
               suffixes=('_x', ''))\
        .drop(columns=[f'{version}_x', 'version_match', f'{code_type}_x', 'type_match'])

    # Remove decimals from codes
    df[code] = df[code].str.replace(r'\.', '', regex=True)
    # Ensure codes are uppercase
    df[code] = df[code].str.upper()

    # Limit the outcomes regex to their relevant sections to avoid erroneous matches
    dx9_smm, dx10_smm, px_smm = smm_map_version_split()

    # Limit the data to be matched by code_type
    df_dx = df[df[code_type] == 'DX'].copy().drop_duplicates()
    df_px = df[df[code_type] == 'PX'].copy().drop_duplicates()
    df_transfusion = df[df[code_type] == 'PX'].copy().drop_duplicates()

    # Limit the diagnoses by VERSION since these can have overlap
    df_dx9 = df_dx[df_dx[version] == ICD9].copy()
    df_dx10 = df_dx[df_dx[version] == ICD10].copy()

    # Apply the regex to the cleaned CODE column
    df_dx9['regex'] = df_dx9[code].replace(dx9_smm['smm_code'].to_list(),
                                           dx9_smm['smm_code'].to_list(),
                                           regex=True)
    df_dx10['regex'] = df_dx10[code].replace(dx10_smm['smm_code'].to_list(),
                                             dx10_smm['smm_code'].to_list(),
                                             regex=True)
    df_px['regex'] = df_px[code].replace(px_smm['smm_code'].to_list(),
                                         px_smm['smm_code'].to_list(),
                                         regex=True)
    df_transfusion['regex'] = df_transfusion[code].replace(TRANSFUSION['smm_code'].to_list(),
                                                           TRANSFUSION['smm_code'].to_list(),
                                                           regex=True)

    # Apply SMM and Transfusion indicators to the pandas df
    matched_dx9 = df_dx9.merge(dx9_smm[['smm_code', 'smm']],
                               how='inner',
                               left_on='regex',
                               right_on='smm_code',
                               suffixes=('', '_x'))
    matched_dx10 = df_dx10.merge(dx10_smm[['smm_code', 'smm']],
                                 how='inner',
                                 left_on='regex',
                                 right_on='smm_code',
                                 suffixes=('', '_x'))
    matched_px = df_px.merge(px_smm[['smm_code', 'smm']],
                             how='inner',
                             left_on='regex',
                             right_on='smm_code',
                             suffixes=('', '_x'))
    matched_transfusion = df_transfusion.merge(TRANSFUSION[['smm_code', 'transfusion']],
                                               how='inner',
                                               left_on='regex',
                                               right_on='smm_code',
                                               suffixes=('', '_x'))

    smm_encs = pd.concat([matched_dx9,
                          matched_dx10,
                          matched_px])

    # If the user wants a reporting of each indicator in addition to SMM and TRANSFUSION
    if indicators:
        # Join the SMM panda again, but keep the indicator column.
        # This may result in an indicator not being present in the
        # final output as it's not present in the data
        matched_dx9_indicators = matched_dx9.merge(_SMM[['indicator',
                                                         'smm_type',
                                                         'smm_version',
                                                         'smm_code']],
                                                   # right merge to keep all indicator columns
                                                   how='right',
                                                   left_on=[code_type,
                                                            version,
                                                            'regex'],
                                                   right_on=['smm_type',
                                                             'smm_version',
                                                             'smm_code']).dropna()
        matched_dx10_indicators = matched_dx10.merge(_SMM[['indicator',
                                                           'smm_type',
                                                           'smm_version',
                                                           'smm_code']],
                                                     # right merge to keep all indicator columns
                                                     how='right',
                                                     left_on=[code_type,
                                                              version,
                                                              'regex'],
                                                     right_on=['smm_type',
                                                               'smm_version',
                                                               'smm_code']).dropna()
        matched_px_indicators = matched_px.merge(_SMM[['indicator',
                                                       'smm_type',
                                                       'smm_version',
                                                       'smm_code']],
                                                 # right merge to keep all indicator columns
                                                 how='right',
                                                 left_on=[code_type,
                                                          version,
                                                          'regex'],
                                                 right_on=['smm_type',
                                                           'smm_version',
                                                           'smm_code']).dropna()
        # Pivot on the indicator column to get the presence of each SMM indicator
        matched_dx9_indicators = pd.pivot(matched_dx9_indicators,
                                          index=[enc_id, code],
                                          columns='indicator',
                                          values='smm') \
            .reset_index(names=[enc_id, code]) \
            .drop(columns=code) \
            .fillna(False)
        matched_dx10_indicators = pd.pivot(matched_dx10_indicators,
                                           index=[enc_id, code],
                                           columns='indicator',
                                           values='smm') \
            .reset_index(names=[enc_id, code]) \
            .drop(columns=code) \
            .fillna(False)
        matched_px_indicators = pd.pivot(matched_px_indicators,
                                         index=[enc_id, code],
                                         columns='indicator',
                                         values='smm') \
            .reset_index(names=[enc_id, code]) \
            .drop(columns=code) \
            .fillna(False)

        indicators = pd.concat([matched_dx9_indicators,
                                matched_dx10_indicators,
                                matched_px_indicators]).fillna(False)
        # Aggregate the rows down to one
        indicators = indicators.groupby(enc_id).agg(lambda x: any(x))

        # Ensure all indicators are present
        indicator_list = _SMM.indicator.drop_duplicates().to_list()
        col_list = list(set().union(indicators.columns, indicator_list))
        indicators = indicators.reindex(columns=col_list, fill_value=False)

        # Join the indicator data back to the SMM data
        smm_encs = smm_encs.merge(indicators,
                                  how='inner',
                                  left_on=enc_id,
                                  right_index=True)
        smm_encs.index.name = None

    # Prep the output data
    warnings.simplefilter('ignore', category=FutureWarning)
    output_df = smm_encs.merge(matched_transfusion[[enc_id, 'transfusion']],
                               how='outer',
                               left_on=enc_id,
                               right_on=enc_id)
    warnings.simplefilter('always')
    output_df.fillna(False, inplace=True)
    output_df['transfusion'] = output_df['transfusion'].astype(bool)
    output_df.drop(columns=[code, version, code_type, 'smm_code', 'regex'], inplace=True)
    output_df.drop_duplicates(inplace=True)

    output_df.rename(columns=restore_cols, inplace=True)

    return output_df


def smm_map_version_split():
    """
    Splits the map into separate components like ICD9 Dx, ICD10 DX, and PX

    :return: 3 dataframes for dx9, dx10, and px SMM codes
    """

    # Rename map reference
    map_df = _SMM

    # Limit the outcomes regex to their relevant sections to avoid erroneous matches
    dx9_smm = map_df[(map_df.smm_type == 'DX') & (map_df.smm_version == ICD9)]
    dx10_smm = map_df[(map_df.smm_type == 'DX') & (map_df.smm_version == ICD10)]
    px_smm = map_df[map_df.smm_type == 'PX']

    return dx9_smm, dx10_smm, px_smm
