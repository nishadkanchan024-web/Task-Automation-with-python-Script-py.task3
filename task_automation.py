import os
import shutil
import re
import requests
from bs4 import BeautifulSoup

print("Python Task Automation")
print("1. Move JPG Files")
print("2. Extract Emails from Text File")
print("3. Scrape Website Title")

choice = input("Enter your choice (1-3): ")

# Task 1: Move JPG Files
if choice == "1":
    source = "source_folder"
    destination = "destination_folder"

    if not os.path.exists(destination):
        os.makedirs(destination)

    for file in os.listdir(source):
        if file.endswith(".jpg"):
            shutil.move(os.path.join(source, file),
                        os.path.join(destination, file))

    print("All JPG files moved successfully!")

# Task 2: Extract Emails
elif choice == "2":
    with open("input.txt", "r") as file:
        text = file.read()

    emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+", text)

    with open("extracted_emails.txt", "w") as file:
        for email in emails:
            file.write(email + "\n")

    print("Emails extracted successfully!")

# Task 3: Website Title Scraper
elif choice == "3":
    url = "https://example.com"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.title.string

    with open("webpage_title.txt", "w") as file:
        file.write(title)

    print("Website title saved successfully!")

else:
    print("Invalid choice")
