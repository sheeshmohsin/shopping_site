Shopping Site
=============

## Setup

1. Install system dependencies: 
    1. For Installing git in Fedora: ``$ sudo yum install git``
    1. For Installing git in Ubuntu: ``$ sudo apt-get install git``

The steps below will get you up and running with a local development environment. We assume you have the following installed:

* pip
* virtualenv

First make sure to create and activate a virtualenv_, then open a terminal at the project root and install the requirements for local development::

    $ pip install -r requirements.txt

.. _virtualenv: http://docs.python-guide.org/en/latest/dev/virtualenvs/

1. Get the source: ``$ git clone https://github.com/sheeshmohsin/shopping_site.git``
1. Go to **shopping_site**'s repository directory just cloned: ``$ cd shopping_site``

You can now run the usual Django ``runserver`` command after syncdb(replace ``yourapp`` with the name of the directory containing the Django project)::

    $ python yourapp/manage.py syncdb
    $ python yourapp/manage.py runserver