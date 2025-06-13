Django REST API with JWT Authentication and PostgreSQL
This project implements a RESTful API using Django and Django REST Framework, featuring JWT (JSON Web Token) authentication and PostgreSQL as the database. It allows authenticated users to perform standard CRUD (Create, Read, Update, Delete) operations on a Customer entity.

Table of Contents
Features

Prerequisites

Setup Instructions

1. Clone the repository

2. Create a Python Virtual Environment

3. Install Dependencies

4. PostgreSQL Setup

5. Environment Variables Setup

6. Database Migrations

7. Create a Superuser

8. Run the Django Application

API Usage

Authentication Endpoints

Customer Endpoints

Postman Collection

Project Structure

Optional: Bonus Features

Troubleshooting

License

Features
Customer Entity: CRUD operations for a Customer with fields like id, name, email, mobile, address, created_at, updated_at.

JWT Authentication: Secure API access using djangorestframework-simplejwt.

User Registration (/api/register/)

Token Generation (/api/token/)

Token Refresh (/api/token/refresh/)

Protected Routes: All Customer API endpoints require a valid JWT.

Data Validation & Error Handling:

Unique email validation.

Basic mobile number format validation.

Appropriate HTTP status codes for responses.

PostgreSQL Integration: Robust database management.

Search: Filter customers by name or email using query parameters (e.g., /api/customers/?search=John or /api/customers/?search=john@example.com).

Pagination: Paginate customer listings.

Prerequisites
Before you begin, ensure you have the following installed:

Python 3.8+: Download Python

PostgreSQL: Download PostgreSQL or use Docker.

pip: Python package installer (usually comes with Python).

Git: Download Git

Setup Instructions
Follow these steps to get the project up and running on your local machine.

1. Clone the repository
git clone <your-github-repo-url>
cd <your-project-directory> # e.g., cd django_customer_api

2. Create a Python Virtual Environment
It's highly recommended to use a virtual environment to manage dependencies.

python -m venv venv

Activate the virtual environment:

On macOS/Linux:

source venv/bin/activate

On Windows:

venv\Scripts\activate

3. Install Dependencies
Once the virtual environment is activated, install the required Python packages:

pip install -r requirements.txt

4. PostgreSQL Setup
You need a PostgreSQL database running.

Option A: Using Docker (Recommended)
If you have Docker installed, you can quickly set up a PostgreSQL container:

docker run --name my_pg_db -e POSTGRES_DB=django_db -e POSTGRES_USER=django_user -e POSTGRES_PASSWORD=password -p 5432:5432 -d postgres:13

This command will:

Create a container named my_pg_db.

Set the database name to django_db.

Set the username to django_user.

Set the password to password.

Map port 5432 on your host to port 5432 in the container.

Run the container in detached mode (-d).

Option B: Local PostgreSQL Installation
If you have PostgreSQL installed locally, create a new database and a user for your project.

-- Connect to your PostgreSQL server (e.g., using psql or pgAdmin)
CREATE DATABASE django_db;
CREATE USER django_user WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE django_db TO django_user;

Important: Ensure the database name, user, and password match the values in your .env file (see next step).

5. Environment Variables Setup
Create a .env file in the root of your project directory based on the provided .env.example.

cp .env.example .env

Open the .env file and fill in your details:

# .env file
SECRET_KEY='your_very_secret_key_here' # Generate a strong Django secret key
DEBUG=True # Set to False in production
DB_NAME='django_db'
DB_USER='django_user'
DB_PASSWORD='password'
DB_HOST='localhost' # Or your PostgreSQL container IP if not using host.docker.internal or 127.0.0.1
DB_PORT='5432'

For SECRET_KEY, you can generate one using:

python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

6. Database Migrations
Apply the database migrations to create the necessary tables in your PostgreSQL database:

python manage.py makemigrations
python manage.py migrate

7. Create a Superuser (Optional, for Django Admin)
You can create a superuser to access the Django admin panel (useful for managing users and customers directly):

python manage.py createsuperuser

Follow the prompts to set up username, email, and password.

8. Run the Django Application
Start the Django development server:

python manage.py runserver

The API will be accessible at http://127.0.0.1:8000/.

API Usage
All API endpoints are prefixed with /api/.

Authentication Endpoints
These endpoints do not require authentication.

User Registration

Endpoint: POST /api/register/

Description: Creates a new user account.

Request Body (JSON):

{
    "username": "testuser",
    "email": "test@example.com",
    "password": "strongpassword123"
}

Response (JSON):

{
    "message": "User registered successfully",
    "user_id": 1,
    "username": "testuser",
    "email": "test@example.com"
}

Token Generation (Login)

Endpoint: POST /api/token/

Description: Obtains JWT access and refresh tokens.

Request Body (JSON):

{
    "username": "testuser",
    "password": "strongpassword123"
}

Response (JSON):

{
    "refresh": "eyJ...",
    "access": "eyJ..."
}

Note: Copy the access token. It will be used in the Authorization header for protected routes.

Token Refresh

Endpoint: POST /api/token/refresh/

Description: Refreshes the access token using a valid refresh token.

Request Body (JSON):

{
    "refresh": "eyJ..."
}

Response (JSON):

{
    "access": "eyJ..."
}

Customer Endpoints
All Customer endpoints require a valid JWT access token in the Authorization header.
Format: Authorization: Bearer <your_access_token>

Create Customer

Endpoint: POST /api/customers/

Description: Creates a new customer record.

Request Body (JSON):

{
    "name": "John Doe",
    "email": "john.doe@example.com",
    "mobile": "+1234567890",
    "address": "123 Main St, Anytown"
}

Response (JSON): Returns the created customer object with id, created_at, updated_at.

{
    "id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
    "name": "John Doe",
    "email": "john.doe@example.com",
    "mobile": "+1234567890",
    "address": "123 Main St, Anytown",
    "created_at": "2023-10-27T10:00:00Z",
    "updated_at": "2023-10-27T10:00:00Z"
}

Error Handling: If email is not unique or mobile format is invalid, appropriate 400 Bad Request error will be returned.

List All Customers

Endpoint: GET /api/customers/

Description: Retrieves a paginated list of all customer records.

Query Parameters (Optional):

page: Page number (e.g., /api/customers/?page=2)

page_size: Number of items per page (e.g., /api/customers/?page_size=10)

search: Search by name or email (e.g., /api/customers/?search=Jane or /api/customers/?search=jane@example.com)

Response (JSON):

{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": "...",
            "name": "John Doe",
            "email": "john.doe@example.com",
            "mobile": "+1234567890",
            "address": "123 Main St, Anytown",
            "created_at": "...",
            "updated_at": "..."
        },
        {
            "id": "...",
            "name": "Jane Smith",
            "email": "jane.smith@example.com",
            "mobile": "+9876543210",
            "address": "456 Oak Ave, Othertown",
            "created_at": "...",
            "updated_at": "..."
        }
    ]
}

Get Specific Customer

Endpoint: GET /api/customers/<uuid:id>/

Description: Retrieves a single customer record by its UUID.

Example: GET /api/customers/a1b2c3d4-e5f6-7890-1234-567890abcdef/

Response (JSON): Returns the customer object or 404 Not Found if not found.

Update Customer Info

Endpoint: PUT /api/customers/<uuid:id>/

Description: Updates an existing customer record by its UUID.

Request Body (JSON): (Partial updates are also allowed with PATCH)

{
    "name": "Johnny Doe",
    "mobile": "+1122334455"
}

Response (JSON): Returns the updated customer object.

Example: PUT /api/customers/a1b2c3d4-e5f6-7890-1234-567890abcdef/

Delete Customer

Endpoint: DELETE /api/customers/<uuid:id>/

Description: Deletes a customer record by its UUID.

Response: 204 No Content on successful deletion.

Example: DELETE /api/customers/a1b2c3d4-e5f6-7890-1234-567890abcdef/

Postman Collection
Due to the nature of this platform, a Postman collection JSON file cannot be directly provided. However, you can easily create one by importing the following requests:

Register User (POST): http://127.0.0.1:8000/api/register/

Headers: Content-Type: application/json

Body (raw JSON): {"username": "yourusername", "email": "your@email.com", "password": "yourpassword"}

Get Token (POST): http://127.0.0.1:8000/api/token/

Headers: Content-Type: application/json

Body (raw JSON): {"username": "yourusername", "password": "yourpassword"}

Save the access token from the response for subsequent requests.

Refresh Token (POST): http://127.0.0.1:8000/api/token/refresh/

Headers: Content-Type: application/json

Body (raw JSON): {"refresh": "your_refresh_token_from_login"}

Create Customer (POST): http://127.0.0.1:8000/api/customers/

Headers: Content-Type: application/json, Authorization: Bearer <your_access_token>

Body (raw JSON): {"name": "...", "email": "...", "mobile": "...", "address": "..."}

List Customers (GET): http://127.0.0.1:8000/api/customers/

Headers: Authorization: Bearer <your_access_token>

Try with query parameters: ?search=John, ?page=1&page_size=5

Get Customer by ID (GET): http://127.0.0.1:8000/api/customers/{{customer_id}}/

Headers: Authorization: Bearer <your_access_token>

Replace {{customer_id}} with an actual customer UUID.

Update Customer (PUT): http://127.0.0.1:8000/api/customers/{{customer_id}}/

Headers: Content-Type: application/json, Authorization: Bearer <your_access_token>

Body (raw JSON): { "name": "New Name" } (or full update)

Delete Customer (DELETE): http://127.0.0.1:8000/api/customers/{{customer_id}}/

Headers: Authorization: Bearer <your_access_token>

Project Structure
project/
│
├── customers/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── users/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py      # Optional: Custom User Model (not implemented in this example)
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── django_customer_api/  # Main project directory
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── .env                 # Environment variables (gitignore)
├── .env.example         # Example environment variables
├── manage.py            # Django management script
└── requirements.txt     # Python dependencies

Optional: Bonus Features
Search: Implemented. Use GET /api/customers/?search=<query>

Pagination: Implemented. Uses PageNumberPagination. Defaults to 10 items per page. Customize in settings.py or with page_size query parameter.

Troubleshooting
Database Connection Issues:

Ensure PostgreSQL is running and accessible.

Verify your .env database credentials (DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT).

If using Docker, ensure the port mapping is correct (-p 5432:5432).

ModuleNotFoundError:

Ensure your virtual environment is activated (source venv/bin/activate).

Make sure all dependencies are installed (pip install -r requirements.txt).

JWT Errors (401 Unauthorized):

Ensure you are sending the Authorization: Bearer <token> header with a valid and unexpired access token.

Double-check the SECRET_KEY in your .env matches the one used by Django.

Unique Constraint Failed:

If you try to create a customer with an email that already exists, you will get a 400 Bad Request error indicating a unique constraint violation.

License
This project is open-source and available under the MIT License.