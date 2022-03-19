import os
from datetime import datetime
from constants import ACTIVE
from hospital_data_configuration import hospital_name_to_date_format_dict, ACTIVE_VALUES


def add_missing_columns(df, required_columns):
    for column in required_columns:
        if column not in list(df.columns):
            df[column] = [""] * len(df)

    return df


def fix_date_values(hospital_name, df):
    column_name_to_date_format = hospital_name_to_date_format_dict[hospital_name]
    for column_name, date_format in column_name_to_date_format.items():
        if column_name in df:
            raw_date_strings = df[column_name]
            fixed_date_strings = [get_date_from_date_string(date_string, date_format)
                                  for date_string in raw_date_strings]
            df[column_name] = fixed_date_strings

    return df


def get_date_from_date_string(date_string, date_format):
    try:
        _date = datetime.strptime(date_string, date_format)
        return _date

    except Exception:
        return None


def fix_active_values(df):
    raw_active_values = df[ACTIVE]
    fixed_active_values = [1 if raw_active_value in ACTIVE_VALUES
                           else None if not raw_active_value
                           else 0
                           for raw_active_value in raw_active_values]
    df[ACTIVE] = fixed_active_values

    return df


def remove_rows_without_required_fields(df, required_columns):
    for required_column in required_columns:
        df = df[~df[required_column].isna()]

    return df


def get_environment_variable(environment_variable_name):
    environment_variable = os.getenv(environment_variable_name)
    return environment_variable

