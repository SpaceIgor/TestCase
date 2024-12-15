# Expense Manager API

## Project Description
Expense Manager API is a RESTful API for managing user expenses. This project uses Django and Django REST Framework to implement CRUD operations and additional functionalities such as filtering expenses by date range and summarizing expenses by categories.

## Project Setup

### Requirements
- Python 3.8+
- Django 3.2+
- djangorestframework 3.12+

### Setup Instructions

1. **Clone the Repository**

    ```bash
    git clone <REPOSITORY_URL>
    cd expense_manager_project
    ```

2. **Create a Virtual Environment**

    ```bash
    python -m venv venv
    ```

3. **Activate the Virtual Environment**

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On Unix or MacOS:

        ```bash
        source venv/bin/activate
        ```

4. **Install Required Dependencies**

    ```bash
    pip install django djangorestframework  or pip install req.txt
    ```

5. **Apply Migrations to Set Up the Database**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Run the Development Server**

    ```bash
    python manage.py runserver
    ```

7. **Verify the API**
   
   Open your browser and navigate to [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/)

## API Endpoints

### User Endpoints
- **GET /api/users/**: List all users
- **POST /api/users/**: Create a new user

### Expense Endpoints
- **GET /api/expenses/**: List all expenses
- **POST /api/expenses/**: Create a new expense
- **GET /api/expenses/<id>/**: Retrieve a specific expense
- **PUT /api/expenses/<id>/**: Update a specific expense
- **DELETE /api/expenses/<id>/**: Delete a specific expense

### Expense by Date Range
- **GET /api/expenses/user/<user_id>/date_range/<start_date>/<end_date>/**: List all expenses for a user within a specific date range

### Category Summary
- **GET /api/expenses/user/<user_id>/summary/<year>/<month>/**: Get total expenses per category for a given month for a user

## Usage Examples

### Create a New User
```bash
curl -X POST http://127.0.0.1:8000/api/users/ -H "Content-Type: application/json" -d '{"username": "john", "email": "john@example.com"}'
