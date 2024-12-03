import tkinter as tk
import time

class DigitalClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Clock")

        self.time_label = tk.Label(root, font=('Helvetica', 48), bg='black', fg='white')
        self.time_label.pack(anchor='center')

        self.update_time()

    def update_time(self):
        current_time = time.strftime("%H:%M:%S %p")
        self.time_label.config(text=current_time)
        self.root.after(1000, self.update_time)

def main():
    root = tk.Tk()
    clock = DigitalClock(root)
    root.mainloop()

if __name__ == "__main__":
    main()
