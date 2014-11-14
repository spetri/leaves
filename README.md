Leaves:

A Baha'i search engine that allows an individual to search the Baha'i Writings.

Technical Details:
To run the server: python manage.py runserver
To run migrations:

> python manage.py makemigrations
> python manage.py migrate

To run ElasticSearch module, the command is simply: elasticsearch

Regarding indices, to clear and rebuild an index, use the following commands:

> python manage.py rebuild_index

(rebuild_index is a short for running two commands: clear_index and update_index)
