import typing
from collections import defaultdict
from casanet.device import Device
from casanet.network import Network

class Parser:
    def __init__(self, net):
            self.command = None
            self.device_types = ['computer', 'repeater']
            self.net = net
    
    def add(self,count):
        if count != 3:
            return "Error: Invalid command syntax."
        if self.command[1] not in self.device_types:
            return "Error: Invalid command syntax."
        device = Device()
        device.set_type(self.command[1])
        device.set_name(self.command[2])
        return self.net.add_device(device)
    
    def set_device_strenght(self, device: str, strenght: int):
        for i in self.net.devices:
            if i.get_name() == device:
                return self.net.set_device_strenght(device, strenght)
        
    def connect_device(self,device_1: str, device_2: str):
        if device_1 == None or device_2 == None:
            return "Error: Invalid command syntax."
        if device_1 == device_2:
            return "Error: Cannot connect device to itself."
        dev1, dev2 = None, None
        for i in self.net.devices:
            if i.get_name() == device_1:
                dev1 = i
            if i.get_name() == device_2:
                dev2 = i
        return self.net.add_connections([dev1, dev2])
        
    def info_router(self,device_1: str,device_2: str):
        if device_1 == None or device_2 == None:
            return "Error: Invalid command syntax."
        if device_1 == device_2:
            return "Error: Cannot connect device to itself."
        dev1, dev2 = None, None
        for i in self.net.devices:
            if i.get_name() == device_1:
                dev1 = i
            if i.get_name() == device_2:
                dev2 = i
        return self.net.info_router(dev1, dev2)


    def get_all_devices(self):
        return self.net.devices



    def parse(self,command):
        '''
        Commands : ADD, SET, CONNECT, INFO_ROUTE

        '''
        self.command = command.split(" ")
        cn = len(self.command)
        if cn <= 2:
            return "Error: Invalid command syntax."
        if self.command[0] == "add":
            return self.add(cn)
        if self.command[0] == "get":
            return self.get_all_devices()
        if self.command[0] == "set_device_strength":
            # check if self.command[2] is a number
            if self.command[2].isdigit():
                return self.set_device_strenght(self.command[1], int(self.command[2]))
            else:
                return "Error: Invalid command syntax."
        if self.command[0] == "connect":
            return self.connect_device(self.command[1], self.command[2])
        if self.command[0] == "info_route":
            return self.info_router(self.command[1], self.command[2])

            

        




        pass
