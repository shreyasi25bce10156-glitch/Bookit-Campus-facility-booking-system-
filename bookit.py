import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

UNIVERSITY_NAME = "Vellore Institute of Technology"
APP_VERSION = "MVP 1.2"

COLOR_PRIMARY = "#2c3e50"
COLOR_SECONDARY = "#3498db"
COLOR_SUCCESS = "#27ae60"
COLOR_WARNING = "#f39c12"
COLOR_DANGER = "#e74c3c"
COLOR_LIGHT = "#ecf0f1"
COLOR_WHITE = "#ffffff"

USERS = [
    {"id": 1, "username": "priya.sharma", "password": "password", "role": "student"},
    {"id": 2, "username": "rohan.verma", "password": "password", "role": "student"},
    {"id": 3, "username": "ananya.iyer", "password": "password", "role": "student"},
    {"id": 4, "username": "vikram.patel", "password": "password", "role": "student"},
    {"id": 5, "username": "kavita.reddy", "password": "password", "role": "student"},
    {"id": 6, "username": "admin1", "password": "adminpass", "role": "admin"}
]

RESOURCES = [
    {"id": 1, "name": "Library Cubicle A-01", "type": "Cubicle", "location": "Main Library, 1st Floor", "assistant": "N/A"},
    {"id": 2, "name": "Study Room 201", "type": "Meeting Room", "location": "Academic Block, Room 201", "assistant": "Dr. Sharma"},
    {"id": 3, "name": "Computer Lab 101", "type": "PC Lab", "location": "Science Block, Room 101", "assistant": "Mr. Kumar"},
    {"id": 4, "name": "Music Practice Room 1", "type": "Practice Room", "location": "Arts Block, Basement", "assistant": "Ms. Iyer"},
    {"id": 5, "name": "Physics Lab", "type": "Science Lab", "location": "Newton Hall, Room 305", "assistant": "Prof. Nair"},
    {"id": 6, "name": "3D Printing Studio", "type": "Makerspace", "location": "Engineering Hub, 2nd Floor", "assistant": "Mr. Joshi"},
    {"id": 7, "name": "Group Study Pod B", "type": "Study Pod", "location": "Main Library, 3rd Floor", "assistant": "N/A"},
    {"id": 8, "name": "Quiet Study Zone Q1", "type": "Quiet Zone", "location": "Main Library, 4th Floor", "assistant": "N/A"},
    {"id": 9, "name": "VR Headset Station", "type": "Equipment", "location": "Media Center, Room 102", "assistant": "Ms. Rao"},
    {"id": 10, "name": "Presentation Room 5", "type": "Presentation Room", "location": "Management School, Wing B", "assistant": "Dr. Menon"},
]

PRE_POPULATED_BOOKINGS = [
    {"id": 1, "user_id": 1, "resource_id": 2, "date": "2024-05-21", "start_time": "10:00", "end_time": "11:00"},
    {"id": 2, "user_id": 2, "resource_id": 3, "date": "2024-05-21", "start_time": "14:00", "end_time": "16:00"},
    {"id": 3, "user_id": 1, "resource_id": 6, "date": "2024-05-22", "start_time": "13:00", "end_time": "14:30"},
    {"id": 4, "user_id": 3, "resource_id": 5, "date": "2024-05-23", "start_time": "09:00", "end_time": "12:00"},
    {"id": 5, "user_id": 4, "resource_id": 10, "date": "2024-05-24", "start_time": "15:00", "end_time": "17:00"},
]

BOOKINGS = PRE_POPULATED_BOOKINGS[:]

main_window = None
current_user = None

def find_user_by_username(username):
    return next((user for user in USERS if user["username"] == username), None)

def find_resource_by_id(resource_id):
    return next((res for res in RESOURCES if res["id"] == resource_id), None)

def find_user_by_id(user_id):
    return next((user for user in USERS if user["id"] == user_id), None)

def login():
    global current_user

    username = username_entry.get()
    password = password_entry.get()

    user = find_user_by_username(username)

    if user and user["password"] == password:
        current_user = user
        clear_window()
        if user["role"] == "student":
            show_student_dashboard()
        else:
            show_admin_dashboard()
    else:
        messagebox.showerror("Login Failed", "Oops! That username or password isn't right. Try again.")

def logout():
    global current_user
    current_user = None
    clear_window()
    show_login_screen()

def clear_window():
    for widget in main_window.winfo_children():
        widget.destroy()

def show_login_screen():
    global username_entry, password_entry

    main_window.title(f"BookIt - {UNIVERSITY_NAME}")
    main_window.configure(bg=COLOR_PRIMARY)

    title_frame = tk.Frame(main_window, bg=COLOR_PRIMARY)
    title_frame.pack(fill=tk.BOTH, expand=True)

    logo_label = tk.Label(title_frame, text="📚", font=("Arial", 72), bg=COLOR_PRIMARY, fg=COLOR_WHITE)
    logo_label.pack(pady=(40, 0))

    tk.Label(title_frame, text="BookIt", font=("Arial", 36, "bold"), fg=COLOR_WHITE, bg=COLOR_PRIMARY).pack()
    tk.Label(title_frame, text=f"{UNIVERSITY_NAME} Resource Booking", font=("Arial", 14), fg=COLOR_LIGHT, bg=COLOR_PRIMARY).pack(pady=(0, 20))

    login_frame = tk.Frame(title_frame, bg=COLOR_WHITE, relief=tk.RAISED, borderwidth=2)
    login_frame.pack(pady=20, padx=40)

    tk.Label(login_frame, text="Username:", font=("Arial", 12), bg=COLOR_WHITE).grid(row=0, column=0, sticky="w", padx=20, pady=(20, 5))
    username_entry = tk.Entry(login_frame, font=("Arial", 12), width=30)
    username_entry.grid(row=0, column=1, padx=20, pady=(20, 5))
    username_entry.focus_set()

    tk.Label(login_frame, text="Password:", font=("Arial", 12), bg=COLOR_WHITE).grid(row=1, column=0, sticky="w", padx=20, pady=5)
    password_entry = tk.Entry(login_frame, show="*", font=("Arial", 12), width=30)
    password_entry.grid(row=1, column=1, padx=20, pady=5)

    main_window.bind('<Return>', lambda event: login())

    login_button = tk.Button(login_frame, text="Login", command=login, font=("Arial", 12, "bold"), bg=COLOR_SECONDARY, fg=COLOR_WHITE, width=20, relief=tk.FLAT)
    login_button.grid(row=2, column=0, columnspan=2, pady=(20, 20))

    tk.Label(title_frame, text=f"v{APP_VERSION}", font=("Arial", 8), fg=COLOR_LIGHT, bg=COLOR_PRIMARY).pack(side=tk.BOTTOM, pady=10)

def show_student_dashboard():
    main_window.title(f"BookIt - Student Dashboard ({current_user['username']})")
    main_window.configure(bg=COLOR_LIGHT)

    header_frame = tk.Frame(main_window, bg=COLOR_PRIMARY, relief=tk.RAISED, borderwidth=1)
    header_frame.pack(fill=tk.X)
    tk.Label(header_frame, text=f"Welcome, {current_user['username']}!", font=("Arial", 18, "bold"), fg=COLOR_WHITE, bg=COLOR_PRIMARY).pack(pady=10)
    tk.Label(header_frame, text=UNIVERSITY_NAME, font=("Arial", 10), fg=COLOR_LIGHT, bg=COLOR_PRIMARY).pack(pady=(0, 10))

    notebook = ttk.Notebook(main_window)
    notebook.pack(fill="both", expand=True, padx=10, pady=10)

    resources_tab = ttk.Frame(notebook)
    notebook.add(resources_tab, text="Browse Resources")
    create_resources_view(resources_tab)

    booking_tab = ttk.Frame(notebook)
    notebook.add(booking_tab, text="Make a Booking")
    create_booking_form(booking_tab)

    my_bookings_tab = ttk.Frame(notebook)
    notebook.add(my_bookings_tab, text="My Bookings")
    my_bookings_tree = create_my_bookings_view(my_bookings_tab)

    logout_btn = tk.Button(main_window, text="Logout", command=logout, font=("Arial", 10), bg=COLOR_DANGER, fg=COLOR_WHITE, relief=tk.FLAT)
    logout_btn.pack(pady=10, side=tk.BOTTOM, anchor=tk.SE, padx=10)

def create_resources_view(parent_frame):
    tree = ttk.Treeview(parent_frame, columns=("name", "type", "location", "assistant"), show="headings")
    tree.heading("name", text="Resource Name")
    tree.heading("type", text="Type")
    tree.heading("location", text="Location")
    tree.heading("assistant", text="Assistant")
    tree.column("name", width=250)
    tree.column("type", width=120)
    tree.column("location", width=250)
    tree.column("assistant", width=150)
    tree.pack(fill="both", expand=True, padx=10, pady=10)

    tree.tag_configure('oddrow', background=COLOR_WHITE)
    tree.tag_configure('evenrow', background=COLOR_LIGHT)

    for i, res in enumerate(RESOURCES):
        tag = 'evenrow' if i % 2 == 0 else 'oddrow'
        tree.insert("", "end", values=(res["name"], res["type"], res["location"], res["assistant"]), tags=(tag,))

def create_booking_form(parent_frame):
    form_frame = ttk.Frame(parent_frame, padding="20")
    form_frame.pack(fill="both", expand=True)

    ttk.Label(form_frame, text="Select a Resource:", font=("Arial", 11)).grid(row=0, column=0, sticky="w", pady=5)
    resource_var = tk.StringVar()
    resource_dropdown = ttk.Combobox(form_frame, textvariable=resource_var, state="readonly", width=60)
    resource_dropdown['values'] = [f"{res['id']}: {res['name']}" for res in RESOURCES]
    resource_dropdown.grid(row=0, column=1, sticky="ew", pady=5)

    ttk.Label(form_frame, text="Date (YYYY-MM-DD):", font=("Arial", 11)).grid(row=1, column=0, sticky="w", pady=5)
    date_entry = ttk.Entry(form_frame, width=62)
    date_entry.grid(row=1, column=1, sticky="ew", pady=5)

    time_frame = ttk.Frame(form_frame)
    time_frame.grid(row=2, column=0, columnspan=2, sticky="ew", pady=5)
    ttk.Label(time_frame, text="Start Time (HH:MM):", font=("Arial", 11)).pack(side=tk.LEFT, padx=(0, 10))
    start_time_entry = ttk.Entry(time_frame, width=20)
    start_time_entry.pack(side=tk.LEFT, padx=5)
    ttk.Label(time_frame, text="End Time (HH:MM):", font=("Arial", 11)).pack(side=tk.LEFT, padx=(20, 10))
    end_time_entry = ttk.Entry(time_frame, width=20)
    end_time_entry.pack(side=tk.LEFT, padx=5)

    confirm_btn = tk.Button(form_frame, text="Confirm Booking",
                             command=lambda: handle_booking_confirmation(resource_var, date_entry, start_time_entry, end_time_entry),
                             bg=COLOR_SUCCESS, fg=COLOR_WHITE, font=("Arial", 11, "bold"), relief=tk.FLAT)
    confirm_btn.grid(row=3, column=0, columnspan=2, pady=20)

    form_frame.columnconfigure(1, weight=1)

def create_my_bookings_view(parent_frame):
    tree = ttk.Treeview(parent_frame, columns=("resource", "date", "time", "assistant"), show="headings")
    tree.heading("resource", text="Resource")
    tree.heading("date", text="Date")
    tree.heading("time", text="Time Slot")
    tree.heading("assistant", text="Assistant")
    tree.pack(fill="both", expand=True, padx=10, pady=10)

    tree.tag_configure('oddrow', background=COLOR_WHITE)
    tree.tag_configure('evenrow', background=COLOR_LIGHT)

    cancel_btn = tk.Button(parent_frame, text="Cancel Selected Booking",
                            command=lambda: handle_booking_cancellation(tree),
                            bg=COLOR_WARNING, fg=COLOR_WHITE, font=("Arial", 10, "bold"), relief=tk.FLAT)
    cancel_btn.pack(pady=5)

    refresh_my_bookings(tree)
    return tree

def refresh_my_bookings(tree):
    for item in tree.get_children():
        tree.delete(item)
    for i, booking in enumerate(BOOKINGS):
        if booking["user_id"] == current_user["id"]:
            resource = find_resource_by_id(booking["resource_id"])
            if resource:
                time_slot = f"{booking['start_time']} - {booking['end_time']}"
                tag = 'evenrow' if i % 2 == 0 else 'oddrow'
                tree.insert("", "end", values=(resource["name"], booking["date"], time_slot, resource["assistant"]), tags=(booking["id"], tag))

def handle_booking_confirmation(resource_var, date_entry, start_time_entry, end_time_entry):
    try:
        resource_id = int(resource_var.get().split(":")[0])
        date = date_entry.get()
        start_time = start_time_entry.get()
        end_time = end_time_entry.get()

        if not all([date, start_time, end_time]):
            raise ValueError("All fields must be filled.")

        datetime.strptime(date, "%Y-%m-%d")
        datetime.strptime(start_time, "%H:%M")
        datetime.strptime(end_time, "%H:%M")

        if start_time >= end_time:
            raise ValueError("End time must be after start time.")

    except (ValueError, IndexError) as e:
        messagebox.showerror("Invalid Input", f"Please check your input. {e}")
        return

    for booking in BOOKINGS:
        if booking["resource_id"] == resource_id and booking["date"] == date:
            if not (end_time <= booking["start_time"] or start_time >= booking["end_time"]):
                messagebox.showerror("Booking Conflict", "Sorry, this resource is already booked for that time.")
                return

    new_booking = {
        "id": len(BOOKINGS) + 1,
        "user_id": current_user["id"],
        "resource_id": resource_id,
        "date": date,
        "start_time": start_time,
        "end_time": end_time
    }
    BOOKINGS.append(new_booking)
    messagebox.showinfo("Success", "Your booking has been confirmed!")

    date_entry.delete(0, tk.END)
    start_time_entry.delete(0, tk.END)
    end_time_entry.delete(0, tk.END)
    resource_var.set('')

    for widget in main_window.winfo_children():
        if isinstance(widget, ttk.Notebook):
            for tab_id in widget.tabs():
                tab = widget.nametowidget(tab_id)
                for child in tab.winfo_children():
                    if isinstance(child, ttk.Treeview) and "Time Slot" in child.heading("time")["text"]:
                        refresh_my_bookings(child)
                        break

def handle_booking_cancellation(tree):
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("No Selection", "Please select a booking to cancel.")
        return

    booking_id_str = tree.item(selected_item, "tags")[0]
    booking_id = int(booking_id_str)

    for i, booking in enumerate(BOOKINGS):
        if booking["id"] == booking_id:
            BOOKINGS.pop(i)
            messagebox.showinfo("Cancelled", "Your booking has been cancelled.")
            refresh_my_bookings(tree)
            return

def show_admin_dashboard():
    main_window.title(f"BookIt - Admin Dashboard ({current_user['username']})")
    main_window.configure(bg=COLOR_LIGHT)

    header_frame = tk.Frame(main_window, bg=COLOR_PRIMARY, relief=tk.RAISED, borderwidth=1)
    header_frame.pack(fill=tk.X)
    tk.Label(header_frame, text="Welcome, Admin!", font=("Arial", 18, "bold"), fg=COLOR_WHITE, bg=COLOR_PRIMARY).pack(pady=10)
    tk.Label(header_frame, text=UNIVERSITY_NAME, font=("Arial", 10), fg=COLOR_LIGHT, bg=COLOR_PRIMARY).pack(pady=(0, 10))

    notebook = ttk.Notebook(main_window)
    notebook.pack(fill="both", expand=True, padx=10, pady=10)

    add_resource_tab = ttk.Frame(notebook)
    notebook.add(add_resource_tab, text="Add New Resource")
    create_add_resource_form(add_resource_tab)

    all_bookings_tab = ttk.Frame(notebook)
    notebook.add(all_bookings_tab, text="All Bookings")
    all_bookings_tree = create_all_bookings_view(all_bookings_tab)

    stats_tab = ttk.Frame(notebook)
    notebook.add(stats_tab, text="System Statistics")
    create_stats_view(stats_tab)

    logout_btn = tk.Button(main_window, text="Logout", command=logout, font=("Arial", 10), bg=COLOR_DANGER, fg=COLOR_WHITE, relief=tk.FLAT)
    logout_btn.pack(pady=10, side=tk.BOTTOM, anchor=tk.SE, padx=10)

def create_add_resource_form(parent_frame):
    form_frame = ttk.Frame(parent_frame, padding="20")
    form_frame.pack(fill="both", expand=True)

    ttk.Label(form_frame, text="Name:", font=("Arial", 11)).grid(row=0, column=0, sticky="w", pady=5)
    name_entry = ttk.Entry(form_frame, width=60)
    name_entry.grid(row=0, column=1, sticky="ew", pady=5)

    ttk.Label(form_frame, text="Type:", font=("Arial", 11)).grid(row=1, column=0, sticky="w", pady=5)
    type_entry = ttk.Entry(form_frame, width=60)
    type_entry.grid(row=1, column=1, sticky="ew", pady=5)

    ttk.Label(form_frame, text="Location:", font=("Arial", 11)).grid(row=2, column=0, sticky="w", pady=5)
    location_entry = ttk.Entry(form_frame, width=60)
    location_entry.grid(row=2, column=1, sticky="ew", pady=5)

    ttk.Label(form_frame, text="Assistant:", font=("Arial", 11)).grid(row=3, column=0, sticky="w", pady=5)
    assistant_entry = ttk.Entry(form_frame, width=60)
    assistant_entry.grid(row=3, column=1, sticky="ew", pady=5)

    add_btn = tk.Button(form_frame, text="Add Resource",
                         command=lambda: handle_add_resource(name_entry, type_entry, location_entry, assistant_entry),
                         bg=COLOR_SUCCESS, fg=COLOR_WHITE, font=("Arial", 11, "bold"), relief=tk.FLAT)
    add_btn.grid(row=4, column=0, columnspan=2, pady=20)

    form_frame.columnconfigure(1, weight=1)

def handle_add_resource(name_entry, type_entry, location_entry, assistant_entry):
    name = name_entry.get()
    type_ = type_entry.get()
    location = location_entry.get()
    assistant = assistant_entry.get() or "N/A"

    if not all([name, type_, location]):
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    new_resource = {
        "id": len(RESOURCES) + 1,
        "name": name,
        "type": type_,
        "location": location,
        "assistant": assistant
    }
    RESOURCES.append(new_resource)
    messagebox.showinfo("Success", f"'{name}' has been added to the resources!")

    name_entry.delete(0, tk.END)
    type_entry.delete(0, tk.END)
    location_entry.delete(0, tk.END)
    assistant_entry.delete(0, tk.END)

def create_all_bookings_view(parent_frame):
    tree = ttk.Treeview(parent_frame, columns=("user", "resource", "date", "time", "assistant"), show="headings")
    tree.heading("user", text="Student")
    tree.heading("resource", text="Resource")
    tree.heading("date", text="Date")
    tree.heading("time", text="Time Slot")
    tree.heading("assistant", text="Assistant")
    tree.pack(fill="both", expand=True, padx=10, pady=10)

    tree.tag_configure('oddrow', background=COLOR_WHITE)
    tree.tag_configure('evenrow', background=COLOR_LIGHT)

    refresh_all_bookings(tree)
    return tree

def refresh_all_bookings(tree):
    for item in tree.get_children():
        tree.delete(item)
    for i, booking in enumerate(BOOKINGS):
        user = find_user_by_id(booking["user_id"])
        resource = find_resource_by_id(booking["resource_id"])
        if user and resource:
            time_slot = f"{booking['start_time']} - {booking['end_time']}"
            tag = 'evenrow' if i % 2 == 0 else 'oddrow'
            tree.insert("", "end", values=(user["username"], resource["name"], booking["date"], time_slot, resource["assistant"]), tags=(tag,))

def create_stats_view(parent_frame):
    stats_frame = ttk.LabelFrame(parent_frame, text="Current System Overview", padding="20")
    stats_frame.pack(fill="both", expand=True, padx=20, pady=20)

    stats_data = {
        "Total Users:": len(USERS),
        "Total Resources:": len(RESOURCES),
        "Total Bookings:": len(BOOKINGS)
    }

    row = 0
    for label, value in stats_data.items():
        ttk.Label(stats_frame, text=label, font=("Arial", 14, "bold")).grid(row=row, column=0, sticky="w", padx=10, pady=10)
        ttk.Label(stats_frame, text=str(value), font=("Arial", 14)).grid(row=row, column=1, sticky="w", padx=10, pady=10)
        row += 1

def main():
    global main_window
    main_window = tk.Tk()
    main_window.geometry("1000x750")
    main_window.minsize(800, 600)
    show_login_screen()
    main_window.mainloop()

if __name__ == "__main__":
    main()