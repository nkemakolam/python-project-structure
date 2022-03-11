#!/usr/bin/env bash

#it prints the execution process
set -x
#code to install dependencies for user authentication using pip3
# pip install pandas==1.3.2 numpy==1.21.2 Flask==2.0.2 for specific versions
# pip install --no-cache-dir -r requirements.txt

#python -m venv tutorial-env

virtualenv flask

source flask/bin/activate

pip3 install flask flask_sqlalchemy flask_login flask_bcrypt flask_wtf wtforms email_validator psycopg2

pip freeze > requirements.txt