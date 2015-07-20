#!/usr/bin/env python

# Update the application version from Git repository

command = "cd /etc/ansible && ansible-playbook -i hosts site.yml --tags 'update'"
os.system(command)
