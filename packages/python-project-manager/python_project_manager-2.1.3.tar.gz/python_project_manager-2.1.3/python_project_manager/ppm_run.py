import os
import re
from python_project_manager import Config
import click
from python_project_manager.app import pass_command_to_engine, ACTIVATE_VENV, DEACTIVATE_VENV

@click.command()
@click.argument('script_name', type=str, required=True)
@click.option('--non_venv', '-n', is_flag=True, help='Run the script without the virtual environment')
def run(script_name, non_venv) -> None:
    '''
    <script_name> - Name of the script to be run
    '''
    
    cli_command: str = Config.get(f'scripts.{script_name}')
    
    pass_command_to_engine('run', _run,
        script_name=script_name, cli_command=cli_command, non_venv=non_venv)

def _run(**kwargs) -> bool:
    cli_command: str = kwargs.get('cli_command', None)
    script_name: str = kwargs.get('script_name', None)
    non_venv: bool = kwargs.get('non_venv', False)

    cli_command = re.sub(r'ppm\s.*?(?=\s&&|$)', lambda x: f'{DEACTIVATE_VENV} && {x.group(0)} && {ACTIVATE_VENV}', cli_command)

    if not cli_command:
        print(f"Script '{script_name}' not found")
        return

    ## Smart change directory
    old_cwd = os.getcwd() # Get the current working directory
    new_cwd = old_cwd

    # Checks if 'cwd' is in the 'src' directory
    skip_chdir = re.search(r'(^|\s)cd\s\w*', cli_command) # Check for 'cd' command
    skip_chdir = skip_chdir and re.search(r'(^|\s)unittest\s\w', cli_command) # Check for 'unittest' command
    if not skip_chdir:
        # Searches for the 'python' command along with the script path
        python_command = re.search(r'python.*\.py', cli_command)
        if python_command:
            # Get the python path
            python_path = re.search(r'\S*\.py', python_command[0])
            if python_path:
                # Get the first dir in python path
                targ_dir = re.search(r'^\w*(.|\|/)(?!py)', python_path[0])
                if targ_dir:
                    # Join the target dir with the current working directory
                    new_cwd = os.path.join(old_cwd, targ_dir[0][:-1])
                    # Remove targ_dir from python_path
                    cli_command = cli_command.replace(python_path[0],python_path[0].replace(targ_dir[0], ""))
                    if targ_dir[0][:-1] == Config.get('test_dir'):
                        cli_command = f'set PYTHONPATH=C:\\{Config.get('src_dir')};%PYTHONPATH% && {cli_command}'
                        
    os.chdir(new_cwd) # Change the current working directory

    if "VIRTUAL_ENV" in os.environ and non_venv:
        print('Deactivating virtual environment')
        os.system(f'venv\Scripts\deactivate.bat && {cli_command}')
    elif non_venv:
        print('Running without virtual environment')
        os.system(cli_command)
    else:
        print('Running with virtual environment')
        os.system(f'{ACTIVATE_VENV} && {cli_command}')

    os.chdir(old_cwd) # Change the current working directory back to the original
    if "VIRTUAL_ENV" in os.environ:
        os.system('venv\Scripts\deactivate.bat')
