from os import getcwd,devnull,listdir
import os.path
from time import sleep
from random import randint,choice
from selenium.webdriver.firefox.options import Options
from selenium import webdriver



options = Options()
options.headless = True
driver = webdriver.Firefox(options=options,service_log_path=devnull)

driver.maximize_window()
driver.implicitly_wait(10)

driver.get('https://m.vk.com/')

sleep(2)

with open("email-password.txt") as f:

    data = f.readlines()


driver.find_element_by_name('email').send_keys(data[0].strip())

driver.find_element_by_name('pass').send_keys(data[-1].strip())

driver.find_element_by_css_selector('.fi_row_new > .button').click()

sleep(1)

while 1:

    with open("pub.txt") as f:

        pub = f.readlines()

    for x in range(len(pub)):

        for x in range(2):

            driver.get(pub[x].strip())

            sleep(2)

            driver.find_element_by_css_selector('.new_post_placeholder__text').click()

            sleep(1)

            with open("hashtag.txt") as f:

                hashtag = f.readlines()

            driver.find_element_by_name('message').send_keys(f"#{choice(hashtag)}")

            count_file = len(listdir(os.path.join(getcwd(),"img")))

            img = os.path.join(getcwd(),"img",f"photo{randint(1,count_file)}.jpg")

            driver.find_element_by_css_selector(".inline_upload").send_keys(img)

            sleep(5)

            driver.find_element_by_css_selector('.Btn_theme_regular:nth-child(1)').click()

            sleep(1)

    sleep(3600)