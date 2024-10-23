import tkinter as tk
from tkinter import ttk, messagebox

class AllAApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ALL-A")
        
        # Set window size and position it in center
        window_width = 400
        window_height = 300
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        
        center_x = int(screen_width/2 - window_width/2)
        center_y = int(screen_height/2 - window_height/2)
        
        self.root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        
        # Create main frame
        main_frame = ttk.Frame(root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title Label
        title_label = ttk.Label(
            main_frame,
            text="ALL-A",
            font=("Helvetica", 24, "bold")
        )
        title_label.pack(pady=20)
        
        # Subtitle Label
        subtitle_label = ttk.Label(
            main_frame,
            text="MYM youtube account",
            font=("Helvetica", 14)
        )
        subtitle_label.pack(pady=10)
        
        # Connect Button
        self.connect_button = ttk.Button(
            main_frame,
            text="Connect",
            command=self.handle_connect,
            style="Custom.TButton",
            padding=(20, 10)  # Add some padding to make the button bigger
        )
        self.connect_button.pack(pady=30)
        
        # Create a custom style for the button
        style = ttk.Style()
        style.configure("Custom.TButton", font=("Helvetica", 12))

    def handle_connect(self):
        # This is a placeholder for the connect functionality
        messagebox.showinfo("Connection", "Attempting to connect...")
        # Add your connection logic here

if __name__ == "__main__":
    root = tk.Tk()
    app = AllAApp(root)
    root.mainloop()
