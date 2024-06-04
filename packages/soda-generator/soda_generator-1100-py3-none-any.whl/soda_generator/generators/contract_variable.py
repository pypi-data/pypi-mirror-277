from soda_generator.profilers.profiler import Profiler
import polars as pl
import re

class ContractVariable(Profiler):
    def __init__(self, connection_name: str, **creds):
        super().__init__(connection_name, **creds)


    def get_data(self, query, parameters=None):
        lf = self.connector.read_data(query, parameters)
        lf = lf.cast({pl.Decimal: pl.Float64})
        profiling_data = self.compute_metrics(lf)
        dtypes = self.connector.origin_dtypes

        return lf, profiling_data, dtypes

    def get_regex_columns(self, lf):
        regexes = {
            'email_regex': r'^[\w\.-]+@[\w\.-]+\.\w+$',
            "card_regex": r'^(2200|2204)|^5[1-5]\d{2}\d{12}$|^4\d{15}$|^3[47]\d{13}$|^6\d{15,17}$|^6\d{15}$|^9860\d{12}$|^(8600|5614)\d{12}$|^94\d{14}$|^30[0-5]\d{11}$|^36\d{12}$|^38\d{12}$|^39\d{12}$',
            "uuid": r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$',
            "phone_number": r'^(?:\+?(?:7|8|996|995|994|998|374|375|972))\d{9,10}$',
            "ip_address": r'([0-9]{1,3}[\.]){3}[0-9]{1,3}',
            "web_site": r'^(https?://)?(www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,63}([/\?#][a-zA-Z0-9-_=#%&.+]+)*$',
            "date": r'^(19\d{2}|20\d{2})$|^(19\d{2}|20\d{2})-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$|^(19\d{2}|20\d{2})-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])\s([01]\d|2[0-3]):([0-5]\d):([0-5]\d)(\.\d{2,3})?$|^(19\d{2}|20\d{2})-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])\s([01]\d|2[0-3]):([0-5]\d):([0-5]\d)(\.\d{2,3})?\s\+([01]\d|2[0-3]):([0-5]\d)$|^(19\d{2}|20\d{2})-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])T([01]\d|2[0-3]):([0-5]\d):([0-5]\d)(\.\d{2,3})?$',
            "int": r'^-?\d+$',
            "float": r'\s*-?\d+[,.]\d+\s*$'
        }

        result = {
            "columns": [],
            "regexes": {}
        }

        for column in lf.columns:
            col_full_rows = \
            lf.select(pl.col(column).drop_nans()).drop_nulls(subset=column).select(pl.len()).collect().row(0)[0]
            for regex_name, regex in regexes.items():
                matching_rows = lf.select(pl.col(column).map_elements(
                    lambda x: len(re.findall(regex, str(x))),
                    return_dtype=pl.Int64,
                    skip_nulls=True
                )).sum().collect().row(0)[0]
                if matching_rows != 0 and (matching_rows * 100) / col_full_rows >= 60:
                    result["columns"].append(column)
                    if regex_name not in result["regexes"]:
                        result["regexes"][regex_name] = {
                            "match_columns": [],
                            "regex": regex
                        }
                    result["regexes"][regex_name]["match_columns"].append(column)

        return result




    def get_checks_config(self, query, parameters=None):
        lf, profiling_data, dtypes = self.get_data(query, parameters)
        unique_columns = profiling_data.filter(pl.col('percent_dup') == 0)['column'].to_list()
        not_null_columns =  profiling_data.filter(pl.col('null_count') == 0)['column'].to_list()
        min_max_columns = profiling_data.filter(pl.col('minimum').is_not_null() |
                                                 pl.col('maximum').is_not_null())['column'].to_list()
        min_max_dict = {}
        for col in min_max_columns:
            min_value = profiling_data.filter(pl.col('column') == col)['minimum'].to_list()[0]
            max_value = profiling_data.filter(pl.col('column') == col)['maximum'].to_list()[0]
            min_max_dict[col] = {'valid_min': min_value, 'valid_max': max_value}


        categorical_columns = profiling_data.filter(pl.col('cat_dist').is_not_null())['column'].to_list() if 'cat_dist' in profiling_data.columns else None
        categorical_dict = {}
        for key in categorical_columns:
            categorical_dict[key] = pl.Series(lf.select(pl.col(key).unique()).collect()).to_list()

        regex_columns_dict = self.get_regex_columns(lf)

        contracts_checks = {'duplicate_count_checks': {'columns':unique_columns},
                            'missing_count': {'columns': not_null_columns},
                            'invalid_count_numeric': {'columns': min_max_columns, 'min_max_dict': min_max_dict},
                            'invalid_count_categorical': {'columns': categorical_columns, 'categorical_dict': categorical_dict},
                            'regex_columns': {'columns': regex_columns_dict['columns'],
                            'regexes': regex_columns_dict['regexes']}
                            }

        return contracts_checks, dtypes

    def get_regex_for_column(self, column_name, checks_config_dict):
        for regex_name, regex_config in checks_config_dict['regex_columns']['regexes'].items():
            if column_name in regex_config['match_columns']:
                return regex_config['regex']
        return None

    def get_valid_values_list(self, list_values):
        return [f"'{val}'" for val in list_values]


