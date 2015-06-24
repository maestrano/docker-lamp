FROM ubuntu:14.10
MAINTAINER Maestrano <it@maestrano.com>

# Add ansible configuration
ADD ansible /etc/ansible

WORKDIR /etc/ansible

# Install Ansible
RUN apt-get -y update &&  \
    apt-get -y upgrade &&  \
    apt-get -q -y --no-install-recommends install unattended-upgrades git \
              python-yaml python-jinja2 python-httplib2 python-keyczar \
              python-paramiko python-setuptools python-pkg-resources python-pip &&  \
    mkdir -p /etc/ansible/ &&  \
    pip install ansible
RUN ansible-playbook -i hosts site.yml &&  \
    apt-get clean purge -y python2.6 python2.6-minimal &&  \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Expose port 22 and 80
EXPOSE 22 80

# Configuration script
ADD /scripts/configure.py /root/configure.py
RUN chmod 755 /root/configure.py

# Startup script to run mysql and apache
ADD /scripts/init.sh /root/init.sh
RUN chmod 755 /root/init.sh

ENTRYPOINT ["/root/init.sh"]
CMD ["/root/init.sh"]
