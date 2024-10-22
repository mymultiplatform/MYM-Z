import tkinter as tk
from tkinter import ttk
import random
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException

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
platforms = ["YouTube", "Discord", "X (Twitter)", "Reddit", "Instagram", "Facebook", "Gmail"]

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

    # Update the title above the square
    square_title_label.config(text=title_text, fg="white")  # Set the title color to white

    # Update the description below the square
    initial_description_label.config(text=f"Description: {description_text}", fg="white")

    # Call Instagram automation here
    start_instagram_automation()

# Function to automate Instagram login and infinite scroll
def automate_instagram():
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.instagram.com")
    time.sleep(3)

    # Log in to Instagram
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    username.send_keys("cincomember")  # Replace with your Instagram username
    password.send_keys("Sexo247420")  # Replace with your Instagram password
    password.send_keys(Keys.RETURN)
    time.sleep(5)

    # Handle "Save login info?" popup
    try:
        save_info_button = driver.find_element(By.XPATH, "//button[text()='Save info']")
        save_info_button.click()
        time.sleep(5)  # Delay to ensure the popup is handled
    except NoSuchElementException:
        print("Save info popup not found. Continuing...")

    # Scroll down function
    def infinite_scroll():
        start_time = time.time()
        while True:
            driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
            time.sleep(2)
            if time.time() - start_time > 20:  # Scroll for 20 seconds
                break
    infinite_scroll()

    # Simulate a post comment
    def comment_on_post():
        try:
            # Find the first post
            post = driver.find_element(By.XPATH, "//article//a[contains(@href, '/p/')]")
            post.click()
            time.sleep(3)

            # Locate the comment bar
            comment_bar = driver.find_element(By.XPATH, "//textarea[@aria-label='Add a comment...']")
            comment_bar.click()

            # Simulate typing "Dante" using pyautogui after 7 seconds
            time.sleep(7)
            pyautogui.typewrite("Dante")

            # Click Post
            post_button = driver.find_element(By.XPATH, "//button[contains(text(),'Post')]")
            post_button.click()
            time.sleep(5)  # Wait to ensure the comment is posted

            # Keep browser open for an additional period
            time.sleep(60)  # Adjust the sleep time as needed to keep the browser open

        except NoSuchElementException:
            print("Element not found. The script might need updates to match the current Instagram structure.")
        except WebDriverException as e:
            print(f"WebDriverException occurred: {e}")

    comment_on_post()

# Function to start Instagram automation
def start_instagram_automation():
    automate_instagram()

# Add the "Generate" button at the center of the left frame
generate_button = ttk.Button(left_frame, text="Generate", command=generate_random)
generate_button.pack(pady=(20, 20), padx=10, anchor='center')

# Run the application
root.mainloop()
