History
-------

v11.4.0 (04 June 2024)
++++++++++++++++++++++
- Add support for begin_at_strategy parameter in
  get_calibration_constant_versions_by_detector_conditions api
- Fix update_calibration_constant_version method due to the introduction of
  new field in the CCV serialization

v11.3.0 (11 July 2023)
++++++++++++++++++++++
 - Restrict version of requests to <2.30 to avoid OpenSSL version problem
 - Return HTTP status code as part of responses
 - Add support for retrieving CCVs by report ID or path
 - Adapt the Report API tests to reflect the new Reports requirements in CalCat

v11.2.0 (06 January 2022)
++++++++++++++++++++++++++
- Replace `snapshot_at` parameter with `pdu_snapshot_at` when specific to PDUs
- Take into account additional not updatable fields in CCV (`created_at`)
- Adjust tests for additional changes in CalCat

v11.1.0 (15 November 2022)
++++++++++++++++++++++++++
- Add support for new `flg_text` in Parameters API

v11.0.0 (23 June 2022)
+++++++++++++++++++++
- Add new CalCat APIs for Report failsafe creation
- Add new CalCat APIs for CCVs retrieval with strategy prior_in_time and multiple CCs
- Implemented pagination meta-information from CalCat
- Removed support for Python 3.6
- Update external dependency

v10.0.0 (10 May 2022)
+++++++++++++++++++++
- Add option `use_oauth2` for clients to have the possibility to connect to proxy services

*IMPORTANT* - CalibrationClient class signature broke retro-compatibility in case you are using/expecting 'Positional Arguments'. *Please invoke this class using 'keyword arguments'*.

v9.2.0 (9 May 2022)
+++++++++++++++++++
- Update internal libraries used as external_dependencies, especially oauth2_xfel_client
- Expose `max_retries`, `timeout` and `ssl_verify` parameters from oauth2_xfel_client
- Improve documentation in README file

v9.1.0 (14 December 2021)
+++++++++++++++++++++++++
- Add new CalCat APIs to interact with Calibration Constant Versions
- Update external dependency
- Add python 3.10 to Gitlab-ci

v9.0.6 (3 June 2021)
++++++++++++++++++++
- Fix broken tag in pypi.org
- Remove not used /docs folder

v9.0.5 (2 June 2021)
++++++++++++++++++++
- Update external dependency

v9.0.4 (30 April 2021)
++++++++++++++++++++++
- Remove Condition name truncation when generating the new name for the Calibration Constant to avoid that a Calibration Constant injection fails due to the name uniqueness constraint.
- Update external dependency urllib3
- Stop supporting Python 3.5
- Start supporting Python 3.9

v9.0.3 (9 January 2021)
+++++++++++++++++++++++
- Update external dependencies
- Include UUID parameter in PDUs API tests to guarantee the parameter is present in the received response

v9.0.2 (9 December 2020)
++++++++++++++++++++++++
- Apply security patch

v9.0.1 (8 December 2020)
++++++++++++++++++++++++
- Update external dependencies
- Adapt detectors APIs tests to changes in performed on CalCat service

  - Adapt to immutable identifiers in CalCat detectors' model.
  - Adapt to order in which Physical Detector Units are returned.

v9.0.0 (15 July 2020)
+++++++++++++++++++++
- Rename strategy 'closest_by_pdu' to 'pdu_closest_by_time'
- Rename strategy 'exactly_contained_by_pdu' to 'pdu_prior_in_time'
- Rename strategy 'closest_by_detector' to 'detector_closest_by_time'

v8.0.1 (29 June 2020)
+++++++++++++++++++++
- Reformat code
- Solve all pycodestyle findings

v8.0.0 (29 June 2020)
+++++++++++++++++++++
- Update CalCat APIs from version 1 to version 2
- Update APIs tests to validate CalCat version 2 APIs successfully
- Update retrieve and inject APIs to take into account the return strategy:

  - `closest_by_pdu`
  - `exactly_contained_by_pdu`
  - `closest_by_detector`
  - Default value is: `closest_by_detector`

- Add new APIs:

  - PhysicalDetectorUnitApi:

    - `get_all_physical_detector_units_by_detector_id_api`
    - `get_all_physical_detector_units_by_det_and_krbda_api`

  - DetectorApi:

    - `create_detector_api`
    - `delete_detector_api`
    - `update_detector_api`
    - `get_detector_by_id_api`
    - `get_all_detectors_by_name_api`
    - `get_all_detectors_by_identifier_api`

  - ReportApi:
  
    - `create_report_api`
    - `delete_report_api`
    - `update_report_api`
    - `get_report_by_id_api`
    - `get_all_reports_by_name_api`
    - `get_all_reports_by_name_and_file_path_api`
- Upgrade internal libraries versions in use

v7.0.0 (8 June 2020)
++++++++++++++++++++
- Improve README documentation
- Improve setup.py
- Upgrade tests to use pytest
- Upgrade internal libraries versions in use

v6.1.3 (21 August 2019)
+++++++++++++++++++++++
- Improve setup.py so that information in pypi.org is better rendered
- Upgrade oauth2_xfel_client library to version 5.1.1

v6.1.2 (16 August 2019)
+++++++++++++++++++++++
- Add gitlab-ci
- Solve issues in tests when executed in gitlab-ci due to long hostname

v6.1.1 (12 August 2019)
+++++++++++++++++++++++
- Minor tests related code improvements

v6.1.0 (6 August 2019)
++++++++++++++++++++++
- Update dependencies versions

v6.0.0 (6 August 2019)
++++++++++++++++++++++
- Applied change of strategy in the `retrieve_calibration_constant_version` API as discussed on MR10.

 - With the applied changes all conditions in the boundaries will be taken into account... and from them, the respective Calibration Constant Version `begin_at` with the closest ABSOLUTE (past or future) datetime interval to the desired `event_at` will be returned.
 - Please note that the API `retrieve_all_calibration_constant_versions` will return all the matching Calibration Constant Versions order by the closest ABSOLUTE datetime interval to the desired `event_at`

- Added new methods to calibration_client to return.

 - APIs:

  - `calibration_api -> get_all_calibration_constants_by_conditions_api` to get all avaialble calibration constants of several conditions
  - `calibration_constant_api -> get_closest_calibration_constant_version_api` to get the closest avaialble (smaller distance between provided event_at and CCV.begin_at) calibration constant version from several calibration constants
  - `calibration_constant_api -> get_all_calibration_constant_versions_api` to get all avaialble calibration constant versions from several calibration constants

 - Modules:

  - `calibration_constant -> get_all_by_conditions` to get all calibration constants from all matching conditions
  - `calibration_constant_version -> get_closest_by_time` that user API `get_closest_calibration_constant_version_api` method
  - `calibration_constant_version -> get_all_versions` that user API `get_all_calibration_constant_version_api` method

 - Statically available:

  - `search_possible_conditions_from_dict` to get all avaialble matching conditions ordered by closest date
  - `retrieve_all_calibration_constant_versions` to return all avaialble calibration constant versions of all avaialble matching conditions

v5.0.1 (6 December 2018)
++++++++++++++++++++++++
- Hotfix for returning newest CalibrationConstant by default

v5.0.0 (21 December 2017)
+++++++++++++++++++++++++
- Upgrade oauth2_client library to oauth2_xfel_client version 5.0.0
- Upgrade oauthlib library to version 2.0.6

v4.0.0 (1 November 2017)
++++++++++++++++++++++++
- Upgrade library to contain dependent libraries
- Update dependencies versions in use
- Update descriptions

v3.0.0 (7 March 2017)
+++++++++++++++++++++
- Separate this Python library from the KaraboDevices code.
- Clean code and remove all references to Karabo.
- Set up new project under ITDM group in Gitlab.

v2.0.0 (4 November 2016)
++++++++++++++++++++++++
- Update library dependencies
- Integrate this library with Karabo 2.0

v1.0.0 (4 December 2015)
++++++++++++++++++++++++
- First official release

v0.0.1 (20 June 2015)
+++++++++++++++++++++
- Initial code
