# Importing the required libraries
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.parse import urlparse


def take_partial_screenshots(url, folder_name):
    # Setting up the Chrome driver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")  # Run Chrome with no GUI
    driver = webdriver.Chrome(options=chrome_options)

    try:
        os.makedirs(folder_name, exist_ok=True) # Create folder to store Screenshot.

        # Open the webpage given by the user.
        driver.get(url)
        time.sleep(3)  # Wait for the page to load

        # getting height of the entire webpage.
        total_height = driver.execute_script("return document.body.scrollHeight")

        # Standard width and height for desktop
        viewport_width = 1200
        viewport_height = 800

        # Take partial screenshots
        scroll_position = 0
        screenshot_index = 1
    
        while scroll_position < total_height:
            # dimensions of the viewport to capture
            driver.set_window_size(viewport_width, viewport_height)

            # Scroll to the current position
            driver.execute_script(f"window.scrollTo(0, {scroll_position});")

            # To settle content briefly
            time.sleep(3)

            # Capture screenshot of the current scroll and save
            screenshot_path = os.path.join(folder_name, f"screenshot_{screenshot_index}.png")
            driver.save_screenshot(screenshot_path)

            # Increment scroll position
            scroll_position += viewport_height - 100

            # Increment screenshot index
            screenshot_index += 1

    finally:
        # Quit the driver
        driver.quit()

if __name__ == "__main__":
    while True:
        url = input("Enter the URL of the website: ").strip()

        # Check if the URL is valid or not
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "http://" + url  # Prepending "http://" if missing
        
        parsed_url = urlparse(url)

        website_name = parsed_url.netloc.replace("www.", "")  # Remove "www." if present
        folder_name = f"{website_name}_Screenshots" 


        take_partial_screenshots(url, folder_name)

        print(f"Screenshots for {url} saved successfully in folder: {folder_name}")


        # Asking user for choice to continue or exit.
        while True:
            user_choice = input("\n1. Enter the URL of another website\n2. Exit the program\nEnter your choice (1/2): ")

            if user_choice == '1':
                break  # Break out of the inner loop to enter a new URL
            elif user_choice == '2':
                break  # Exit the outer loop and end the program
            else:
                print("Invalid choice. Please enter 1 or 2.")

        if user_choice == '2':
            break  # Exit the outer loop and end the program
