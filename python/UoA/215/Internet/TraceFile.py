#!/usr/bin/env python
from sys import stdout

__author__ = 'Laurence Armstrong'
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
        "TraceFile.py", "11/04/16", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
stdout.write(authorship_string)

import matplotlib.pyplot as plt
import math

traceLines = []

f = open("trace.txt")

for l in f:
    traceLines.append(l.strip().split())

f.close()


class Packet(object):
    def __init__(self, data):
        self.timestamp = float(data[0])
        self.sourceID = int(data[1])
        self.destID = int(data[2])
        self.sourcePort = int(data[3])
        self.destPort = int(data[4])
        self.size = int(data[5])

    def __str__(self):
        return "time: {}, source ID: {}, dest ID: {}, source port: {}, dest port: {}, size: {} byte(s)".format(
            self.timestamp,
            self.sourceID,
            self.destID,
            self.sourcePort,
            self.destPort,
            self.size
        )

    def __len__(self):
        return self.size

    def __repr__(self):
        return str(self)


class Trace(object):
    def __init__(self, packet_data):
        self.sender_hosts = set()
        self.recieve_hosts = set()
        self.source_hosts = set()
        self.dest_hosts = set()

        # For iteration
        self.current_item = 0

        self.packets = []
        for p in packet_data:
            packet_p = Packet(p)

            self.sender_hosts.add(packet_p.sourceID)
            self.recieve_hosts.add(packet_p.destID)
            self.source_hosts.add(packet_p.sourcePort)
            self.dest_hosts.add(packet_p.destPort)

            self.packets.append(packet_p)

    def __str__(self):
        s = ""
        for p in self.packets:
            s += str(p) + '\n'
        return s

    def __getitem__(self, item):
        return self.packets[item]

    def __len__(self):
        return len(self.packets)

    def trace_duration(self):
        return self[-1].timestamp

    def total_bytes(self):
        sum = 0
        for p in self.packets:
            sum += len(p)
        return sum

    def __iter__(self):
        return self

    def __next__(self):
        # return current_item until next second
        start_second = int(self[self.current_item].timestamp)
        second_packets = []
        while start_second == int(self[self.current_item].timestamp):
            second_packets.append(self[self.current_item])
            self.current_item += 1
            if self.current_item > len(self)-1:
                self.current_item = 0
                raise StopIteration
        return second_packets

    def packets_per_host(self):
        host_packets = {}
        for p in self.packets:
            host_packets[p.sourceID] = host_packets.get(p.sourceID, 0) + 1
        return host_packets

    def packets_per_port(self):
        port_packets = {}
        for p in self.packets:
            port_packets[p.sourcePort] = port_packets.get(p.sourcePort, 0) + 1
        return port_packets

traceData = Trace(traceLines)


def print_stats(trace):
    print("Number of packets transferred: {} packets".format(len(trace)))
    print("Average packet arival rate: {:.2f} packets/second".format(len(trace)/trace.trace_duration()))
    print("Average data rate: {:.2f} bits/second".format(trace.total_bytes() * 8 / trace.trace_duration()))
    print("Trace duration: {:.2f} seconds".format(trace.trace_duration()))
    print("Number of distinct sender hosts: {}".format(len(trace.sender_hosts)))
    print("Number of distinct reciever hosts: {}".format(len(trace.recieve_hosts)))
    print("Number of distinct source ports: {}".format(len(trace.source_hosts)))
    print("Number of distinct destination ports: {}".format(len(trace.dest_hosts)))


def plot_packets_per_second(trace):
    plt.figure()
    time = []
    packets_at_time = []

    for second, packets in enumerate(trace):
        time.append(second)
        packets_at_time.append(len(packets))

    plt.plot(time, packets_at_time)
    plt.xlabel("time (s)")
    plt.ylabel("packets")


def plot_bytes_per_second(trace):
    plt.figure()
    time = []
    bytes_at_time = []

    for second, packets in enumerate(trace):
        time.append(second)
        bytes_at_time.append(sum([len(packet)/1000 for packet in packets]))

    plt.plot(time, bytes_at_time)
    plt.xlabel("time (s)")
    plt.ylabel("data transferred (kB)")


def plot_packet_size_feq(trace):
    plt.figure()
    packet_sizes = [len(p) for p in trace.packets]

    plt.hist(packet_sizes, bins=(0, 200, 400, 1000, 1600))
    plt.xlabel("frequency")
    plt.ylabel("packet size (kB)")


def plot_packets_per_host(trace):
    plt.figure()
    packets_per_host = sorted(trace.packets_per_host().items(), key=lambda x: x[1], reverse=True)

    plt.plot([math.log10(i) for i in range(1, len(packets_per_host)+1)], [math.log10(p[1]) for p in packets_per_host])
    plt.xlabel("log(host rank)")
    plt.ylabel("log(number of packets)")


def plot_packets_per_port(trace):
    plt.figure()
    packets_per_port = sorted(trace.packets_per_port().items(), key=lambda x: x[1], reverse=True)

    plt.plot([math.log10(i) for i in range(1, len(packets_per_port)+1)], [math.log10(p[1]) for p in packets_per_port])
    plt.xlabel("log(port rank)")
    plt.ylabel("log(number of packets)")

print_stats(traceData)
plot_packets_per_second(traceData)
plot_bytes_per_second(traceData)
plot_packet_size_feq(traceData)
plot_packets_per_host(traceData)
plot_packets_per_port(traceData)

plt.show()


