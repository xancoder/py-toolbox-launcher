import logging
import pathlib
import sys
import time


def init_logger_console(debug: bool = False) -> None:
    logging.Formatter.converter = time.gmtime
    ch_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    ch = logging.StreamHandler(sys.stdout)
    ch.setFormatter(ch_format)
    if debug:
        logging.getLogger().setLevel(logging.DEBUG)
        ch.setLevel(logging.DEBUG)
    else:
        logging.getLogger().setLevel(logging.INFO)
        ch.setLevel(logging.ERROR)

    logging.getLogger().addHandler(ch)


def init_logger_file(path: pathlib.Path) -> None:
    fh = logging.FileHandler(path / 'py-toolbox-launcher.log')
    fh_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(fh_format)
    fh.setLevel(logging.INFO)

    logging.getLogger().addHandler(fh)
