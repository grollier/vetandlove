# Python: Getting Started

A barebones Django app, which can easily be deployed to Heroku.

This application supports the [Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python) article - check it out.

## Running Locally

Make sure you have Python [installed properly](http://install.python-guide.org). Also, install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) and [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup). and [PIP](https://pip.pypa.io/en/stable/installing/)

## Creating an Enviroment for your app

Now that you have all of the above installed its time to set a virtual enviroment for your application to work propertly.

### why do YOU need a virtual enviroment?
The reason that we will create a virtualenv its for a better use of versionig withing your system distributios. Lets say you want to install a version of foundation for *genericApp* but you dont want to remove the actual installed version.Setting enviroments for your apps creates a segmented portion in your system so your can use various of all of the features you would like to install for your framework to work the wey you want it.

lets begin with: [Virtualenv](https://virtualenv.pypa.io/en/stable/installation/) next you will have to install [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) after you have succesfully installed virtualenv and wrapper lets clone an already prepared Django app

```sh
$ git clone git@github.com:heroku/python-getting-started.git
$ cd python-getting-started

$ pipenv install

$ createdb python_getting_started

$ python manage.py migrate
$ python manage.py collectstatic

$ heroku local
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)



## PipFile
Hey guys this is how the actual pipfiles looks like:

```sh
[[source]]

url = "https://pypi.python.org/simple"
verify_ssl = true


[packages]

django = "*"
gunicorn = "*"
django-heroku = "*"
psycopg2 = "*"
django-cors-headers = "*"
djangorestframework = "*"
coreapi = "*"
Markdown = "*"
django-filter = "*"
django-crispy-forms = "*"
django-guardian = "*"
httpie = "*"
dajngo-zurb-foundation = "*"

[requires]

python_version = "3.6"
```
 please be sure you have all the dependencies installed by checking with:
 ```sh
 pip freeze
 ```
 if not! then proceed to install them
 ```sh
 pip install #name of the dependencies
 ```
 
 
 <a href="http://www.youtube.com/watch?feature=player_embedded&v=y-Gmg-XxNAc
" target="_blank"><img src="http://img.youtube.com/vi/y-Gmg-XxNAc/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>
