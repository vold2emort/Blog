# 📝 Django Blog Project

A simple and customizable blog web application built with Django. Users can create, update, and delete blog posts, view author profiles, and leave comments.

## 🚀 Features

- Create, update, delete blog posts (CRUD)
- Comment system
- Admin panel for content management

## 🖥️ Tech Stack

- Backend: [Django](https://www.djangoproject.com/)
- Database: SQLite (default), easy to switch to PostgreSQL or MySQL
- Frontend: HTML, CSS, Bootstrap
- Authentication: Django's built-in auth system

## 🏁 Getting Started

### Prerequisites

- Python 3.9+
- pip
- Git (optional)

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/django-blog-project.git
cd django-blog-project

# Create virtual environment
python -m venv env
source env/bin/activate  # on Windows use `env\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver
