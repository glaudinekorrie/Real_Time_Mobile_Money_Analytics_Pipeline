import psycopg
import random

from faker import Faker

fake = Faker("en_KE")

connection = psycopg.connect(
    host="localhost",
    port=5432,
    dbname="mobile_money",
    user="postgres",
    password="postgres"
)

cursor = connection.cursor()

cursor.execute("SELECT phone_no FROM customers;")
phone_numbers = {row[0] for row in cursor.fetchall()}

num_customers = 1000

for _ in range(num_customers):
    customer_name = fake.name()

    while True:
        phone_no = "077" + "".join(str(random.randint(0, 9)) for _ in range(8))

        if phone_no not in phone_numbers:
            phone_numbers.add(phone_no)
            break

    customer_segment = random.choice(["Regular", "Premium", "Business"])
    registration_date = fake.date_time_between(start_date="-3y",end_date="now")

    customer = {
        "customer_name": customer_name,
        "phone_no": phone_no,
        "customer_segment": customer_segment,
        "registration_date": registration_date

    }
    cursor.execute("""
    INSERT INTO customers (
        customer_name,
        phone_no,
        customer_segment,
        registration_date
    )
    VALUES (%s, %s, %s, %s);
""", (
    customer_name,
    phone_no,
    customer_segment,
    registration_date
))
connection.commit()
cursor.close()
connection.close()