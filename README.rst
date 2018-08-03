 .. image:: https://img.shields.io/badge/License-MIT-yellow.svg?style=flat
    :target: https://opensource.org/licenses/MIT
    :alt: License

Hikyaku Server
================

API server in Hikyaku system.

Quick Start
--------------------

::

    $ git clone https://github.com/k-tamura/hikyaku-server.git
    $ cd hikyaku-server/
    $ python3 -m venv venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt
    # If you are using proxy server, add the following options to pip command,
    # --proxy=http://[PROXY_USER]:[PROXY_PASSWORD]@[PROXY_HOST]:[PROXY_PORT]/ --trusted-host pypi.python.org  --trusted-host pypi.org  --trusted-host files.pythonhosted.org
    $ cd src/hikyaku_server
    $ python manage.py runserver

Access to the admin console: http://localhost:8000/admin/

Access to the user maintenance API: http://localhost:8000/api/
