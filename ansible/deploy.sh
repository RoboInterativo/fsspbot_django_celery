#!/bin/bash
ansible-playbook -u root  -vv -i  inventories/dev/hosts  $1

#--key-file ~/projects/myssh 
