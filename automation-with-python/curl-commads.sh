#!/usr/bin/env bash
set -x -o
set -x -o pipefail
#this command list all the process and ports that are active on a Macor linux system

#[lsof means'list open file', in unix mechine everythong including sockets are treated as files]
lsof 
lsof -i @localhost

curl https://nomad.kubebridge.com/

curl -I https://nomad.kubebridge.com/

curl --include https://nomad.kubebridge.com/

curl -v --include https://nomad.kubebridge.com/


