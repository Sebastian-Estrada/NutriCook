# NutriCook
A digital recipe cookbook focused on promoting healthy eating habits Users can search for recipes based on ingredients, meal types. It will take ingredients as input and output recipes based on the input ingredients.

# Clone Repository:
- git clone (https://github.com/Sebastian-Estrada/NutriCook.git)

# Navigate to Project Directory:
- cd NutriCook

# Create and Activate Virtual Environment:
- python3 -m venv venv
- source venv/bin/activate (For Linux/Mac)
- venv\Scripts\activate (For Windows)

# Install Dependencies:
- pip install -r requirements.txt

# Install and Run Redis Server:
- Download and install Redis from https://redis.io/download
- Start the Redis server

# Configure Settings:
- Update DATABASES configuration in base.py with your database details
- Configure other settings as required

# Settings example and environment variables:
- SECRET_KEY="the_secret_key"
- DEBUG=True
- OWN_DOMAINS=localhost
- DATABASE_DEFAULT='{"ENGINE": "django.db.backends.postgresql", "NAME": "nutricook", "USER": "your_db_user", "PASSWORD": "password", "HOST": "localhost", "PORT": "5432", "ATOMIC_REQUESTS": true}'
- REDIS_HOST=localhost
- REDIS_PORT=6379
- REDIS_PASSWORD=
- INITIAL_USER=''

# Perform Database Migrations:
- python manage.py makemigrations
- python manage.py migrate

# Create Superuser (Optional):
- python manage.py createsuperuser

# Run Development Server:
- python manage.py runserver

# Access Application:
- Open your web browser and navigate to http://localhost:8000/

# Run Initial Script:
- This script will create multiple instances of your application.
- python manage.py shell.
- Paste the script into your CLI.
