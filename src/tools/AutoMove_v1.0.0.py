import tkinter as tk
import threading
import time
from pynput.keyboard import Controller, Key

class KeyMacro:
    def __init__(self, master):
        self.master = master
        master.title("AutoMove")
        self.master.geometry("100x70")
        self.master.resizable(False, False)
        
        self.is_running = False
        self.create_widgets()

    def create_widgets(self):
        # Button hinzufügen
        self.button = tk.Button(self.master, text="Start macro", command=self.toggle_macro)
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
                keyboard.press('w')
                time.sleep(0.1)
                keyboard.release('w')

                time.sleep(0.1)

                keyboard.press('d')
                time.sleep(0.1)
                keyboard.release('d')

                time.sleep(0.1)

                keyboard.press('s')
                time.sleep(0.1)
                keyboard.release('s')

                time.sleep(0.1)

                keyboard.press('a')
                time.sleep(0.1)
                keyboard.release('a')

                time.sleep(0.1)

        # Ein neuer Thread für das Makro starten
        threading.Thread(target=macro_thread).start()

def main():
    root = tk.Tk()
    app = KeyMacro(root)
    root.mainloop()

if __name__ == "__main__":
    main()
