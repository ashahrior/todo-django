# Todo Django

A simple todo application built with Django 2.0.6 featuring task management with Bootstrap styling.

![image](https://user-images.githubusercontent.com/36689470/172991665-42c3e503-644d-44f3-abcb-030093c0323d.png)

## Features

- ✅ Add new todo items
- ✅ Mark tasks as completed
- ✅ Delete completed tasks
- ✅ Delete all tasks
- ✅ Responsive Bootstrap UI

## Tech Stack

- **Backend**: Django 2.0.6
- **Database**: SQLite
- **Frontend**: Bootstrap 4.5.3, jQuery 3.5.1
- **Styling**: Custom CSS with Bootstrap themes

## Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

3. **Start development server:**
   ```bash
   python manage.py runserver
   ```

4. **Access the app:**
   Open http://127.0.0.1:8000 in your browser

## Project Structure

```
todo-django/
├── mylist/              # Django project settings
│   ├── settings.py      # Project configuration
│   ├── urls.py          # Root URL routing
│   └── wsgi.py          # WSGI configuration
├── todolist/            # Main Django app
│   ├── models.py        # Todolist model
│   ├── views.py         # View functions
│   ├── forms.py         # Form definitions
│   ├── urls.py          # App URL routing
│   ├── templates/       # HTML templates
│   └── static/          # CSS, JS, fonts
└── db.sqlite3           # SQLite database
```

## Admin Interface

Create a superuser to access Django admin:

```bash
python manage.py createsuperuser
```

Then visit http://127.0.0.1:8000/admin
