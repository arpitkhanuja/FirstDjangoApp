from selenium import webdriver

browser = webdriver.Firefox() # opens a Firefox browser window
browser.get('http://localhost:8000') # opens the web page we want to test

assert 'Django' in browser.title # checks whether or not 'Django' is in the browser title
