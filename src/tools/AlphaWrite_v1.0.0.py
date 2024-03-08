import tkinter as tk
import threading
import time
from pynput.keyboard import Controller, Key

class KeyMacro:
    def __init__(self, master):
        self.master = master
        master.title("AlphaWrite")

        self.is_running = False
        self.create_widgets()

    def create_widgets(self):
        # Button hinzufügen
        self.button = tk.Button(self.master, text="Start Macro", command=self.toggle_macro)
        self.button.pack(pady=20)

        # F2-Taste für das Makro binden
        self.master.bind("<F2>", lambda event: self.toggle_macro())

    def toggle_macro(self, *_):
        if not self.is_running:
            self.is_running = True
            self.start_macro()
            self.button.config(text="Stoppe Makro")
        else:
            self.is_running = False
            self.button.config(text="Starte Makro")

    def start_macro(self):
        def macro_thread():
            keyboard = Controller()

            while self.is_running:
                for char in 'qwertzuiopasdfghjklyxcvbnm':
                    keyboard.press(char)
                    time.sleep(0.001)
                    keyboard.release(char)
                    time.sleep(0.001)

        # Ein neuer Thread für das Makro starten
        threading.Thread(target=macro_thread).start()

def main():
    root = tk.Tk()
    app = KeyMacro(root)
    root.mainloop()

if __name__ == "__main__":
    main()
