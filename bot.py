from string import ascii_letters
import random
import time

import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from webdriver_manager.chrome import ChromeDriverManager

email = input('Введите ваш email: ')
username = input('Введите ваш username: ')

login_url = 'https://discord.com/api/v9/auth/login'
register_url = 'https://discord.com/register'

def get_random_password():
    password = ''
    for i in range(16):
        password += random.choice(list(ascii_letters))
    return password

def sign_up(email, username, password):
    try:
        driver = webdriver.Chrome(
            executable_path=ChromeDriverManager().install(),
        )
        driver.get(register_url)
        time.sleep(2)
        email_input = driver.find_element(By.NAME, 'email')
        username_input = driver.find_element(By.NAME, 'username')
        password_input = driver.find_element(By.NAME, 'password')
        day_of_birth = driver.find_element(By.ID, 'react-select-2-input')
        month_of_birth = driver.find_element(By.ID, 'react-select-3-input')
        year_of_birth = driver.find_element(By.ID, 'react-select-4-input')
        button_register = driver.find_element(By.CLASS_NAME, 'button-1cRKG6')
        email_input.click()
        email_input.send_keys(email)
        username_input.send_keys(username)
        password_input.send_keys(password)
        time.sleep(1)
        day_of_birth.send_keys(1)
        time.sleep(2)
        month_of_birth.send_keys('январь')
        month_of_birth.send_keys(Keys.ENTER)
        time.sleep(2)
        year_of_birth.send_keys(2000)
        time.sleep(2)
        button_register.click()
        time.sleep(30)
    finally:
        driver.close()
        driver.quit()

def login(email, password):
    json_data = {
        'login': email,
        'password': password,
    }
    r = requests.post(login_url, json=json_data)
    return r.json().get('token')

def main():
    password = get_random_password()
    print(f'password: {password}')
    sign_up(email, username, password)
    print(f'token: {login(email, password)}')

if __name__ == '__main__':
    main()
