```sql
CREATE TABLE USERS (
    id INT PRIMARY KEY,
    username VARCHAR(255),
    email VARCHAR(255),
    address VARCHAR(255),
    phone_number VARCHAR(20)
);

CREATE TABLE ORDERS (
    id INT PRIMARY KEY,
    created_at DATETIME,
    updated_at DATETIME,
    is_paid BOOLEAN,
    is_shipped BOOLEAN,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES USERS(id)
);

CREATE TABLE ORDER_ITEMS (
    id INT PRIMARY KEY,
    quantity INT,
    order_id INT,
    product_id INT,
    FOREIGN KEY (order_id) REFERENCES ORDERS(id),
    FOREIGN KEY (product_id) REFERENCES PRODUCTS(id)
);

CREATE TABLE PRODUCTS (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    description TEXT,
    price DECIMAL(10, 2),
    stock INT,
    category_id INT,
    FOREIGN KEY (category_id) REFERENCES CATEGORIES(id)
);

CREATE TABLE CATEGORIES (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    description TEXT
);

CREATE TABLE REVIEWS (
    id INT PRIMARY KEY,
    rating INT,
    comment TEXT,
    product_id INT,
    user_id INT,
    FOREIGN KEY (product_id) REFERENCES PRODUCTS(id),
    FOREIGN KEY (user_id) REFERENCES USERS(id)
);

CREATE TABLE PAYMENTS (
    id INT PRIMARY KEY,
    amount DECIMAL(10, 2),
    payment_method VARCHAR(255),
    payment_date DATETIME,
    status VARCHAR(255),
    order_id INT,
    FOREIGN KEY (order_id) REFERENCES ORDERS(id)
);

CREATE TABLE SHIPPING_ADDRESS (
    id INT PRIMARY KEY,
    address_line_1 VARCHAR(255),
    address_line_2 VARCHAR(255),
    city VARCHAR(255),
    state VARCHAR(255),
    postal_code VARCHAR(20),
    country VARCHAR(255),
    order_id INT,
    FOREIGN KEY (order_id) REFERENCES ORDERS(id)
);

CREATE TABLE SHIPPING_STATUS (
    id INT PRIMARY KEY,
    status VARCHAR(255),
    updated_at DATETIME,
    order_id INT,
    FOREIGN KEY (order_id) REFERENCES ORDERS(id)
);
```
