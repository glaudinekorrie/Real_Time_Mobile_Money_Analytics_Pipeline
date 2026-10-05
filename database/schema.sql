CREATE TABLE Customers (
    customer_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    customer_name VARCHAR,
    phone_no VARCHAR UNIQUE,
    customer_segment VARCHAR,
    registration_date TIMESTAMP
);

CREATE TABLE Merchants (
    merchant_id VARCHAR PRIMARY KEY,
    merchant_name VARCHAR,
    merchant_type VARCHAR,
    location VARCHAR
);

CREATE TABLE Transactions (
    transaction_id VARCHAR PRIMARY KEY,
    sender_id VARCHAR,
    sender_type VARCHAR,
    receiver_id VARCHAR,
    receiver_type VARCHAR,
    amount DECIMAL(12,2),
    transaction_timestamp TIMESTAMP,
    transaction_type VARCHAR,
    status VARCHAR,
    channel VARCHAR
);