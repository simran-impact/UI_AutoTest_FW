import time

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

"""This class is for all web driver wait methods used across the project"""


class WebDriverWait_Util(object):
    implicit_timeout_inSec = 30
    explicit_timeout_inSec = 45

    def __init__(self, driver):
        self.driver = driver

    def wait_in_seconds(self, sec):
        time.sleep(sec)

    def wait_until_pageLoad(self):
        try:
            self.driver.implicitly_wait(self.implicit_timeout_inSec)
        except TimeoutException as e:
            print(e)

    def wait_till_element_visible(self, wb_element):
        try:
            WebDriverWait(self.driver, self.explicit_timeout_inSec).until(EC.visibility_of_element_located(wb_element),
                                                                          "Unable to locate element")
        except NoSuchElementException as e:
            print(e)
        return wb_element

    def wait_till_element_invisible(self, wb_element):
        try:
            WebDriverWait(self.driver, self.explicit_timeout_inSec).until(EC.invisibility_of_element(wb_element),
                                                                          "Able to locate element")
        except NoSuchElementException as e:
            print(e)
        return wb_element

    def wait_till_element_clickable(self, wb_element):
        try:
            WebDriverWait(self.driver, self.explicit_timeout_inSec).until(EC.visibility_of_element_located(wb_element),
                                                                          "Unable to locate element")
            WebDriverWait(self.driver, self.explicit_timeout_inSec).until(EC.element_to_be_clickable(wb_element),
                                                                          "Element not clickable")
        except NoSuchElementException as e:
            print(e)
        return wb_element

    def wait_click(self, wb_element):
        try:
            WebDriverWait(self.driver, self.explicit_timeout_inSec).until(EC.visibility_of_element_located(wb_element),
                                                                          "Unable to locate element")
            WebDriverWait(self.driver, self.explicit_timeout_inSec).until(EC.element_to_be_clickable(wb_element),
                                                                          "Element not clickable").click()
        except NoSuchElementException as e:
            print(e)

    def wait_till_element_clickable_jsClick(self, wb_element):
        try:
            self.wait_till_element_clickable(wb_element)
            self.driver.execute_script("arguments[0].click();", wb_element)
        except NoSuchElementException as e:
            print(e)

    def wait_till_element_clickable_send_keys(self, wb_element, text):
        try:
            WebDriverWait(self.driver, self.explicit_timeout_inSec).until(EC.visibility_of_element_located(wb_element),
                                                                          "Unable to locate element")
            WebDriverWait(self.driver, self.explicit_timeout_inSec).until(EC.element_to_be_clickable(wb_element),
                                                                          "Element not clickable").clear()
            WebDriverWait(self.driver, self.explicit_timeout_inSec).until(EC.element_to_be_clickable(wb_element),
                                                                          "Element not clickable").send_keys(
                text)
        except NoSuchElementException as e:
            print(e)

    def wait_locate_element_send_keys(self, wb_element, text):
        try:
            WebDriverWait(self.driver, self.explicit_timeout_inSec).until(EC.presence_of_element_located(wb_element),
                                                                          "Unable to locate element")
            WebDriverWait(self.driver, self.explicit_timeout_inSec).until(EC.presence_of_element_located(wb_element),
                                                                          "Unable to locate element").send_keys(
                text)
        except NoSuchElementException as e:
            print(e)

    def wait_get_wbElement_text(self, wb_element):
        try:
            element = WebDriverWait(self.driver, self.explicit_timeout_inSec).until(
                EC.visibility_of_element_located(wb_element),
                "Unable to locate element")
            return element.text
        except NoSuchElementException as e:
            print(e)

    def wait_and_get_wbElement_list(self, wb_element_list):
        try:
            elements = WebDriverWait(self.driver, self.explicit_timeout_inSec).until(
                EC.visibility_of_all_elements_located(wb_element_list), "Unable to locate the elements")
            return elements
        except NoSuchElementException as e:
            print(e)

    def is_displayed(self, wb_element):
        try:
            element = WebDriverWait(self.driver, self.explicit_timeout_inSec).until(
                EC.visibility_of_element_located(wb_element),
                "Unable to locate element")
            return bool(element)
        except NoSuchElementException as e:
            print(e)

    def is_enabled(self, wb_element):
        self.wait_till_element_visible(wb_element)
        try:
            element = WebDriverWait(self.driver, self.explicit_timeout_inSec).until(
                EC.element_to_be_clickable(wb_element),
                "Element not clickable")
        except:
            element = False
        return bool(element)

    def wait_get_title(self, title):
        try:
            WebDriverWait(self.driver, self.explicit_timeout_inSec).until(EC.title_contains(title))
            act_title = self.driver.title
            return act_title
        except NoSuchElementException as e:
            print(e)

    def wait_select_dropdown_text(self, wb_element, text):
        try:
            self.wait_till_element_clickable(wb_element)
            drp = Select(wb_element)
            drp.select_by_visible_text(text)
        except NoSuchElementException as e:
            print(e)
