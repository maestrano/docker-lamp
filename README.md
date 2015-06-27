# Build Maestrano LAMP stack based on Ubuntu 14.10

## Build Docker container locally
`sudo docker build -t .`

## Entry point
The script `scripts/init.sh` will be run on container start, taking care of starting Apache and MySQL services.
As part of the container initialization process, the script `scripts/configure.py` is executed. It will call Ansible to run the playbook `ansible/site.yml` passing all environment variables prefixed by "MNO_". The intent is to overwrite the Ansible configuration adding playbooks to be run to install and configure PHP applications.