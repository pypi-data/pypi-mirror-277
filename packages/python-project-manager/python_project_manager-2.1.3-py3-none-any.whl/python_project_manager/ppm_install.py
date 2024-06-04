import os
import re
import click
from python_project_manager.app import ACTIVATE_VENV

@click.command(context_settings=dict(ignore_unknown_options=True))
@click.argument('args', nargs=-1, type=click.UNPROCESSED)
@click.option('--dev', '-d', is_flag=True) # Add the package to the dev requirements
@click.option('--help', '-h', is_flag=True) # Allows '--help' to be passed as an argument
def install(args, help, dev) -> None:
    '''
    Uses pip's 'install' command
    '''
    # Create the command
    cmd = f'{ACTIVATE_VENV} && pip install {" ".join(args)}'.strip()

    # If 'pip install pip' is passed, install pip
    if cmd == f'{ACTIVATE_VENV} && pip install pip':
        os.system(f'{ACTIVATE_VENV} && python -m ensurepip')
        return

    # Use the help command if the '--help' flag is passed
    if help:
        os.system(f'{ACTIVATE_VENV} && pip install --help')
        return

    # If no arguments are passed, install the requirements
    if cmd == f'{ACTIVATE_VENV} && pip install':
        os.system(f'{ACTIVATE_VENV} && pip install -r requirements.txt -r requirements-dev.txt')

    # Otherwise, install the packages
    output = os.popen(cmd)

    # Read and print each line of the output
    for line in output:
        print(line.strip())
        if 'Successfully installed' in line:
            # Update the requirements file
            update_requirements(line.strip(), dev)

    # Close the output stream
    output.close()
    
def update_requirements(packages_to_update: str, is_dev=False) -> None:
    requirement_file = 'requirements-dev.txt' if is_dev else 'requirements.txt'
    packages_to_update = packages_to_update.replace('Successfully installed ', '').split(' ')
    packages_to_update = [re.split(r'-(?=[^-]*$)', package) for package in packages_to_update]
    packages_to_update = [(package[0], package[1]) for package in packages_to_update]
    
    packages_to_keep = []
    with open(requirement_file, 'r') as file:
        for line in file:
            package_name = re.match(r'^(\w|_|-|\d)*', line.strip())[0]
            if package_name not in [package[0] for package in packages_to_update]:
                packages_to_keep.append(line)

    packages_to_write = []

    for package in packages_to_update:
        packages_to_write.append(f'{package[0]}~={package[1]}'.strip())
    for package in packages_to_keep:
        packages_to_write.append(f'{package}'.strip())

    packages_to_write.sort()

    with open(requirement_file, 'w') as file:
        file.write('\n'.join(packages_to_write))
