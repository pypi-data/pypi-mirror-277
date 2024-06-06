import ast
import json
from .helpers import json_to_table, convert_input_json_to_users_custom_json

def process_json(input_file, settings_file, output_file):
    # Read canonical JSON
    with open(input_file, "r") as input:
        canonical_json = json.load(input)

    # Reformat canonical json
    custom_json = None
    if canonical_json:
        table_format = json_to_table(canonical_json)
        new_format_data = {}
        for item in table_format:
            for key, value in item.items():
                new_format_data[f"{key}"] = f"{value}"

    with open(settings_file, "r") as setting:
        user_json_settings = json.load(setting)

    if user_json_settings:
        try:
            custom_json = convert_input_json_to_users_custom_json(
                table_data=new_format_data,
                customer_id=None,
                settings=user_json_settings,
            )

            cleaned_string = str(json.loads(custom_json))
            custom_json = ast.literal_eval(cleaned_string)

            with open(output_file, "w") as file:
                file.write(json.dumps(custom_json, indent=4))

            return json.dumps(custom_json, indent=4)   
        except Exception as e:
            raise e

# Example usage
# process_json("files/input.json", "files/setting.json", "files/output.json")
