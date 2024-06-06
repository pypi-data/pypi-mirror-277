# -- import packages: --------------------------------------------------------
import ABCParse as ABCParse
import logging as logging
import pathlib as pathlib


# -- import local dependencies: ----------------------------------------------
from ._log_config import LogConfig


# -- operational class: ------------------------------------------------------
class PackageLogging(ABCParse.ABCParse):
    def __init__(self, name: str, file: str, *args, **kwargs):
        """
        Args:
            name (str): package name given by __name__

            file (str): filename given by __file__

        Returns:
            None
        """
        self.__parse__(locals())

        self.logger.info(
            f"Logs for {self._name} will be saved to: {self.log_config.log_fpath}"
        )
        self.logger.debug(f"Importing from local install location: {self._file}")

    @property
    def fname(self):
        return pathlib.Path(self._file).parent.name

    @property
    def _log_fpath(self):
        return f"{self._name}.log"

    @property
    def log_config(self):
        if not hasattr(self, "_log_config"):
            self._log_config = LogConfig(name=self._name, log_file=self._log_fpath)
        return self._log_config

    @property
    def logger(self):
        if not hasattr(self, "_logger"):
            self._logger = logging.getLogger(f"{self._name}.{self.fname}")
        return self._logger
