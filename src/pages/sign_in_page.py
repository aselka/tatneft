from seleniumpagefactory.Pagefactory import PageFactory


class SignUpPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'login': ('NAME', 'login'),
        'password': ('NAME', 'password'),
        'login_btn': ('CLASS_NAME', 'btn-new__content')
    }

    def select_login(self):
        self.login.set_text('log')

    def select_password(self):
        self.password.set_text('pass')

    def click_login_btn(self):
        self.login_btn.click()