 .. image:: https://img.shields.io/badge/License-MIT-yellow.svg?style=flat
    :target: https://opensource.org/licenses/MIT
    :alt: License

Hikyaku Server
================

API server in Hikyaku system.

Quick Start
--------------------

::

    $ git clone https://github.com/ossc-bukatsu/hikyaku-server
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

Operation Examples
--------------------

Create a user:
::
    $ curl -X POST http://localhost:8000/api/users/ -d "name=user01" -d "mail=user01@gmail.com" -d "password=password" -d "point=12" -d "note=090-9999-8888"
    {"id":8,"name":"user01","mail":"user01@gmail.com","password":"password","point":12,"note":"090-9999-8888"}

Read the user:
::
    $ curl http://localhost:8000/api/users/8/
    {"id":8,"name":"user01","mail":"user01@gmail.com","password":"password","point":12,"note":"090-9999-8888"}t

Create another user:
::
    $ curl -X POST http://localhost:8000/api/users/ -d "name=user02" -d "mail=user02@gmail.com" -d "password=password" -d "point=12" -d "note=090-9999-8888"
    {"id":9,"name":"user02","mail":"user02@gmail.com","password":"password","point":12,"note":"090-9999-8888"}

Read users:
::
    $ curl http://localhost:8000/api/users/
    {"count":2,"next":null,"previous":null,"results":[{"id":8,"name":"user01","mail":"user01@gmail.com","password":"password","point":12,"note":"090-9999-8888"},{"id":9,"name":"user02","mail":"user02@gmail.com","password":"password","point":12,"note":"090-9999-8888"}]}

Update the first user:
::
    $ curl -X PUT http://localhost:8000/api/users/8/  -d "name=user01" -d "mail=user01@gmail.com" -d "password=password" -d "point=15" -d "note=090-9999-8888"
    {"id":8,"name":"user01","mail":"user01@gmail.com","password":"password","point":15,"note":"090-9999-8888"}t

Delete the second user:
::
    curl -X DELETE http://localhost:8000/api/users/9/

Read the users:
::
    $ curl http://localhost:8000/api/users/
    {"count":1,"next":null,"previous":null,"results":[{"id":8,"name":"user01","mail":"user01@gmail.com","password":"password","point":15,"note":"090-9999-8888"}]}
