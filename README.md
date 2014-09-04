 Kiwi Test
=====

- git clone git@github.com:Animasola/kiwiq.git
- mkvirtualenv dummy_env
- cd ./kiwiq/
- pip install -r requirements.txt
- make syncdb
- make migrate
- make test
- make run

Notes
=====
Facebook is not allows to use 'localhost' or '127.0.0.1', as Web Application Url, so
  To login via Facebook:
- Add to your etc/hosts this line -
127.0.0.1       my.kiwiapp.com

- Use this address [my.kiwiapp.com:8000] to browse this application locally.
