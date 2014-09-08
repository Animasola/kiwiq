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
