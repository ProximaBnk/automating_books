import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://jarirreader.com")

login = driver.find_element(By.ID,value="header-login")
login.click()

# email = input("Please Enter Already Existing Email: ")
email_input = driver.find_element(By.ID,value="loginform-email")
email_input.send_keys("akaz.reading@gmail.com")

password_input = driver.find_element(By.ID,value="loginform-password")
password_input.send_keys("JAR!@iS1A2B3C4d")
password_input.send_keys(Keys.ENTER)

time.sleep(3)
search = driver.find_element(By.ID,value="keyword")
# book_name = input("Enter the name of your book: ")
search.send_keys("أربعون")
search.send_keys(Keys.ENTER)
time.sleep(3)
books = driver.find_elements(By.CSS_SELECTOR,value=".view-mode-gird > .title-field > h3 > a")
for book in books:
    print(book.text)

time.sleep(3)
arbon = driver.find_element(By.XPATH,value='//*[@id="w0"]/div[1]/div[1]/a')
arbon.click()
time.sleep(3)
add_to_cart= driver.find_element(By.CSS_SELECTOR,value="button.add-to-cart")
add_to_cart.click()
time.sleep(3)
finish_shopping= driver.find_elements(By.CSS_SELECTOR,value=".sa-confirm-button-container > button")
print(finish_shopping)
time.sleep(3)

finish_shopping[0].click()
time.sleep(1000)
driver.quit()