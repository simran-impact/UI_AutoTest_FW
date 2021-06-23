from selenium.webdriver.common.by import By

from src.pages_MP import BasePage


class LoginPage(BasePage):
    """Web_Elements"""
    wb_tb_userEmail_id = (By.ID, "loginInputEmail")
    wb_tb_password_id = (By.ID, "loginPassword")
    wb_btn_signIn_id = (By.ID, "btnLogin")
    wb_btn_signIn_xpath = (By.XPATH, "//button[contains(text(),'Sign in')]")  # TimeBeing
    wb_btn_forgotPwd_id = (By.ID, "btnReset")
    wb_hdr_markSmart_xpath = (By.XPATH, "//span[@id='titleColor' and contains(text(),'MarkSmart')]")
    wb_appBtn_AttributeSmart_id = (By.ID, "Attribute Smart")
    wb_appBtn_MarkSmart_id = (By.ID, "MarkSmart")

    """Constructor of the page class"""

    def __init__(self, context):
        super().__init__(context)

    """Page Actions"""

    def enter_username_and_password(self, strUseremail, strPassword):
        try:
            self.wait_till_element_clickable_send_keys(self.wb_tb_userEmail_id, strUseremail)
            self.wait_in_seconds(2)
            self.wait_till_element_clickable_send_keys(self.wb_tb_password_id, strPassword)
            self.wait_in_seconds(2)
        except AssertionError as e:
            print(e)

    def clickSignIn(self):
        try:
            # self.wait_click(self.wb_btn_signIn_id)
            self.wait_click(self.wb_btn_signIn_xpath)
            self.wait_in_seconds(2)
        except AssertionError as e:
            print(e)

    def clickForgotPassword(self):
        try:
            self.wait_click(self.wb_btn_forgotPwd_id)
            self.wait_in_seconds(1)
        except AssertionError as e:
            print(e)

    def markSmartHeader_isDisplayed(self):
        try:
            return self.is_displayed(self.wb_hdr_markSmart_xpath)
        except AssertionError as e:
            print(e)

    def clickOn_application_btn(self, strApp):
        try:
            self.wait_in_seconds(2)
            if strApp == "AttributeSmart":
                self.wait_click(self.wb_appBtn_AttributeSmart_id)
            elif strApp == "MarkSmart":
                self.wait_click(self.wb_appBtn_MarkSmart_id)
            self.wait_in_seconds(2)
        except AssertionError as e:
            print(e)
