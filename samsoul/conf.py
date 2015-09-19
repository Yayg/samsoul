#! /usr/bin/env python

import sys
import os

def generate_base_conf():
    conf = dict()
    conf['login'] = 'login_x'
    conf['pass_socks'] = 'donteven think about it'
    conf['sm14'] = '10.41.14'
    conf['sm15'] = '10.41.15'
    conf['labsr'] = '10.41.16'
    conf['midlab'] = '10.41.17'
    conf['cisco'] = '10.41.18'
    conf['pasteur'] = '10.41.19'
    conf['VJ'] = '10.3'
    return conf

def generate_conf():
    conf = generate_base_conf()
    print('login' + ": " + conf['login'])
    print('pass_socks' + ": " + conf['pass_socks'])
    print()
    for i in conf:
        if (i != 'login' and i != 'pass_socks'):
            print(i + ": " + conf[i])

def get_conf(conf):
    rooms = dict()
    conf = conf.split('\n')
    conf_list = []
    for line in conf:
        conf_list.append(line.split())
    login = False
    passwd = False
    for room in conf_list:
        if room == []:
            continue
        if len(room) < 2:
            sys.exit('Missing parameters in config')
        room[0] = room[0][:-1]
        if room[0] == "login":
            login = True
        if room[0] == "pass_socks":
            passwd = True
        rooms[room[0]] = room[1]
    if not (login and passwd):
        sys.exit('Missing login or password in config file')
    return rooms
