from behave import *
from delayed_assert import delayed_assert, expect

from tests.instances import setupInstances
from utilities import Date_Utils


@when('User lands on Attribute Smart Dashboard Page')
def user_lands_on_Attribute_Smart_Dashboard_Page(context):
    expt_AS_text = "Attribute Smart"
    act_AS_text = context.dashboard_page.get_attributeSmart_hdrTxt()
    if act_AS_text == expt_AS_text:
        assert True
    else:
        print("\n[ " + expt_AS_text + " ]-----is not displayed, Thus not landed on the Attribute Smart Application\n")
        print("\n Expected: [ " + expt_AS_text + " ], but found [ " + act_AS_text + " ]\n")
        assert False
    expt_text = "Dashboard"
    act_text = context.dashboard_page.get_dashboard_hdrTxt()
    if act_text == expt_text:
        assert True
    else:
        print("\n[ " + expt_text + " ]-----is not displayed, Thus not landed on the Attribute Smart Dashboard Page\n")
        print("\n Expected: [ " + expt_text + " ], but found [ " + act_text + " ]\n")
        assert False


@then('User validates the columns available in the batch table')
def test_user_validates_the_columns_available_in_the_batch_table(context):
    for row in context.table:
        expt_columnName = row["Column Names"]
        act_columnName = context.dashboard_page.get_batchSummary_tbl_colName(expt_columnName)
        expect(act_columnName == expt_columnName,
               "\n Column name is not as expected for : [ " + expt_columnName + " ]\n")
    delayed_assert.assert_expectations()


@then('User clicks on Upload button on the Dashboard Page')
def user_clicks_on_Upload_button_on_the_Dashboard_Page(context):
    expt_text = "Create Batch"
    act_text = context.dashboard_page.clickUploadBtn()
    if act_text == expt_text:
        assert True
    else:
        print("\nClick upload button failed\n")
        print("\n Expected: [" + expt_text + "], but found [" + act_text + "]\n")
        assert False


@then('Enters the new batch name in the Create Batch Tab and uploads CSV file')
def enters_the_new_Batch_Name_in_the_Create_Batch_Tab_and_uploads_CSV_file(context):
    strTestCondition = ""
    setupInstances.lstMapTestData = dict(context.table)
    for x in setupInstances.lstMapTestData:
        strTestCondition = x
    setupInstances.strFileName = setupInstances.lstMapTestData.get(strTestCondition)
    setupInstances.strCreatedBatchName = context.dashboard_page.create_batch_by_uploadingCSV("Enter Batch Name",
                                                                                             "toUploadAndProcessBatch\\" + setupInstances.strFileName)


@then('User checks if the created batch name is displayed in the batch table on Dashboard Page with following')
def test_user_checks_if_the_created_batch_name_is_displayed_in_the_batch_table_on_Dashboard_Page(context):
    setupInstances.lstMapTestData = dict(context.table)
    expt_createdBatch_txt = setupInstances.strCreatedBatchName + " - Created On: " + Date_Utils.get_currentDate_in_MMDDYYY()
    context.base_page.wait_in_seconds(15)
    act_createdBatch_txt = context.dashboard_page.validate_batchCreated(setupInstances.strCreatedBatchName)
    expect(act_createdBatch_txt == expt_createdBatch_txt,
           "\n Batch name and created date incorrect : [Result: " + act_createdBatch_txt + " ]\n")
    context.dashboard_page.clickDashBoardRefreshBtn(35)
    context.dashboard_page.clickDashBoardRefreshBtn(35)
    context.base_page.wait_in_seconds(10)
    for colName in setupInstances.lstMapTestData:
        if colName not in ["Num of broken urls", "Actions", "Batch Name", "Num of images uploaded"]:
            expt_Text = setupInstances.lstMapTestData.get(colName)
            act_Text = context.dashboard_page.validate_batchTbl_data(colName, setupInstances.strCreatedBatchName)
            expect(act_Text == expt_Text, "\n Data not as expected for the Column : [ " + colName + " ]\n")
    delayed_assert.assert_expectations()


@then('Does not enter batch name in the Create Batch Tab and uploads CSV file')
def does_not_enter_batch_name_in_the_Create_Batch_Tab_and_uploads_CSV_file(context):
    strTestCondition = ""
    setupInstances.lstMapTestData = dict(context.table)
    for x in setupInstances.lstMapTestData:
        strTestCondition = x
    setupInstances.strFileName = setupInstances.lstMapTestData.get(strTestCondition)
    setupInstances.strCreatedBatchName = context.dashboard_page.create_batch_by_uploadingCSV("",
                                                                                             "toUploadAndProcessBatch\\" + setupInstances.strFileName)


@then('User performs "{action}" action on the created Batch present in the batch table')
def user_performs_action_on_the_created_Batch_present_in_the_batch_table(context, action):
    context.dashboard_page.postBatchCreation_actions(action, setupInstances.strCreatedBatchName)
    if action in ["DOWNLOAD", "WARNING"]:
        setupInstances.downloaded_fileName = setupInstances.strCreatedBatchName + "_" + Date_Utils.get_currentDate_in_YYYMMDD().replace(
            "/", "_")


@then('checks if the Batch is deleted from the batch table')
def test_checks_if_the_Batch_is_deleted_from_the_batch_table(context):
    expect(context.dashboard_page.validate_batchDeleted(setupInstances.strCreatedBatchName) == False,
           "\nBatch not deleted successfully.\n")
    delayed_assert.assert_expectations()


@then('User clicks on the download input template button on the create batch tab')
def user_clicks_on_the_download_input_template_button_on_the_create_batch_tab(context):
    context.dashboard_page.click_downloadSample_templateBtn()
    setupInstances.downloaded_fileName = "dsg_sample.csv"


@then('checks if the file is downloaded successfully')
def test_checks_if_the_file_is_downloaded_successfully(context):
    expect(context.base_page.check_file_download(setupInstances.downloaded_fileName) == True,
           "\nFile not downloaded successfully. File Name [" + setupInstances.downloaded_fileName + "]\n")
    delayed_assert.assert_expectations()
