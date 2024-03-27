import tkinter as tk
import pyautogui
import keyboard

class AutoClick:
    def __init__(self, master):
        self.master = master
        self.master.title("AutoClick")
        
        self.master.resizable(False, False)

        self.label = tk.Label(master, text="Distance between clicks (in milliseconds):")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.insert(0, "10")  # Default interval of 10 milliseconds
        self.entry.pack()

        self.button = tk.Button(master, text="Start/Stop AutoClick", command=self.toggle_auto_click)
        self.button.pack(pady=20)

        self.is_auto_clicking = False
        self.click_interval = 10  # Default interval of 10 milliseconds

        # Adding key event for F3 using the keyboard module
        keyboard.on_press_key("F3", self.toggle_auto_click)

    def toggle_auto_click(self, event=None):
        if not self.is_auto_clicking:
            print("Started AutoClick!")
            self.is_auto_clicking = True
            self.click_interval = int(self.entry.get())
            self.auto_click()
        else:
            print("Stopped AutoClick!")
            self.is_auto_clicking = False

    def auto_click(self):
        if self.is_auto_clicking:
            x, y = pyautogui.position()
            pyautogui.click(x, y)
            print(f"Automatic click at position ({x}, {y})!")
            self.master.after(self.click_interval, self.auto_click)

def main():
    root = tk.Tk()
    root.geometry("230x100")
    app = AutoClick(root)
    root.mainloop()

if __name__ == "__main__":
    main()
