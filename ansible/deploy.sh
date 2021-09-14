#!/bin/bash
ansible-playbook --key-file ~/projects/myssh -u root  -vv -i  inventories/dev-stage/dyn.py  $1.yml
