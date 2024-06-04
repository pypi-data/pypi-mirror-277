import src.pypreg.pregnancy_outcome

if __name__  == "__main__":
    import pandas as pd
    from pandas.testing import assert_frame_equal

    pd.set_option('future.no_silent_downcasting', True)

    def test_outcome_list_output():
        from src.pypreg import OUTCOME_LIST

        print(OUTCOME_LIST)

    def test_outcomes_output():
        from src.pypreg import OUTCOMES

        print(OUTCOMES.head())

    def test_leonard_score():
        from src.pypreg import calc_index

        max_leonard_codes = [[1, 1, 'O24.49', '10', 35],
                             [1, 1, 'O98.79', '10', 35],
                             [1, 1, 'O24.09', '10', 35],
                             [1, 1, 'O34.21', '10', 35],
                             [1, 1, 'I27.09', '10', 35],
                             [1, 1, 'O30.59', '10', 35],
                             [1, 1, 'O99.59', '10', 35],
                             [1, 1, 'D66.49', '10', 35],
                             [1, 1, 'Z68.49', '10', 35],
                             [1, 1, 'O99.41', '10', 35],
                             [1, 1, 'I10.09', '10', 35],
                             [1, 1, 'O26.835', '10', 35],
                             [1, 1, 'M30.49', '10', 35],
                             [1, 1, 'O44.03', '10', 35],
                             [1, 1, 'O14.14', '10', 35],
                             [1, 1, 'O14.09', '10', 35],
                             [1, 1, 'O99.31', '10', 35],
                             [1, 1, 'O99.01', '10', 35],
                             [1, 1, 'O99.84', '10', 35],
                             [1, 1, 'O99.649', '10', 35],
                             [1, 1, 'O99.34', '10', 35],
                             [1, 1, 'O99.35', '10', 35],
                             [1, 1, 'O45.09', '10', 35],
                             [1, 1, 'O43.29', '10', 35],
                             [1, 1, 'Z3A.36', '10', 35],
                             [1, 1, 'E05.29', '10', 35]]

        min_leonard_codes = [[1, 2, 'O80', '10', 34]]

        cols = ['patient_id',
                'preg_num',
                'code',
                'version',
                'age']

        max_leonard_df = pd.DataFrame(max_leonard_codes, columns=cols)
        min_leonard_df = pd.DataFrame(min_leonard_codes, columns=cols)

        leonard_df = pd.concat([max_leonard_df,
                                min_leonard_df],
                               ignore_index=True)

        leonard_scores_df = calc_index(leonard_df,
                                       patient_col=cols[0],
                                       pregnancy_col=cols[1],
                                       code_col=cols[2],
                                       version_col=cols[3],
                                       method='leonard',
                                       age_col=cols[4]
                                       )

        expected_df = [[1, 1, 478, 281],
                       [1, 2, 0, 0]]

        expected_cols = [cols[0],
                         cols[1],
                         'leonard_smm_score',
                         'leonard_nontransfusion_smm_score']

        expected_df = pd.DataFrame(expected_df, columns=expected_cols)

        assert_frame_equal(leonard_scores_df, expected_df)


    def test_bateman_score():
        from src.pypreg import calc_index

        all_bateman_codes = [[1, 1, '416.09', '9'],
                             [1, 1, '641.09', '9'],
                             [1, 1, '282.49', '9'],
                             [1, 1, '642.39', '9'],
                             [1, 1, '642.49', '9'],
                             [1, 1, '642.59', '9'],
                             [1, 1, '581.49', '9'],
                             [1, 1, '401.49', '9'],
                             [1, 1, '412.49', '9'],
                             [1, 1, '747.49', '9'],
                             [1, 1, '710.09', '9'],
                             [1, 1, 'V08.49', '9'],
                             [1, 1, '651.49', '9'],
                             [1, 1, '304.49', '9'],
                             [1, 1, '291.49', '9'],
                             [1, 1, '649.09', '9'],
                             [1, 1, '424.49', '9'],
                             [1, 1, '428.22', '9'],
                             [1, 1, '493.49', '9'],
                             [1, 1, '250.49', '9'],
                             [1, 1, '648.89', '9'],
                             [1, 1, '649.19', '9'],
                             [1, 1, '277.09', '9'],
                             [1, 1, '654.29', '9']]

        max_bateman_codes = [[1, 2, '416.09', '9', 45],
                             [1, 2, '641.09', '9', 45],
                             [1, 2, '282.49', '9', 45],
                             [1, 2, '642.39', '9', 45],
                             [1, 2, '642.49', '9', 45],
                             [1, 2, '642.59', '9', 45],
                             [1, 2, '581.49', '9', 45],
                             [1, 2, '401.49', '9', 45],
                             [1, 2, '412.49', '9', 45],
                             [1, 2, '747.49', '9', 45],
                             [1, 2, '710.09', '9', 45],
                             [1, 2, 'V08.49', '9', 45],
                             [1, 2, '651.49', '9', 45],
                             [1, 2, '304.49', '9', 45],
                             [1, 2, '291.49', '9', 45],
                             [1, 2, '649.09', '9', 45],
                             [1, 2, '424.49', '9', 45],
                             [1, 2, '428.22', '9', 45],
                             [1, 2, '493.49', '9', 45],
                             [1, 2, '250.49', '9', 45],
                             [1, 2, '648.89', '9', 45],
                             [1, 2, '649.19', '9', 45],
                             [1, 2, '277.09', '9', 45],
                             [1, 2, '654.29', '9', 45]]

        min_bateman_codes = [[1, 3, '777.09', '9', 25]]

        gt_ht_bateman_codes = [[1, 4, '416.09', '9', 45],
                             [1, 4, '641.09', '9', 45],
                             [1, 4, '282.49', '9', 45],
                             [1, 4, '642.39', '9', 45],
                             # [1, 4, '642.49', '9', 45],
                             # [1, 4, '642.59', '9', 45],
                             [1, 4, '581.49', '9', 45],
                             # [1, 4, '401.49', '9', 45],
                             [1, 4, '412.49', '9', 45],
                             [1, 4, '747.49', '9', 45],
                             [1, 4, '710.09', '9', 45],
                             [1, 4, 'V08.49', '9', 45],
                             [1, 4, '651.49', '9', 45],
                             [1, 4, '304.49', '9', 45],
                             [1, 4, '291.49', '9', 45],
                             [1, 4, '649.09', '9', 45],
                             [1, 4, '424.49', '9', 45],
                             [1, 4, '428.22', '9', 45],
                             [1, 4, '493.49', '9', 45],
                             [1, 4, '250.49', '9', 45],
                             [1, 4, '648.89', '9', 45],
                             [1, 4, '649.19', '9', 45],
                             [1, 4, '277.09', '9', 45],
                             [1, 4, '654.29', '9', 45]]

        cols = ['patient_id',
                'preg_num',
                'code',
                'version',
                'age']

        all_bateman_df = pd.DataFrame(all_bateman_codes, columns=cols[:-1])
        max_bateman_df = pd.DataFrame(max_bateman_codes, columns=cols)
        min_bateman_df = pd.DataFrame(min_bateman_codes, columns=cols)
        gt_ht_bateman_df = pd.DataFrame(gt_ht_bateman_codes, columns=cols)

        bateman_df = pd.concat([max_bateman_df,
                                min_bateman_df,
                                gt_ht_bateman_df],
                               ignore_index=True)

        bateman_result1 = calc_index(all_bateman_df,
                                     patient_col=cols[0],
                                     pregnancy_col=cols[1],
                                     code_col=cols[2],
                                     version_col=cols[3],
                                     method='bateman')

        bateman_result = calc_index(bateman_df,
                                    patient_col=cols[0],
                                    pregnancy_col=cols[1],
                                    code_col=cols[2],
                                    version_col=cols[3],
                                    method='bateman',
                                    age_col=cols[4])

        results = pd.concat([bateman_result1,
                             bateman_result],
                            ignore_index=True)

        expected_df = [[1, 1, 42],
                       [1, 2, 45],
                       [1, 3, 0],
                       [1, 4, 40]]

        expected_cols = [cols[0],
                         cols[1],
                         'bateman_score']

        expected_df = pd.DataFrame(expected_df,
                                   columns=expected_cols)

        assert_frame_equal(results,
                           expected_df,
                           check_dtype=False)


    def test_apo():
        from src.pypreg import apo

        data = [[1, 1, 'DX', '9', '669.75'],
                [1, 1, 'DX', '9', '656.55'],
                [1, 1, 'DX', '9', '648.85'],
                [1, 1, 'DX', '9', '642.37'],
                [1, 1, 'DX', '9', '642.75'],
                [1, 2, 'DX', '9', '700.75'],
                [1, 2, 'DX', '9', '701.75'],
                [1, 2, 'DX', '9', '705.75'],
                [1, 2, 'DX', '9', '707.75'],
                [1, 2, 'DX', '9', '723.75']]

        cols = ['patient_id', 'preg_id', 'code_type', 'code_version', 'code']
        df = pd.DataFrame(data, columns=cols)

        result = apo(df, patient_id=cols[0],
                     preg_id=cols[1],
                     code_type=cols[2],
                     version=cols[3],
                     code=cols[4])

        expected = [[1, 1, True, True, True, True, True],
                    [1, 2, False, False, False, False, False]]
        expected_cols = [cols[0],
                         cols[1],
                         'cesarean',
                         'fetal growth restriction',
                         'gest diabetes mellitus',
                         'gest hypertension',
                         'preeclampsia']

        expected_df = pd.DataFrame(expected, columns=expected_cols)

        assert_frame_equal(result, expected_df)


    def test_smm():
        from src.pypreg import smm

        data = [[1, 'DX', "9", "410.12", "acute_myocardial_infarction"],
                [1, 'DX', "10", "I22.0", "acute_myocardial_infarction"],
                # [1,'DX',"9","441.12","aneurysm"],
                # [1,'DX',"10","I79.0","aneurysm"],
                [1, 'DX', "9", "584.9", "acute_renal_failure"],
                [1, 'DX', "10", "O90.4", "acute_renal_failure"],
                [1, 'DX', "9", "799.1", "adult_respiratory_distress_syndrome"],
                [1, 'DX', "10", "R09.2", "adult_respiratory_distress_syndrome"],
                [1, 'DX', "9", "673.10", "amniotic_fluid_embolism"],
                [1, 'DX', "10", "O88.119", "amniotic_fluid_embolism"],
                [1, 'DX', "9", "427.41", "cardiac_arrest_ventricular_fibrillation"],
                [1, 'DX', "10", "I49.00", "cardiac_arrest_ventricular_fibrillation"],
                [1, 'PX', "9", "99.60", "conversion_of_cardiac_rhythm"],
                [1, 'PX', "10", "5A12012", "conversion_of_cardiac_rhythm"],
                [1, 'DX', "9", "286.6", "disseminated_intravascular_coagulation"],
                [1, 'DX', "10", "O72.3", "disseminated_intravascular_coagulation"],
                [1, 'DX', "9", "642.60", "eclampsia"],
                [1, 'DX', "10", "O15.0", "eclampsia"],
                [1, 'DX', "9", "997.1", "heart_failure_arrest_during_surgery_or_procedure"],
                [1, 'DX', "10", "I97.711", "heart_failure_arrest_during_surgery_or_procedure"],
                [1, 'DX', "9", "997.02", "puerperal_cerebrovascular_disorders"],
                [1, 'DX', "10", "O87.3", "puerperal_cerebrovascular_disorders"],
                [1, 'DX', "9", "518.4", "pulmonary_edema_acute_heart_failure"],
                [1, 'DX', "10", "I50.9", "pulmonary_edema_acute_heart_failure"],
                [1, 'DX', "9", "995.86", "severe_anesthesia_complications"],
                [1, 'DX', "10", "O89.2", "severe_anesthesia_complications"],
                [1, 'DX', "9", "449", "sepsis"],
                [1, 'DX', "10", "A32.7", "sepsis"],
                [1, 'DX', "9", "998.0", "shock"],
                [1, 'DX', "10", "O75.1", "shock"],
                [1, 'DX', "9", "289.52", "sickle_cell_disease_with_crisis"],
                [1, 'DX', "10", "D57.03", "sickle_cell_disease_with_crisis"],
                [1, 'DX', "9", "415.0", "air_and_thrombotic_embolism"],
                [1, 'DX', "10", "I26.99", "air_and_thrombotic_embolism"],
                [1, 'PX', "9", "99.00", "transfusion"],
                [1, 'PX', "10", "30230H0", "transfusion"],
                [1, 'PX', "9", "68.79", "hysterectomy"],
                [1, 'PX', "10", "0UT90ZL", "hysterectomy"],
                [1, 'PX', "9", "31.1", "temporary_tracheostomy"],
                [1, 'PX', "10", "0B110F4", "temporary_tracheostomy"],
                [1, 'PX', "9", "96.72", "ventilation"],
                [1, 'PX', "10", "5A1935Z", "ventilation"],
                [1, 'PX', "9", "0000", "nothing"],
                [1, 'PX', "10", "0000", "nothing"],
                [2, 'PX', "9", "96.72", "ventilation"],
                [2, 'PX', "10", "5A1935Z", "ventilation"],
                [2, 'PX', "9", "0000", "nothing"],
                [2, 'PX', "10", "0000", "nothing"],
                [3, 'PX', "9", "0000", "nothing"],
                [3, 'PX', "10", "0000", "nothing"],
                ]

        cols = ['encounter_id', 'code_type', 'code_version', 'code', 'desc']
        df = pd.DataFrame(data, columns=cols)

        df = smm(df, enc_id=cols[0], code_type=cols[1], version=cols[2], code=cols[3], indicators=True)

        expected_data = [[1, True, True, True, True, True, True,
                          True, True, True, True, True, True, True,
                          True, True, True, True, False, True, True, True, True],
                         [2, True, False, False, False, False, False,
                          False, False, False, True, False, False, False,
                          False, False, False, False, False, False, False, False, False]
                         ]

        cols = ['encounter_id',
                'smm',
                'eclampsia',
                'amniotic_fluid_embolism',
                'severe_anesthesia_complications',
                'acute_renal_failure',
                'cardiac_arrest_ventricular_fibrillation',
                'acute_myocardial_infarction',
                'hysterectomy',
                'adult_respiratory_distress_syndrome',
                'ventilation',
                'disseminated_intravascular_coagulation',
                'heart_failure_arrest_during_surgery_or_procedure',
                'air_and_thrombotic_embolism',
                'sickle_cell_disease_with_crisis',
                'temporary_tracheostomy',
                'conversion_of_cardiac_rhythm',
                'puerperal_cerebrovascular_disorders',
                'aneurysm',
                'shock',
                'pulmonary_edema_acute_heart_failure',
                'sepsis',
                'transfusion']

        expected_df = pd.DataFrame(expected_data, columns=cols)
        df = df.reindex(columns=cols).reset_index(drop=True)

        assert_frame_equal(df, expected_df)


    def test_outcome_map_split():
        from src.pypreg import OUTCOMES, map_version_split

        out = map_version_split()

        print(OUTCOMES)

        print(out[0][out[0].outcome == 'THERAPEUTIC_ABORTION'].code.str.cat(sep='|'))
        print(out[1][out[1].outcome == 'THERAPEUTIC_ABORTION'].code.str.cat(sep='|'))
        print(out[2][out[2].outcome == 'THERAPEUTIC_ABORTION'].code.str.cat(sep='|'))
        print(out[3][out[3].outcome == 'THERAPEUTIC_ABORTION'].code.str.cat(sep='|'))

    def test_basic_preg_outcomes():
        from src.pypreg import process_outcomes, OUTCOME_LIST

        basic_date = pd.to_datetime('2010-01-01')

        data = [[1, 1, basic_date, 'DX', '9', '633.1'],
                [2, 2, basic_date, 'DX', '9', '631.8'],
                [3, 3, basic_date, 'DX', '9', '632.5'],
                [4, 4, basic_date, 'DX', '9', '635.9'],
                [5, 5, basic_date, 'DX', '9', 'V27.1'],
                [6, 6, basic_date, 'DX', '9', '650'],
                [7, 7, basic_date, 'DX', '9', '652.21'],
                ]

        cols = ['PATIENT_SK', 'ENCOUNTER_ID', 'ADMITTED_DT_TM', 'CODE_TYPE', 'CODE_VERSION', 'CODE']

        df = pd.DataFrame(data, columns=cols)

        outcome = process_outcomes(df,
                                   patient_col=cols[0],
                                   encounter_col=cols[1],
                                   admit_date_col=cols[2],
                                   version_col=cols[4],
                                   type_col=cols[3],
                                   code_col=cols[5])

        expected = [[1, 1, basic_date, OUTCOME_LIST[4],
                     pd.to_datetime('2009-10-9'), pd.to_datetime('2009-11-20'), 1],
                    [2, 2, basic_date, OUTCOME_LIST[3],
                     pd.to_datetime('2009-9-11'), pd.to_datetime('2009-11-20'), 1],
                    [3, 3, basic_date, OUTCOME_LIST[6],
                     pd.to_datetime('2009-8-21'), pd.to_datetime('2009-12-4'), 1],
                    [4, 4, basic_date, OUTCOME_LIST[5],
                     pd.to_datetime('2009-7-17'), pd.to_datetime('2009-11-20'), 1],
                    [5, 5, basic_date, OUTCOME_LIST[1],
                     pd.to_datetime('2009-3-6'), pd.to_datetime('2009-8-14'), 1],
                    [6, 6, basic_date, OUTCOME_LIST[0],
                     pd.to_datetime('2009-3-6'), pd.to_datetime('2009-7-31'), 1],
                    [7, 7, basic_date, OUTCOME_LIST[2],
                     pd.to_datetime('2009-3-6'), pd.to_datetime('2009-8-14'), 1]
                    ]

        expected_cols = [cols[0],
                         cols[1],
                         cols[2],
                         'outcome',
                         'start_window',
                         'end_window',
                         'preg_num']

        expected_df = pd.DataFrame(expected, columns=expected_cols)
        outcome = outcome[[x for x in outcome.columns if x in expected_cols]].reset_index(drop=True)

        outcome['start_window'] = pd.to_datetime(outcome['start_window'])
        outcome['end_window'] = pd.to_datetime(outcome['end_window'])

        assert_frame_equal(outcome, expected_df)

    def test_preg_hierarchy():
        from src.pypreg import process_outcomes, OUTCOME_LIST

        basic_date = pd.to_datetime('2010-01-01')

        data = [[1, 1, basic_date, 'DX', '9', '633.1'],
                [1, 2, basic_date, 'DX', '9', '631.8'],
                [1, 3, basic_date, 'DX', '9', '632.5'],
                [1, 4, basic_date, 'DX', '9', '635.9'],
                [1, 5, basic_date, 'DX', '9', 'V27.1'],
                [1, 6, basic_date, 'DX', '9', '650'],
                [1, 7, basic_date, 'DX', '9', '652.21'],
                [2, 1, basic_date, 'DX', '9', '633.1'],
                [2, 2, basic_date, 'DX', '9', '631.8'],
                [2, 3, basic_date, 'DX', '9', '632.5'],
                [2, 4, basic_date, 'DX', '9', '635.9'],
                [2, 5, basic_date, 'DX', '9', 'V27.1'],
                [2, 7, basic_date, 'DX', '9', '652.21'],
                [3, 1, basic_date, 'DX', '9', '633.1'],
                [3, 2, basic_date, 'DX', '9', '631.8'],
                [3, 3, basic_date, 'DX', '9', '632.5'],
                [3, 4, basic_date, 'DX', '9', '635.9'],
                [3, 7, basic_date, 'DX', '9', '652.21'],
                [4, 1, basic_date, 'DX', '9', '633.1'],
                [4, 2, basic_date, 'DX', '9', '631.8'],
                [4, 3, basic_date, 'DX', '9', '632.5'],
                [4, 4, basic_date, 'DX', '9', '635.9'],
                [5, 2, basic_date, 'DX', '9', '631.8'],
                [5, 3, basic_date, 'DX', '9', '632.5'],
                [5, 4, basic_date, 'DX', '9', '635.9'],
                [6, 3, basic_date, 'DX', '9', '632.5'],
                [6, 4, basic_date, 'DX', '9', '635.9'],
                ]

        cols = ['PATIENT_SK', 'ENCOUNTER_ID', 'ADMITTED_DT_TM', 'CODE_TYPE', 'CODE_VERSION', 'CODE']

        df = pd.DataFrame(data, columns=cols)

        outcome = process_outcomes(df,
                                   patient_col=cols[0],
                                   encounter_col=cols[1],
                                   admit_date_col=cols[2],
                                   version_col=cols[4],
                                   type_col=cols[3],
                                   code_col=cols[5])

        expected = [[1, 6, basic_date, OUTCOME_LIST[0],
                     pd.to_datetime('2009-3-6'), pd.to_datetime('2009-7-31'), 1],
                    [2, 5, basic_date, OUTCOME_LIST[1],
                     pd.to_datetime('2009-3-6'), pd.to_datetime('2009-8-14'), 1],
                    [3, 7, basic_date, OUTCOME_LIST[2],
                     pd.to_datetime('2009-3-6'), pd.to_datetime('2009-8-14'), 1],
                    [4, 2, basic_date, OUTCOME_LIST[3],
                     pd.to_datetime('2009-9-11'), pd.to_datetime('2009-11-20'), 1],
                    [5, 1, basic_date, OUTCOME_LIST[4],
                     pd.to_datetime('2009-10-9'), pd.to_datetime('2009-11-20'), 1],
                    [6, 4, basic_date, OUTCOME_LIST[5],
                     pd.to_datetime('2009-7-17'), pd.to_datetime('2009-11-20'), 1],
                    ]

        expected_cols = [cols[0],
                         cols[1],
                         cols[2],
                         'outcome',
                         'start_window',
                         'end_window',
                         'preg_num']

        expected_df = pd.DataFrame(expected, columns=expected_cols)
        outcome = outcome[[x for x in outcome.columns if x in expected_cols]].reset_index(drop=True)

        outcome['start_window'] = pd.to_datetime(outcome['start_window'])
        outcome['end_window'] = pd.to_datetime(outcome['end_window'])

        assert_frame_equal(outcome, expected_df)

    def test_multiple_pregs():
        from src.pypreg import process_outcomes, OUTCOME_LIST

        data = [[1, 1, pd.to_datetime('2010-01-01'), 'DX', '9', '633.1'],
                [1, 8, pd.to_datetime('2010-01-05'), 'DX', '9', '632.5'],
                [1, 2, pd.to_datetime('2010-2-26'), 'DX', '9', '631.8'],
                [1, 3, pd.to_datetime('2010-4-9'), 'DX', '9', '632.5'],
                [1, 4, pd.to_datetime('2010-6-4'), 'DX', '9', '635.9'],
                [1, 5, pd.to_datetime('2010-11-5'), 'DX', '9', 'V27.1'],
                [1, 6, pd.to_datetime('2011-5-6'), 'DX', '9', '650'],
                [1, 7, pd.to_datetime('2011-10-21'), 'DX', '9', '652.21'],
                ]

        cols = ['PATIENT_SK', 'ENCOUNTER_ID', 'ADMITTED_DT_TM', 'CODE_TYPE', 'CODE_VERSION', 'CODE']

        df = pd.DataFrame(data, columns=cols)

        outcome = process_outcomes(df,
                                   patient_col=cols[0],
                                   encounter_col=cols[1],
                                   admit_date_col=cols[2],
                                   version_col=cols[4],
                                   type_col=cols[3],
                                   code_col=cols[5])

        expected = [[1, 1, pd.to_datetime('2010-01-01'), OUTCOME_LIST[4],
                     pd.to_datetime('2009-10-9'), pd.to_datetime('2009-11-20'), 1],
                    [1, 2, pd.to_datetime('2010-2-26'), OUTCOME_LIST[3],
                     pd.to_datetime('2010-1-15'), pd.to_datetime('2010-1-15'), 2],
                    [1, 3, pd.to_datetime('2010-4-9'), OUTCOME_LIST[6],
                     pd.to_datetime('2010-3-12'), pd.to_datetime('2010-3-12'), 3],
                    [1, 4, pd.to_datetime('2010-6-4'), OUTCOME_LIST[5],
                     pd.to_datetime('2010-4-23'), pd.to_datetime('2010-4-23'), 4],
                    [1, 5, pd.to_datetime('2010-11-5'), OUTCOME_LIST[1],
                     pd.to_datetime('2010-6-18'), pd.to_datetime('2010-6-18'), 5],
                    [1, 6, pd.to_datetime('2011-5-6'), OUTCOME_LIST[0],
                     pd.to_datetime('2010-12-3'), pd.to_datetime('2010-12-3'), 6],
                    [1, 7, pd.to_datetime('2011-10-21'), OUTCOME_LIST[2],
                     pd.to_datetime('2011-6-3'), pd.to_datetime('2011-6-3'), 7]
                    ]

        expected_cols = [cols[0],
                         cols[1],
                         cols[2],
                         'outcome',
                         'start_window',
                         'end_window',
                         'preg_num']

        expected_df = pd.DataFrame(expected, columns=expected_cols)
        outcome = outcome[[x for x in outcome.columns if x in expected_cols]].reset_index(drop=True)

        outcome['start_window'] = pd.to_datetime(outcome['start_window'])
        outcome['end_window'] = pd.to_datetime(outcome['end_window'])

        assert_frame_equal(outcome, expected_df)
    

    test_smm()
    test_outcome_map_split()
    test_basic_preg_outcomes()
    test_multiple_pregs()
    test_apo()
    test_bateman_score()
    test_leonard_score()
    test_outcomes_output()
    test_outcome_list_output()
