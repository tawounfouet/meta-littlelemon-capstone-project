
```bash
# Create virtual environment
python3 -m venv .MetaCapPvenv

# Activate virtual environment
source .MetaCapPvenv/bin/activate

# Install Django
pip install django

# Create Django project
django-admin startproject littlelemon  .

# Create Django app Restaurant
python manage.py startapp restaurant

python manage.py startapp LittleLemonAPI
```

## Django Database Configuration and Models

```bash

#Install MySQL Development Files:
brew install mysql



#  append the path to MySQL to the environment variables
export PATH=${PATH}:/usr/local/mysql/bin/

#Set Environment Variables:
export MYSQLCLIENT_CFLAGS=`mysql_config --cflags`
export MYSQLCLIENT_LDFLAGS=`mysql_config --libs`

# Set MySQL Include and Library Directories:
export MYSQLCLIENT_CFLAGS="-I/usr/local/opt/mysql/include/mysql"
export MYSQLCLIENT_LDFLAGS="-L/usr/local/opt/mysql/lib -lmysqlclient"

# install mysqlclient
pip3 install mysqlclient



# connect to mysql
mysql -u root -p 

# 

pip3 install mysqlclient 


LittleLemonAPI
