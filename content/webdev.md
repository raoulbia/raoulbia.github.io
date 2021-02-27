Title: Web Development
Date: 2017-11-01
Category: Web Development
Slug: web_development
Summary: Web Development

#### nginx

* `sudo nginx -t` to test nginx
* `sudo /etc/init.d/nginx reload` to restart nginx
* `sudo apt-get remove nginx nginx-common` to to remove all but config files
* `sudo apt-get purge nginx nginx-common` to remove everything
* `find /etc/nginx -name '*.conf' | xargs grep -i log`
* [How To Set Up nginx Virtual Hosts (Server Blocks)](https://www.youtube.com/watch?v=fpeQlbdRmKI)

<br>

#### start ngrok

`./ngrok http 5000`

<br>

#### Heroku

Pre-requisite: Heroku Command Line Tool

* needed for `heroku login --interactive` and `heroku create`
* Option 1: `sudo snap install --classic heroku`
* Option 2: `curl https://cli-assets.heroku.com/install.sh | sh`
* [read more](https://devcenter.heroku.com/categories/command-line)

Stop/Start Heroku VM

* `heroku ps:scale web=0` wait for a few secs, then `heroku ps:scale web=1`
  
General Heroku Deployment Guidelines

* [overview](https://devcenter.heroku.com/articles/git)
* add `Pipfile` to `.gitignore` to ensure that dependencies are installed from `requirements.txt`.
* add `.env/` to `.gitignore` to ensure that secret key is hidden on github/gitlab.
* after deployment run `heroku ps:scale web=1 --app  name-of-app`
* view logs:`heroku logs --tail --app  name-of-app`
* Login to Heroku VM:
* `heroku login`
* `heroku run bash`
* [clear the build cache](https://help.heroku.com/18PI5RSY/how-do-i-clear-the-build-cache)
* [related article](https://chatbotslife.com/github-repo-heroku-explained-how-to-host-your-bot-server-python-8b3ec4f071ce)

Heroku **Flask** Deployment

* `heroku create <NAME>` to create a Heroku remote
* `git add . ; git commit -m "update"`
* `git push heroku master`
* `heroku run python manage.py migrate`
* `heroku run python manage.py createsuperuser`

Heroku **Dash** Deployment

* [see here](https://github.com/plotly/dash-heroku-template)
* change Step 6 to: `git remote add heroku https://git.heroku.com/semmeddb`
    
Heroku **Django** Deployment

* [heroku django template](https://github.com/heroku/heroku-django-template)
*  [about static assets](https://devcenter.heroku.com/articles/django-assets)
* `pipenv install whitenoise`
* `python manage.py collectstatic`

Procfile, gunicorn, django-heroku

* [Django App configuration](https://devcenter.heroku.com/articles/django-app-configuration)
* in Procfile `web: gunicorn myproject.wsgi` replace "myproject" by name of dir in which `settings.py` is located.
* add `import django_heroku` to `settings.py` (top)
* add `django_heroku.settings(locals())` to `settings.py` (bottom)

<br>

#### Django2

Useful commands

```python
django-admin startproject app1
python manage.py runserver
python manage.py migrate
python manage.py makemigrations
python manage.py createsuperuser
```

Django templates

in `settings.py`

```
 BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
 ...
 TEMPLATES = [
   {
       'DIRS': [os.path.join(BASE_DIR, 'firstwebsite/templates')]
   }]
```

in `urls.py`

 * ...to be completed (Django1 vs Django2 issue)
 * try `from views import` appraoch

Django Resources

*  [Classy Class-Based Views ccbv.co.uk](https://ccbv.co.uk/)
*  [docs.djangoproject.com/en/2.1/ref/models](https://docs.djangoproject.com/en/2.1/ref/models/)
*  [docs.djangoproject.com/en/2.1/ref/class-based-views/generic-display](https://docs.djangoproject.com/en/2.1/ref/class-based-views/generic-display/)
*  [docs.djangoproject.com/en/2.1/topics/class-based-views/generic-display](https://docs.djangoproject.com/en/2.1/topics/class-based-views/generic-display/)
*  [docs.djangoproject.com/en/2.1/ref/templates/builtins](https://docs.djangoproject.com/en/2.1/ref/templates/builtins/)
*  [docs.djangoproject.com/en/2.1/topics/db/queries](https://docs.djangoproject.com/en/2.1/topics/db/queries/)

<br>

#### Apache2

* `apachectl -S`
* `sudo service apache2 restart`
* [Configure Apache for Flask](http://flask.pocoo.org/docs/1.0/deploying/mod_wsgi/#configuring-apache)
* [Deploy Flask Python3 on Apache2 on Ubuntu](http://terokarvinen.com/2016/deploy-flask-python3-on-apache2-ubuntu)
* [Flask HelloWorld App_with_Apache WSGI_Ubuntu14](https://www.bogotobogo.com/python/Flask/Python_Flask_HelloWorld_App_with_Apache_WSGI_Ubuntu14.php)
* [Installing LAMP](https://websiteforstudents.com/installing-apache2-mariadb-on-ubuntu-16-04-17-10-18-04-with-php-7-2-support-lamp/)

<br>

#### Flask

* `import pdb; pdb.set_trace()`
*  error: address already in use
    * `sudo lsof -i :5000`
    * `sudo kill-9 PID`
* `FLASK_APP=run.py flask run`
* [flask does not see change in .js file](https://stackoverflow.com/questions/41144565/flask-does-not-see-change-in-js-file)
* [API Tutorial: How to get run data using Python & Flask](https://help.parsehub.com/hc/en-us/articles/217751808-API-Tutorial-How-to-get-run-data-using-Python-Flask)
* [gunicorn and wsgi configuration](https://stackoverflow.com/questions/53258168/gunicorn-wont-start-flask-app-because-application-object-must-be-callable)
* [gunicorn and flask](https://coderwall.com/p/pstm1w/deploying-a-flask-app-at-heroku)

<br>

#### Node JS

Install nodejs:

```
curl -sL https://deb.nodesource.com/setup_8.x — Node.js 8 LTS "Carbon" | sudo -E bash -
sudo apt-get install -y nodejs
```

symlink issue with Vagrant VM shared folder:

`npm install --no-bin-links`

port alread in use

`ps aux | awk '/node/{print $2}' | xargs kill -9`

<br>

#### Redux

* <https://www.bram.us/2016/10/25/plotly-academy-state-management-with-redux/>

<br>

#### Ansible

* [Developing a VM-with Vagrant and Ansible](https://blog.jetbrains.com/pycharm/2017/12/developing-in-a-vm-with-vagrant-and-ansible/)

<br>

#### SAP Conversational AI

* markdown URL syntax: `[Click Here]({{memory.url}})` 

<br>

#### Misc.

* <https://wireframe.cc/>
* <https://www.creative-tim.com/product/get-shit-done-kit>
* <https://uxplanet.org/how-the-bootstrap-4-grid-works-a1b04703a3b7>
* <https://hackerthemes.com/bootstrap-cheatsheet/#col-sm-1>


