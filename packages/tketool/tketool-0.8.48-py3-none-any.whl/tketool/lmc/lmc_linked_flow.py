from tketool.lmc.prompts.prompt_controller import *
from tketool.lmc.lmc_linked import lmc_linked_model
from tketool.lmc.models import LLM_Plus, LLM_Buffer_Plus
from pydantic import BaseModel, create_model, Field
from langchain.output_parsers import PydanticOutputParser, BooleanOutputParser
from enum import Enum, EnumMeta


class lmc_linked_flow_model():
    def __init__(self, prompt_file: prompt_define_file, retry_time=3):

        self.type_parser_mapping = {
            "bool": BooleanOutputParser(),
        }

        self.define_file = prompt_file
        self.retry_time = retry_time

        self.enum_models = {}
        for k, enum_define in self.define_file.enums.items():
            # enum_type = self._create_enum(k, list(enum_define.enums_list.keys()))
            self.enum_models[k] = Enum(k, list(enum_define.enums_list.items()))  # list(enum_define.enums_list.keys())

        self.models = {}
        for k, define in self.define_file.models.items():
            field_dict = {}
            for f in define.fields_list:
                data_type = None
                if f.field_type in self.enum_models:
                    data_type = self.enum_models[f.field_type]
                elif f.field_type in self.models:
                    data_type = self.models[f.field_type]
                else:
                    data_type = eval(f.field_type)
                field_dict[f.field_name] = (data_type, Field(description=f.field_des))

            dynamic_model = create_model(k, **field_dict)
            self.models[k] = dynamic_model

        self.linked_model = {}

        pass

    def __call__(self, llm, **kwargs):

        for k, pro_def in self.define_file.prompts.items():
            if k in self.linked_model:
                continue

            output_type = pro_def.prompt_output.strip()
            li = lmc_linked_model(llm).set_prompt_template(pro_def.prompt_content).set_retry(self.retry_time)

            if pro_def.prompt_output in self.models:
                parser_out = PydanticOutputParser(pydantic_object=self.models[pro_def.prompt_output])
                li = li.set_output_parser(parser_out).set_output_fix()
            elif pro_def.prompt_output in self.enum_models:
                li = li.set_enum_output_parser(self.enum_models[pro_def.prompt_output]).set_output_fix()
            elif output_type in self.type_parser_mapping:
                parser_out = self.type_parser_mapping[output_type]
                li = li.set_output_parser(parser_out).set_output_fix()

            self.linked_model[k] = li

        root_prompt_key = 'default' if 'default' in self.linked_model else list(self.linked_model.keys())[0]

        logs = []
        results = []

        pointer = self.linked_model[root_prompt_key]
        p_define = self.define_file.prompts[root_prompt_key]
        last_result = None
        while True:
            result, log = pointer(last=last_result, **kwargs)

            logs.append(log)

            if len(result) > 0:
                last_result = result[0]
                results.append(result[0])

                if len(p_define.prompt_goto) > 0:
                    value_mapping = {}
                    default_to = None
                    for sub_p_k in p_define.prompt_goto:
                        if sub_p_k in self.define_file.prompts:
                            value_mapping[self.define_file.prompts[sub_p_k].prompt_condition_value] = sub_p_k

                        if self.define_file.prompts[sub_p_k].prompt_condition_default:
                            default_to = sub_p_k

                    navigate_value = eval(f"last_result." + p_define.prompt_condition_field)
                    navigate_value = str(navigate_value)

                    if navigate_value in value_mapping:
                        pointer = self.linked_model[value_mapping[navigate_value]]
                        p_define = self.define_file.prompts[value_mapping[navigate_value]]
                        continue

                    if default_to:
                        pointer = self.linked_model[default_to]
                        p_define = self.define_file.prompts[default_to]
                        continue
                else:
                    break
            raise Exception("error in invoke flow.")

        return results, logs
