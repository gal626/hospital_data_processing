from pathlib import Path
from pandas import read_csv
from db.my_sql import ProductionHospitalsData, Patients, Treatments
from hospital_data_configuration import hospital_name_to_treatment_columns_dict, treatment_columns, \
    hospital_name_to_patient_columns_dict, patient_columns, patient_required_columns
from utils import add_missing_columns, fix_date_values, fix_active_values, remove_rows_without_required_fields

sources_path = Path("~/hospitals_data/").expanduser()


def save_patients_data_from_file_path(file_path):
    file_name = file_path.stem
    hospital_name = file_name.replace("_Patient", "")
    patients_df = read_csv(file_path)
    patients_df = patients_df.fillna("")
    patients_df = patients_df.rename(columns=hospital_name_to_patient_columns_dict[hospital_name])
    patients_df = add_missing_columns(patients_df, patient_columns)
    patients_df = fix_date_values(hospital_name, patients_df)
    patients_df = remove_rows_without_required_fields(patients_df, patient_required_columns)

    with ProductionHospitalsData() as production_hospitals_data:
        for _, row in patients_df.iterrows():
            patient = Patients()
            patient.patient_id = row.patient_id
            patient.mrn = row.mrn
            patient.date_of_birth = row.date_of_birth
            patient.is_deceased = row.is_deceased
            patient.date_of_death = row.date_of_death
            patient.last_name = row.last_name
            patient.first_name = row.first_name
            patient.gender = row.gender
            patient.sex = row.sex
            patient.address = row.address
            patient.city = row.city
            patient.state = row.state
            patient.zip_code = row.zip_code
            patient.last_modified_date = row.last_modified_date
            production_hospitals_data.session.merge(patient)


def save_treatment_data_from_file_path(file_path):
    file_name = file_path.stem
    hospital_name = file_name.replace("_Treatment", "")
    treatments_df = read_csv(file_path)
    treatments_df = treatments_df.fillna("")
    treatments_df = treatments_df.rename(columns=hospital_name_to_treatment_columns_dict[hospital_name])
    treatments_df = remove_rows_without_required_fields(treatments_df, patient_required_columns)
    treatments_df = add_missing_columns(treatments_df, treatment_columns)
    treatments_df = fix_date_values(hospital_name, treatments_df)
    treatments_df = fix_active_values(treatments_df)

    with ProductionHospitalsData() as production_hospitals_data:
        for _, row in treatments_df.iterrows():
            treatment = Treatments()
            treatment.patient_id = row.patient_id
            treatment.start_date = row.start_date
            treatment.end_date = row.end_date
            treatment.active = row.active
            treatment.display_name = row.display_name
            treatment.diagnoses = row.diagnoses
            treatment.treatment_line = row.treatment_line
            treatment.number_of_cycles = row.number_of_cycles
            treatment.treatment_id = row.treatment_id
            treatment.protocol_id = row.protocol_id
            production_hospitals_data.session.merge(treatment)


def main():
    for file_path in sources_path.iterdir():
        file_path_string = str(file_path)

        if file_path_string.endswith("csv"):
            if "patient" in file_path_string.lower():
                save_patients_data_from_file_path(file_path)

            elif "treatment" in file_path_string.lower():
                save_treatment_data_from_file_path(file_path)

            else:
                raise ValueError(f"unsupported name for file {file_path_string}")

        else:
            raise ValueError(f"unsupported file type received in {file_path_string}")


if __name__ == '__main__':
    main()
