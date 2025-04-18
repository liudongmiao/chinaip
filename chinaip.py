#!/usr/bin/env python
#fileencoding: utf-8
#Author: Liu DongMiao <liudongmiao@gmail.com>
#Created  : TIMESTAMP
#Modified : TIMESTAMP
import sys
import socket
import struct
MAXBITS = 12
getip = lambda x: socket.inet_ntoa(struct.pack('!I', x))
getint = lambda x: struct.unpack('!I', socket.inet_aton(x))[0]
def check_range(start, end):
    count = 0
    base = start
    while base <= end:
        step = 0
        while (base | (1 << step)) != base:
            if (base | (0xffffffff >> (31 - step))) > end:
                break
            step += 1
        if step >= (32 - MAXBITS):
            count += (1 << step)
            print('%s/%s' % (getip(base), (32 - step)))
        base += (1 << step)
    return count
def parse_record(name):
    routed = 0
    amount = 0
    start = end = 0
    for x in open(name):
        # apnic|CN|ipv4|1.0.1.0|256|20110414|allocated
        if 'CN|ipv4' not in x:
            continue
        lists = x.split('|')
        ip = lists[3]
        count = int(lists[4])
        newstart = getint(ip)
        newend = newstart + count
        if end == newstart:
            end = newend
        else:
            if end - start + 1 >= (1 << (32 - MAXBITS)):
                routed += check_range(start, end - 1)
            amount += end - start
            start = newstart
            end = newend
    print('%d%%' % (100 * routed / amount), file=sys.stderr)
DELEGATED_APNIC = 'ftp.apnic.net/stats/apnic/delegated-apnic-latest'
if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('please download %s' % DELEGATED_APNIC, file=sys.stderr)
    else:
        print('10.0.0.0/8')
        print('172.16.0.0/12')
        print('192.168.0.0/16')
        if len(sys.argv) > 2:
            MAXBITS = int(sys.argv[2])
        parse_record(sys.argv[1])
# vim: set sta sw=4 et:
