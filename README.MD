Gettings Started
===
```bash
#configure django and postgres 
http://www.marinamele.com/taskbuster-django-tutorial/install-and-configure-posgresql-for-django
#modify .env file to fit db settings
vi .env
#create virtualenvironment
virtualenv venv --python=python3.6
#activate virtual environment
source venv/bin/activate
pip install -r requirements.txt --global-option=build_ext --global-option="-I/usr/local/opt/openssl/include" --global-option="-L/usr/local/opt/openssl/lib"
#update requirements.txt
pur -r requirements.txt

#replace {{project_name}} with target name

#init db
./manage.py makemigrations
./manage.py migrate
#init assets
./manage.py collectstatic
#init admin
./manage.py createsuperuser
#test run
./manage.py runserver
```
