import time
from tkinter import *
from PIL import Image, ImageTk
from plyer import notification
import threading
from tkinter import messagebox

t = Tk()
t.title('Notifier')
t.geometry("500x350")  # Increased window height

dpi = 300

img = Image.open("notify-label.png")
tkimage = ImageTk.PhotoImage(img)

# Function to show the notification
def show_notification():
    get_title = title.get()
    get_msg = msg.get()
    get_time = time_entry.get()
    time_unit = time_unit_var.get()  # Get the selected time unit

    if get_title == "" or get_msg == "" or get_time == "":
        messagebox.showerror("Alert", "All fields are required!")
    else:
        int_time = int(float(get_time))
        if time_unit == "Seconds":
            delay_seconds = int_time
        else:
            delay_seconds = int_time * 60

        messagebox.showinfo("Notifier set", "Notification set!")
        t.destroy()

        def notify():
            time.sleep(delay_seconds)
            notification.notify(
                title=get_title,
                message=get_msg,
                app_name="Notifier",
                app_icon="ico.ico",
                toast=True,
                timeout=10
            )

        # Create a separate thread for notification
        notification_thread = threading.Thread(target=notify)
        notification_thread.start()

img_label = Label(t, image=tkimage)
img_label.place(x=0, y=0, relwidth=1, relheight=1)

# Label - Title
t_label = Label(t, text="Title to Notify", font=("poppins", 10))
t_label.place(x=12, y=70)

# ENTRY - Title
title = Entry(t, width="25", font=("poppins", 13))
title.place(x=123, y=70)

# Label - Message
m_label = Label(t, text="Display Message", font=("poppins", 10))
m_label.place(x=12, y=120)

# ENTRY - Message
msg = Entry(t, width="40", font=("poppins", 13))
msg.place(x=123, height=30, y=120)

# Label - Time
time_label = Label(t, text="Set Time", font=("poppins", 10))
time_label.place(x=12, y=175)

# ENTRY - Time
time_entry = Entry(t, width="5", font=("poppins", 13))
time_entry.place(x=123, y=175)

# Dropdown for time unit (Seconds or Minutes)
time_units = ["Seconds", "Minutes"]
time_unit_var = StringVar(value="Minutes")
time_unit_menu = OptionMenu(t, time_unit_var, *time_units)
time_unit_menu.place(x=180, y=170)

# Button
but = Button(t, text="SET NOTIFICATION", font=("poppins", 10, "bold"), fg="#ffffff", bg="#528DFF", width=20,
             relief="raised", command=show_notification)
but.place(x=170, y=230)

t.resizable(0, 0)
t.mainloop()
