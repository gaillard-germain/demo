# Demo

## About
This is a technical test carried out on behalf of Beesbusy.  
<br>
The requested features were:
- search for users according to one or more criteria.
- display of the result list.
- consultation of the details of a user.

*I added an extra feature to add new user.*

## Language and dependencies:
- Python3
- Django
- Django Rest Framework
- Vue CLI
- Bootstrap
- Axios
- jquery
- ...

## Install

### Install Django
- Fork and clone the project.
- Create a python virtual environnement in the fresh cloned directory: `python3 -m venv <your venv name>`
- Activate it: `source <your venv name>/bin/activate`.
- Install python dependencies: `pip install -r requirements.txt`.
- Migrate: `./manage.py migrate`.
- You can populate database with some fake data: `./manage.py loadata fake_data.json`.

### Install Vue CLI
- `npm install -g @vue/cli`

## Run
- Run django server at port 8080: in the root of the project `./manage.py runserver 8080`.
- Run vue server: in vue-demo directory `npm run serve`.
- Open your web brother at this address: [http://localhost:8081/](http://localhost:8081/).
