import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta
import threading
import time

class ReminderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Reminder App")
        
        
        self.label = tk.Label(root, text="Enter your reminder:")
        self.label.pack(pady=10)
        
        
        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=10)
        
        
        self.time_label = tk.Label(root, text="Set time for reminder (HH:MM):")
        self.time_label.pack(pady=10)
        
        
        self.time_entry = tk.Entry(root, width=50)
        self.time_entry.pack(pady=10)
        
        
        self.set_button = tk.Button(root, text="Set Reminder", command=self.set_reminder)
        self.set_button.pack(pady=10)
        
        self.reminders = []
        
    def set_reminder(self):
        reminder_text = self.entry.get()
        reminder_time_str = self.time_entry.get()
        
        try:
            reminder_time = datetime.strptime(reminder_time_str, '%H:%M').time()
            now = datetime.now()
            reminder_datetime = datetime.combine(now.date(), reminder_time)
            if reminder_datetime < now:
                reminder_datetime += timedelta(days=1)
            
            self.reminders.append((reminder_datetime, reminder_text))
            messagebox.showinfo("Reminder Set", f"Reminder set for {reminder_time_str}: {reminder_text}")
            self.entry.delete(0, tk.END)
            self.time_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Invalid Time", "Please enter time in HH:MM format")
        
    def check_reminders(self):
        while True:
            now = datetime.now()
            for reminder in self.reminders:
                if now >= reminder[0]:
                    messagebox.showinfo("Reminder", reminder[1])
                    self.reminders.remove(reminder)
            time.sleep(30)


root = tk.Tk()
app = ReminderApp(root)


thread = threading.Thread(target=app.check_reminders, daemon=True)
thread.start()

root.mainloop()
