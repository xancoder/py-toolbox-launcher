import pathlib

import PyInstaller.__main__

HERE = pathlib.Path(__file__).parent.absolute()
path_to_icon = str((HERE / '../assets/logo.ico').resolve())
path_to_main_cli = str((HERE / '../cmd/cli.py').resolve())

APP_NAME = 'py-toolbox-launcher'


def build_linux_cli():
    PyInstaller.__main__.run([
        path_to_main_cli,
        '--onefile',
        '--console',
        '--clean',
        f'-n{APP_NAME}_cli'
    ])


def build_windows_cli():
    PyInstaller.__main__.run([
        path_to_main_cli,
        '--onefile',
        '--console',
        '--clean',
        f'--icon={path_to_icon}',
        f'-n{APP_NAME}_cli'
    ])
