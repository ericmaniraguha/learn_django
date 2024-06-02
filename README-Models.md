## Data modeling Building an e commerce data model Organize models in apps

```mermaid
erDiagram

    USERS {
        int id PK
        string username
        string email
        string address
        string phone_number
    }

    ORDERS {
        int id PK
        datetime created_at
        datetime updated_at
        boolean is_paid
        boolean is_shipped
        int user_id FK
    }

    ORDER_ITEMS {
        int id PK
        int quantity
        int order_id FK
        int product_id FK
    }

    PRODUCTS {
        int id PK
        string name
        string description
        decimal price
        int stock
        int category_id FK
    }

    CATEGORIES {
        int id PK
        string name
        string description
    }

    REVIEWS {
        int id PK
        int rating
        string comment
        int product_id FK
        int user_id FK
    }

    PAYMENTS {
        int id PK
        decimal amount
        string payment_method
        datetime payment_date
        string status
        int order_id FK
    }

    SHIPPING_ADDRESS {
        int id PK
        string address_line_1
        string address_line_2
        string city
        string state
        string postal_code
        string country
        int order_id FK
    }

    SHIPPING_STATUS {
        int id PK
        string status
        datetime updated_at
        int order_id FK
    }

    USERS ||--o{ ORDERS: "places"
    ORDERS ||--o{ ORDER_ITEMS: "contains"
    PRODUCTS ||--o{ ORDER_ITEMS: "is part of"
    CATEGORIES ||--o{ PRODUCTS: "categorizes"
    USERS ||--o{ REVIEWS: "writes"
    PRODUCTS ||--o{ REVIEWS: "receives"
    ORDERS ||--|| PAYMENTS: "has"
    ORDERS ||--|| SHIPPING_ADDRESS: "ships to"
    ORDERS ||--|| SHIPPING_STATUS: "tracks"


```

## Create Django Apps

Navigate to your project directory in the terminal and run the following commands to create Django apps:

```python
python manage.py startapp users
python manage.py startapp products
python manage.py startapp orders
python manage.py startapp payments
python manage.py startapp shipping

```

## Register Apps

Add the newly created apps to your project's` INSTALLED_APPS` in `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'users',
    'products',
    'orders',
    'payments',
    'shipping',
]

```

## Run Migrations

Run migrations to create database tables for your models:

```python
python manage.py makemigrations
python manage.py migrate

```

`This will create the necessary tables in your database based on the models you've defined.`
