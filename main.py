from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from bs4 import BeautifulSoup
from pynput import keyboard
import pyautogui
import time


# VarChar list
characters = []


def on_press(key):
    if key == keyboard.Key.f5:
        for char in characters:
            pyautogui.typewrite(characters, interval=0.0)
        time.sleep(10)


# Setup Firefox options
firefox_options = webdriver.FirefoxOptions()

# Start a browser session
browser = webdriver.Firefox(
    service=Service(GeckoDriverManager().install()), options=firefox_options
)

# Open a webpage
browser.get("https://humanbenchmark.com/tests/typing")

# Wait for the page to load (optional, could be more sophisticated)
browser.implicitly_wait(10)  # seconds

# Get page HTML
html = browser.page_source

# Use BeautifulSoup to parse the HTML content
soup = BeautifulSoup(html, "lxml")  # or 'html.parser' if you didn't install lxml

# Now you can use BeautifulSoup methods to find data in the HTML
# For example, to find all paragraph tags:
paragraphs = soup.find_all("span")
for p in paragraphs:
    characters.append(p.text)


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
# Close the browser

input()
browser.quit()
