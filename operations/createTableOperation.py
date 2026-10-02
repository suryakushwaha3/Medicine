import sqlite3

#Auth aperation for the user in the medical shop


def createtable():

    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()


    cursor.execute('''

        CREATE TABLE IF NOT EXISTS Users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id VARCHAR(255),
            password VARCHAR(255),
            date_of_account_creation DATE,
            isApproved BOOLEAN,
            block BOOLEAN,
            name VARCHAR(255),
            address VARCHAR(255),
            email VARCHAR(255) UNIQUE,
            phone_number VARCHAR(255),
            pincode VARCHAR(255)
        )

    ''')


    # This table for storing the products in the medical shop
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id VARCHAR(255),
            product_name VARCHAR(255),
            category VARCHAR(255),
            stock INTEGER,
            product_image VARCHAR(500)
        )
    ''')


    # Order details table for storing the order details
    # of the products in the medical shop
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Orders_Details(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id VARCHAR(255),
            user_id VARCHAR(255),
            product_id VARCHAR(255),
            isApproved BOOLEAN,
            quantity INTEGER,
            date_of_order_creation DATE,
            price FLOAT,
            total_amount FLOAT,
            product_name VARCHAR(255),
            user_name VARCHAR(255),
            message VARCHAR(1000),
            category VARCHAR(255)
        )
    ''')

     # This table is for storing the sell history
     # of products in the medical shop

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Sell_History(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sell_id VARCHAR(255),
        product_id VARCHAR(255),
        quantity INTEGER,
        reamining_stock INTEGER,
        date_of_sell DATE,
        total_amount FLOAT,
        price FLOAT,
        product_name VARCHAR(255),
        user_name VARCHAR(255),
        user_id VARCHAR(255)
    )
''')

    # Available stock table for storing the available stock
    # of the products in the medical shop
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Available_Stock(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id VARCHAR(255),
            product_name VARCHAR(255),
            category VARCHAR(255),
            price FLOAT,
            stock INTEGER,
            user_id VARCHAR(255),
            user_name VARCHAR(255)
        )
    ''')

    #Notifications table for storing the notifications

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Notifications(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title VARCHAR(255) NOT NULL,
            message VARCHAR(1000) NOT NULL,
            type VARCHAR(100) NOT NULL,
            is_read BOOLEAN DEFAULT 0,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

 
  
    print("Notifications table created successfully.")


    # This table is for storing home screen posters
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Posters(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            poster_name VARCHAR(255),
            poster_image VARCHAR(500),
            is_active BOOLEAN DEFAULT 1,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')



    # This table is for storing medicine categories
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Categories(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category_name VARCHAR(255) UNIQUE,
            category_image VARCHAR(500),
            is_active BOOLEAN DEFAULT 1,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
 


    conn.commit()
    conn.close()