# Django To-Do List Project (using TTD)

This is a Django-based To-Do List project designed to demonstrate Test-Driven Development (TDD). The project features a simple CRUD application that allows users to create, read, update, and delete tasks. Additionally, it allows users to mark tasks as "checked" or "unchecked" with a checkbox.

It is focused rather on backend functionality and example of how one can implement functional tests (aka end-to-end tests) using **Selenium** and **pytest** with **django plugin**.

I almost completely abandoned tries to make it visually appealing.

## Installation

```sh
git clone https://github.com/yourusername/django-todo-list.git
cd django-todo-list
```

```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

```sh
python manage.py migrate
python manage.py runserver
```

Open your browser and go to
`http://localhost:8000`

## Running tests

To run all tests

```sh
pytest
```

When you want to run only one file you can specify it like this:

```sh
pytest <filename>
```

for example

```sh
pytest todo_list/tests/functional_tests.py
```
