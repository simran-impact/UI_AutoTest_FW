import os
import random
import secrets
import shutil
import string

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains

from configurations import baseConfig
from utilities.WebDriver_Wait import WebDriverWait_Util


class Driver_Utils(WebDriverWait_Util):

    def scroll_into_view(self, wb_element):
        try:
            self.wait_till_element_visible(wb_element)
            self.driver.execute_script("arguments[0].scrollIntoView();", wb_element)
        except NoSuchElementException as e:
            print(e)

    def hoverOver_wbElement(self, wb_element):
        try:
            self.wait_till_element_visible(wb_element)
            ActionChains(self.driver).move_to_element(wb_element).perform()
        except NoSuchElementException as e:
            print(e)

    def random_string(self=10):
        # string.ascii_letters same as string.ascii_uppercase + string.ascii_lowercase
        character_set = string.ascii_letters
        random_str_value = ''.join(random.choice(character_set) for i in range(self))
        return random_str_value

    def random_email(self=15):
        # string.ascii_letters same as string.ascii_uppercase + email domain
        character_set = string.ascii_letters
        domains = ["hotmail.com", "gmail.com", "aol.com", "mail.com", "mail.kz", "yahoo.com"]
        random_email_value = ''.join(random.choice(character_set) for i in range(self)) + "@" + domains[
            random.randint(0, len(domains) - 1)]
        return random_email_value

    def random_string_num(self=5):
        # string.digits generates random numbers
        random_str_num_value = ''.join(secrets.choice(string.digits) for x in range(self))
        return random_str_num_value
