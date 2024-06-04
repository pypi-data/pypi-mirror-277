import click
from python_project_manager.ppm_init import init
from python_project_manager.ppm_install import install
from python_project_manager.ppm_run import run
from python_project_manager.ppm_list import list
from python_project_manager.ppm_version import version

@click.group()
def cli():
    pass

cli.add_command(init)
cli.add_command(install)
cli.add_command(run)
cli.add_command(list)
cli.add_command(version)