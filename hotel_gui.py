import tkinter as tk
from tkinter import messagebox
from hotel_db import init_db, add_guest, add_reservation, update_reservation_status, generate_invoice

# Initialize database   
init_db()

def add_guest_gui():
    def save_guest():
        name = entry_name.get()
        phone = entry_phone.get()
        email = entry_email.get()
        guest_id = add_guest(name, phone, email)
        messagebox.showinfo("Success", f"Guest added with ID {guest_id}")
        add_guest_window.destroy()

    add_guest_window = tk.Toplevel()
    add_guest_window.title("Add Guest")
    
    tk.Label(add_guest_window, text="Name:").grid(row=0, column=0)
    entry_name = tk.Entry(add_guest_window)
    entry_name.grid(row=0, column=1)
    
    tk.Label(add_guest_window, text="Phone:").grid(row=1, column=0)
    entry_phone = tk.Entry(add_guest_window)
    entry_phone.grid(row=1, column=1)
    
    tk.Label(add_guest_window, text="Email:").grid(row=2, column=0)
    entry_email = tk.Entry(add_guest_window)
    entry_email.grid(row=2, column=1)
    
    tk.Button(add_guest_window, text="Save", command=save_guest).grid(row=3, column=0, columnspan=2)

def add_reservation_gui():
    def save_reservation():
        guest_id = int(entry_guest_id.get())
        room_type = entry_room_type.get()
        check_in = entry_check_in.get()
        check_out = entry_check_out.get()
        reservation_id = add_reservation(guest_id, room_type, check_in, check_out)
        messagebox.showinfo("Success", f"Reservation added with ID {reservation_id}")
        add_reservation_window.destroy()

    add_reservation_window = tk.Toplevel()
    add_reservation_window.title("Add Reservation")
    
    tk.Label(add_reservation_window, text="Guest ID:").grid(row=0, column=0)
    entry_guest_id = tk.Entry(add_reservation_window)
    entry_guest_id.grid(row=0, column=1)
    
    tk.Label(add_reservation_window, text="Room Type:").grid(row=1, column=0)
    entry_room_type = tk.Entry(add_reservation_window)
    entry_room_type.grid(row=1, column=1)
    
    tk.Label(add_reservation_window, text="Check-in Date:").grid(row=2, column=0)
    entry_check_in = tk.Entry(add_reservation_window)
    entry_check_in.grid(row=2, column=1)
    
    tk.Label(add_reservation_window, text="Check-out Date:").grid(row=3, column=0)
    entry_check_out = tk.Entry(add_reservation_window)
    entry_check_out.grid(row=3, column=1)
    
    tk.Button(add_reservation_window, text="Save", command=save_reservation).grid(row=4, column=0, columnspan=2)

def update_reservation_status_gui():
    def update_status():
        reservation_id = int(entry_reservation_id.get())
        status = entry_status.get()
        update_reservation_status(reservation_id, status)
        messagebox.showinfo("Success", "Reservation status updated")
        update_status_window.destroy()

    update_status_window = tk.Toplevel()
    update_status_window.title("Update Reservation Status")
    
    tk.Label(update_status_window, text="Reservation ID:").grid(row=0, column=0)
    entry_reservation_id = tk.Entry(update_status_window)
    entry_reservation_id.grid(row=0, column=1)
    
    tk.Label(update_status_window, text="Status:").grid(row=1, column=0)
    entry_status = tk.Entry(update_status_window)
    entry_status.grid(row=1, column=1)
    
    tk.Button(update_status_window, text="Update", command=update_status).grid(row=2, column=0, columnspan=2)

def generate_invoice_gui():
    def create_invoice():
        reservation_id = int(entry_reservation_id.get())
        amount = float(entry_amount.get())
        invoice_id = generate_invoice(reservation_id, amount)
        messagebox.showinfo("Success", f"Invoice generated with ID {invoice_id}")
        generate_invoice_window.destroy()

    generate_invoice_window = tk.Toplevel()
    generate_invoice_window.title("Generate Invoice")
    
    tk.Label(generate_invoice_window, text="Reservation ID:").grid(row=0, column=0)
    entry_reservation_id = tk.Entry(generate_invoice_window)
    entry_reservation_id.grid(row=0, column=1)
    
    tk.Label(generate_invoice_window, text="Amount:").grid(row=1, column=0)
    entry_amount = tk.Entry(generate_invoice_window)
    entry_amount.grid(row=1, column=1)
    
    tk.Button(generate_invoice_window, text="Generate", command=create_invoice).grid(row=2, column=0, columnspan=2)

# Main window
root = tk.Tk()
root.title("Hotel Management System")

tk.Button(root, text="Add Guest", command=add_guest_gui).grid(row=0, column=0, padx=20, pady=20)
tk.Button(root, text="Add Reservation", command=add_reservation_gui).grid(row=0, column=1, padx=20, pady=20)
tk.Button(root, text="Update Reservation Status", command=update_reservation_status_gui).grid(row=1, column=0, padx=20, pady=20)
tk.Button(root, text="Generate Invoice", command=generate_invoice_gui).grid(row=1, column=1, padx=20, pady=20)

root.mainloop()
