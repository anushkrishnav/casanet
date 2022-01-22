from casanet.parser import Parser
from casanet.network import Network
from casanet.device import Device
import typing

if __name__ == '__main__':
    net = Network()
    def main():
        
        parser = Parser(net)
        while True:
            try:
                command = input('>> ').lower()
            except EOFError:
                break
            if not command:
                continue
            print(parser.parse(command))
    main()