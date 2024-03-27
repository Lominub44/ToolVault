import tkinter as tk
from tkinter import messagebox, filedialog
import qrcode
from PIL import Image, ImageTk

class QRCodeGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("QRGen")
        self.master.geometry("250x355")
        self.master.resizable(True, True)
        self.master.eval('tk::PlaceWindow . center')

        self.label = tk.Label(master, text="Enter text or URL:")
        self.label.pack()

        self.entry = tk.Entry(master, width=35)
        self.entry.pack()
        self.entry.focus_set()  # Eingabefeld automatisch fokussieren

        self.generate_button = tk.Button(master, text="Generate QR Code", command=self.generate_qr_code)
        self.generate_button.pack()

        self.save_button = tk.Button(master, text="Save QR Code", command=self.save_qr_code)
        self.save_button.pack_forget()  # "Save QR Code"-Button verstecken

        self.canvas = tk.Canvas(master, width=250, height=250)
        self.canvas.pack()

    def generate_qr_code(self):
        text = self.entry.get()
        if text:
            qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
            qr.add_data(text)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            img = img.resize((250, 250))
            self.qr_img = ImageTk.PhotoImage(img)
            self.canvas.create_image(0, 0, anchor="nw", image=self.qr_img)
            self.save_button.pack()  # "Save QR Code"-Button anzeigen
        else:
            messagebox.showerror("Error", "Please enter some text or URL.")

    def save_qr_code(self):
        if hasattr(self, 'qr_img'):
            filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
            if filename:
                self.qr_img.write(filename)
                messagebox.showinfo("Success", "QR Code saved successfully.")
        else:
            messagebox.showerror("Error", "Please generate a QR Code first.")

def main():
    root = tk.Tk()
    app = QRCodeGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
