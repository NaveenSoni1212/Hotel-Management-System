import sqlite3

def init_db():
    conn = sqlite3.connect('hotel.db')
    c = conn.cursor()
    
    # Create tables
    c.execute('''CREATE TABLE IF NOT EXISTS guests (
                    guest_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    phone TEXT,
                    email TEXT)''')

    c.execute('''CREATE TABLE IF NOT EXISTS reservations (
                    reservation_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    guest_id INTEGER,
                    room_type TEXT NOT NULL,
                    check_in_date TEXT NOT NULL,
                    check_out_date TEXT NOT NULL,
                    status TEXT NOT NULL,
                    FOREIGN KEY (guest_id) REFERENCES guests(guest_id))''')

    c.execute('''CREATE TABLE IF NOT EXISTS invoices (
                    invoice_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    reservation_id INTEGER,
                    amount REAL NOT NULL,
                    invoice_date TEXT NOT NULL,
                    FOREIGN KEY (reservation_id) REFERENCES reservations(reservation_id))''')
    
    conn.commit()
    conn.close()

def add_guest(name, phone, email):
    conn = sqlite3.connect('hotel.db')
    c = conn.cursor()
    c.execute('INSERT INTO guests (name, phone, email) VALUES (?, ?, ?)', (name, phone, email))
    conn.commit()
    guest_id = c.lastrowid
    conn.close()
    return guest_id

def add_reservation(guest_id, room_type, check_in, check_out, status="Booked"):
    conn = sqlite3.connect('hotel.db')
    c = conn.cursor()
    c.execute('''INSERT INTO reservations (guest_id, room_type, check_in_date, check_out_date, status)
                 VALUES (?, ?, ?, ?, ?)''', (guest_id, room_type, check_in, check_out, status))
    conn.commit()
    reservation_id = c.lastrowid
    conn.close()
    return reservation_id

def update_reservation_status(reservation_id, status):
    conn = sqlite3.connect('hotel.db')
    c = conn.cursor()
    c.execute('UPDATE reservations SET status = ? WHERE reservation_id = ?', (status, reservation_id))
    conn.commit()
    conn.close()

def generate_invoice(reservation_id, amount):
    conn = sqlite3.connect('hotel.db')
    c = conn.cursor()
    c.execute('''INSERT INTO invoices (reservation_id, amount, invoice_date)
                 VALUES (?, ?, DATE('now'))''', (reservation_id, amount))
    conn.commit()
    invoice_id = c.lastrowid
    conn.close()
    return invoice_id
