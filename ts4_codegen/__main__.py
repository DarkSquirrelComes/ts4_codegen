import argparse
import json
import os
import sys
from jinja2 import Template

template = Template('''
import tonos_ts4.ts4 as ts4


class {{ name }}(ts4.BaseContract):
    def __init__(
        self,

        {% for static_variable in static_variables -%}
        {{ static_variable }}=None,
        {% endfor %}
        {% for constructor_arg in constructor_args -%}
        {{ constructor_arg }}=None,
        {% endfor %}
        address=None,
        balance=None,
        keypair=None,
    ):
        keypair = keypair or ts4.make_keypair()
        if address:
            super().__init__(
                '{{ name }}',
                ctor_params=None,
                initial_data=dict(),
                address=address,
                nickname='{{ name }}',
                keypair=keypair,
            )
        else:
            super().__init__(
                '{{ name }}',
                ctor_params=None,
                initial_data=dict(
                    {% for static_variable in static_variables -%}
                        {{ static_variable }}={{ static_variable }},
                    {% endfor %}
                ),
                keypair=keypair,
                balance=balance,
                nickname='{{ name }}',
            )

            super().call_method(
                'constructor',
                params=dict(
                    {% for constructor_arg in constructor_args -%}
                        {{ constructor_arg }}={{ constructor_arg }},
                    {% endfor %}
                ),
                private_key=self.private_key_,
            )


    {% for function in functions -%}
    def {{ function['name'] }}(
        self,
        {% for arg in function['inputs'] -%}
        {{ arg['name'] }},
        {% endfor %}
        is_getter=False,
    ):
        if is_getter:
            return super().call_getter(
                method='{{ function['name'] }}',
                params=dict(
                    {% for arg in function['inputs'] -%}
                    {{ arg['name'] }}={{ arg['name'] }},
                    {% endfor %}
                ),
            )
        else:
            return super().call_method(
                method='{{ function['name'] }}',
                params=dict(
                    {% for arg in function['inputs'] -%}
                    {{ arg['name'] }}={{ arg['name'] }},
                    {% endfor %}
                ),
                private_key=self.private_key_,
            )

    {% endfor %}


    {% for field in fields -%}
    @property
    def {{ field }}(self):
        return self.call_getter('{{ field }}')

    {% endfor %}
''')


def create_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'abiDir',
        help='Path to the directory with .abi.json files',
        default='./',
    )
    return parser


if __name__ == '__main__':
    arg_parser = create_arg_parser()
    parsed_args = arg_parser.parse_args(sys.argv[1:])

    target_dir = './ts4_generated_classes'
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)

    for root, dirs, files in os.walk(parsed_args.abiDir):
        for abi_json_filename in files:
            if abi_json_filename.endswith('.abi.json'):
                with open(os.path.join(root, abi_json_filename)) as f:
                    abi_json = json.load(f)

                constructor = {}
                for f in abi_json['functions']:
                    if f['name'] == 'constructor':
                        constructor = f

                name = abi_json_filename[:-9]
                with open(os.path.join(target_dir, f'{name}.py'), 'w') as f:
                    all_functions_names = [
                        fu['name'] for fu in abi_json['functions']
                    ]
                    fields = [
                        fi['name'] for fi in abi_json.get('fields', []) if fi['name'] in all_functions_names
                    ]
                    functions = [
                        fu for fu in abi_json['functions'] if fu['name'] not in ['constructor'] + fields
                    ]
                    print(template.render(
                        name=name,
                        static_variables=list(map(lambda d: d['name'], abi_json['data'])),
                        constructor_args=list(map(lambda arg: arg['name'], constructor.get('inputs', []))),
                        functions=functions,
                        fields=fields,
                    ), file=f)

                with open(os.path.join(target_dir, '__init__.py'), 'a') as f:
                    print(f'from .{name} import {name}', file=f)
