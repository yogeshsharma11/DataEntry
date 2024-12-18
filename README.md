# Django Project

This is a Django project for managing and editing data.

## Features
- User authentication
- CRUD operations
- Data export to CSV

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yogeshsharma11/DataEntry
    ```
    
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. **Make Migrations**:
    Run the following command to create migration files:
    ```bash
    python manage.py makemigrations
    ```

4. **Apply Migrations**:
    Apply the migrations to update your database schema:
    ```bash
    python manage.py migrate
    ```

5. Run the development server:
    ```bash
    python manage.py runserver
    ```

    Your project will be accessible at `http://127.0.0.1:8000`.

