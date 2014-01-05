Django-Allauth flows with python-social-auth
============================================

This is an small demo project looking to mimic django-allauth_ flows as they
are detailed in `their docs`_ using python-social-auth_. This comes as an answer
to a `request on reddit`_.

Running the demos
-----------------

The project is quite easy to setup once the dependencies are met. Follow these
steps:

* Clone the repository::

    $ git clone https://github.com/omab/psa-allauth.git
    $ cd psa-allauth

* Lets create a virtualenv_ (I'm using virtualenvwrapper_ here)::

    psa-allauth $ mkvirt demo
    [demo] psa-allauth $ 

* Install the dependencies (django_ and python-social-auth_)::

    [demo] psa-allauth $ pip install -r requirements.txt 

* Copy ``local_settings.py.template`` as ``local_settings.py`` and fill the
  blanks::

    [demo] psa-allauth $ cp example/local_settings.py.template example/local_settings.py

* Sync the database::

    [demo] psa-allauth $ python manage.py syncdb --noinput

* Run the demo::

    [demo] psa-allauth $ python manage.py runserver

* Open a browser at ``http://localhost:8000/`` and follow the instructions
  there.

.. _django-allauth: https://github.com/pennersr/django-allauth
.. _their docs: http://django-allauth.readthedocs.org/en/latest/index.html#supported-flows
.. _python-social-auth: https://github.com/omab/python-social-auth
.. _request on reddit: http://www.reddit.com/r/django/comments/1u9nh9/modern_django_registration_packages/cegam4d
.. _virtualenv: http://www.virtualenv.org/en/latest/
.. _virtualenvwrapper: http://virtualenvwrapper.readthedocs.org/en/latest/
.. _django: http://djangoproject.com/
