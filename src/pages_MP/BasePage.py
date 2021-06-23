from os import *

from selenium.webdriver.common.by import By

from configurations.baseConfig import *
from utilities import Date_Utils
from utilities.WebDriver_Wait import WebDriverWait_Util

"""This class is a parent of all pages"""
"""Containing all the generic methods for all the pages"""


class BasePage(WebDriverWait_Util):
    """Web_Elements"""
    wb_hdr_AISmartPlatform_xpath = (By.XPATH, "//span[contains(text(),'IA Smart Platform')]")
    wb_txt_errorMsg_xpath = (By.XPATH,
                             "//div[contains(@class, 'Toastify__toast Toastify__toast--error')]//div[contains(@class, 'Toastify__toast-body')]")
    wb_txt_successMsg_xpath = (By.XPATH,
                               "//div[contains(@class, 'Toastify__toast Toastify__toast--success')]//div[contains(@class, 'Toastify__toast-body')]")

    """Constructor of the page class"""

    def __init__(self, context):
        super().__init__(context.driver)

    def get_loginPage_title(self, title):
        try:
            return self.wait_get_title(title)
        except AssertionError as e:
            print(e)

    def get_displayed_error_msg(self):
        errorMsg = ""
        try:
            errorMsg = self.wait_get_wbElement_text(self.wb_txt_errorMsg_xpath)
            if "\n" in errorMsg:
                errorMsg = errorMsg.replace("\n", ": ")
            self.wait_in_seconds(2)
        except AssertionError as e:
            print(e)
        return errorMsg

    def get_displayed_success_msg(self):
        successMsg = ""
        try:
            successMsg = self.wait_get_wbElement_text(self.wb_txt_successMsg_xpath)
            self.wait_in_seconds(2)
        except AssertionError as e:
            print(e)
        return successMsg

    def aiSmartPlatformHeader_isDisplayed(self):
        try:
            boolResult = self.is_displayed(self.wb_hdr_AISmartPlatform_xpath)
            self.wait_in_seconds(2)
            return boolResult
        except AssertionError as e:
            print(e)

    def check_button_enabled_or_disabled(self, wb_Element):
        try:
            return self.is_enabled(wb_Element)
        except AssertionError as e:
            print(e)

    def get_tbl_colName(self, wb_ElementList, strColumnName):
        strActColName = ""
        try:
            for wb_Element in wb_ElementList:
                strActColName = wb_Element.text
                if strColumnName in strActColName:
                    break
                else:
                    strActColName = strActColName.replace("\n", " ")
                    if strColumnName in strActColName:
                        break
        except AssertionError as e:
            print(e)
        return strActColName

    def file_upload_action(self, wbElement, strFilePath):
        try:
            self.wait_in_seconds(1)
            self.wait_locate_element_send_keys(wbElement, strFilePath)
            self.wait_in_seconds(1)
        except AssertionError as e:
            print(e)

    def check_file_download(self, strFileName):
        boolResult = False
        try:
            self.wait_in_seconds(5)
            if Date_Utils.get_currentDate_in_YYYMMDD().replace("/", "_") in strFileName:
                for filename in listdir(DOWNLOADEDFILES_FLD_PATH):
                    if strFileName in filename:
                        print("[" + filename, "] File downloaded successfully")
                        boolResult = True
                        break
            else:
                downloaded_FilePath = DOWNLOADEDFILES_FLD_PATH + strFileName
                boolResult = path.exists(downloaded_FilePath)
        except AssertionError as e:
            print(e)
        return boolResult
