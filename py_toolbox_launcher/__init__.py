import datetime
import pathlib
import platform
import re
import subprocess


def get_platform():
    return platform.system()


def check_tools_folder(path: pathlib.Path) -> pathlib.Path:
    tmp = path / 'toolbox'
    if not tmp.exists():
        raise FileNotFoundError(f'folder does not exist: {tmp}')
    return tmp


def get_toolbox(system_current: str, path: pathlib.Path) -> dict:
    if system_current == 'Windows':
        extensions = ['bat']
    else:
        extensions = ['sh']

    tools_available = {}
    for e in extensions:
        for i in path.glob(f'**/*.{e}'):
            if i.is_file():
                description = extract_description(i)
                tools_available.update({
                    i.name: {
                        'path': str(i),
                        'description': description
                    }
                })
    return tools_available


def extract_description(path_file: pathlib.Path) -> str:
    pattern = 'DESCRIPTION:'
    with path_file.open(mode="r", encoding="utf-8") as fh:
        for line in fh:
            m = re.search(f'{pattern}(.+?)$', line)
            if m:
                return m.group(1).strip()
    return ''


def prepare_destination_folder(path: pathlib.Path) -> pathlib.Path:
    dev = platform.node()
    now = datetime.datetime.now(datetime.UTC).strftime('%Y-%m-%d_%H%M%S')
    res = path / f'{dev}_{now}'
    return res.resolve()


def run_tool(system_current: str, path_tool: str, args: str) -> None:
    if system_current == 'Windows':
        p = subprocess.Popen(
            args=[path_tool, args],
            creationflags=subprocess.CREATE_NEW_CONSOLE
        )
    else:
        p = subprocess.Popen(args=[path_tool, args])
    p.wait()
