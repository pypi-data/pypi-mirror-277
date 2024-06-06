import importlib
import os
import sys
from argparse import ArgumentParser
from typing import Dict
from flask import Blueprint


class Definition:
    def __init__(self, url_prefix, blueprint):
        self.url_prefix = url_prefix
        self.blueprint = blueprint


blueprints: Dict[str, Definition] = dict()


def register_blueprints(blueprints_name: str, app):
    for path in sys.path:
        if os.path.isdir(path):
            for name in os.listdir(path):
                dir_path = os.path.join(path, name)
                if os.path.isdir(dir_path):
                    file_path = os.path.join(dir_path, blueprints_name)
                    if os.path.isfile(file_path):
                        with open(file_path, 'r') as fp:
                            for line in fp:
                                module_name = '.'.join(line.split('.')[0:-1])
                                package_name = '.'.join(line.split('.')[0:-2])
                                blueprint_name = line.split('.')[-1]
                                url_prefix = '/' + '/'.join(package_name.split('.'))
                                print(f'Load blueprint {blueprint_name} in {module_name}')
                                try:
                                    module = importlib.import_module(module_name)
                                    blueprint: Blueprint = getattr(module, blueprint_name)
                                    if blueprint.url_prefix is not None:
                                        url_prefix = blueprint.url_prefix
                                    print(f"\tRegister at {url_prefix}")
                                    blueprint.register(app, {'url_prefix': url_prefix})
                                    blueprints[name] = Definition(url_prefix, blueprint)
                                except Exception as e:
                                    print('\t', e)
                                    print(f'\tFailed to load blueprint {blueprint_name} in {module_name}')


def parse_arguments():
    parser = ArgumentParser(description='Blueprints')
    parser.add_argument('--host', type=str, required=False, default='127.0.0.1', help='Host name')
    parser.add_argument('--port', type=int, required=False, default=5000, help='Port number')
    return parser.parse_args()
