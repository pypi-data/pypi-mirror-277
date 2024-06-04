import os
import re
from .toml import load as toml_load, dump as toml_dump, dumps as toml_dumps
from python_project_manager import Config, sanitize_string_for_file, sanitize_string_for_module

def init(_method, **kwargs) -> bool:
    print('Initializing Setuptools Engine...')
    initRunner = kwargs['initRunner']
    initRunner['Dependencies'].append('build==1.2.1 twine==5.0.0 setuptools==69.2.0 --dev')
    edit_config(initRunner)
    create_template_app(initRunner)
    create_tempalte_test(initRunner)
    set_default_scripts(initRunner)
    create_files(initRunner)
    return False

def version(_method, **kwargs) -> bool:
    action: str = kwargs.get('action', None)
    if action == 'sync':
        try:
            output = os.popen(f'pip index versions {Config.get("project_name")}')
            for line in output:
                print(line.strip())
                version_number = re.search(r'\((\d|\.)*\)', line)
                if version_number:
                    pypi_version = version_number.group(0)[1:-1]
            output.close()
            
            print(f'Version: {Config.get('version')} -> {pypi_version}')
            Config.set('version', pypi_version)
            Config.save()
        except Exception as e:
            print(f'Error: {e}')
    else:
        _method(**kwargs)

    toml_file = load_toml()
    toml_file['project']['version'] = Config.get('version')
    save_toml(toml_file)
    return False

def edit_config(initRunner: object) -> None:
    initRunner['ConfigValues']['version'] = '0.0.0'
    initRunner['ConfigValues']['src_dir'] = sanitize_string_for_file(initRunner['ConfigValues']['project_name'])
    initRunner['ConfigValues']['test_dir'] = 'tests'
    initRunner['ConfigValues']['twine.username'] = '%env:pypi_username%'
    initRunner['ConfigValues']['twine.password'] = '%env:pypi_password%'
    initRunner['ConfigValues']['twine.wheel'] = sanitize_string_for_file(initRunner['ConfigValues']['project_name'])

def create_template_app(initRunner: object) -> None:
    src_dir = sanitize_string_for_module(initRunner['ConfigValues']['src_dir'])
    initRunner['Folders'].append(src_dir)
    initRunner['Files'].append({'Target': f'{src_dir}/app.py', 'Content': f'''import os
import sys

def app():
    print("Hello World. From '{initRunner['ConfigValues']['project_name']}'.")

if __name__ == "__main__":
    app()'''})

def create_tempalte_test(initRunner: object) -> None:
    test_dir = initRunner['ConfigValues']['test_dir']
    initRunner['Folders'].append(test_dir)
    initRunner['Files'].append({'Target': f'{test_dir}/test_app.py', 'Content':
f'''
import unittest

class TestApp(unittest.TestCase):
    def test_app(self):
        self.assertEqual(1, 1)
'''})

def set_default_scripts(initRunner: object) -> None:
    initRunner['ConfigValues']['dist_dir'] = 'dist'

    initRunner['ConfigValues']['scripts.start'] = f'python -m %src_dir%.app'
    initRunner['ConfigValues']['scripts.test'] = f'python -m unittest discover -s %test_dir%'
    initRunner['ConfigValues']['scripts.build'] = f'ppm run _cleandist_ && python -m build'
    initRunner['ConfigValues']['scripts.publish:major'] = f'ppm version sync && ppm version inc -M 1 && ppm run build && ppm run _publish_'
    initRunner['ConfigValues']['scripts.publish:minor'] = f'ppm version sync && ppm version inc -m 1 && ppm run build && ppm run _publish_'
    initRunner['ConfigValues']['scripts.publish:patch'] = f'ppm version sync && ppm version inc -p 1 && ppm run build && ppm run _publish_'

    initRunner['ConfigValues']['scripts._cleandist_'] = f'IF EXIST %dist_dir% (del /S /Q %dist_dir%\\*)'
    initRunner['ConfigValues']['scripts._publish_'] = f'twine upload -u %twine.username% -p %twine.password% -r pypi %dist_dir%/*'

def create_files(initRunner: object) -> None:
    proj_name = sanitize_string_for_module(initRunner['ConfigValues']['project_name'])
    src_dir = sanitize_string_for_module(initRunner['ConfigValues']['src_dir'])
    test_dir = f'tests'
    toml_config = {
        'build-system': {
            'requires': ['setuptools', 'wheel'],
            'build-backend': 'setuptools.build_meta'
        },

        'project': {
            'name': proj_name,
            'version': initRunner['ConfigValues']['version'],
            'description': 'A Python package.',
            'authors': [],
            'readme': 'README.md',
            'keywords': [],
            'dynamic': ['dependencies']
        },
        
        'tool': {
            'setuptools': {
                'dynamic': {
                    'dependencies': {
                        'file': ['requirements.txt']
                    }
                }
            }
        }
    }
    
    initRunner['Files'].append({'Target': f'{src_dir}/__init__.py', 'Content': ''})
    initRunner['Files'].append({'Target': 'pyproject.toml', 'Content': toml_dumps(toml_config)})
    initRunner['Files'].append({'Target': 'LICENSE.txt', 'Content': ''})
    initRunner['Files'].append({'Target': 'README.md', 'Content': ''})
    initRunner['Files'].append({'Target': '.env', 'Content': '''pypi_username=__token__\npypi_password=pypi-<api-key>'''})
    
def load_toml() -> dict:
    with open('pyproject.toml', 'r') as f:
        return toml_load(f)
    
def save_toml(toml_config) -> None:
    with open('pyproject.toml', 'w') as f:
        toml_dump(toml_config, f)

# Setuptools Engine built-in cli commands
# Allows for shorthand commands to be used in the cli
_publish_command = f'del /S /Q %dist_dir%\\* || python -m build && twine upload -u %twine.username% -p %twine.password% -r pypi %dist_dir%/*'
VENV = f'venv\\Scripts\\activate'
def _build():
    os.system(Config.parse(f'del /S /Q %dist_dir%\\* || ppm version inc -t && python -m build', Config._value_config))
def _publish_patch():
    os.system(Config.parse(f'ppm version sync && ppm version inc -p 1 && {_publish_command}', Config._value_config))
def _publish_minor():
    os.system(Config.parse(f'ppm version sync && ppm version inc -m 1 && {_publish_command}', Config._value_config))
def _publish_major():
    os.system(Config.parse(f'ppm version sync && ppm version inc -M 1 && {_publish_command}', Config._value_config))