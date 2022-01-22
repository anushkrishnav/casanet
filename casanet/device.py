import typing
from collections import defaultdict

class Device:
    def __init__(self):
        self.__device_name = None
        self.__device_type = None
        self.__device_strenght = 5

    def set_name(self,name: str):
        self.__device_name = name
    def get_name(self) -> str:
        return self.__device_name
    def set_type(self,type: str):
        self.__device_type = type.lower()
    def get_type(self) -> str:
        return self.__device_type
    def set_device(self,name: str, type: str):
        self.__device_name = name
        self.__device_type = type.lower()
    def set_strenght(self,strenght: int):
        self.__device_strenght = strenght
    def get_strenght(self) -> int:
        return self.__device_strenght
    def __repr__(self):
        return f"Device(name={self.__device_name}, type={self.__device_type})"

