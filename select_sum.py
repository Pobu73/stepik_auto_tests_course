from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = browser.find_element_by_id('num1')
    num2 = browser.find_element_by_id('num2')
    x = num1.text
    y = num2.text
    res = int(x) + int(y)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(res))
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
