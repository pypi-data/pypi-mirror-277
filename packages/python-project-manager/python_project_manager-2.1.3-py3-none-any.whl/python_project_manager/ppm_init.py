import os
import click
from python_project_manager.app import pass_command_to_engine, get_engine
from python_project_manager import Config

InitRunner = {
    'ConfigValues': {
        'src_dir': 'src', # Required
    },
    'Dependencies': [],
    'Files': [], # object: { 'Target': '', 'Content': '' }
    'Folders': [] # list of strs
}

@click.command()
@click.argument('project_name', type=str, required=True)
@click.option('--engine', '-e', type=str, default='',
    help='Choose the engine \'module\' to use. Built in engines are \'ppm-builtin-setuptools\' and \'ppm-builtin-pyinstaller\'.')
@click.option('--force', '-f', is_flag=True, help='Force initialization of the project')
# @click.option('--python', '-p', type=str, default='', help='Python version to use')
def init(project_name: str, engine: str, force: bool) -> None:
    '''
    <project_name> - Name of the project to be setup
    '''
    # Check if the project has already been initialized
    if not force and Config.load():
        print('Project already initialized')
        return False
    
    # Check if the engine is available
    try:
        get_engine(engine)
    except ImportError:
        print(f"Engine '{engine}' not found")
        return False

    # Set the project name and engine
    InitRunner['ConfigValues']['project_name'] = project_name # required
    InitRunner['ConfigValues']['engine'] = engine # required

    # Create the requirements.txt and requirements-dev.txt files
    with open(os.path.join(os.getcwd(), 'requirements.txt'), 'w') as file:
        pass
    with open(os.path.join(os.getcwd(), 'requirements-dev.txt'), 'w') as file:
        pass

    # Create the venv
    os.system('python -m venv venv')

    # Initialize the project
    pass_command_to_engine('init', _init,
        initRunner=InitRunner, _engine=engine)
    create_project(InitRunner)

def _init(**kwargs) -> bool:
    initRunner = kwargs['initRunner']
    src_dir = initRunner['ConfigValues']['src_dir']

    template_app = f'{src_dir}/app.py'

    initRunner['Files'].append({
        'Target': template_app,
        'Content': f'''if __name__ == '__main__':
    print('Hello, World!, from {initRunner['ConfigValues']['project_name']}!')'''
    })

    initRunner['ConfigValues']['scripts.start'] = 'py -m %src_dir%.app'

    initRunner['Folders'].append(src_dir)

    return True

def create_project(initRunner: dict[str, any]):
    # Set up the configuration values
    for key, value in initRunner['ConfigValues'].items():
        Config.set(key, value)
    Config.save()

    # Install the dependencies
    for dep in initRunner['Dependencies']:
        os.system(f'ppm install {dep}')

    # Create the project directories
    for folder in initRunner['Folders']:
        os.makedirs(os.path.join(os.getcwd(), folder), exist_ok=True)

    # Create the project files    
    for file in initRunner['Files']:
        with open(os.path.join(os.getcwd(), file['Target']), 'w') as f:
            f.write(file['Content'])