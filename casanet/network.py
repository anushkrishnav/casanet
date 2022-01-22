from pickle import GET
import typing
from collections import defaultdict
from casanet.device import Device

# class Message:
#     def __init__(self, message, strenght):
#         self.message = message
#         self.strenght = strenght

class Network:
    def __init__(self):
        self.devices = []
        self.connections = defaultdict(list)

        
        '''
        connections : { c1: [c2,r2] }
        a2: [conn(1,2)]
        [ [1,2], [2,3] ] 
        '''
    
    def add_device(self, device: Device):
        name = device.get_name()
        for i in self.devices:
            if name == i.get_name():
                return " Error: That name already exists."
        if device.get_type() == None:
            return " Cannot identify device type"
        self.devices.append(device)
        return f"Successfully added {name.upper()}"

    
    def add_connections(self, devices: list[Device]):
        '''
        Rules: 
            * A device cannot be connected to itself.
            * A device can be connected to any number of devices.
            * A device does not necessarily need to be connected to other devices
        '''

        if devices[0] == devices[1]:
            return "Error: Cannot connect device to itself."
        
        self.connections[devices[0]].append(devices[1])
        self.connections[devices[1]].append(devices[0])
        return 'Successfully connected.'
    
    def set_device_strenght(self, device: str, strenght):
        # Get Device based on device name from self.devices
        for i in self.devices:
            if i.get_name() == device:
                i.set_strenght(strenght)
                return f"Successfully set {device} strenght to {strenght}."
        return "Error: Device not found."

    def info_router(self, source: Device, dest: Device):
        '''
        * If no route is found between two devices, then an error message must be displayed.
        * The route for a device to itself should only have a source and destination which are both itself.
        * The source or the destination device cannot be a repeater.

        '''
        if source.get_type() == "repeater":
            return "Error: Route cannot be calculated with a repeater."
        if dest.get_type() == "repeater":
            return "Error: Route cannot be calculated with a repeater."
        
        visited = {key: False for key in self.devices}


        path = [] 
        result = self.find_path(source = source, dest = dest, visited = visited, path = path)
        name = []
        for i in result:
            name.append(i.get_name().upper())


        return ' -> '.join(name)

    def find_path(self,source: Device, dest: Device,visited: dict,path: list) -> list:
        '''
        Visting device by device present in connections.
        value set to True if a particular device is visited 
        adding the devices visited in order to the path list.

        '''
        visited[source] = True
        path.append(source)
        # reduce the strenght by one as it moves to next device



        if source.get_name() == dest.get_name():
            return
        else:
            # if current not the path then repeat the process 
            for i in self.connections[source]:
                if visited[i] == False:
                    if i.get_type() == "computer":
                        self.set_device_strenght(i.get_name(), source.get_strenght() - 1)
                    if i.get_type() == "repeater":
                        self.set_device_strenght(i.get_name(), (source.get_strenght() -1)*2)
                    if i.get_strenght() <= 0:
                        return "Error: Device Strenght insufficient."
                    self.find_path(i,dest,visited,path)
                    return path
        path.pop()
        visited[source] = False


# if __name__ == '__main__':
#     '''
#     c1 -> r1 -> c2
#     (c1, r1) ( c2,r1) 
#     c1 -> r1 
#     search for  devices connected to r1 in connection_list
#     if r1 connected to only 1 device:
#     check if the device connected to r1 is the destination 
#     yes : terminate and return list of devices 
#     no: repeat the process

#     if r1 is connected to more than 1:
#         recursive search 
#     c1 - c2 - r1 - c4 
#             - c3
#     To find c1 - c4
#     '''
#     c1 = Device()
#     c1.set_device("C1", "Computer")

#     c2 = Device()
#     c2.set_device("C2", "Computer")

#     r1 = Device()
#     r1.set_device("R1", "Repeater")

#     c3 = Device()
#     c3.set_device("C3", "Computer")

#     c4 = Device()
#     c4.set_device("C4", "Computer")

#     net = Network()
#     net.add_device(c1)
#     net.add_device(c2)
#     net.add_device(r1)
#     net.add_device(c3)
#     net.add_device(c4)
# #    print(net.devices)
#     net.add_connections([c1,c2])
#     net.add_connections([c2,r1])
#     net.add_connections([c2,c3])
#     net.add_connections([c4,r1])
# #    print(net.connections)
#     net.set_device_strenght("C4", 1)
#     print(net.info_router(c4,c1))

