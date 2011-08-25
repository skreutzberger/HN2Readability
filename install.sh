#!/bin/bash
# a script which installs the Readability API
# and sets the file permissions
# requires Python 2.7 and Pip

# install readability-api
sudo pip install readability-api 
chmod +x setup.py
chmod +x hn2readability.py
cd data
cp settings_default.json settings.json
cd ..
./setup.py
