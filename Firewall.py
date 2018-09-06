import csv
import ipaddress
import collections


class Firewall:
    def __init__(self, filepath):
        """ We create 4 different branches for the four different direction-protocol pairs, each of which has a
        dictionary at the end, with the port tuple as a key and a list of IP rules. If the IP rule has already been
        seen before then we don't append it, if it isn't then we append it to the list"""
        self.filepath = filepath
        self.data = {"inbound": {"tcp": collections.defaultdict(list), "udp": collections.defaultdict(list)},
                     "outbound": {"tcp": collections.defaultdict(list), "udp": collections.defaultdict(list)}}
        with open(filepath) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                ip_tuple = self.__get_ip_tuple(row[3])
                port_tuple = self.__get_port_tuple(row[2])
                for ip_range in self.data[row[0]][row[1]][port_tuple]:
                    if (int(ip_range[0]) <= int(ip_tuple[0])) and (int(ip_tuple[1]) <= int(ip_range[1])):
                        break
                else:
                    self.data[row[0]][row[1]][port_tuple].append(ip_tuple)

    def accept_packet(self, direction, protocol, port, ip_address):
        """ We take just the single branch which has the matching direction and protocol,
         and loop through the ports in that subset. If we find a match, we loop through the IPs in that
         subset of the port. If we find a match, we return True"""
        required_subset = self.data[direction][protocol]
        for port_in_subset in required_subset:
            if port_in_subset[0] <= port <= port_in_subset[1]:
                for ip_in_subset in required_subset[port_in_subset]:
                    if int(ip_in_subset[0]) <= int(ipaddress.ip_address(ip_address)) <= int(ip_in_subset[1]):
                        return True
        return False

    @staticmethod
    def __get_port_tuple(ports):
        if '-' in ports:
            return tuple(int(i) for i in ports.split("-"))
        else:
            return int(ports), int(ports)

    @staticmethod
    def __get_ip_tuple(ips):
        if '-' in ips:
            return tuple(ipaddress.ip_address(i) for i in ips.split("-"))
        else:
            return ipaddress.ip_address(ips), ipaddress.ip_address(ips)
