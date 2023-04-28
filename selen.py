from selenium import webdriver
from selenium.webdriver.common.by import By
from getpass import getpass

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://edu-support.mephi.ru")
button = driver.find_element(By.TAG_NAME, "button")
button.click()
username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")
username_field.send_keys(input("USERNAME: "))
password_field.send_keys(getpass("PASSWORD: "))
submit = driver.find_element(By.TAG_NAME, "button")
submit.click()
course_name = "Python для анализа данных и научной визуализации"
course_link = driver.find_element(By.PARTIAL_LINK_TEXT, course_name)
course_link.click()
news_link = driver.find_element(By.LINK_TEXT, "Новости")
news_link.click()
fragments = driver.find_element(By.CLASS_NAME, "fragment")
for fragment in fragments:
    time = fragment.find_element(By.CLASS_NAME, "card-header")
    body = fragment.find_element(By.CLASS_NAME, "card-block")
    print(time.text)
    print(body.text)
    print("\n\n")
driver.save_full_page_screenshot("test.png")
driver.close()