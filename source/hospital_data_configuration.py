from constants import PATIENT_ID, START_DATE, END_DATE, ACTIVE, DISPLAY_NAME, DIAGNOSES, TREATMENT_LINE, \
    NUMBER_OF_CYCLES, TREATMENT_ID, PROTOCOL_ID, MRN, DATE_OF_BIRTH, IS_DECEASED, DEATH_DATE, LAST_NAME, \
    FIRST_NAME, GENDER, SEX, ADDRESS, STATE, CITY, ZIP_CODE, LAST_MODIFIED_DATE

treatment_columns = [PATIENT_ID, START_DATE, END_DATE, ACTIVE, DISPLAY_NAME, DIAGNOSES, TREATMENT_LINE,
                     NUMBER_OF_CYCLES, TREATMENT_ID, PROTOCOL_ID]

treatment_required_columns = [PATIENT_ID, TREATMENT_ID]

patient_columns = [PATIENT_ID, MRN, DATE_OF_BIRTH, IS_DECEASED, DEATH_DATE, LAST_NAME, FIRST_NAME, GENDER, SEX, ADDRESS,
                   CITY, STATE, ZIP_CODE, LAST_MODIFIED_DATE]

patient_required_columns = [PATIENT_ID]

hospital_name_to_treatment_columns_dict = {"hospital_1": {"PatientID": PATIENT_ID,
                                                          "StartDate": START_DATE,
                                                          "EndDate": END_DATE,
                                                          "Active": ACTIVE,
                                                          "DisplayName": DISPLAY_NAME,
                                                          "Diagnoses": DIAGNOSES,
                                                          "TreatmentLine": TREATMENT_LINE,
                                                          "CyclesXDays": NUMBER_OF_CYCLES,
                                                          "TreatmentID": TREATMENT_ID},
                                           "hospital_2": {"PatientId": PATIENT_ID,
                                                          "StartDate": START_DATE,
                                                          "EndDate": END_DATE,
                                                          "Status": ACTIVE,
                                                          "DisplayName": DISPLAY_NAME,
                                                          "AssociatedDiagnoses": DIAGNOSES,
                                                          "ProtocolID": PROTOCOL_ID,
                                                          "NumberOfCycles": NUMBER_OF_CYCLES,
                                                          "TreatmentId": TREATMENT_ID}
                                           }

hospital_name_to_patient_columns_dict = {"hospital_1": {"PatientID": PATIENT_ID,
                                                        "MRN": MRN,
                                                        "PatientDOB": DATE_OF_BIRTH,
                                                        "IsDeceased": IS_DECEASED,
                                                        "DOD_TS": DEATH_DATE,
                                                        "LastName": LAST_NAME,
                                                        "FirstName": FIRST_NAME,
                                                        "Gender": GENDER,
                                                        "Sex": SEX,
                                                        "Address": ADDRESS,
                                                        "City": CITY,
                                                        "State": STATE,
                                                        "ZipCode": ZIP_CODE,
                                                        "LastModifiedDate": LAST_MODIFIED_DATE},
                                         "hospital_2": {"PatientId": PATIENT_ID,
                                                        "MRN": MRN,
                                                        "PatientDOB": DATE_OF_BIRTH,
                                                        "IsPatientDeceased": IS_DECEASED,
                                                        "DeathDate": DEATH_DATE,
                                                        "LastName": LAST_NAME,
                                                        "FirstName": FIRST_NAME,
                                                        "Gender": GENDER,
                                                        "Sex": SEX,
                                                        "AddressLine": ADDRESS,
                                                        "AddressCity": CITY,
                                                        "AddressState": STATE,
                                                        "AddressZipCode": ZIP_CODE}
                                         }

hospital_name_to_date_format_dict = {"hospital_1": {START_DATE: "%m/%d/%Y %H:%M",
                                                    END_DATE: "%m/%d/%Y",
                                                    DATE_OF_BIRTH: "%m/%d/%Y %H:%M",
                                                    DEATH_DATE: "%m/%d/%Y %H:%M",
                                                    LAST_MODIFIED_DATE: "%m/%d/%Y"
                                                    },
                                     "hospital_2": {START_DATE: "%m/%d/%Y",
                                                    END_DATE: "%m/%d/%Y",
                                                    DATE_OF_BIRTH: "%m/%d/%Y %H:%M",
                                                    DEATH_DATE: "%m/%d/%Y %H:%M"
                                                    }
                                     }

ACTIVE_VALUES = ["Ordered", "Active"]
