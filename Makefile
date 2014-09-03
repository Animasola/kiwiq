SHELL=/bin/bash

MANAGE=PYTHONPATH=$(CURDIR) python manage.py

# commands
run:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=kiwi.settings $(MANAGE) runserver
	
shell:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=kiwi.settings $(MANAGE) shell

syncdb:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=kiwi.settings $(MANAGE) syncdb --noinput

migrate:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=kiwi.settings $(MANAGE) migrate qa

test:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=kiwi.settings $(MANAGE) test qa