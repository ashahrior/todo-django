# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Django 2.0.6 todo application with a single `todolist` app. The project uses SQLite database and Bootstrap for styling.

**Project Structure:**
- `mylist/` - Django project configuration
- `todolist/` - Main Django app containing todo functionality
- `db.sqlite3` - SQLite database file
- `requirements.txt` - Python dependencies (Django~=2.0.6)

## Architecture

**Django App Structure:**
- **Model**: `Todolist` model in `todolist/models.py` with `text` (CharField, max 45 chars) and `completed` (BooleanField) fields
- **Views**: Function-based views in `todolist/views.py` handling CRUD operations
- **Forms**: `TodoListForm` in `todolist/forms.py` for input validation with Bootstrap styling
- **Templates**: Single template at `todolist/templates/todolist/index.html`
- **Static Files**: Bootstrap CSS/JS and jQuery located in `todolist/static/todolist/`

**URL Routing:**
- Root URLs in `mylist/urls.py` route to todolist app
- App URLs in `todolist/urls.py` handle: index, add, completed, deleteCompleted, deleteAll

**Database:**
- Uses SQLite with single `Todolist` table
- Migration file: `todolist/migrations/0001_initial.py`

## Common Commands

**Development Server:**
```bash
python manage.py runserver
```

**Database Operations:**
```bash
python manage.py makemigrations
python manage.py migrate
```

**Admin Interface:**
```bash
python manage.py createsuperuser
```

**Django Shell:**
```bash
python manage.py shell
```

**Run Tests:**
```bash
python manage.py test
```

## Key Features

- Add new todo items
- Mark items as completed
- Delete completed items
- Delete all items
- Bootstrap-styled responsive UI