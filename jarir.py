"""This is a program for choosing a book from jarir reader website and buy it instantly!"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://jarirreader.com")

login = driver.find_element(By.ID, value="header-login")
login.click()

email_input = driver.find_element(By.ID, value="loginform-email")
email = input("Please Enter Your already existing email:").strip().lower()
email_input.send_keys(email)

password_input = driver.find_element(By.ID, value="loginform-password")
password = input("Please Enter Your password:")
password_input.send_keys(password)
password_input.send_keys(Keys.ENTER)

time.sleep(3)
search = driver.find_element(By.ID, value="keyword")
book_name = input("Enter the name of your book: ")
search.send_keys(book_name)
search.send_keys(Keys.ENTER)
time.sleep(1)
books = driver.find_elements(
    By.CSS_SELECTOR, value=".view-mode-gird > .title-field > h3 > a"
)
for index, book in enumerate(books):
    print(f"{index+1}: {book.text}")
select_book = int(input("Please Enter The Number Of The Required Book:"))
time.sleep(1)

selected_book = driver.find_element(
    By.XPATH, value=f'//*[@id="w0"]/div[{select_book}]/div[1]/a'
)
selected_book.click()
time.sleep(1)

add_to_cart = driver.find_element(By.CSS_SELECTOR, "button.add-to-cart")
driver.execute_script("arguments[0].click();", add_to_cart)
time.sleep(1)

finish_shopping = driver.find_element(
    By.CSS_SELECTOR, ".sa-confirm-button-container > button"
)
driver.execute_script("arguments[0].click();", finish_shopping)
time.sleep(1)

mada = driver.find_element(By.XPATH, '//*[@id="payments-checkout"]/label[1]')
driver.execute_script("arguments[0].click();", mada)
time.sleep(1)

dont_save = driver.find_element(By.XPATH, '//*[@id="add_credit_card_container"]/label')
driver.execute_script("arguments[0].click();", dont_save)
time.sleep(1)

pay = driver.find_element(By.CSS_SELECTOR, ".btn-primary.checkout")
driver.execute_script("arguments[0].click();", pay)
time.sleep(1)
driver.quit()
