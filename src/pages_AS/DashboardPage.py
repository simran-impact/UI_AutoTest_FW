from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from configurations.baseConfig import *
from src.pages_MP import BasePage
from utilities.Driver_Utils import Driver_Utils


class DashboardPage(BasePage):
    """Web_Elements"""
    wb_hdr_attributeSmart_id = (By.XPATH, "//div[@class='navbar-brand']/span")
    wb_hdr_dashboard_id = (By.ID, "dashboardTitle")
    wb_btn_upload_id = (By.ID, "dashboardUploadBtn")
    wb_tabHdr_createBatch_xpath = (
        By.XPATH, "//div[@class='MuiDialogTitle-root']//span[contains(text(),'Upload Batch')]")
    wb_btn_downloadSample_id = (By.ID, "DownloadLinkSample")
    wb_tb_batchName_id = (By.ID, "upldInputBatchName")
    wb_input_fileUpload_ID = (
        By.XPATH, "//input[contains(@id,'filepond--browser')]")  # Need To Change later to the BasePage if Needed
    wb_btn_dashboardRefresh_ID = (By.ID, "dashboardRefreshBtn")
    wb_tabHdr_deleteBatch_xpath = (By.XPATH, "//div[@class='MuiDialogTitle-root']//h2[contains(text(),'Delete Batch')]")
    wb_tabTxt_deleteBatch_xpath = (
        By.XPATH, "//div[@class='delete-download-container']//h3")  # check  //div[@class='MuiDialogContent-root']//p
    wb_btn_downloadCSV_xpath = (By.XPATH, "//span[contains(@id, 'download') and contains(text(),'CSV file')]")
    # "//button[contains(@id, 'download')]//li[contains(text(),'CSV')]"
    # "//ul[contains(@class,'MuiList-root')]//li[contains(text(),'CSV')]/*[1]"

    """String_Elements"""
    strBatchSummaryTbl = "//div//table[@id='dashboardBatchTable']"
    strDecisionBtnYesNo = "//button[@class='decision-button' and contains(text(),'?')]"

    """Constructor of the page class"""

    def __init__(self, context):
        super().__init__(context)

    def get_attributeSmart_hdrTxt(self):
        strASHeader = ""
        try:
            strASHeader = self.wait_get_wbElement_text(self.wb_hdr_attributeSmart_id)
        except AssertionError as e:
            print(e)
        return strASHeader

    def get_dashboard_hdrTxt(self):
        strDashboardHdr = ""
        try:
            strDashboardHdr = self.wait_get_wbElement_text(self.wb_hdr_dashboard_id)
        except AssertionError as e:
            print(e)
        return strDashboardHdr

    def get_batchSummary_tbl_colName(self, strColumnName):
        strActColName = ""
        try:
            strHeaderColmListLocator = self.strBatchSummaryTbl + "//td[contains(@id,'dashboardBatchTable')]"
            wb_lst_batchSummary_tbl_colHdr_xpath = self.driver.find_elements(By.XPATH, strHeaderColmListLocator)
            strActColName = self.get_tbl_colName(wb_lst_batchSummary_tbl_colHdr_xpath, strColumnName)
        except AssertionError as e:
            print(e)
        return strActColName

    def clickUploadBtn(self):
        strTabHdr = ""
        try:
            self.wait_click(self.wb_btn_upload_id)
            self.wait_in_seconds(2)
            strTabHdr = self.wait_get_wbElement_text(self.wb_tabHdr_createBatch_xpath)
            self.wait_in_seconds(1)
        except AssertionError as e:
            print(e)
        return strTabHdr

    def click_downloadSample_templateBtn(self):
        try:
            self.wait_click(self.wb_btn_downloadSample_id)
            self.wait_in_seconds(3)
        except AssertionError as e:
            print(e)

    def clickDashBoardRefreshBtn(self, intWaitSec):
        try:
            self.wait_in_seconds(intWaitSec)
            self.wait_click(self.wb_btn_dashboardRefresh_ID)
        except AssertionError as e:
            print(e)

    def waitTillBatchProcessedAndRefreshBtn(self, intWaitSec, strBatchName):
        try:
            attempts = 0
            iRowCount = 0
            strRowListLocator = self.strBatchSummaryTbl + "//tbody//tr"
            wb_lstTableRows = self.driver.find_elements(By.XPATH, strRowListLocator)
            for i in range(1, len(wb_lstTableRows) + 1):
                strBatchNameLocator = self.strBatchSummaryTbl + "//tbody//tr[" + str(
                    i) + "]//div[contains(@class,'table__batchname')]/./span//span"
                wb_batchName = self.driver.find_element(By.XPATH, strBatchNameLocator)
                if strBatchName == wb_batchName.text:
                    iRowCount = i
                    break
            strBatchProcessedLocator = self.strBatchSummaryTbl + "//tbody//tr[" + str(
                iRowCount) + "]//div[contains(@class,'table__batchname')]//a//span/*[1]"
            while [attempts <= 15]:
                try:
                    self.driver.find_element(By.XPATH, strBatchProcessedLocator)
                    result = True
                    if result is True:
                        break
                except NoSuchElementException:
                    self.wait_in_seconds(intWaitSec)
                    self.wait_click(self.wb_btn_dashboardRefresh_ID)
        except AssertionError as e:
            print(e)

    def create_batch_by_uploadingCSV(self, strBatchName, strFileName):
        try:
            self.wait_in_seconds(2)
            if strBatchName == "":
                self.wait_till_element_clickable(self.wb_tb_batchName_id)
            elif strBatchName == "Enter Batch Name":
                strBatchName = "AutoTest_Batch_" + Driver_Utils.random_string_num()
                self.wait_till_element_clickable_send_keys(self.wb_tb_batchName_id, strBatchName)
            self.wait_in_seconds(2)
            strFilePath = FILES2UPLOAD_FLD_PATH + strFileName
            self.file_upload_action(self.wb_input_fileUpload_ID, strFilePath)
        except AssertionError as e:
            print(e)
        return strBatchName

    def validate_batchCreated(self, strBatchName):
        strActBatchCreatedText = ""
        try:
            strBatchCreated = ""
            strRowListLocator = self.strBatchSummaryTbl + "//tbody//tr"
            wbLstTableRows = self.driver.find_elements(By.XPATH, strRowListLocator)
            for i in range(1, len(wbLstTableRows) + 1):
                strBatchNameLocator = self.strBatchSummaryTbl + "//tbody//tr[" + str(
                    i) + "]//div[contains(@class,'table__batchname')]/./span//span"
                strBatchCreatedLocator = self.strBatchSummaryTbl + "//tbody//tr[" + str(
                    i) + "]//div[contains(@class,'table__batchname')]//span[2]"
                wb_batchName = self.driver.find_element(By.XPATH, strBatchNameLocator)
                wb_batchCreated = self.driver.find_element(By.XPATH, strBatchCreatedLocator)
                if strBatchName == wb_batchName.text:
                    strBatchName = wb_batchName.text
                    strBatchCreated = wb_batchCreated.text
                    break
            strActBatchCreatedText = strBatchName + " - " + strBatchCreated.replace("\n", " ")
        except AssertionError as e:
            print(e)
        return strActBatchCreatedText

    def validate_batchDeleted(self, strBatchName):
        boolResult = False
        try:
            self.wait_in_seconds(2)
            strRowListLocator = self.strBatchSummaryTbl + "//tbody//tr"
            wbLstTableRows = self.driver.find_elements(By.XPATH, strRowListLocator)
            for i in range(1, len(wbLstTableRows) + 1):
                strBatchNameLocator = self.strBatchSummaryTbl + "//tbody//tr[" + str(i) + "]//u"
                wb_batchName = self.driver.find_element(By.XPATH, strBatchNameLocator)
                if strBatchName == wb_batchName.text:
                    boolResult = True
                    break
        except AssertionError as e:
            print(e)
        return boolResult

    # """Need to change or create new table reader if needed for future use"""
    # """verify_batchTbl_data"""

    def validate_batchTbl_data(self, strGetMapKey, strBatchName):
        strBatchTblData = ""
        try:
            if strGetMapKey not in ["Batch Name", "Num of products uploaded", "Num of broken urls", "Actions"]:
                iThCount = 0
                iRowCount = 0
                strHeaderColmListLocator = self.strBatchSummaryTbl + "//thead//td//span"
                wb_lstTableHeaders = self.driver.find_elements(By.XPATH, strHeaderColmListLocator)
                strRowListLocator = self.strBatchSummaryTbl + "//tbody//tr"
                wb_lstTableRows = self.driver.find_elements(By.XPATH, strRowListLocator)
                for j in range(1, len(wb_lstTableHeaders) + 1):
                    strHeaderColmLocator = self.strBatchSummaryTbl + "//thead//td[" + str(j) + "]//span"
                    wb_TableHeader = self.driver.find_element(By.XPATH, strHeaderColmLocator)
                    str_HdrTxt = wb_TableHeader.text
                    if "\n" in str_HdrTxt:
                        str_HdrTxt = str_HdrTxt.replace("\n", " ")
                    if strGetMapKey == str_HdrTxt:
                        iThCount = j
                        break
                for i in range(1, len(wb_lstTableRows) + 1):
                    strBatchNameLocator = self.strBatchSummaryTbl + "//tbody//tr[" + str(
                        i) + "]//div[contains(@class,'table__batchname')]//a//span"
                    wb_batchName = self.driver.find_element(By.XPATH, strBatchNameLocator)
                    if strBatchName == wb_batchName.text:
                        iRowCount = i
                        break
                strBatchTblDataLocator = self.strBatchSummaryTbl + "//tbody//tr[" + str(iRowCount) + "]//td[" + str(
                    iThCount) + "]"
                wb_batchTblData = self.driver.find_element(By.XPATH, strBatchTblDataLocator)
                strBatchTblData = wb_batchTblData.text
        except AssertionError as e:
            print(e)
        return strBatchTblData

    def postBatchCreation_actions(self, strBatchAction, strBatchName):
        try:
            iRowCount = 0
            strRowListLocator = self.strBatchSummaryTbl + "//tbody//tr"
            wb_lstTableRows = self.driver.find_elements(By.XPATH, strRowListLocator)
            for i in range(1, len(wb_lstTableRows) + 1):
                strBatchNameLocator = self.strBatchSummaryTbl + "//tbody//tr[" + str(i) + "]//u"
                wb_batchName = self.driver.find_element(By.XPATH, strBatchNameLocator)
                if strBatchName == wb_batchName.text:
                    iRowCount = i
                    break
            strActionLocator = self.strBatchSummaryTbl + "//tbody//tr[" + str(
                iRowCount) + "]//button[contains(@id,'?')]"
            if "DELETE" not in strBatchAction and "DOWNLOAD" not in strBatchAction:
                if strBatchAction == "ADD":
                    strActionLocator = strActionLocator.replace("?", "add")
                elif strBatchAction == "WARNING":
                    strActionLocator = strActionLocator.replace("?", "errorReport")
                wb_action = self.driver.find_element(By.XPATH, strActionLocator)
                wb_action.click()
            elif "DELETE" in strBatchAction:
                strActionLocator = strActionLocator.replace("?", "delete")
                wb_action = self.driver.find_element(By.XPATH, strActionLocator)
                wb_action.click()
                self.wait_in_seconds(1)
                if self.is_displayed(self.wb_tabHdr_deleteBatch_xpath) is True and self.wait_get_wbElement_text(
                        self.wb_tabTxt_deleteBatch_xpath) == "Are you sure you want to delete this Batch?":
                    if "YES" in strBatchAction:
                        wb_decisionAction = self.driver.find_element(By.XPATH,
                                                                     self.strDecisionBtnYesNo.replace("?", "Yes"))
                    elif "NO" in strBatchAction:
                        wb_decisionAction = self.driver.find_element(By.XPATH,
                                                                     self.strDecisionBtnYesNo.replace("?", "No"))
                wb_decisionAction.click()
            elif "DOWNLOAD" in strBatchAction:
                strActionLocator = strActionLocator.replace("?", "download") + "//span/span"
                wb_action = self.driver.find_element(By.XPATH, strActionLocator)
                ActionChains(self.driver).move_to_element(wb_action).perform()
                self.wait_in_seconds(2)
                self.wait_click(self.wb_btn_downloadCSV_xpath)
        except AssertionError as e:
            print(e)

    def clickOn_createdBatch(self, strBatchName):
        try:
            self.wait_in_seconds(2)
            strRowListLocator = self.strBatchSummaryTbl + "//tbody//tr"
            wbLstTableRows = self.driver.find_elements(By.XPATH, strRowListLocator)
            for i in range(1, len(wbLstTableRows) + 1):
                strBatchNameLocator = self.strBatchSummaryTbl + "//tbody//tr[" + str(i) + "]//u"
                wb_batchName = self.driver.find_element(By.XPATH, strBatchNameLocator)
                if strBatchName == wb_batchName.text:
                    wb_batchName.click()
                    break
            self.wait_in_seconds(7)
        except AssertionError as e:
            print(e)
