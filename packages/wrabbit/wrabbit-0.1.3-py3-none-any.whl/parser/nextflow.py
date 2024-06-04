from wrabbit.parser.utils import (
    get_config_files,
    get_nf_schema,
    parse_config_file,
    create_profile_enum,
    nf_to_sb_input_mapper,
    get_tower_yml,
    get_dict_depth,
    get_docs_file,
)

from wrabbit.parser import (
    sample_sheet,
    SB_SCHEMA_DEFAULT_NAME,
    EXTENSIONS,
    NF_TO_CWL_CATEGORY_MAP,
    GENERIC_FILE_ARRAY_INPUT,
    AUX_FILES_REQUIREMENT,
    INLINE_JS_REQUIREMENT,
    GENERIC_NF_OUTPUT_DIRECTORY,
    SAMPLE_SHEET_FILE_ARRAY_INPUT,
    SAMPLE_SHEET_SWITCH,
    LOAD_LISTING_REQUIREMENT,
    SKIP_NEXTFLOW_TOWER_KEYS,
)

from wrabbit.specification import (
    RecordType,
    FileType,
    DirectoryType,
    ArrayType,
)

import yaml
import re
import os
import json

from wrabbit.wrapper.wrapper import SbWrapper


class NextflowParser:
    def __init__(self, workflow_path, sb_doc=None):
        self.sb_wrapper = SbWrapper()
        self.workflow_path = workflow_path

        # Locate nextflow files in the package if possible
        self.nf_config_files = get_config_files(self.workflow_path) or []
        self.nf_schema_path = get_nf_schema(self.workflow_path)
        self.readme_path = get_docs_file(self.workflow_path)

        self.sb_doc = sb_doc

    def generate_sb_inputs(self):
        """
        Generate SB inputs schema
        """

        # ## Add profiles to the input ## #

        profiles = dict()

        for path in self.nf_config_files:
            profiles.update(parse_config_file(path))

        profiles_choices = sorted(list(set(profiles.keys())))

        if profiles:
            self.sb_wrapper.safe_add_input(
                create_profile_enum(profiles_choices)
            )

        # Optional inputs due to profiles
        # optional_inputs = []
        # for profile_id, profile_contents in profiles.items():
        #     for key in profile_contents.keys():
        #         if 'params.' in key:
        #             input_ = key.rsplit('params.', 0)
        #             optional_inputs.extend(input_)
        # optional_inputs = set(optional_inputs)

        # ## Add inputs ## #
        if self.nf_schema_path:
            with open(self.nf_schema_path, 'r') as f:
                nf_schema = yaml.safe_load(f)

            for p_key, p_value in nf_schema.get('properties', {}).items():
                self.sb_wrapper.safe_add_input(
                    nf_to_sb_input_mapper(p_key, p_value))
            for def_name, definition in nf_schema.get(
                    'definitions', {}).items():
                # Nextflow inputs schema contains multiple definitions where
                # each definition contains multiple properties
                category = dict()

                for nf_field, sb_field in NF_TO_CWL_CATEGORY_MAP.items():
                    if nf_field in definition:
                        category[sb_field] = definition[nf_field]

                input_category = 'Inputs'
                if 'title' in definition:
                    input_category = category['sbg:title']

                for port_id, port_data in definition['properties'].items():
                    req = False
                    # if port_id in definition.get('required', []) and \
                    #         port_id not in optional_inputs:
                    #     req = True

                    self.sb_wrapper.safe_add_input(nf_to_sb_input_mapper(
                        port_id,
                        port_data,
                        category=input_category,
                        required=req,
                    ))

        # Add the generic file array input - auxiliary files
        self.sb_wrapper.safe_add_input(GENERIC_FILE_ARRAY_INPUT)
        self.sb_wrapper.add_requirement(AUX_FILES_REQUIREMENT)
        self.sb_wrapper.add_requirement(INLINE_JS_REQUIREMENT)

    def generate_sb_outputs(self):
        """
        Generate SB output schema
        """
        if get_tower_yml(self.workflow_path):
            for output in self.parse_output_yml(
                    open(get_tower_yml(self.workflow_path))
            ):
                self.sb_wrapper.safe_add_output(output)

        # if the only output is reports, or there are no outputs, add generic
        if len(self.sb_wrapper.outputs) == 0 or \
                (len(self.sb_wrapper.outputs) == 1 and
                 self.sb_wrapper.outputs[0]['id'] == 'reports'):
            self.sb_wrapper.safe_add_output(GENERIC_NF_OUTPUT_DIRECTORY)

    def generate_sb_app(
            self, sb_entrypoint='main.nf',
            executor_version=None, sb_package_id=None, execution_mode=None,
            sample_sheet_schema=None,
    ):
        """
        Generate an SB app for a nextflow workflow, OR edit the one created and
        defined by the user
        """

        self.sb_wrapper.cwl_version = 'None'
        self.sb_wrapper.class_ = 'nextflow'

        self.generate_sb_inputs()
        self.generate_sb_outputs()

        if sample_sheet_schema:
            self.parse_sample_sheet_schema(open(sample_sheet_schema))

        self.sb_wrapper.set_app_content(
            code_package=sb_package_id,
            entrypoint=sb_entrypoint,
            executor_version=executor_version,
        )

        if execution_mode:
            self.sb_wrapper.add_hint({
                'class': 'sbg:NextflowExecutionMode',
                'value': execution_mode
            })

        if self.sb_doc:
            self.sb_wrapper.add_docs(self.sb_doc)
        elif self.readme_path:
            with open(self.readme_path, 'r') as docs:
                self.sb_wrapper.add_docs(docs.read())

    def parse_sample_sheet_schema(self, path):
        """
        Example sample sheet:
        sample_sheet_input: input_sample_sheet  # taken from app wrapper
        sample_sheet_name: samplesheet.csv
        header:
          - SampleID
          - Fastq1
          - Fastq2
        rows:
          - sample_id
          - path
          - path
        defaults:
          - NA
          - NA
          - NA
        group_by: sample_id
        format_: csv

        """
        schema = yaml.safe_load(path)

        sample_sheet_input = schema.get('sample_sheet_input')
        sample_sheet_name = schema.get('sample_sheet_name', 'samplesheet')
        header = schema.get('header', 'null')

        # fix rows
        rows = schema.get('rows')
        for i, r in enumerate(rows):
            if "." not in r:
                if r == 'path':
                    n = 0
                    new_r = f'files[{n}].path'
                    while new_r in rows:
                        n += 1
                        new_r = f'files[{n}].path'
                    rows[i] = new_r
                else:
                    rows[i] = f'files[0].metadata.{r}'

        defaults = schema.get('defaults', 'null')

        # fix group by
        group_by = schema.get('group_by')
        if type(group_by) is str:
            group_by = [group_by]
        for i, gb in enumerate(group_by):

            if "." not in gb:
                if gb in ['file', 'none']:
                    group_by[i] = 'file.path'
                else:
                    group_by[i] = f'file.metadata.{gb}'

        format_ = schema.get('format_', None)

        if format_ and not sample_sheet_name.endswith(format_):
            sample_sheet_name += f".{format_}".lower()

        if not format_ and not sample_sheet_name.endswith(['.tsv', '.csv']):
            raise Exception('Sample sheet format could not be identified. '
                            'Please specify one of "tsv" or "csv" in the '
                            'sample sheet schema file.')

        if not format_ and sample_sheet_name.endswith(['.tsv', '.csv']):
            format_ = sample_sheet_name.split('.').pop().lower()

        if format_.lower() not in ['tsv', 'csv']:
            raise Exception(f'Unrecognized sample sheet format "{format_}".')

        # Step 1:
        # add a new input to the pipeline
        #    - new input must not clash with other inputs by ID
        # Ensure that the new input is unique

        # Create the sample sheet file array input
        file_input = self.sb_wrapper.safe_add_input(
            SAMPLE_SHEET_FILE_ARRAY_INPUT
        )
        file_input_id = file_input.get('id')

        # Step 2:
        # add argument for sample sheet
        #    - requires: sample sheet input (sample_sheet_input),
        #                file input (ss_file_input)
        #    - if the sample sheet is provided on input,
        #      do not generate a new ss
        input_changes = {
            'id': sample_sheet_input,
            'loadContents': True
        }

        prefix = self.sb_wrapper.get_input(
            sample_sheet_input
        )['inputBinding']['prefix']

        self.sb_wrapper.remove_input(sample_sheet_input)
        self.sb_wrapper.add_input(input_changes)
        self.sb_wrapper.add_argument(
            {
                "prefix": prefix,
                "shellQuote": False,
                "valueFrom": SAMPLE_SHEET_SWITCH.format(
                    file_input=f"inputs.{file_input_id}",
                    sample_sheet=f"inputs.{sample_sheet_input}",
                    sample_sheet_name=sample_sheet_name,
                )
            }
        )

        # Step 3:
        # add file requirement
        #    - requires: sample sheet schema
        #    - add InitialWorkDirRequirement if there are none
        #    - if there are, append the entry to listing
        ss = sample_sheet(
            file_name=sample_sheet_name,
            sample_sheet_input=f"inputs.{sample_sheet_input}",
            format_=format_,
            input_source=f"inputs.{file_input_id}",
            header=header,
            rows=rows,
            defaults=defaults,
            group_by=group_by,
        )

        self.sb_wrapper.add_requirement(ss)
        self.sb_wrapper.add_requirement(INLINE_JS_REQUIREMENT)
        self.sb_wrapper.add_requirement(LOAD_LISTING_REQUIREMENT)

    def make_output_type(self, key, output_dict, is_record=False):
        """
        This creates an output of specific type based on information provided
        through output_dict.

        :param key:
        :param output_dict:
        :param is_record:
        :return:
        """

        converted_cwl_output = dict()

        file_pattern = re.compile(r'.*\.(\w+)$')
        folder_pattern = re.compile(r'[^.]+$')
        id_key = 'id'

        if is_record:
            id_key = 'name'

        name = key
        if 'display' in output_dict:
            name = output_dict['display']

        clean_id = re.sub(r'[^a-zA-Z0-9_]', "", name.replace(
            " ", "_")).lower()

        # Case 1: Output is a Record-type
        if get_dict_depth(output_dict) > 0:
            # this is a record, go through the dict_ recursively
            fields = [self.make_output_type(key, val, is_record=True)
                      for key, val in output_dict.items()]

            used_field_ids = set()

            for field in fields:
                base_field_id = field.get('name', 'Output')

                # Since name fields can be the same for multiple inputs,
                # correct the name if it has already been used.
                chk_id = base_field_id
                i = 1
                if chk_id in used_field_ids:
                    chk_id = f"{base_field_id}_{i}"
                    i += 1
                used_field_ids.add(chk_id)

                field['name'] = chk_id

            converted_cwl_output = {
                id_key: clean_id,
                "label": name,
                "type": RecordType(fields=fields, name=clean_id, optional=True)
            }

        # Case 2: Output is a File type
        elif re.fullmatch(file_pattern, key):
            # create a list of files output
            converted_cwl_output = {
                id_key: clean_id,
                "label": name,
                "type": ArrayType(items=[FileType()], optional=True),
                "outputBinding": {
                    "glob": key
                }
            }

        # Case 3: Output is a folder type
        elif re.fullmatch(folder_pattern, key):
            # create a list of directories output
            converted_cwl_output = {
                id_key: clean_id,
                "label": name,
                "type": DirectoryType(optional=True),
                "outputBinding": {
                    "glob": key,
                    "loadListing": "deep_listing"
                }
            }
        return converted_cwl_output

    def parse_output_yml(self, yml_file):
        """
        Extracts output information from a YAML file, usually in tower.yml
        format.

        :param yml_file: path to YAML file.
        :return: list of outputs in CWL format.
        """
        outputs = list()
        yml_schema = yaml.safe_load(yml_file)

        for key, value in yml_schema.items():
            # Tower yml file can use "tower" key in the yml file to designate
            # some configurations tower uses. Since these are not output
            # definitions, we skip these.
            if key in SKIP_NEXTFLOW_TOWER_KEYS:
                continue

            outputs.append(
                self.make_output_type(key, value)
            )

        return outputs

    def dump_sb_wrapper(self, out_format=EXTENSIONS.yaml):
        """
        Dump SB wrapper for nextflow workflow to a file
        """
        print('Writing sb nextflow schema file...')
        basename = SB_SCHEMA_DEFAULT_NAME
        counter = 0
        sb_wrapper_path = os.path.join(
            self.workflow_path,
            f'{basename}.{out_format}'
        )

        while os.path.exists(sb_wrapper_path):
            counter += 1
            sb_wrapper_path = os.path.join(
                self.workflow_path,
                f'{basename}.{counter}.{out_format}'
            )

        print(f"Schema written to file <{sb_wrapper_path}>")

        if out_format in EXTENSIONS.yaml_all:
            with open(sb_wrapper_path, 'w') as f:
                yaml.dump(self.sb_wrapper.dump(), f, indent=4, sort_keys=True)
        elif out_format in EXTENSIONS.json_all:
            with open(sb_wrapper_path, 'w') as f:
                json.dump(self.sb_wrapper.dump(), f, indent=4, sort_keys=True)

