#!/usr/bin/env python

# Update the application version from Git repository

import json
import os

# Extra variables to be passed to Ansible
extra_vars = {}

# Map the environment variables starting with MNO_VARIABLE_NAME=123 to a hash {'variable_name' : 123}
for key in os.environ.keys():
  if key.startswith('MNO_'):
    name = key.replace("MNO_", "").lower()
    value = os.environ[key]
    extra_vars[name] = value

# Call Ansible to update the application
command = "cd /etc/ansible && ansible-playbook -i hosts site.yml --tags 'update'"
os.system(command)

# Call Ansible to re-configure the environment as the previous command may have reset the API keys
command = "cd /etc/ansible && ansible-playbook -i hosts site.yml --tags 'configuration' --extra-vars='" + json.dumps(extra_vars) + "'"
os.system(command)
