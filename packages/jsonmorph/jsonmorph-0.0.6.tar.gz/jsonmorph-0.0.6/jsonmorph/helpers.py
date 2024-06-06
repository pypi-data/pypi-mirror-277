import ast
import json
import re
import datetime

from datetime import datetime, timezone

def extract_content_if_starts_with_string(s):
    # Define the regular expression pattern to match and capture the content inside string('...')
    pattern = r"^string\('(.*)'\)"
    match = re.match(pattern, s)
    if match:
        return str(match.group(1))
    else:
        return None
    
def get_formatted_time():
    # Get the current time in UTC
    now = datetime.now(timezone.utc)
    formatted_time = now.strftime('%a %b %d %Y %H:%M:%S GMT%z (UTC)')

    # Adjust the GMT offset formatting if needed
    if formatted_time.endswith('+0000 (UTC)'):
        formatted_time = formatted_time.replace('+0000', '-0000')
    
    return str(formatted_time)

def is_valid_function_call_string(s):
    # Define the regular expression pattern
    pattern = r'^\{\{.*\}\}$'
    
    if re.fullmatch(pattern, s):
        return True
    else:
        return False

def extract_brace_content(s):
    # Define the regular expression pattern to extract content between `{{` and `}}`
    pattern = r'\{\{(.*?)\}\}'
    match = re.search(pattern, s)
    
    if match:
        return str(match.group(1))
    else:
        return None
    
def json_to_table(json_obj, parent_key="", separator="."):
    items = []
    for key, value in json_obj.items():
        new_key = f"{parent_key}{separator}{key}" if parent_key else key

        if isinstance(value, dict) or isinstance(value, list):
            items.append({new_key: str(value)})
            if isinstance(value, dict):
                items.extend(json_to_table(value, new_key, separator))
            elif isinstance(value, list):
                for index, item in enumerate(value):
                    if isinstance(item, dict):
                        items.extend(
                            json_to_table(item, f"{new_key}[{index}]", separator)
                        )
                    else:
                        items.append({f"{new_key}[{index}]": item})
        else:
            items.append({new_key: value})
    return items

def convert_input_json_to_users_custom_json(table_data, customer_id, settings):
    output_json = replace_strings_with_function(data=settings, table_data=table_data)
    output_data = {}
    output_data =  format_json_output_data(output_data, output_json)
    output_json = json.dumps(output_data, indent=4)

    return output_json

def format_json_output_data(output_data, output_json):
    for key, value in output_json.items():
        try:
            parsed_value = json.loads(value)
        except:
            parsed_value = value

        output_data[key] = parsed_value
    
    return output_data

def replace_strings_with_function(data, table_data):
    if isinstance(data, str):
        if is_valid_function_call_string(data):
            if function_name:=extract_brace_content(data):
                if function_name == "now()":
                    return get_formatted_time()
                elif function_name.startswith("string('"):
                    return extract_content_if_starts_with_string(function_name)
                elif function_name == "NULL":
                    return None 
                elif function_name == "original_file_name()":
                    return "<original file name>"
            
        return extract_value(table_data, data)
    elif isinstance(data, dict):
        new_dict = {}
        for key, value in data.items():
            new_dict[key] = replace_strings_with_function(value, table_data)
        return new_dict
    elif isinstance(data, list):
        new_list = []
        for item in data:
            new_list.append(replace_strings_with_function(item, table_data))
        return new_list
    else:
        return data
    
def extract_value(json_obj, key_path):
    try:
        json_obj[key_path] = json.loads(json_obj[key_path].replace("'",'"').replace("True","true").replace("False","false").replace("None","null"))
    except Exception as e:
        pass
    return json_obj[key_path] if key_path in json_obj else {}

def parse_json_values(data):
    if isinstance(data, dict):
        parsed_data = {}
        for key, value in data.items():
            if isinstance(value, str):
                try:
                    cleaned_string = value.replace("\n", "").replace(" ", "")
                    value = ast.literal_eval(cleaned_string)
                    parsed_data[key] = value
                except ValueError:
                    parsed_data[key] = (
                        value  # Leave the value unchanged if parsing fails
                    )
            else:
                parsed_data[key] = parse_json_values(value)
        return parsed_data
    elif isinstance(data, list):
        parsed_data = [parse_json_values(item) for item in data]
        return parsed_data
    else:
        cleaned_string = data.replace("\n", "").replace(" ", "")
        data = ast.literal_eval(cleaned_string)
        return data

def convert_nested_json_strings(data):
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, str):
                try:
                    parsed_value = json.loads(value)
                    data[key] = convert_nested_json_strings(parsed_value)
                except json.JSONDecodeError:
                    pass
            elif isinstance(value, (dict, list)):
                data[key] = convert_nested_json_strings(value)
    elif isinstance(data, list):
        for index, item in enumerate(data):
            if isinstance(item, str):
                try:
                    parsed_item = json.loads(item)
                    data[index] = convert_nested_json_strings(parsed_item)
                except json.JSONDecodeError:
                    pass
            elif isinstance(item, (dict, list)):
                data[index] = convert_nested_json_strings(item)
    return data