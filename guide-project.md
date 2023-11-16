
```bash
# Create virtual environment
python3 -m venv .MetaCapPvenv

# Activate virtual environment
source .MetaCapPvenv/bin/activate

# Install Django
pip install django

# Create Django project
django-admin startproject littlelemon  .

# Create Django app Restaurant
python manage.py startapp restaurant