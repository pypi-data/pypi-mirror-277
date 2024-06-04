"""
This module is a collection of functions needed to take longitudinal
patient data and identify and classify pregnancies.

Copyright (C) 2023 Dave Walsh

Available functions
subsequent_outcome : Returns a pandas dataframe with the date of the next
    possible outcome for each outcome type
process_spacing : Returns a pandas dataframe with additional timing information
spacing : Utility to set up process_spacing
validate_outcomes : Selects the outcome classification based on a hierarchy
next_event_valid : Compares two events to determine if one is valid
number_pregnancy : Calculates the gravida number for each pregnancy
set_preg_window : Utility function to convert spacing data to dates
calc_preg_window : Utility function to calculate a date from a date and offset
select_valid : Utility function that selects only the rows that are indicated as valid
check_window : Utility to adjust the start window dates for valid pregnancies
standardize_type_and_version : Utility function to accept a variety of configurations
    for DX, PX, DRG codes and versions
process_outcomes : Main function to process pregnancy data.

"""

import pandas as pd
from .attach_map import attach_map
from .outcome_map import OUTCOME_LIST


BAD_DATE = pd.to_datetime('1900-01-01')
MAX_TERM = 'max_term'
MIN_TERM = 'min_term'
SUBSEQUENT = 'subsequent_preg'
EVENT_DATE = 'event_date'

# Dictionary that defines the distance to the next feasible event date.
#     Key: Current event outcome class
#     Value: List of days to next outcome code_type in order:
#         0: LIVE_BIRTH
#         1: STILLBIRTH
#         2: unknown DELIVERY
#         3: TROPHOBLASTIC
#         4: ECTOPIC
#         5: therapeutic abortion
#         6: spontaneous abortion
NEXT_OUTCOME = {OUTCOME_LIST[0]: pd.to_timedelta([182, 168, 168, 70, 70, 70, 56], unit='d'),
                OUTCOME_LIST[1]: pd.to_timedelta([182, 168, 168, 70, 70, 70, 56], unit='d'),
                OUTCOME_LIST[2]: pd.to_timedelta([182, 168, 168, 70, 70, 70, 56], unit='d'),
                OUTCOME_LIST[3]: pd.to_timedelta([168, 154, 154, 56, 56, 56, 42], unit='d'),
                OUTCOME_LIST[4]: pd.to_timedelta([168, 154, 154, 56, 56, 56, 42], unit='d'),
                OUTCOME_LIST[5]: pd.to_timedelta([168, 154, 154, 56, 56, 56, 42], unit='d'),
                OUTCOME_LIST[6]: pd.to_timedelta([168, 154, 154, 56, 56, 56, 42], unit='d')}


def subsequent_outcome(df: pd.DataFrame,
                       outcome: str,
                       admit_col: str):
    """
    Utility function that calculates the event date of the next outcome class.

    Distance is based on that given by Moll. NEXT_OUTCOME is a globally defined dictionary.

    :param df: Pandas dataframe that contains pregnancy OUTCOMES of a single code_type
    :param outcome: String that defines the outcome classification - use the OUTCOME_LIST
    :param admit_col: Column in the dataframe that contains the date of the outcome

    :return: Returns the dataframe with 7 new columns that define the feasible
    date a subsequent outcome of each class can occur
    """

    df['next_lb'] = df[admit_col] + NEXT_OUTCOME[outcome][0]
    df['next_sb'] = df[admit_col] + NEXT_OUTCOME[outcome][1]
    df['next_uk'] = df[admit_col] + NEXT_OUTCOME[outcome][2]
    df['next_tr'] = df[admit_col] + NEXT_OUTCOME[outcome][3]
    df['next_ec'] = df[admit_col] + NEXT_OUTCOME[outcome][4]
    df['next_ab'] = df[admit_col] + NEXT_OUTCOME[outcome][5]
    df['next_sa'] = df[admit_col] + NEXT_OUTCOME[outcome][6]

    return df


def process_spacing(df: pd.DataFrame,
                    admit_col: str,
                    outcome_col: str,
                    patient_col: str):
    """
    Calculate the dates for the max term, min term, subsequent starts, and subsequent outcomes

    :param df: Pandas dataframe containing encounters classified to a pregnancy outcome
    :param admit_col: Column containing the admit date
    :param outcome_col: Column containing the outcome classification
    :param patient_col: Column containing the patient identifier

    :return: Returns the original pandas dataframe with the pregnancy
    start window (Max term and Min term) and the subsequent event dates added in.
    """

    # Sets the pregnancy start window, and the feasible start date of the next pregnancy
    df['Max_Term_Date'] = df[admit_col] - pd.to_timedelta(df[MAX_TERM], unit='d')
    df['Min_Term_Date'] = df[admit_col] - pd.to_timedelta(df[MIN_TERM], unit='d')
    df['Subsequent_Start_Date'] = pd.to_datetime(df[admit_col]) +\
                                  pd.to_timedelta(df[SUBSEQUENT], unit='d')

    # Split the data frame up by classification
    df_lb = df[df[outcome_col] == OUTCOME_LIST[0]]
    df_sb = df[df[outcome_col] == OUTCOME_LIST[1]]
    df_uk = df[df[outcome_col] == OUTCOME_LIST[2]]
    df_tr = df[df[outcome_col] == OUTCOME_LIST[3]]
    df_ec = df[df[outcome_col] == OUTCOME_LIST[4]]
    df_ab = df[df[outcome_col] == OUTCOME_LIST[5]]
    df_sa = df[df[outcome_col] == OUTCOME_LIST[6]]

    # Calculate the subsequent outcome date using the outcome separated dataframes
    df_lb = subsequent_outcome(df_lb, OUTCOME_LIST[0], admit_col)
    df_sb = subsequent_outcome(df_sb, OUTCOME_LIST[1], admit_col)
    df_uk = subsequent_outcome(df_uk, OUTCOME_LIST[2], admit_col)
    df_tr = subsequent_outcome(df_tr, OUTCOME_LIST[3], admit_col)
    df_ec = subsequent_outcome(df_ec, OUTCOME_LIST[4], admit_col)
    df_ab = subsequent_outcome(df_ab, OUTCOME_LIST[5], admit_col)
    df_sa = subsequent_outcome(df_sa, OUTCOME_LIST[6], admit_col)

    # Recombine the data and sort
    output = pd.concat([df_lb, df_sb, df_uk, df_tr, df_ec, df_ab, df_sa])
    output = output.sort_values(by=[patient_col, admit_col])\
        .reset_index(drop=True)

    return output


def spacing(df: pd.DataFrame,
            patient_col: str,
            outcome_col: str,
            admit_col: str):
    """
    Utility function to setup and start adding spacing data to classified encounters

    :param df: Pandas dataframe containing classified encounters
    :param patient_col: Column containing the patient identifier
    :param outcome_col: Column containing the outcome classification
    :param admit_col: Column containing the encounter admit date

    :return: Returns the original dataframe with the spacing information
    added defining the pregnancy start window for the current outcome as
    well as the spacing to the next pregnancy start and next pregnancy
    outcome by class. The subsequent pregnancy data is used to validate
    pregnancy outcomes as possible longitudinally.
    """

    # Set up a pandas data frame with day spacing from the event date
    data = {outcome_col: OUTCOME_LIST,
            MAX_TERM: [301, 301, 301, 112, 84, 168, 133],
            MIN_TERM: [154, 140, 140, 42, 42, 42, 28],
            SUBSEQUENT: [28, 28, 28, 14, 14, 14, 14]}
    spacing_df = pd.DataFrame(data)

    # Join the spacing data to the classified encounters
    joined_df = df.merge(spacing_df,
                         how='left',
                         left_on=outcome_col,
                         right_on=outcome_col)

    # Get all of the spacing data from utility functions
    output = process_spacing(joined_df,
                             admit_col=admit_col,
                             outcome_col=outcome_col,
                             patient_col=patient_col)

    return output


def validate_outcomes(df: pd.DataFrame,
                      outcome_col: str,
                      admit_col: str,
                      encounter_col: str):
    """
    Receives a df sliced by the unique patient identifier. Iterates over
    each encounter within an individual and validates the outcome types.
    Outcome types are processed according to the hierarchical order
    to determine validity.

    :param df: Pandas dataframe containing the classified encounters and spacing data
    :param outcome_col: Column that contains the outcome classification
    :param admit_col: Column that contains the admit date for the encounter
    :param encounter_col: Column that contains the encounter identifier

    :return: Returns the original pandas dataframe with the
    outcome_valid column appended and completed. 1 indicates
    the outcome classification is valid.
    """

    df.reset_index(drop=True, inplace=True)

    # Outcome_list is ordered in the hierarchy
    for outcome in OUTCOME_LIST:
        # Iterate over each classified encounter in a patient
        for idx, row in df.iterrows():
            # If the outcome in the row matches the current outcome in the hierarchy - proceed
            if df.iloc[idx][outcome_col] == outcome:
                # If the current row has not already been determined to be valid - proceed
                if not df.iloc[idx]['outcome_valid']:
                    # Temp dataframe that holds all the classified encounters that are valid
                    df_valid = df[df['outcome_valid']]
                    # If there are no previously found valid classified encounters
                    # if len(df_valid.index) == 0:
                    if df_valid.empty:
                        # This encounter is valid by default as it sits at
                        # the top of the hierarchy in this patient's data
                        df.loc[idx, 'outcome_valid'] = True
                        df.loc[idx, 'event_date'] = df.loc[idx, admit_col]
                    else:
                        # If other valid encounters exist, add the current
                        # encounter to that timeline and sort it
                        df_valid = pd.concat([row.to_frame(1).T, df_valid], axis=0)\
                            .sort_values(by=[admit_col, encounter_col])\
                            .reset_index(drop=True)
                        # Get the list of indices for the current encounter
                        current_index = df_valid[df_valid[encounter_col] ==
                                                 df[encounter_col].iloc[idx]].index.values
                        if len(current_index) == 1:
                            # if false, the encounter already exists with a valid outcome

                            # Initialize default values
                            valid = False
                            event_dt = BAD_DATE

                            if current_index[0] == 0:  # First in the list
                                # Only need to check the event after
                                valid, event_dt = next_event_valid(df_valid.iloc[0],
                                                                   df_valid.iloc[1],
                                                                   base=0)
                            elif current_index[0] == df_valid.index.max():  # Last in the list
                                # Only need to check the event before
                                valid, event_dt = \
                                    next_event_valid(df_valid.iloc[current_index[0] - 1],
                                                     df_valid.iloc[current_index[0]],
                                                     base=1)
                            else:
                                # Check before and after, both must be valid
                                valid_before, event_before = \
                                    next_event_valid(df_valid.iloc[current_index[0] - 1],
                                                     df_valid.iloc[current_index[0]],
                                                     base=1)
                                valid_after, event_after = \
                                    next_event_valid(df_valid.iloc[current_index[0]],
                                                     df_valid.iloc[current_index[0] + 1],
                                                     base=0)
                                if valid_before & valid_after:
                                    valid = valid_before
                                    event_dt = event_before
                            # Set the validity
                            df.loc[idx, 'outcome_valid'] = valid
                            df.loc[idx, 'event_date'] = event_dt

    return df


def next_event_valid(first_event: pd.DataFrame,
                     second_event: pd.DataFrame,
                     base: int):
    """
    Utility function to determine if an event is valid compared to the other

    :param first_event: Pandas dataframe that contains a classified encounter with spacing data
    :param second_event: Pandas dataframe that contains a classified encounter with spacing data
    :param base: Switch to determine which event is the primary event to compare against

    :return: Returns boolean validity and the date (global bad date is returned if not valid)
    """

    valid_base = [0, 1]
    if base not in valid_base:
        raise ValueError(f'next_event_valid: base must be one of {valid_base}. {valid_base[0]}'
                         f' to select the first event as the base, {valid_base[1]} for the other.')

    colname_translate = {OUTCOME_LIST[0]: 'next_lb',
                         OUTCOME_LIST[1]: 'next_sb',
                         OUTCOME_LIST[2]: 'next_uk',
                         OUTCOME_LIST[3]: 'next_tr',
                         OUTCOME_LIST[4]: 'next_ec',
                         OUTCOME_LIST[5]: 'next_ab',
                         OUTCOME_LIST[6]: 'next_sa',
                         }

    col = colname_translate[second_event.outcome]

    outcome_valid = second_event.admit >= first_event[col]

    if outcome_valid:
        if base == valid_base[0]:
            return True, first_event.admit
        else:
            return True, second_event.admit
    else:
        return False, BAD_DATE


def outcomes(df: pd.DataFrame,
             max_id: str,
             patient_col: str,
             encounter_col: str,
             admit_date_col: str,
             outcome_col: str):
    """
    Deprecated

    :param df:
    :param max_id:
    :param patient_col:
    :param encounter_col:
    :param admit_date_col:
    :param outcome_col:
    :return:
    """

    cols = [patient_col,
            encounter_col,
            admit_date_col,
            outcome_col]

    if len(df[patient_col].unique()) > 1:
        raise ValueError(f'OUTCOMES: More than 1 patient received. '
                         f'Limit dataframe to only include 1 patient at a time.')

    df = df[cols]

    print(f'{df.loc[df.index[0]][patient_col]}/{max_id}')

    # Get the spacing data
    df_spacing_data = spacing(df,
                              patient_col=patient_col,
                              outcome_col=outcome_col,
                              admit_col=admit_date_col)

    # Prepare columns to validate the OUTCOMES
    df_spacing_data = df_spacing_data.assign(outcome_valid=lambda x: False,
                                             event_date=lambda x: BAD_DATE)

    output = validate_outcomes(df_spacing_data,
                               outcome_col=outcome_col,
                               admit_col=admit_date_col,
                               encounter_col=encounter_col)

    output = select_valid(output)
    output = set_preg_window(output)
    output = number_pregnancy(output,
                              patient_col=patient_col,
                              admit_col=admit_date_col)
    output = check_window(output)

    return output


def number_pregnancy(df: pd.DataFrame,
                     patient_col: str,
                     admit_col: str):
    """
    Utility function that numbers the pregnancies of a patient. Synonymous with gravida

    :param df: Pandas dataframe with validated classified encounters
    where each row indicates an individual pregnancy outcome
    :param patient_col: Column that contains the patient identifier
    :param admit_col: Column that contains the admit date of the encounter

    :return: Returns the original dataframe with the preg_num appended in the columns
    """

    df.sort_values(by=[patient_col, admit_col], inplace=True)
    df['preg_num'] = df.groupby(patient_col).cumcount() + 1

    return df


def set_preg_window(df: pd.DataFrame):
    """
    Utility function to convert the spacing data to a date for the
    pregnancy window start and end

    :param df: Pandas dataframe containing classified pregnancies with an event_date,
    max_term, and min_term present

    :return: Returns the original dataframe with the start_window and end_window
    dates appended to the columns
    """
    df = df.assign(start_window=lambda x: calc_preg_window(x[EVENT_DATE],
                                                           pd.to_timedelta(x[MAX_TERM], unit='d')),
                   end_window=lambda x: calc_preg_window(x[EVENT_DATE],
                                                         pd.to_timedelta(x[MIN_TERM], unit='d')))
    df.event_date = df.event_date.dt.date
    df.start_window = df.start_window.dt.date
    df.end_window = df.end_window.dt.date

    return df


def calc_preg_window(date, offset):
    """
    Utility function to calculate a date from a base date and an offset.
    Function is designed assuming the offset refers to the past.
    Future dates should use a negative offset.

    :param date: Base date
    :param offset: Offset in days

    :return: Returns the new date offset from the base date
    """
    return_date = date - pd.to_timedelta(offset, unit='d')

    return return_date


def select_valid(df: pd.DataFrame):
    """
    Utility function that selects only the rows where outcome_valid is True

    :param df: Pandas dataframe that contains the outcome_valid as a boolean column.

    :return: Returns a pandas dataframe where all rows have True outcome_valid
    """
    return df[df.outcome_valid]


def check_window(df: pd.DataFrame):
    """
    Utility function that adjusts the start window of a subsequent pregnancy per Moll

    :param df: Pandas dataframe with classified pregnancies with all date information

    :return: Returns the original pandas dataframe with the start_window adjusted if required
    """
    df.reset_index(drop=True, inplace=True)
    for idx, row in df.iterrows():
        if idx > 0:
            if df.loc[idx, 'start_window'] <= df.loc[idx - 1, 'event_date']:
                df.loc[idx, 'start_window'] = calc_preg_window(df.loc[idx - 1, 'event_date'],
                                                             -1 * df.loc[idx - 1, 'subsequent_preg'])

    return df


def standardize_type_and_version(df: pd.DataFrame,
                                 type_col: str,
                                 version_col: str):
    """
    Utility function to standardize the data present in the code_type
    and version columns to allow for later matching. Function will warn
    user about variations that are not acceptable to allow them to correct
    the information before running again.

    :param df: Pandas dataframe that contains patient encounter data with diagnostic,
    procedure, and DRG codes and code metadata. Codes should be labeled as being diagnostic,
    procedure, or DRG with the appropriate coding system.
    :param type_col: Column containing CODE information regarding diagnostic, PROCEDURE, or DRG
    :param version_col: Column containing information about the coding system for the CODE

    :return: Returns the original pandas dataframe with the code_type and
    version data replaced with standard forms if they match acceptable variations.
    """

    import warnings

    # Types can accept a CODE label as dx/DIAGNOSIS/diagnostic,
    # px/PROCEDURE, DRG/diagnostic related group
    types = dict()
    types['DX'] = ('dx',
                   'DIAGNOSIS',
                   'diagnostic')
    types['PX'] = ('px',
                   'PROCEDURE')
    types['DRG'] = ('DRG',
                    'diagnostic related group')

    # Versions can accept different coding systems: 9/ICD9, 10/ICD10/ICD10-CM/ICD10-PCS
    versions = dict()
    versions['ICD9'] = ('9',
                        'ICD9')
    versions['ICD10'] = ('10',
                         'ICD10',
                         'ICD10-CM',
                         'ICD10-PCS')
    versions['CPT'] = ('CPT',
                       'CPT4',
                       'HCPCS')
    versions['DRG'] = ('DRG',
                       'MS-DRG')

    # Check the contents of the Type column and warn user if
    # the contents don't match the expected types. This doesn't constitute
    # an error as the dataset could contain valid codes from other systems for other uses
    df[type_col] = df[type_col].str.lower()
    df_types = set(df[type_col].unique().flat)
    this_types = set([val for value in types.values() for val in value])
    if not df_types.issubset(this_types):
        warnings.warn(f"Some code types ({df_types-this_types}) do not match {this_types}."
                      f" Ensure these are not in error.", stacklevel=2)

    # Check the contents of the Version column and warn user if
    # the contents don't match the expected. This doesn't constitute
    # an error as the dataset could contain valid codes from other systems for other uses
    df[version_col] = df[version_col].str.upper()
    df_versions = set(df[version_col].unique().flat)
    this_versions = set([val for value in versions.values() for val in value])
    if not df_versions.issubset(this_versions):
        warnings.warn(f"Some code versions ({df_versions-this_versions})"
                      f" do not match {this_versions}."
                      f" Ensure these are not in error.", stacklevel=2)

    # Convert dictionary to dataframe
    types = pd.DataFrame.from_dict(types, orient='index').stack().to_frame()
    types = pd.DataFrame(types[0].values.tolist(),
                         index=types.index).reset_index().drop('level_1', axis=1)
    types.columns = [type_col, 'type_match']

    # Convert dictionary to dataframe
    versions = pd.DataFrame.from_dict(versions, orient='index').stack().to_frame()
    versions = pd.DataFrame(versions[0].values.tolist(),
                            index=versions.index).reset_index().drop('level_1', axis=1)
    versions.columns = [version_col, 'version_match']

    # Replace Type and Version in the provided dataframe with standard forms
    df = df.merge(types,
                  how='inner',
                  left_on=type_col,
                  right_on='type_match',
                  suffixes=('_x', ''))\
        .merge(versions,
               how='inner',
               left_on=version_col,
               right_on='version_match',
               suffixes=('_x', ''))\
        .drop(columns=[f'{version_col}_x',
                       'version_match',
                       f'{type_col}_x',
                       'type_match'])

    return df


def process_outcomes(df: pd.DataFrame,
                     patient_col: str,
                     encounter_col: str,
                     admit_date_col: str,
                     version_col: str,
                     type_col: str,
                     code_col: str,
                     expanded: bool = False):
    """
    Main function to classify pregnancies. Accepts a dataframe with the listed columns to begin the
    pregnancy classification.

    :param df: Pandas dataframe with encounter data - rows should be unique to each CODE provided
    :param patient_col: Column containing the unique patient identifier
    :param encounter_col: Column containing the encounter identifier
    :param admit_date_col: Column containing the admit date for the encounter
    :param version_col: Column containing the coding system for the provided CODE
    :param type_col: Column containing if the CODE describes a PROCEDURE, DIAGNOSIS, or DRG
    :param code_col: Column containing the CODE.
    :param expanded: Boolean flag to indicate if the classification should use the
    Moll and crosswalked codes or if the additional codes added by the author should
    be included in the classification process

    :return: Returns a pandas dataframe containing a single row per pregnancy, the pregnancy number,
    the outcome classification, and date information about the pregnancy start window
    """

    from .outcome_map import OUTCOME_COL

    # Set a reference for the column names used in the package to the provided column names.
    package_cols = {admit_date_col: 'admit',
                    patient_col: 'group_id',
                    encounter_col: 'encounter_id',
                    version_col: 'version',
                    type_col: 'code_type',
                    code_col: 'code',
                    }
    # Set a dictionary to restore the original column names
    restore_cols = {i: j for j, i in package_cols.items()}

    # Refactor the passed column names
    admit_date_col = package_cols[admit_date_col]
    patient_col = package_cols[patient_col]
    encounter_col = package_cols[encounter_col]
    version_col = package_cols[version_col]
    type_col = package_cols[type_col]
    code_col = package_cols[code_col]

    # A lot of operations are done on the original dataframe, this turns off the warning
    pd.options.mode.chained_assignment = None

    # Set the column names to what is used throughout the package
    df.rename(columns=package_cols, inplace=True)

    # Standardize the CODE metadata
    data = standardize_type_and_version(df,
                                        type_col,
                                        version_col)

    # Classify each row based on the CODE and CODE metadata
    data = attach_map(data,
                      code_col,
                      type_col,
                      version_col,
                      expanded)
    # Utility to give an idea of progress
    # max_id = data[patient_col].max()

    # Get the spacing data
    df_spacing_data = spacing(data,
                              patient_col=patient_col,
                              outcome_col=OUTCOME_COL,
                              admit_col=admit_date_col)
    # Prepare columns to validate the OUTCOMES
    df_spacing_data['outcome_valid'] = False
    df_spacing_data['event_date'] = BAD_DATE

    # Code metadata is no longer needed at this stage - also lose the duplicates
    df_spacing_data.drop(columns=[code_col, type_col, version_col], inplace=True)
    df_spacing_data.drop_duplicates(inplace=True)

    # Validate the OUTCOMES for each patient
    pregs = df_spacing_data.groupby(patient_col,
                                    group_keys=True)\
        .apply(validate_outcomes,
               outcome_col=OUTCOME_COL,
               admit_col=admit_date_col,
               encounter_col=encounter_col,
               include_groups=False)\
        .reset_index(level=0, names=patient_col)

    # Only keep the valid patients
    output = select_valid(pregs)

    # Set the pregnancy start window
    output = set_preg_window(output)

    # Prepare dataframe to get the pregnancy number
    output.reset_index(drop=True, inplace=True)
    output = number_pregnancy(output, patient_col=patient_col, admit_col=admit_date_col)

    # Adjust the start window date if needed
    output = output.groupby(patient_col,
                            group_keys=True)\
        .apply(check_window,
               include_groups=False)\
        .reset_index(level=0, names=patient_col)

    # Restore the pandas settings
    pd.options.mode.chained_assignment = 'warn'

    # Restore the column names
    output.rename(columns=restore_cols, inplace=True)

    return output
