#!/bin/bash

# Execute configuration script
/root/configure.py

# Start services
/etc/init.d/mysql start
/etc/init.d/apache2 start
/bin/bash