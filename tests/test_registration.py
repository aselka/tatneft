from selenium import webdriver
from src.pages.sign_in_page import SignUpPage


def test_registration():
    driver = webdriver.Chrome()
    driver.get('https://azs.tatneft.ru/')
    driver.window_width = 1080
    driver.window_height = 950

    sign_in_page = SignUpPage(driver)

    sign_in_page.select_login()
    sign_in_page.select_password()
    sign_in_page.click_login_btn()

    if driver.current_url == 'https://azs.tatneft.ru/profile':
        print('Авторизация завершилась успешно')
    else:
        print('Авторизация не прошла')

    driver.quit()
