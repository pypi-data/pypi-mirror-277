from soda_generator.generators.contract_variable import ContractVariable
import re
from typing import Optional

class SODAGenerator(ContractVariable):
    def __init__(self, connection_name: str, **creds):
        super().__init__(connection_name, **creds)

    def generate_soda_yaml(self, table_name, dtypes, where_clause, checks_config_dict: dict):
        soda_yaml = f"""dataset: {table_name}

filter_sql |: {where_clause}

columns:"""

        for nm_col in dtypes['column_name']:
            column_info = f"""
  - name: {nm_col}
    data_type: {dtypes[dtypes['column_name'] == nm_col]['data_type'].values[0]}
    checks:"""

            regex = self.get_regex_for_column(nm_col, checks_config_dict)
            if regex:
                column_info += f"""
    - type: missing_count
      missing regex: ({regex})
      must_be: 0"""

            for check_type, check_config in checks_config_dict.items():
                if check_type != 'regex_columns' and nm_col in check_config.get('columns', []):
                    if check_type == 'duplicate_count_checks' or check_type == 'missing_count':
                        column_info += f"""
    - type: {check_type}
      must_be: 0"""
                    if check_type == 'invalid_count_numeric':
                        column_info += f"""
    - type: invalid_count
      valid_min: {check_config['min_max_dict'][nm_col]['valid_min']}
      valid_max: {check_config['min_max_dict'][nm_col]['valid_max']}
      must_be: 0"""

                    if check_type == 'invalid_count_categorical':
                        valid_values = check_config['categorical_dict'][nm_col]
                        column_info += f"""
    - type: invalid_count
      valid_values: {str(valid_values)}"""

            column_info += "\n"
            soda_yaml += column_info

        return soda_yaml


    def generate_soda_contracts(self, query: str, parameters: Optional[dict] = None):
        table_name = re.search(r'from\s+(?:[\w\-\."])+\.(\w+)\b', query).group(1)
        where_clause = re.search(r'\bWHERE\b\s*(.*?)(?=\sGROUP\sBY|\s*LIMIT|\s*$)', query, re.IGNORECASE).group(1)
        checks_config_dict, dtypes = self.get_checks_config(query, parameters)

        soda_yaml = self.generate_soda_yaml(table_name, dtypes, where_clause, checks_config_dict)

        yaml_file = f'{table_name}_contract.yml'
        with open(yaml_file, "a", encoding='utf-8') as log_file:
            log_file.write(str(soda_yaml) + '\n')


