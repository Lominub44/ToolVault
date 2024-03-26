import customtkinter as ctk
from customtkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox  # separate import for messagebox
import requests
import os
import sys
import subprocess
from pypresence import *
import threading
import time
import webbrowser
# Function for downloading the tool
def download_tool(tool):
    try:
        # Determine download path based on operating system
        if sys.platform.startswith('win'):  # Windows
            download_path = os.path.join(os.environ['USERPROFILE'], '.ToolVault')
        elif sys.platform.startswith('darwin'):  # macOS
            download_path = os.path.join(os.path.expanduser('~'), '.ToolVault')
        elif sys.platform.startswith('linux'):  # Linux
            download_path = os.path.join(os.path.expanduser('~'), '.ToolVault')
        else:
            download_path = os.path.join(os.path.expanduser('~'), '.ToolVault')  # Default path for unknown systems

        # Check if the hidden folder exists, and if not, create it
        if not os.path.exists(download_path):
            os.makedirs(download_path, exist_ok=True)

        tool_name = tool.url.split("/")[-1]  # Extract the tool name from the URL

        # Send request to the URL and save the content
        response = requests.get(tool.url)
        response.raise_for_status()  # Raise error if the request is not successful

        # Download and save the tool
        with open(os.path.join(download_path, tool_name), 'wb') as f:
            f.write(response.content)

        # Show success message
        messagebox.showinfo("Download",
                            f"{tool.name} successfully downloaded to: {os.path.join(download_path, tool_name)}")
    except Exception as e:
        # Show error message if an error occurs
        messagebox.showerror("Error", f"Error downloading {tool.name}: {str(e)}")


# Function for starting a tool
def start_tool(tool):
    try:
        # Path to the hidden folder for installed tools
        if sys.platform.startswith('win'):  # Windows
            target_folder = os.path.join(os.environ['USERPROFILE'], '.ToolVault')
        elif sys.platform.startswith('darwin'):  # macOS
            target_folder = os.path.join(os.path.expanduser('~'), '.ToolVault')
        elif sys.platform.startswith('linux'):  # Linux
            target_folder = os.path.join(os.path.expanduser('~'), '.ToolVault')
        else:
            target_folder = os.path.join(os.path.expanduser('~'), '.ToolVault')  # Default hidden folder for unknown systems
        
        tool_path = os.path.join(target_folder, tool)
        
        if sys.platform.startswith('win'):  # Windows
            os.startfile(tool_path)
        else:
            subprocess.run(tool_path, shell=True)

    except Exception as e:
        # Show error message if an error occurs
        messagebox.showerror("Error", f"Error starting {tool}: {str(e)}")

# Class for a tool site
class Tool:
    def __init__(self, name, description, url):
        self.name = name
        self.description = description
        self.url = url

# Function for showing the product page
def show_product_page(tool):
    product_page = ctk.CTkToplevel(root)
    product_page.title(tool.name)
    print("product-page opened")
    

    # Get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Set window width and height (slightly smaller than main window)
    window_width = 600
    window_height = 400

    # Calculate x and y coordinates for centered window
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)

    # Product page settings
    product_page.geometry(f"{window_width}x{window_height}+{x}+{y}")

    ctk.CTkLabel(product_page, text=f"Name: {tool.name}", font=("Helvetica", 18)).pack(pady=10)
    ctk.CTkLabel(product_page, text=f"Description: {tool.description}").pack(pady=5)

    # Add download button
    download_button = ctk.CTkButton(product_page, text="Download", command=lambda: download_tool(tool))
    download_button.pack(pady=10)
    
    # Lift the product page to the top level
    product_page.wm_attributes("-topmost", 1)

# Example tool creation
tool1 = Tool("tool 1", "for now its a snake game, we will add real tools soon", "https://github.com/Lominub44/SaphireHub/raw/main/snake_V0.0.3.exe")
tool2 = Tool("tool 2", "the same (again) ", "https://github.com/Lominub44/SaphireHub/raw/main/snake_V0.0.3.exe")
featured_tool = Tool("Featured Tool", "A powerful tool for various tasks", "https://github.com/Lominub44/SaphireHub/raw/main/snake_V0.0.3.exe")

# Function for showing the discover page
def show_discover_page():
    discover_frame = ctk.CTkFrame(notebook)
    notebook.add(discover_frame, text="Discover")

    ctk.CTkLabel(discover_frame, text="Discover new tools!", font=("Helvetica", 18)).pack(pady=10)
    ctk.CTkButton(discover_frame, text=tool1.name, command=lambda: show_product_page(tool1)).pack(pady=5)
    ctk.CTkButton(discover_frame, text=tool2.name, command=lambda: show_product_page(tool2)).pack(pady=5)
    ctk.CTkButton(discover_frame, text=featured_tool.name, command=lambda: show_product_page(featured_tool)).pack(pady=5)
    
    # Show the library page after the discover page
    show_library()

# Function for creating a hidden directory (only for Windows)
def create_hidden_directory(directory):
    try:
        # Create the hidden directory
        if not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)

        # Hide the directory
        if sys.platform.startswith('win'):  # Only for Windows
            import ctypes
            FILE_ATTRIBUTE_HIDDEN = 0x02
            ctypes.windll.kernel32.SetFileAttributesW(directory, FILE_ATTRIBUTE_HIDDEN)
    except Exception as e:
        print(f"Error creating or hiding directory: {str(e)}")

# Function for showing installed tools in the library
def show_library():
    # Check if the library page has already been added
    if len(notebook.tabs()) < 3:
        library_frame = ctk.CTkFrame(notebook)
        notebook.add(library_frame, text="Library")

        # Path to the hidden folder for installed tools
        if sys.platform.startswith('win'):  # Windows
            target_folder = os.path.join(os.environ['USERPROFILE'], '.ToolVault')
        elif sys.platform.startswith('darwin'):  # macOS
            target_folder = os.path.join(os.path.expanduser('~'), '.ToolVault')
        elif sys.platform.startswith('linux'):  # Linux
            target_folder = os.path.join(os.path.expanduser('~'), '.ToolVault')
        else:
            target_folder = os.path.join(os.path.expanduser('~'), '.ToolVault')  # Default hidden folder for unknown systems

        # Check if the hidden folder exists
        if os.path.exists(target_folder):
            # List tools in the hidden folder
            tools = [file for file in os.listdir(target_folder) if os.path.isfile(os.path.join(target_folder, file))]
            if tools:
                ctk.CTkLabel(library_frame, text="Your Library", font=("Helvetica", 18)).pack(pady=10)
                tools_listbox = tk.Listbox(library_frame, width=50, height=10)
                for tool in tools:
                    tools_listbox.insert(tk.END, tool)
                tools_listbox.pack(pady=5)
                start_button = ctk.CTkButton(library_frame, text="Start", command=lambda: start_tool(tools_listbox.get(tk.ACTIVE)))
                start_button.pack(pady=5)
            else:
                ctk.CTkLabel(library_frame, text="Your library is empty!").pack(pady=10)
        else:
            ctk.CTkLabel(library_frame, text="The hidden folder was not found!").pack(pady=10)
            # Create hidden folder
            create_hidden_directory(target_folder)

# Create main window
root = ctk.CTk()
root.title("ToolVault")

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set window width and height
window_width = 800
window_height = 600

# Calculate x and y coordinates for centered window
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

# Main window settings
root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.resizable(False, False)  # Prevent window resizing

# Create tabs
notebook = ttk.Notebook(root)

# Home page
home_frame = ctk.CTkFrame(notebook)
notebook.add(home_frame, text="Home")


#  _    _                      
# | |  | |                     
# | |__| | ___  _ __ ___   ___ 
# |  __  |/ _ \| '_ ` _ \ / _ \
# | |  | | (_) | | | | | |  __/
# |_|  |_|\___/|_| |_| |_|\___|
                              
                              


# Add a news and updates section
news_and_updates = """
Latest News:
- New tools added to ToolVault!
- Stay tuned for upcoming features!
"""
# Add content to the Home tab
ctk.CTkLabel(home_frame, text="Welcome to ToolVault", font=("Helvetica", 18)).pack(pady=10)
ctk.CTkLabel(home_frame, text=news_and_updates).pack(pady=5)

# Display featured tool
ctk.CTkLabel(home_frame, text=f"Featured Tools: {featured_tool.name}", font=("Helvetica", 14)).pack(pady=5)
ctk.CTkLabel(home_frame, text=f"Description: {featured_tool.description}").pack(pady=5)
ctk.CTkButton(home_frame, text="featured_tool", command=lambda: show_product_page(featured_tool)).pack(pady=5)

# Quick links
ctk.CTkLabel(home_frame, text="Quick Links:", font=("Helvetica", 14)).pack(pady=5)
ctk.CTkButton(home_frame, text="GitHub", command=lambda: webbrowser.open("https://github.com/Lominub44/ToolVault")).pack(pady=5)




# end of home 


# Pack notebook widget
notebook.pack(expand=1, fill="both")

# Close main window when window is closed
root.protocol("WM_DELETE_WINDOW", root.quit)

# Start Discord RPC
RPC = Presence(client_id=1215393701002608710)
RPC.connect()
RPC.update(
    state="Made by LomiLab",
    details="A hub for some useful tools",
    large_image="logo",  # Replace "your_large_image_name" with the name of your large image
    small_image="logo",  # Replace "your_small_image_name" with the name of your small image
    buttons=[
        {"label": "Repository", "url": "https://github.com/Lominub44/ToolVault"},
        {"label": "Discord Server", "url": "https://discord.gg/5gNuWKpzgF"}
    ]
)

# Function to update presence periodically
def update_presence():
    while True:
        RPC.update(
            state="Made by LomiLab",
            details="A hub for some usefull tools",
            large_image="logo",  # Replace "your_large_image_name" with the name of your large image
            small_image="logo",  # Replace "your_small_image_name" with the name of your small image
            buttons=[
                {"label": "Repository", "url": "https://github.com/Lominub44/ToolVault"},
                {"label": "Discord Server", "url": "https://discord.gg/5gNuWKpzgF"}
            ]
        )
        time.sleep(15)  # Update presence every 15 seconds

# Start the thread to update presence
threading.Thread(target=update_presence, daemon=True).start()

# Show discover page
show_discover_page()

# Start main loop
root.mainloop()
