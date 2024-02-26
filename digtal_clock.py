import tkinter as tk
import math
import time

class AnalogClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Analog Clock")
        self.root.geometry("900x500")
        self.root['bg'] = '#003333'

        self.frame = tk.Frame(self.root, bd=2, bg='#003333')
        self.frame.pack(side=tk.LEFT, padx=5, pady=5)

        self.canvas = tk.Canvas(self.frame, width=300, height=300, bg="#65737e")
        self.canvas.pack()

        self.draw_clock_face()
        self.draw_clock_hands()
        self.draw_minute_marks()

        self.update_clock()

    def draw_clock_face(self):
        self.canvas.create_oval(50, 50, 250, 250, outline="black", width=2)
        for i in range(1, 13):
            angle = math.radians(90 - i * 30)
            x = 150 + 90 * math.cos(angle)
            y = 150 - 90 * math.sin(angle)
            self.canvas.create_text(x, y, text=str(i), font=("Arial", 12), fill="black")

    def draw_clock_hands(self):
        self.hour_hand = self.canvas.create_line(150, 150, 150, 90, width=6, fill="black")
        self.minute_hand = self.canvas.create_line(150, 150, 150, 60, width=4, fill="blue")
        self.second_hand = self.canvas.create_line(150, 150, 150, 50, width=2, fill="red")

    def draw_minute_marks(self):
        for i in range(60):
            angle = math.radians(90 - i * 6)
            inner_radius = 130 if i % 5 != 0 else 120
            outer_radius = 150
            x1 = 150 + inner_radius * math.cos(angle)
            y1 = 150 - inner_radius * math.sin(angle)
            x2 = 150 + outer_radius * math.cos(angle)
            y2 = 150 - outer_radius * math.sin(angle)
            self.canvas.create_line(x1, y1, x2, y2, fill="black")

    def update_clock(self):
        current_time = time.localtime()
        hours = current_time.tm_hour
        minutes = current_time.tm_min
        seconds = current_time.tm_sec

        self.update_hand(self.hour_hand, hours * 30 + minutes / 2)
        self.update_hand(self.minute_hand, minutes * 6)
        self.update_hand(self.second_hand, seconds * 6)

        self.root.after(1000, self.update_clock)

    def update_hand(self, hand, angle):
        angle_rad = math.radians(90 - angle)
        hand_length = 90
        x = 150 + hand_length * math.cos(angle_rad)
        y = 150 - hand_length * math.sin(angle_rad)
        self.canvas.coords(hand, 150, 150, x, y)

if __name__ == "__main__":
    root = tk.Tk()
    clock = AnalogClock(root)
    root.mainloop()
