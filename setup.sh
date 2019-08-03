#!/usr/bin/env bash
echo "============================================================================"
# installing
sudo apt-get -y install python3.6 python3-pip
echo "============================================================================"
# install virtualenv
pip3 install virtualenv
echo "============================================================================"
# create virtual env
virtualenv -p /usr/bin/python3.6 venv
echo "============================================================================"
# activate virtual env
source venv/bin/activate
echo "============================================================================"
# install dependancies
pip install -r requirements.txt
echo "============================================================================"
# start server
python app.py
echo "============================================================================"
