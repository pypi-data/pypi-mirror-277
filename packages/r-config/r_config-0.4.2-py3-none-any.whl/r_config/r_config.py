from __future__ import annotations
import yaml
from pathlib import Path

from typing import Any


class RConfig(dict):

    def __init__(
            self,
            *args: tuple[Any],
            **kwargs: dict[str, Any]) -> None:
        super().__init__(*args, **kwargs)
        self.update(self)

    def update(
            self,
            r: RConfig | dict = None,
            **kwargs: dict[str, any]) -> None:

        d = {}
        d.update(kwargs)

        if r is None:
            r = self.__class__()

        for key, value in r.items():
            setattr(self, key, value)

        for key, value in d:
            setattr(self, key, value)

    def __setattr__(
            self,
            key: str,
            value: Any):
        """
        Sets an attribute with the given key and value

        :param key: name of the attribute
        :param value: value of that attribute
        """

        if isinstance(value, (list, tuple)):
            value = [self.__class__(x) if isinstance(x, dict) else x for x in value]
        elif isinstance(value, dict):
            value = self.__class__(value)

        super().__setattr__(key, value)
        super().__setitem__(key, value)

    __setitem__ = __setattr__

    def update_from_file(
            self,
            config_path: str | Path) -> None:
        """
        updates r_config with a given path
        :param config_path:
        :return: None
        """
        str_yaml = RConfig._load_config(config_path)

        self.update_from_str(str_yaml)

    def update_from_str(
            self,
            str_yaml: str) -> None:
        """
        updates r_config a with given RConfig
        :param str_yaml: yaml based string
        :return: None
        """

        cf = RConfig._transfer_str_yaml_to_rconfig(str_yaml)

        self.update(cf)

    @staticmethod
    def _load_config(
            config_path: str | Path) -> str:
        """
        loads a yaml based config file as string
        :param config_path: path of config file
        :return: content of config file
        """
        with open(config_path) as config_file:
            result = config_file.read()
        return result

    @staticmethod
    def _transfer_str_yaml_to_rconfig(
            str_yaml: str) -> RConfig:
        """
        transfers yaml based string to RConfig
        :param str_yaml: yaml based string
        :return: r_config
        """
        f_config = yaml.load(str_yaml, Loader=yaml.SafeLoader)

        return RConfig(f_config)
