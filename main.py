import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Registration:
    real_name: str
    real_email: str
    username: str

    def __init__(self, real_name, user_email, username=""):
        self.real_name = real_name
        self.user_email = user_email
        self.username = username

    def auto_registration(self):
        browser.get('https://timeweb.com/ru/services/hosting/#hosting-optimo')

        name_field = browser.find_element_by_xpath(
            '/html/body/div[4]/div/div/div[17]/form/div[2]/div[1]/div[3]/div[2]/input')
        email_field = browser.find_element_by_xpath(
            '/html/body/div[4]/div/div/div[17]/form/div[2]/div[1]/div[4]/div/div/div[2]/input')
        name_field.send_keys(self.real_name)
        email_field.send_keys(self.user_email + Keys.RETURN)
        # небольшая пауза, чтобы все данные успели передаться
        time.sleep(5)


if __name__ == '__main__':
    browser = webdriver.Firefox(executable_path='/usr/bin/geckodriver')

    name = input('enter your name: ')
    email = input('enter email for registration: ')
    registration = Registration(real_name=name, user_email=email)
    registration.auto_registration()
    browser.quit()
