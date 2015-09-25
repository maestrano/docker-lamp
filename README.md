# Build Maestrano LAMP stack based on Ubuntu 14.04

## Build Docker container locally
`sudo docker build -t local/docker-lamp .`

## Entry point
The script `scripts/init.sh` will be run on container start, taking care of starting Apache and MySQL services.
As part of the container initialization process, the script `scripts/configure.py` is executed. It will call Ansible to run the playbook `ansible/site.yml` passing all environment variables prefixed by "MNO_". The intent is to overwrite the Ansible configuration adding playbooks to be run to install and configure PHP applications.

## Image creation
The image is created using Ansible. A list of variables used by the MySQL and Apache configuration is defined under ansible/group_vars/all. The variable `power_units` is used as a multiplier for the default minimum memory options. To increase the container capacity, you must start the Docker container with a higher memory allocation and specify a higher value for the `power_units` parameter.

## Docker Hub
The image can be pulled down from [Docker Hub](https://registry.hub.docker.com/u/maestrano/docker-lamp/)

## Launch a LAMP Docker container
```bash
docker run -it -e "MNO_POWER_UNITS=4" maestrano/docker-lamp:latest
 ```
