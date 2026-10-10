import psycopg
import random

# from faker import Faker

# fake = Faker("en_KE")



merchant_names = {
    "Wholesale & Retail Groceries": [
        "Baraka General Store",
        "Tumaini Stores",
        "Mwangaza Grocers",
        "Jirani Grocers",
        "Pamoja General Store",
        "Upendo Traders",
        "Mavuno Grocery Store",
        "Imara General Dealers"
    ],

    "Agrochemicals & Farm Inputs (Agroveg)": [
        "Green Harvest Agrovet",
        "Farmers Choice Agrovet",
        "Baraka Agro Supplies",
        "Mavuno Agrovet",
        "Imara Farm Supplies",
        "Shamba Bora Agrovet",
        "Kilimo Plus Supplies",
        "Harvest Point Agrovet"
    ],

    "Hardware & Construction Materials": [
        "Imara Hardware",
        "Jenga Bora Hardware",
        "Mwangaza Building Supplies",
        "Baraka Hardware",
        "Pamoja Building Centre",
        "Msingi Construction Supplies",
        "Jitegemee Hardware",
        "Nguvu Building Materials"
    ],

    "Electronics & Mobile Accessories": [
        "SmartTech Accessories",
        "Mobile Hub Kenya",
        "Digital Point Electronics",
        "TechZone Accessories",
        "Gadget World Kenya",
        "Simu Centre",
        "ElectroLink Kenya",
        "NextGen Electronics"
    ],

    "Pharmacy & Chemist Services": [
        "Afya Plus Pharmacy",
        "Tumaini Chemist",
        "CarePoint Pharmacy",
        "MediCare Chemist",
        "Afya Bora Pharmacy",
        "Wellness Pharmacy",
        "Dawa Direct Chemist",
        "LifeCare Pharmacy"
    ],

    "Boutique & Apparels": [
        "Urban Style Boutique",
        "Classic Trends",
        "Mrembo Fashion",
        "Elegant Wear",
        "Fashion Point",
        "Malkia Styles",
        "Trendy Wear Kenya",
        "Chic Avenue Boutique"
    ],

    "Hotel, Restaurant & Cafeteria": [
        "Sunrise Restaurant",
        "Savanna Café",
        "Mama's Kitchen",
        "Jirani Restaurant",
        "Green Garden Café",
        "Taste of Home Restaurant",
        "Urban Bites Café",
        "Soko Fresh Kitchen"
    ],

    "Gas Cylinder & Energy Refills": [
        "Safi Gas Services",
        "Jua Energy Centre",
        "Mwangaza Gas",
        "Baraka Gas Centre",
        "Pamoja Energy Services",
        "Moto Safe Gas",
        "PowerPlus Refills",
        "Joto Gas Supplies"
    ],

    "Salon, Kinyozi & Beauty Spa": [
        "Elegant Touch Salon",
        "Top Cut Kinyozi",
        "Bella Beauty Spa",
        "Mrembo Salon",
        "Classic Cuts",
        "Glow Up Beauty Studio",
        "Fresh Look Kinyozi",
        "Royal Touch Spa"
    ],

    "Spares & Automotive Repairs": [
        "AutoCare Spares",
        "Jua Kali Auto Garage",
        "Reliable Motor Spares",
        "Mwangaza Auto Services",
        "Imara Motors Garage",
        "QuickFix Auto Centre",
        "Safari Motor Spares",
        "RoadReady Garage"
    ],

    "Supermarket & Mini-Mart": [
        "Mwangaza Supermarket",
        "Tumaini Mini-Mart",
        "GreenMart",
        "Baraka Supermarket",
        "Jirani Mini-Mart",
        "Daily Basket Supermarket",
        "SmartChoice Mini-Mart",
        "FreshWay Supermarket"
    ],

    "Cyber Café & Printing Services": [
        "Digital World Cyber",
        "PrintPoint Services",
        "SmartLink Cyber",
        "Jirani Cyber Café",
        "TechPrint Services",
        "CopyHub Kenya",
        "QuickPrint Centre",
        "Online Point Cyber"
    ],

    "M-Pesa & Financial Services Agent": [
        "Tumaini M-Pesa Agent",
        "Baraka Financial Services",
        "PesaPoint Agent",
        "Jirani M-Pesa Services",
        "Mwangaza Financial Services",
        "PesaLink Agency",
        "Haraka Money Services",
        "Salama Payments Centre"
    ]
}


connection = psycopg.connect(
    host="localhost",
    port=5432,
    dbname="mobile_money",
    user="postgres",
    password="postgres"
)


locations = {
    "Wholesale & Retail Groceries": [
        "Nakuru", "Kisumu", "Nairobi", "Eldoret", "Meru"
    ],
    "Agrochemicals & Farm Inputs (Agroveg)": [
        "Nakuru", "Eldoret", "Meru", "Kitale", "Nyeri"
    ],
    "Hardware & Construction Materials": [
        "Nairobi", "Thika", "Nakuru", "Eldoret", "Kisumu"
    ],
    "Electronics & Mobile Accessories": [
        "Nairobi", "Mombasa", "Kisumu", "Nakuru", "Eldoret"
    ],
    "Pharmacy & Chemist Services": [
        "Nairobi", "Mombasa", "Kisumu", "Meru", "Nakuru"
    ],
    "Boutique & Apparels": [
        "Nairobi", "Mombasa", "Kisumu", "Nakuru", "Thika"
    ],
    "Hotel, Restaurant & Cafeteria": [
        "Nairobi", "Mombasa", "Naivasha", "Nakuru", "Kisumu"
    ],
    "Gas Cylinder & Energy Refills": [
        "Nairobi", "Thika", "Nakuru", "Eldoret", "Meru"
    ],
    "Salon, Kinyozi & Beauty Spa": [
        "Nairobi", "Mombasa", "Kisumu", "Thika", "Nakuru"
    ],
    "Spares & Automotive Repairs": [
        "Nairobi", "Nakuru", "Eldoret", "Mombasa", "Thika"
    ],
    "Supermarket & Mini-Mart": [
        "Nairobi", "Kisumu", "Nakuru", "Eldoret", "Meru"
    ],
    "Cyber Café & Printing Services": [
        "Nairobi", "Thika", "Kisumu", "Nakuru", "Eldoret"
    ],
    "M-Pesa & Financial Services Agent": [
        "Nairobi", "Mombasa", "Kisumu", "Meru", "Kitale"
    ]
}

cursor = connection.cursor()


num_merchant = 10


target_merchant_count = 100

cursor.execute("SELECT COUNT(*) FROM merchants;")
current_count = cursor.fetchone()[0]

remaining = target_merchant_count - current_count

if remaining <= 0:
    print(f"Target already reached: {current_count} merchants.")
else:
    cursor.execute("SELECT merchant_name FROM merchants;")
    existing_names = {row[0] for row in cursor.fetchall()}

    available_merchants = [
        (merchant_type, merchant_name)
        for merchant_type, names in merchant_names.items()
        for merchant_name in names
        if merchant_name not in existing_names
    ]

    random.shuffle(available_merchants)
    merchants_to_create = available_merchants[:remaining]

    for merchant_type, merchant_name in merchants_to_create:
        location = random.choice(locations[merchant_type])

        cursor.execute("""
            INSERT INTO merchants (
                merchant_name,
                merchant_type,
                location
            )
            VALUES (%s, %s, %s);
        """, (
            merchant_name,
            merchant_type,
            location
        ))

    connection.commit()

    print(f"Merchants before generation: {current_count}")
    print(f"New merchants inserted: {len(merchants_to_create)}")
    print(f"Merchants after generation: {current_count + len(merchants_to_create)}")
    print(f"Still needed to reach target: {target_merchant_count - (current_count + len(merchants_to_create))}")

connection.commit()
cursor.close()
connection.close()
       