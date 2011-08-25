#!/bin/bash
# a script which installs the Readability API
# and sets the file permissions
# requires Python 2.7 and pip to be installed
sudo pip install readability-api 
chmod +x setup.py
chmod +x hn2readability.py
cd data
rm settings.json
cp settings_default.json settings.json
cd ..
./setup.py
