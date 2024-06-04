import os
import click
from python_project_manager.app import ACTIVATE_VENV

# Pip commands
@click.command(context_settings=dict(ignore_unknown_options=True))
@click.argument('args', nargs=-1, type=click.UNPROCESSED)
@click.option('--help', '-h', is_flag=True) # Allows '--help' to be passed as an argument
def list(args, help) -> None:
    '''
    Uses pip's 'list' command
    '''
    if help:
        os.system(f'{ACTIVATE_VENV} && pip list --help')
    else:
        os.system(f'{ACTIVATE_VENV} && pip list {' '.join(args)}')
