import telnetlib

class TelnetWorkers(object):

    def __init__(self, ip, port):
        self.ip_addr = ip
        self.telnet_port = port
        self.time_out_telnet = 5

        try:
            self.__tn_connector = telnetlib.Telnet(self.ip_addr, self.telnet_port,
                                                   self.time_out_telnet)  # connect to the telnet
        except:
            pass

    def connect(self):
        self.delimiter_char = b"\n"
        self.time_out_line = 15

        try:
            self.__line = self.__tn_connector.read_until(self.delimiter_char,
                                                         self.time_out_line)  # Read one line with time out 15 seconds
            return self.__line.decode('ascii')
        except:
            pass