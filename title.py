# importing webdriver from selenium 
from selenium import webdriver 

# Here Chrome will be used 
driver = webdriver.Chrome() 
#driver.maximize_window()

# URL of website 
url = "https://www.saucedemo.com/"

# Getting current URL source code 
get_title = driver.title 

# Printing the title of this URL 

print(get_title, " ", len(get_title)) 

# Opening the website 
driver.get(url) 

# Getting current URL source code 
get_title = driver.title 

# Printing the title of this URL 
print(get_title, " ", len(get_title)) 
