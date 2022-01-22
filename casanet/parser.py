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
    
    def set_device_strenght(self, device: str, strenght):
        for i in self.net.devices:
            if i.get_name() == device:
                return self.net.set_device_strenght(device, strenght)
        
    def connect_device(self,d1: str, d2: str):
        pass


    def get_all_devices(self):
        return self.net.devices



    def parse(self,command):
        '''
        Commands : ADD, SET, CONNECT, INFO_ROUTE

        '''
        self.command = command.split(" ")
        cn = len(self.command)
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


            

        




        pass
