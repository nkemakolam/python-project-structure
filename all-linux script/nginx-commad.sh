#!/usr/bin/env bash

#it prints the execution process
set -x
nginx -v
nginx -t
nginx -T
nginx -s reload