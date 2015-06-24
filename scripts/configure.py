#!/usr/bin/env python

# Use environment variables over Ansible defaults
# To do so, the Ansible extra-vars parameters is built based on available environment variables

import json
import os

# Access the variables
notification_mail = os.environ.get('SSMTP_NOTIFICATION_EMAIL')
ssmtp_mailhub = os.environ.get('SSMTP_MAILHUB')
ssmtp_hostname = os.environ.get('SSMTP_HOSTNAME')
ssmtp_auth_user = os.environ.get('SSMTP_AUTH_USER')
ssmtp_auth_pass = os.environ.get('SSMTP_AUTH_PASS')

# The variable skip_install is set so packages installation is skipped
extra_vars = {'skip_install' : True}
# Build the extra_vars parameter
if notification_mail != None:
  extra_vars['notification_mail'] = notification_mail
if ssmtp_mailhub != None:
  extra_vars['ssmtp_mailhub'] = ssmtp_mailhub
if ssmtp_hostname != None:
  extra_vars['ssmtp_hostname'] = ssmtp_hostname
if ssmtp_auth_user != None:
  extra_vars['ssmtp_auth_user'] = ssmtp_auth_user
if ssmtp_auth_pass != None:
  extra_vars['ssmtp_auth_pass'] = ssmtp_auth_pass

# Call Ansible to configure the environment
command = "cd /etc/ansible && ansible-playbook -i hosts site.yml --extra-vars='" + json.dumps(extra_vars) + "'"
os.system(command)
