import tkinter as tk
from tkinter import colorchooser
from datetime import datetime, timedelta
import math

class BearcatsClock:
    def __init__(self, master):
        self.master = master
        self.master.title("Python Clock")

        self.canvas_dim = 400
        self.clock_center = self.canvas_dim / 2
        self.radius = 150

        self.canvas = tk.Canvas(self.master, width=self.canvas_dim, height=self.canvas_dim, bg='black')
        self.canvas.pack(pady=20)

        self.canvas.create_text(self.clock_center, 15, text="Bearcats", font=('Arial', 20), fill='red')

        self.digital_time = tk.Label(self.master, font=('Arial', 20), bg='black', fg='red')
        self.digital_time.pack()

        self.color_var = tk.StringVar(value='red')
        self.format_var = tk.StringVar(value='%I:%M:%S %p')  # Default to 12-hour format

        self.color_button = tk.Button(self.master, text="Select Color", command=self.change_color)
        self.color_button.pack(pady=10)

        self.format_button = tk.Button(self.master, text="Toggle Format (12/24hr)", command=self.toggle_format)
        self.format_button.pack(pady=10)

        self.time_zone = tk.StringVar()
        self.time_zone.set("EST")  # Setting a default value
        self.zone_picker = tk.OptionMenu(self.master, self.time_zone, "UTC", *sorted(self.available_timezones()), command=self.update_display)
        self.zone_picker.pack(pady=10)

        self.update_display()

    def draw_ticks_and_numbers(self):
        for minute in range(60):
            angle = math.radians(minute * 6 - 90)
            if minute % 5 == 0:
                length = 15
                number_distance = self.radius - 30
                x = self.clock_center + number_distance * math.cos(angle)
                y = self.clock_center + number_distance * math.sin(angle)
                self.canvas.create_text(x, y, text=str(int(minute/5) if minute != 0 else 12), fill=self.color_var.get())
            else:
                length = 5

            start_x = self.clock_center + (self.radius - length) * math.cos(angle)
            start_y = self.clock_center + (self.radius - length) * math.sin(angle)
            end_x = self.clock_center + self.radius * math.cos(angle)
            end_y = self.clock_center + self.radius * math.sin(angle)

            self.canvas.create_line(start_x, start_y, end_x, end_y, fill=self.color_var.get())

    def update_display(self):
        self.canvas.delete("all")
        current_utc_time = datetime.utcnow()
        time_offset = timedelta(hours=self.get_time_zone_offset(self.time_zone.get()))
        current_time = current_utc_time + time_offset

        self.canvas.create_text(self.clock_center, 15, text="Bearcats", font=('Arial', 20), fill=self.color_var.get())
        self.digital_time.configure(text=current_time.strftime(self.format_var.get()), fg=self.color_var.get())
        self.color_button.configure(fg=self.color_var.get())
        self.format_button.configure(fg=self.color_var.get())
        self.zone_picker.configure(fg=self.color_var.get())

        self.draw_ticks_and_numbers()

        # Hour hand
        hour_angle = math.radians((current_time.hour % 12 * 30) - 90 + current_time.minute / 2)
        hour_x = self.clock_center + self.radius * 0.5 * math.cos(hour_angle)
        hour_y = self.clock_center + self.radius * 0.5 * math.sin(hour_angle)
        self.canvas.create_line(self.clock_center, self.clock_center, hour_x, hour_y, width=6, fill=self.color_var.get())

        # Minute hand
        minute_angle = math.radians(current_time.minute * 6 - 90)
        minute_x = self.clock_center + self.radius * 0.7 * math.cos(minute_angle)
        minute_y = self.clock_center + self.radius * 0.7 * math.sin(minute_angle)
        self.canvas.create_line(self.clock_center, self.clock_center, minute_x, minute_y, width=4, fill=self.color_var.get())

        # Second hand
        second_angle = math.radians(current_time.second * 6 - 90)
        second_x = self.clock_center + self.radius * 0.9 * math.cos(second_angle)
        second_y = self.clock_center + self.radius * 0.9 * math.sin(second_angle)
        self.canvas.create_line(self.clock_center, self.clock_center, second_x, second_y, fill=self.color_var.get())

        self.master.after(1000, self.update_display)

    def change_color(self):
        color_code = colorchooser.askcolor(title="Choose color")[1]
        if color_code:
            self.color_var.set(color_code)
            self.update_display()

    def toggle_format(self):
        current_format = self.format_var.get()
        if current_format == '%I:%M:%S %p':  # If current format is 12-hour, change to 24-hour
            new_format = '%H:%M:%S'
        else:  # If current format is 24-hour or anything else, change to 12-hour
            new_format = '%I:%M:%S %p'
        self.format_var.set(new_format)
        self.update_display()

    def available_timezones(self):
        # This is a simplified list of time zones
        return ["UTC", "EST", "CST", "MST", "PST", "GMT"]

    def get_time_zone_offset(self, time_zone):
        offsets = {
            "UTC": 0,
            "EST": -4,
            "CST": -6,
            "MST": -7,
            "PST": -8,
            "GMT": 0,
        }
        return offsets.get(time_zone, 0)

root = tk.Tk()
clock = BearcatsClock(root)
root.mainloop()
