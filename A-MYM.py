import tkinter as tk
from tkinter import ttk
import random

# Create the main window
root = tk.Tk()
root.title("ULTIMO-A")
root.geometry("1200x600")

# Create a frame for the left side
left_frame = ttk.Frame(root)
left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Add title and subtitle to the left frame
title = ttk.Label(left_frame, text="ULTIMO-A", font=("Helvetica", 20))
title.pack(pady=10)
subtitle = ttk.Label(left_frame, text="All media management", font=("Helvetica", 14))
subtitle.pack(pady=5)

# Create a list of media platforms with stylization
platforms = ["YouTube", "Discord", "X", "Reddit", "Instagram", "Facebook", "Gmail"]

# Create a stylized list frame
list_frame = ttk.Frame(left_frame, padding=10)
list_frame.pack(pady=(20, 0))

# Add the platforms to the list frame
for platform in platforms:
    label = ttk.Label(list_frame, text=platform, font=("Helvetica", 12), background="#f0f0f0", padding=5)
    label.pack(anchor='w', padx=20, pady=2, fill=tk.X)

# Define lists for titles, colors, and descriptions
titles = ["Power", "Love", "Energy", "Alpha", "Done", "Gizmo"]
colors = ["red", "blue", "yellow", "green", "purple"]
descriptions = ["I want to wake up", "Thank you", "I love you", "Hello World", "Bye World"]

# Create labels for displaying results
# Initial setup to show in the generated area
color_label = tk.Label(left_frame, text="", font=("Helvetica", 12), bg="#f0f0f0")
description_label = tk.Label(left_frame, text="", font=("Helvetica", 10), bg="#f0f0f0")

# Create a black frame on the right side for media display
media_frame = tk.Frame(root, bg="black")
media_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Create a container frame to hold both the label and the color square
container_frame = tk.Frame(media_frame, bg="black")
container_frame.place(relx=0.5, rely=0.5, anchor='center')

# Add the label for the color square title
square_title_label = tk.Label(container_frame, text="", font=("Helvetica", 12), bg="black", fg="white")
square_title_label.pack(pady=(0, 10))  # Add padding below the title label

# Create the initial red square frame
color_square = tk.Frame(container_frame, bg="red", width=200, height=200)
color_square.pack()

# Add initial description below the color square
initial_description_label = tk.Label(container_frame, text="Description: Red Square", font=("Helvetica", 10), bg="black", fg="white")
initial_description_label.pack(pady=(10, 0))  # Add padding above the description

# Function to generate random variables and update the display
def generate_random():
    title_text = random.choice(titles)
    color = random.choice(colors)
    description_text = random.choice(descriptions)

    # Update the color of the square
    color_square.config(bg=color)  # Change color square color to the selected color

    # Update the title above the square (keep it a fixed color)
    square_title_label.config(text=title_text, fg="white")  # Set the title color to white

    # Update the description below the square
    initial_description_label.config(text=f"Description: {description_text}", fg="white")

# Add the "Generate" button at the center of the left frame
generate_button = ttk.Button(left_frame, text="Generate", command=generate_random)
generate_button.pack(pady=(20, 20), padx=10, anchor='center')

# Run the application
root.mainloop()
