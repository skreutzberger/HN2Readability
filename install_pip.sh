#!/bin/bash
# a script which installs the Readability API
# and sets the file permissions
# requires Python 2.7

# install pip
mkdir src
cd src
wget http://pypi.python.org/packages/source/p/pip/pip-0.6.3.tar.gz
tar xzf pip-0.6.3.tar.gz
cd pip-0.6.3 
sudo python setup.py install
cd ..
cd ..
rm  -r src

chmod +x install.sh
./install.sh