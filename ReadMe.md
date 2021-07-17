The Development Impact Fee Calculator:

ImpactFees is a Django 3.x Web Application used for calculating fees assessed in all City of Tucson Service Areas based on its use and size within the designated Service Area.

Current Version Django 3.2.2 

Author:
    Joseph Duclos, IT Analyst (joseph.duclos@tucsonaz.gov)

Installation Instructions:

$ git clone https://github.com/tucsonaz/ImpactFees2021.git

On a fresh repository clone you will need to do the following:
Create The Virtual Environment (ENV)
$ cd ImpactFees
$ virtualenv -p python3.6 env
$ source env/bin/activate
$ pip install --upgrade pip
$ pip install -r requirements.txt
$ deactivate

Create settings.py & wsgi.py Files Under /ImpactFees/core/ Directory, Set Permissions
$ cd core
$ touch settings.py wsgi.py
$ chmod 0774 wsgi.py
$ cd ..

Configuration for Apache SSL.conf
# The <Directory> piece ensures that Apache can access your wsgi.py file.
<Directory /var/www/apps/impactfee>
    <Files wsgi.py>
        Require all granted
    </Files>
</Directory> 

# The Alias directive allows documents to be stored in the local filesystem other than under the DocumentRoot. 
Alias /impactfee/static /var/www/apps/impactfee/static
<Directory /var/www/apps/python>
 Require all granted
</Directory>

WSGIProcessGroup impactfee
WSGIDaemonProcess impactfee python-path=/var/www/apps/impactfee python-home=/var/www/apps/impactfee/env
WSGIScriptAlias /impactfee /var/www/apps/impactfee/core/wsgi.py process-group=impactfee
WSGIApplicationGroup %{GLOBAL}

Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.


Settings.py: Be sure to add the following items:

ALLOWED_HOSTS = ['hostname']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'impactfee',			# Appname
    'django.contrib.humanize'		# Used in the form display
]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],			# For Templates to function
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]




DATABASES�=�{
	'default':�{
	'ENGINE':�'django.db.backends.mysql',
	'NAME':�'dbname',
	'USER':�'username',
	'PASSWORD':�'password',
	'HOST':�'hostname',
	'PORT':�'3306',
	}
}

STATIC_URL�=�'/static/'
MEDIA_ROOT�=�os.path.join(BASE_DIR,�'static/images')
STATICFILES_DIRS�=�[BASE_DIR,�'static']

DEFAULT_AUTO_FIELD =�'django.db.models.BigAutoField'
