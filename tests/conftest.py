from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")  # новый headless, более стабильный
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")    # обязательно в CI
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")  # фиксируем размер окна
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    chrome_browser = webdriver.Chrome(options=options)
    return chrome_browser


