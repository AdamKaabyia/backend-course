import tkinter as tk
from tkinter import ttk

class TaskScheduler:
    def __init__(self):
        self.schedule = {day: [None for _ in range(8)] for day in range(1, 6)}

    def add_task(self, task_name, duration, day=None, start_hour=None):
        if day and start_hour:
            if self.is_time_slot_available(day, start_hour, duration):
                self.populate_time_slot(day, start_hour, duration, task_name)
                print(f"Task '{task_name}' has been scheduled.")
            else:
                print("Time slot is not available.")
        else:
            self.schedule_task_anytime(task_name, duration)

    def is_time_slot_available(self, day, start_hour, duration):
        # Check if the time slot is available
        for hour in range(start_hour, start_hour + duration):
            if hour >= 8 or self.schedule[day][hour] is not None:
                return False
        return True

    def populate_time_slot(self, day, start_hour, duration, task_name):
        for hour in range(start_hour, start_hour + duration):
            self.schedule[day][hour] = task_name

    def schedule_task_anytime(self, task_name, duration):
        for day, hours in self.schedule.items():
            for start_hour in range(8 - duration + 1):
                if self.is_time_slot_available(day, start_hour, duration):
                    self.populate_time_slot(day, start_hour, duration, task_name)
                    print(f"Task '{task_name}' has been scheduled on day {day}, starting at hour {start_hour}.")
                    return
        print("Failed to schedule task, not enough available time slots.")

    def print_schedule(self):
        for day, hours in self.schedule.items():
            print(f"Day {day}: {hours}")

class TaskSchedulerGUI:
    def __init__(self, master):
        self.scheduler = TaskScheduler()
        self.master = master
        self.master.title("Task Scheduler")

        # Frame for input fields
        self.frame = ttk.Frame(master)
        self.frame.grid(row=0, column=0, padx=10, pady=10)

        # Task name input
        self.task_name_label = ttk.Label(self.frame, text="Task Name:")
        self.task_name_label.grid(row=0, column=0, padx=5, pady=5)
        self.task_name_entry = ttk.Entry(self.frame)
        self.task_name_entry.grid(row=0, column=1, padx=5, pady=5)

        # Duration input
        self.duration_label = ttk.Label(self.frame, text="Duration (hours):")
        self.duration_label.grid(row=1, column=0, padx=5, pady=5)
        self.duration_entry = ttk.Entry(self.frame)
        self.duration_entry.grid(row=1, column=1, padx=5, pady=5)

        # Day input (optional)
        self.day_label = ttk.Label(self.frame, text="Day (optional):")
        self.day_label.grid(row=2, column=0, padx=5, pady=5)
        self.day_entry = ttk.Entry(self.frame)
        self.day_entry.grid(row=2, column=1, padx=5, pady=5)

        # Start hour input (optional)
        self.start_hour_label = ttk.Label(self.frame, text="Start Hour (optional):")
        self.start_hour_label.grid(row=3, column=0, padx=5, pady=5)
        self.start_hour_entry = ttk.Entry(self.frame)
        self.start_hour_entry.grid(row=3, column=1, padx=5, pady=5)

        # Add task button
        self.add_task_button = ttk.Button(self.frame, text="Add Task", command=self.add_task)
        self.add_task_button.grid(row=4, column=0, columnspan=2, pady=5)

        # Schedule display
        self.schedule_text = tk.Text(master, height=10, width=50)
        self.schedule_text.grid(row=1, column=0, padx=10, pady=10)

    def add_task(self):
        task_name = self.task_name_entry.get()
        try:
            duration = int(self.duration_entry.get())
            day = int(self.day_entry.get()) if self.day_entry.get() else None
            start_hour = int(self.start_hour_entry.get()) if self.start_hour_entry.get() else None
            self.scheduler.add_task(task_name, duration, day, start_hour)
        except ValueError:
            self.schedule_text.insert(tk.END, "Invalid input. Please enter valid numbers for duration, day, and start hour.\n")
        self.update_schedule_display()

    def update_schedule_display(self):
        self.schedule_text.delete(1.0, tk.END)
        for day, hours in self.scheduler.schedule.items():
            self.schedule_text.insert(tk.END, f"Day {day}: {hours}\n")


def main():
    root = tk.Tk()
    app = TaskSchedulerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
