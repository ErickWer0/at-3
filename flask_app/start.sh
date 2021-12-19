#!/usr/bin/env bash
# apt install python3-virtualenv

virtualenv venv

source venv/bin/activate

pip install -r requirements.txt

export FLASK_APP=hw
export FLASK_DEBUG=1

flask run
