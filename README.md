# Training-and-placement-portal-NITH

Managing Interface for Training and placement portal NITH. [View Demo](http://159.89.167.123/)

* The project is built using [django](https://github.com/django/django).
* Django version: 5.1.6.
* Python version: Python 3.11.11
* Serving Django Applications with Apache and mod_wsgi - [Reference](https://www.digitalocean.com/community/tutorials/how-to-serve-django-applications-with-apache-and-mod_wsgi-on-centos-7).
* [Django Documentation](https://docs.djangoproject.com/en/5.1/contents/) - followed.


# Initial project setup/First time installation
Create a virtual env:
> python -m venv plexus-env

Install pip
> python -m ensurepip --upgrade
> python -m pip install --upgrade pip

Install django
> pip install django

Install mysqlclient
> pip install mysqlclient


Migrate the changes
```
./manage.py migrate
```

* Now collecting all of the static content into the directory location:

```
./manage.py collectstatic
```
The static files will be placed in a directory called static within the project directory.

Testing the project by starting up the Django development server with this command:

```
./manage.py runserver 127.0.0.1:8000
```
Note - Use ``sudo`` before running server as it needs to write ``etc/conf.d/``  and will generate secured keys and certificates.

In the web browser, visit the server's domain name or IP address followed by ``:8000``:
```
http://server_domain_or_IP:8000
```
