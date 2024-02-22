import logging
import pathlib
import sys
import textwrap
import time

from InquirerPy import inquirer
from InquirerPy.validator import PathValidator

import py_toolbox_launcher as tbl
import py_toolbox_launcher.tbl_logging as tbl_log


def main():
    tbl_log.init_logger_console()

    system_current = tbl.get_platform()
    logging.debug(f"system_current: {system_current}")

    path_current = pathlib.Path().resolve()
    logging.debug(f"path_current: {path_current}")
    try:
        path_tools = tbl.check_tools_folder(path_current)
        toolbox = tbl.get_toolbox(system_current, path_tools)
        logging.debug(f"toolbox: {toolbox}")
    except FileNotFoundError as e:
        logging.error('Could not find toolbox folder')
        logging.info('window will close in 5 seconds')
        logging.debug(e)
        time.sleep(5)
        sys.exit(1)

    destination_folder = tbl.prepare_destination_folder(path_current)
    logging.debug(f"destination_folder: {destination_folder}")

    path_selected = inquirer.filepath(
        message=f'Enter result path ({destination_folder}):',
        validate=PathValidator(
            is_dir=True,
            message='Input is not a directory'
        ),
        only_directories=True,
    ).execute()

    if path_selected:
        path_dst = pathlib.Path(path_selected).resolve()
    else:
        path_dst = destination_folder
    path_dst.mkdir(parents=True, exist_ok=True)

    tbl_log.init_logger_file(path_dst)

    logging.info('start toolbox launcher')
    logging.info(f'destination path : {path_dst}')

    toolbox_selection = []
    for item in list(sorted(toolbox.keys())):
        j = [item]
        d = toolbox[item]['description']
        if d:
            ds = textwrap.shorten(d, width=80, placeholder='...')
            j.append(ds)
        toolbox_selection.append(' - '.join(j))
    toolbox_selection.append('Exit - 0')

    while True:
        tool = inquirer.select(
            message='Select tool:',
            choices=toolbox_selection
        ).execute()

        if tool == 'Exit - 0':
            break

        tool_selected = tool.split(' - ')[0]
        path_executable = toolbox[tool_selected]['path']
        msg = 'start tool'
        logging.info(f'{msg:13} : {path_executable}')
        tbl.run_tool(system_current, path_executable, str(path_dst))
        msg = 'end tool'
        logging.info(f'{msg:13} : {path_executable}')

    logging.info('end toolbox launcher')


if __name__ == "__main__":
    main()
