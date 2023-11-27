import subprocess
from selenium import webdriver

# Launch chromedriver.exe in a separate process
subprocess.Popen("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

# Connect to the running chromedriver.exe instance
driver = webdriver.Chrome()

# Open the desired URLs in the browser
driver.get("https://www.example.com/")
# ...more code here...
