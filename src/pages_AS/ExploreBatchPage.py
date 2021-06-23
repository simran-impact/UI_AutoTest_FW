from selenium.webdriver.common.by import By

from configurations.baseConfig import *
from src.pages_MP import BasePage
from tests.instances import setupInstances
from utilities import XLUtils
from utilities.Driver_Utils import Driver_Utils


class ExploreBatchPage(BasePage):
    """Web_Elements"""
    wb_title_exploreBatchName_id = (By.ID, "exploreTitle")
    wb_btn_exportBatch_id = (By.ID, "exportBtn")
    wb_btn_downloadCSV_xpath = (By.XPATH, "//span[contains(@id, 'download') and contains(text(),'CSV file')]")

    """String_Elements"""
    strL1CategoryLbl = "//div[@id='?']//div[contains(text(),'?')]"
    strL2CategoryLbl = "//div[@id='?']//div[@id='@']//div[contains(text(),'@')]"

    """Constructor of the page class"""

    def __init__(self, context):
        super().__init__(context)

    def get_exploreBatchName(self):
        strExploreBatchName = ""
        try:
            self.wait_in_seconds(2)
            strExploreBatchName = self.wait_get_wbElement_text(self.wb_title_exploreBatchName_id)
        except AssertionError as e:
            print(e)
        return strExploreBatchName

    def clickOnExportBtn(self):
        try:
            Driver_Utils.hoverOver_wbElement(self.wb_btn_exportBatch_id)
            self.wait_in_seconds(2)
            self.wait_click(self.wb_btn_downloadCSV_xpath)
            self.wait_in_seconds(3)
        except AssertionError as e:
            print(e)

    def validate_l1Category_isCreated(self, strFileName):
        boolResult = False
        try:
            self.wait_in_seconds(3)
            lst_boolResult = []
            lst_l1Category_values = XLUtils.read_uniqueValues_inACol(FILES2UPLOAD_FLD_PATH + strFileName,
                                                                     setupInstances.l1_category_colName)
            for l1Value in lst_l1Category_values:
                strL1CategoryLocator = self.strL1CategoryLbl.replace("?", l1Value)
                try:
                    wb_L1Category = self.driver.find_element(By.XPATH, strL1CategoryLocator)
                    if l1Value == wb_L1Category.text:
                        lst_boolResult.append(True)
                except:
                    lst_boolResult.append(False)
                    print("L1 Category not visible for : [" + l1Value + "]")
            if False not in lst_boolResult:
                boolResult = True
        except AssertionError as e:
            print(e)
        return boolResult

    def validate_l2Category_createdUnder_l1Category(self, strFileName):
        boolResult = False
        try:
            self.wait_in_seconds(2)
            lst_boolResult = []
            setupInstances.col_list.append([setupInstances.l1_category_colName, setupInstances.l2_category_colName])
            lst_l1Category_values = XLUtils.read_uniqueValues_inACol(FILES2UPLOAD_FLD_PATH + strFileName,
                                                                     setupInstances.l1_category_colName)
            for l1Value in lst_l1Category_values:
                lst_l2Category_values_withL1 = XLUtils.read_uniqueValues_from_Col1_respectTo_Col2Value(
                    FILES2UPLOAD_FLD_PATH + strFileName, setupInstances.col_list, l1Value)
                for l2Value in lst_l2Category_values_withL1:
                    strL2CategoryLocator = self.strL2CategoryLbl.replace("?", l1Value).replace("@", l2Value)
                    try:
                        wb_L2Category = self.driver.find_element(By.XPATH, strL2CategoryLocator)
                        if l2Value == wb_L2Category.text:
                            lst_boolResult.append(True)
                    except:
                        lst_boolResult.append(False)
                        print("L2 Category [" + l2Value + "] for [" + l1Value + "] L1 Category is not visible")
            if False not in lst_boolResult:
                boolResult = True
        except AssertionError as e:
            print(e)
        return boolResult
