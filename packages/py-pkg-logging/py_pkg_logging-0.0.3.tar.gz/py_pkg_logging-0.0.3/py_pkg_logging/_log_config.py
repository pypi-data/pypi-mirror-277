# _log_config.py

import ABCParse
import logging
import pathlib

from typing import Union


class LogConfig(ABCParse.ABCParse):
    """"""

    def __init__(
        self,
        name: Union[pathlib.Path, str] = "py_pkg_logger",
        log_file: Union[pathlib.Path, str] = "log.log",
        log_dir: Union[pathlib.Path, str] = pathlib.os.getcwd(),
        dirname: Union[pathlib.Path, str] = ".log_cache",
        file_level: int = logging.DEBUG,
        console_level: int = logging.INFO,
        *args,
        **kwargs
    ):
        """
        Args:
            name (Union[pathlib.Path, str]): Default: ``"py_pkg_logger"``.

            log_file (Union[pathlib.Path, str]): Default: ``"log.log"``.

            log_dir (Union[pathlib.Path, str]): Default: ``pathlib.os.getcwd()``.

            dirname (Union[pathlib.Path, str]): Default: ``".log_cache"``.

            file_level (int): Default: ``logging.DEBUG``.

            console_level (int): Default: ``logging.DEBUG``.

        Returns:
            None
        """
        self.__parse__(locals())

        if not self.log_dir.exists():
            self.log_dir.mkdir()

        self.logger.addHandler(self.file_handler)
        self.logger.addHandler(self.console_handler)

    @property
    def log_dir(self) -> pathlib.Path:
        return pathlib.Path(self._log_dir).joinpath(self._dirname)

    @property
    def log_fpath(self) -> pathlib.Path:
        return self.log_dir.joinpath(self._log_file)

    @property
    def logger(self):
        if not hasattr(self, "_logger"):
            self._logger = logging.getLogger(self._name)
            self._logger.setLevel(logging.DEBUG)
        return self._logger

    @property
    def file_formatter(self):
        return logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    @property
    def file_handler(self):
        if not hasattr(self, "_file_handler"):
            self._file_handler = logging.FileHandler(self.log_fpath)
            self._file_handler.setFormatter(self.file_formatter)
            self._file_handler.setLevel(self._file_level)
        return self._file_handler

    @property
    def console_formatter(self):
        return logging.Formatter("%(name)s - %(levelname)s - %(message)s")

    @property
    def console_handler(self):
        if not hasattr(self, "_console_handler"):
            self._console_handler = logging.StreamHandler()
            self._console_handler.setFormatter(self.console_formatter)
            self._console_handler.setLevel(self._console_level)
        return self._console_handler
