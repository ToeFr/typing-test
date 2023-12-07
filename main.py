from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from bs4 import BeautifulSoup
from pynput import keyboard
import pyautogui
import time


characters = []


def on_press(key):
    if key == keyboard.Key.f5:
        for char in characters:
            pyautogui.typewrite(characters, interval=0.0)
        time.sleep(10)


firefox_options = webdriver.FirefoxOptions()


browser = webdriver.Firefox(
    service=Service(GeckoDriverManager().install()), options=firefox_options
)


browser.get("https://humanbenchmark.com/tests/typing")


browser.implicitly_wait(10)


html = browser.page_source


soup = BeautifulSoup(html, "lxml")

paragraphs = soup.find_all("span")
for p in paragraphs:
    characters.append(p.text)


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

input()
browser.quit()
