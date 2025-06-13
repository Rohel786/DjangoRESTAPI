# Django REST API with JWT Authentication and PostgreSQL

This project implements a RESTful API using Django and Django REST Framework, featuring JWT (JSON Web Token) authentication and PostgreSQL as the database. It allows authenticated users to perform standard CRUD (Create, Read, Update, Delete) operations on a Customer entity.

---

## Table of Contents

* [Features](#features)
* [Prerequisites](#prerequisites)
* [Setup Instructions](#setup-instructions)

  * [Clone the Repository](#clone-the-repository)
  * [Create a Python Virtual Environment](#create-a-python-virtual-environment)
  * [Install Dependencies](#install-dependencies)
  * [PostgreSQL Setup](#postgresql-setup)
  * [Environment Variables Setup](#environment-variables-setup)
  * [Database Migrations](#database-migrations)
  * [Create a Superuser](#create-a-superuser)
  * [Run the Django Application](#run-the-django-application)
* [API Usage](#api-usage)

  * [Authentication Endpoints](#authentication-endpoints)
  * [Customer Endpoints](#customer-endpoints)
* [Postman Collection](#postman-collection)
* [Project Structure](#project-structure)
* [Troubleshooting](#troubleshooting)
* [License](#license)

---

## Features

* **Customer Entity:** CRUD operations with fields like `id`, `name`, `email`, `mobile`, `address`, `created_at`, and `updated_at`.
* **JWT Authentication:** Secure API access using `djangorestframework-simplejwt`.
* **Endpoints:**

  * `/api/register/` - User registration
  * `/api/token/` - Obtain JWT token
  * `/api/token/refresh/` - Refresh token
* **Protected Routes:** All customer endpoints require a valid JWT.
* **Validation:** Unique email check and mobile format validation.
* **Search and Pagination:** Query customers by name/email and paginate results.
* **PostgreSQL Integration**

---

## Prerequisites

* Python 3.8+
* PostgreSQL
* pip
* Git

---

## Setup Instructions

### Clone the Repository

```bash
git clone <repo-url>
cd <project-directory>
```

### Create a Python Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

* macOS/Linux:

  ```bash
  source venv/bin/activate
  ```
* Windows:

  ```bash
  venv\Scripts\activate
  ```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### PostgreSQL Setup

Create a PostgreSQL database and user:

```sql
CREATE DATABASE django_db;
CREATE USER django_user WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE django_db TO django_user;
```

### Environment Variables Setup

Create a `.env` file:

```bash
cp .env.example .env
```

Fill in the details:

```
SECRET_KEY='your_secret_key'
DEBUG=True
DB_NAME='django_db'
DB_USER='django_user'
DB_PASSWORD='password'
DB_HOST='localhost'
DB_PORT='5432'
```

Generate a Django secret key:

```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

### Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Create a Superuser

```bash
python manage.py createsuperuser
```

### Run the Django Application

```bash
python manage.py runserver
```

---

## API Usage

All endpoints are prefixed with `/api/`.

### Authentication Endpoints

**Register User**

* `POST /api/register/`
* Body:

```json
{
  "username": "testuser",
  "email": "test@example.com",
  "password": "strongpassword123"
}
```

**Obtain Token**

* `POST /api/token/`
* Body:

```json
{
  "username": "testuser",
  "password": "strongpassword123"
}
```

**Refresh Token**

* `POST /api/token/refresh/`
* Body:

```json
{
  "refresh": "<refresh_token>"
}
```

### Customer Endpoints

**Headers Required:**

```
Authorization: Bearer <your_access_token>
```

**Create Customer** - `POST /api/customers/`

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "mobile": "+1234567890",
  "address": "123 Main St"
}
```

**List Customers** - `GET /api/customers/?search=John&page=1&page_size=10`

**Get Customer** - `GET /api/customers/<uuid:id>/`

**Update Customer** - `PUT /api/customers/<uuid:id>/`

```json
{
  "name": "Updated Name",
  "mobile": "+1111111111"
}
```

**Delete Customer** - `DELETE /api/customers/<uuid:id>/`


