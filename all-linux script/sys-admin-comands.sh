#!/usr/bin/env bash

#it prints the execution process
set -x
whoami
hostname
uname
find
export PATH=$PATH:/home/nkem

which <command> # tells you where a command is stored on the file system

# to get the list of all the port on locally

sudo lsof -i -P | grep LISTEN | grep :$PORT
# command to list and grep a specific port
netstat -vanp tcp | grep 5000