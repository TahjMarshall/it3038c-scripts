import tkinter as tk
from datetime import datetime
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

        self.update_display()

    def draw_ticks_and_numbers(self):
        for minute in range(60):
            angle = math.radians(minute * 6 + 90)
            if minute % 5 == 0:
                length = 15
                number_distance = self.radius - 30
                x = self.clock_center - number_distance * math.cos(angle)
                y = self.clock_center - number_distance * math.sin(angle)
                self.canvas.create_text(x, y, text=str(int(minute/5) if minute != 0 else 12), fill='red')
            else:
                length = 5

            start_x = self.clock_center - (self.radius - length) * math.cos(angle)
            start_y = self.clock_center - (self.radius - length) * math.sin(angle)
            end_x = self.clock_center - self.radius * math.cos(angle)
            end_y = self.clock_center - self.radius * math.sin(angle)

            self.canvas.create_line(start_x, start_y, end_x, end_y, fill='red')

    def update_display(self):
        self.canvas.delete("all")
        current_time = datetime.now()

        self.canvas.create_text(self.clock_center, 15, text="Bearcats", font=('Arial', 20), fill='red')
        self.digital_time.configure(text=current_time.strftime('%I:%M:%S %p'))

        self.draw_ticks_and_numbers()

        # Hour hand
        hour_angle = math.radians(90 + (current_time.hour % 12 * 30) + current_time.minute / 2)
        hour_x = self.clock_center - self.radius * 0.5 * math.cos(hour_angle)
        hour_y = self.clock_center - self.radius * 0.5 * math.sin(hour_angle)
        self.canvas.create_line(self.clock_center, self.clock_center, hour_x, hour_y, width=6, fill='red')

        # Minute hand
        minute_angle = math.radians(90 + current_time.minute * 6)
        minute_x = self.clock_center - self.radius * 0.7 * math.cos(minute_angle)
        minute_y = self.clock_center - self.radius * 0.7 * math.sin(minute_angle)
        self.canvas.create_line(self.clock_center, self.clock_center, minute_x, minute_y, width=4, fill='red')

        # Second hand
        second_angle = math.radians(90 + current_time.second * 6)
        second_x = self.clock_center - self.radius * 0.9 * math.cos(second_angle)
        second_y = self.clock_center - self.radius * 0.9 * math.sin(second_angle)
        self.canvas.create_line(self.clock_center, self.clock_center, second_x, second_y, fill='red')

        self.master.after(1000, self.update_display)

if __name__ == "__main__":
    root = tk.Tk()
    clock = BearcatsClock(root)
    root.mainloop()
