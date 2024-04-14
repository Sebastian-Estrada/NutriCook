# NutriCook
A digital recipe cookbook focused on promoting healthy eating habits Users can search for recipes based on ingredients, meal types, and dietary restrictions. It will take ingredients as input and output recipes based on the input ingredients.

# Clone Repository:
- git clone <repository_url>

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
