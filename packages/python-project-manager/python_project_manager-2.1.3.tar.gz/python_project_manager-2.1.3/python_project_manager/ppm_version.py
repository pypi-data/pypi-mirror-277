import re
from python_project_manager import Config
import click
from python_project_manager.app import pass_command_to_engine

@click.command()
@click.argument('action', type=click.Choice(['inc', 'dec', 'show', 'set', 'sync']), required=True, default='show')
@click.option('--major', '-M', type=int, default=0, help='Change the major version')
@click.option('--minor', '-m', type=int, default=0, help='Change the minor version')
@click.option('--patch', '-p', type=int, default=0, help='Change the patch version')
@click.option('--timestamp', '-t', is_flag=True, help='Include timestamp in the version')
def version(action, major, minor, patch, timestamp) -> None:
    '''
    <action> - Action to perform on the version
    '''
    if action == 'show':
        print(Config.get('version'))
        return

    pass_command_to_engine('version', _version,
        action=action, major=major, minor=minor, patch=patch, timestamp=timestamp)

def _version(**kwargs) -> bool:
    action: str = kwargs.get('action', None)
    if action == 'sync':
        print('No built-in sync action, external engine sync action may have been called')
        return True
    
    major: str = kwargs.get('major', None)
    minor: str = kwargs.get('minor', None)
    patch: str = kwargs.get('patch', None)
    timestamp: str = kwargs.get('timestamp', None)

    # Split the version by '.' and '+'
    version_list = re.split(r'\.', Config.get('version'))
    ver_major = int(version_list[0])
    ver_minor = int(version_list[1])
    ver_patch = int(version_list[2])
    ver_timestamp = version_list[3] if len(version_list) > 3 else ''

    # Increment the version
    if action == 'set':
        if major:
            ver_major = major
        if minor:
            ver_minor = minor
        if patch:
            ver_patch = patch
    elif action == 'inc':
        if major:
            ver_minor = 0
            ver_patch = 0
        elif minor:
            ver_patch = 0
        elif patch:
            pass

        ver_major += major
        ver_minor += minor
        ver_patch += patch
    elif action == 'dec':
        ver_major -= major
        ver_minor -= minor
        ver_patch -= patch

    if timestamp:
        import time
        ver_timestamp = time.strftime('%Y%m%d%H%M%S')

    #concat the version
    version = f'{ver_major}.{ver_minor}.{ver_patch}'
    if timestamp:
        version = f'{version}.{ver_timestamp}'

    print(f'Version: {Config.get('version')} -> {version}')
    Config.set('version', version)
    Config.save()
    return True
