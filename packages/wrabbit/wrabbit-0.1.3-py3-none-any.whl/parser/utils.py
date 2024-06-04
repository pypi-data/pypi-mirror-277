import os
import logging
import re

from wrabbit.specification import (
    CompositeType,
    EnumType,
    ArrayType,
    StringType,
    FileType,
    DirectoryType,
    IntegerType,
    FloatType,
    BooleanType,
)

from wrabbit.parser import (
    NF_TO_CWL_PORT_MAP,
    SB_SCHEMA_DEFAULT_NAME,
    SB_SAMPLES_SCHEMA_DEFAULT_NAME,
    NF_SCHEMA_DEFAULT_NAME,
    README_DEFAULT_NAME,
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def nf_schema_type_mapper(input_type_string):
    """
    Convert nextflow schema input type to CWL
    """
    type_ = input_type_string.get('type', 'string')
    format_ = input_type_string.get('format', '')

    return type_mapper(type_, format_)


def nf_to_sb_input_mapper(port_id, port_data, category=None, required=False):
    """
    Convert a single input from Nextflow schema to SB schema
    """
    sb_input = dict()
    sb_input['id'] = port_id

    enum_symbols = port_data.get('enum', [])

    if enum_symbols:
        sb_input['type'] = EnumType(
            name=port_id,
            symbols=enum_symbols,
        )
    else:
        sb_input['type'] = nf_schema_type_mapper(port_data)

    sb_input['inputBinding'] = {
        'prefix': f'--{port_id}',
    }

    if not required:
        sb_input['type'].to_optional()

    if category:
        sb_input['sbg:category'] = category

    for nf_field, sb_field in NF_TO_CWL_PORT_MAP.items():
        if nf_field in port_data:
            value = port_data[nf_field]
            if value == ":" and nf_field == 'default':
                # Bug prevents running a task if an input's
                #  default value is exactly ":". This bug will likely be
                #  fixed at the time of release of this version.
                value = " :"
            sb_input[sb_field] = value

    return sb_input


def type_mapper(type_, format_):
    if isinstance(type_, str):
        if type_ == 'string' and 'path' in format_:
            if format_ == 'file-path':
                return FileType()
            if format_ == 'directory-path':
                return DirectoryType()
            if format_ == 'path':
                return FileType()
        if type_ == 'string':
            return StringType()
        if type_ == 'integer':
            return IntegerType()
        if type_ == 'number':
            return FloatType()
        if type_ == 'boolean':
            return BooleanType()
        if type_ == 'object':
            # this should be a record type (dictionary)
            # it is provided as '{"key1": "value1", "key2": "value2"}'
            return StringType()
    elif isinstance(type_, list):
        temp_type_list = CompositeType()
        for m in type_:
            temp_type_list.extend(type_mapper(m, format_))
        return temp_type_list


def create_profile_enum(profiles: list):
    """
    If profiles are defined in the config file, this input stores the profiles
    They are added to the commandline as -profile foo,bar,foobar
    :param profiles: list of profiles
    :return: Profiles enum array input
    """
    return {
        "id": "profile",
        "type": ArrayType(
            items=[EnumType(name="profile", symbols=profiles)], optional=True
        ),
        "label": "Profiles",
        "doc": "Select which profile(s) you want to use for task execution.",
        "inputBinding": {
            "prefix": "-profile",
            "itemSeparator": ",",
            "shellQuote": False,
        }
    }


def get_dict_depth(dict_, level=0):
    """
    Find the depth of the dictionary. Example:
    {'a': 1} - returns 0;
    {'a': {'b': 2}} - returns 1...

    :param dict_: input dictionary
    :param level: depth of the outer dict
    :return: int
    """
    n = level
    for k, v in dict_.items():
        if type(v) is dict:
            lv = get_dict_depth(v, level + 1)
            if lv > n:
                n = lv
    return n


def get_readme(path):
    """
    Find readme file is there is one in the path folder
    """
    for file in os.listdir(path):
        if file.lower() == 'readme.md':
            return os.path.join(path, file)
    return None


def get_tower_yml(path):
    """
    Find tower.yml file is there is one in the path folder
    """
    for file in os.listdir(path):
        if file.lower() == 'tower.yml':
            return os.path.join(path, file)
    return None


def get_entrypoint(path):
    """
    Auto find main.nf or similar file is there is one in the path folder.
    """
    possible_paths = []
    for file in os.listdir(path):
        if file.lower() == 'main.nf':
            return file

        if file.lower().endswith('.nf'):
            possible_paths.append(file)

    if len(possible_paths) > 1:
        raise Exception(
            'Detected more than 1 nextflow file in the root of the '
            'workflow-path. Please use `--entrypoint` to specify which script '
            'you want to use as the workflow entrypoint')
    elif len(possible_paths) == 1:
        return possible_paths.pop()
    else:
        return None


def get_latest_sb_schema(path):
    """
    Auto find sb_nextflow_schema file.
    """
    possible_paths = []
    for file in os.listdir(path):
        result = re.findall(
            fr"(.*{SB_SCHEMA_DEFAULT_NAME}\.?(\d+)?\.(ya?ml|json))", file
        )
        if result:
            result = result.pop(0)
            if not result[1]:
                prep = 0, result[0]
            else:
                prep = int(result[1]), result[0]
            possible_paths.append(prep)

    if possible_paths:
        latest = sorted(possible_paths).pop()[1]
        sb_schema_path = os.path.join(path, latest)
        print(f"Located latest sb_nextflow_schema at <{sb_schema_path}>")
        return sb_schema_path
    else:
        return None


def get_nf_schema(string):
    path = os.path.join(string, NF_SCHEMA_DEFAULT_NAME)
    if os.path.exists(path):
        return path
    else:
        raise Exception()


def get_docs_file(path):
    """
    Auto find readme file.
    """
    for file in os.listdir(path):
        if file.lower() == README_DEFAULT_NAME.lower():
            return os.path.join(path, file)
    else:
        return None


def get_executor_version(string):
    result = re.findall(
        r"\[Nextflow]\([^(]+(%E2%89%A5|%E2%89%A4|=|>|<)(\d{2}\.\d+\.\d+)[^)]+\)",
        string
    )
    if result:
        sign, version = result.pop(0)
        if sign == "%E2%89%A5":
            sign = ">="
        elif sign == "%E2%89%A4":
            sign = "<="
        elif not sign:
            sign = "="

        print(f"Identified nextflow executor version requirement {sign} {version}")
        return sign, version
    else:
        return None, None


def get_sample_sheet_schema(path):
    ss_path = os.path.join(path, SB_SAMPLES_SCHEMA_DEFAULT_NAME)

    if os.path.exists(ss_path):
        print(f"Located latest sample sheet schema at <{ss_path}>")
        return ss_path
    else:
        return None


def get_config_files(path):
    """
    Auto find config files.
    """
    paths = []
    for file in os.listdir(path):
        if file.lower().endswith('.config'):
            paths.append(os.path.join(path, file))
    return paths or None


def find_config_section(file_path: str, section: str) -> str:
    section_text = ""
    found_section = False
    brackets = 0

    with open(file_path, 'r') as file:
        for line in file.readlines():
            if found_section:
                section_text += line
                brackets += line.count("{") - line.count("}")

            if brackets < 0:
                break

            if re.findall(section + r'\s+\{', line):
                section_text += "{\n"
                found_section = True

    return section_text


def parse_config_file(file_path: str) -> dict:
    profiles_text = find_config_section(file_path, 'profiles')

    # Extract profiles using regex
    profiles = {}
    block_pattern = re.compile(
        r'\s*(\w+)\s*{([^}]+)}', re.MULTILINE | re.DOTALL
    )
    key_val_pattern = re.compile(
        r'([a-zA-Z._]+)(?:\s+|)=(?:\s+|)([^\s]+)'
    )
    include_pattern = re.compile(
        r'includeConfig\s+[\'\"]([a-zA-Z_.\\/]+)[\'\"]'
    )

    blocks = re.findall(block_pattern, profiles_text)
    for name, content in blocks:
        settings = dict(re.findall(key_val_pattern, content))
        profiles[name] = settings
        include_path = re.findall(include_pattern, content)
        if include_path:
            profiles[name]['includeConfig'] = include_path
            include_path = include_path.pop()
            additional_path = os.path.join(
                os.path.dirname(file_path), include_path)
            params_text = find_config_section(additional_path, 'params')
            params = dict(re.findall(key_val_pattern, params_text))
            for param, val in params.items():
                profiles[name][f"params.{param}"] = val

    # return currently returns includeConfig and settings, which are not used
    # but could be used in the future versions of sbpack
    return profiles
