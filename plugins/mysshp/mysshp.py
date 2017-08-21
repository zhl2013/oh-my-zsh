#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys,re

import csv

sshHosts = sys.path[0] + "/sshp.csv"
script = sys.path[0] + "/login.sh"
script_nest = sys.path[0] + "/login_nest.sh"

spliteChar = ":"

def _readSshpConfig():
    hosts=[]
    if(os.path.exists(sshHosts) == False):
        print sshHosts + " is no exist"
        return hosts

    with open(sshHosts, 'rb') as f:        # 采用b的方式处理可以省去很多问题
        reader = csv.DictReader(f)
        for row in reader:
            hosts.append(row)
        # os.execvp(ssh, exe_args)
    return hosts

def _getCompectrlDict(hosts):
    result={}
    strCompectrl=""
    if(len(hosts)>0):
        for host in hosts:
            groupName = host["groupName"]
            user = host["user"]
            if groupName not in result:
                result[groupName]=host
            result[groupName + spliteChar + host["host"]]=host
            result[groupName + spliteChar + host["host"] + spliteChar + user] = host
            for c in host["compectl"].split(" "):
                result[groupName + spliteChar + c + spliteChar + user]=host
    return result

def _sshLogin(host_info):
    port = "22"
    host = host_info["host"]
    user = host_info["user"]
    pwd = host_info["pwd"]
    keyFile = host_info["keyfile"]

    if(host_info["port"]!=''):
        port = host_info["port"]


    ssh = script
    exe_args = []

    # exe_args = [ssh, nest_host, nest_port, nest_parent['user'], nest_parent['password'], host, port, node['user'], node['password']]
    # else:
    # exe_args = [ssh, host, port, node['user'], node['password'], node['id_file']]


    if keyFile:
        # key login
        exe_args = [ssh,host,port,user,"",keyFile]
    elif pwd:
        #pwd login
        exe_args = [ssh,host,port,user,pwd]
    else:
        # 默认秘钥登陆
        exe_args = ["login.sh",host, port,user]
    os.execvp(ssh, exe_args)



if __name__ == '__main__':
    host = _readSshpConfig()
    host_dict = _getCompectrlDict(host)

    if len(sys.argv)==1:
        print "getCompectrl or login"
    elif sys.argv[1]=='getCompectrl':
        print " ".join(host_dict.keys())
    elif sys.argv[1]=='login':
        if sys.argv[2]:
            key = sys.argv[2]
            if host_dict.has_key(key):
                host_info = host_dict[sys.argv[2]]
                _sshLogin(host_info)
            else:
                print "key " + sys.argv[2] + " is not exist host_info"
        else:
            print "lost params"
    else:
        print "getCompectrl or login"

