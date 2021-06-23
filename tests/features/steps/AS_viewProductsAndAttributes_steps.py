from behave import *
from delayed_assert import delayed_assert, expect

from tests.instances import setupInstances
from utilities import Date_Utils


@then('User creates a batch and uploads a csv with "{txt}" and products assigned to it')
def test_User_creates_a_batch_and_uploads_a_csv_with_images_and_products_assigned_to_it(context, txt):
    lstMapTestData = dict(context.table)
    setupInstances.strFileName = lstMapTestData.get("CSV to upload")
    context.dashboard_page.clickUploadBtn()
    setupInstances.strCreatedBatchName = context.dashboard_page.create_batch_by_uploadingCSV("Enter Batch Name",
                                                                                             "toViewProductAndAttributes\\" + setupInstances.strFileName)
    expt_createdBatch_txt = setupInstances.strCreatedBatchName + " - Created On: " + Date_Utils.get_currentDate_in_MMDDYYY()
    context.base_page.wait_in_seconds(5)
    act_createdBatch_txt = context.dashboard_page.validate_batchCreated(setupInstances.strCreatedBatchName)
    expect(act_createdBatch_txt == expt_createdBatch_txt,
           "\n Batch name and created date incorrect : [Result: " + act_createdBatch_txt + " ]\n")
    context.dashboard_page.clickDashBoardRefreshBtn(75)
    context.dashboard_page.clickDashBoardRefreshBtn(75)
    context.dashboard_page.clickDashBoardRefreshBtn(75)
    context.base_page.wait_in_seconds(10)
    for colName in lstMapTestData:
        if colName not in ["CSV to upload", "Num of images uploaded", "Num of broken urls"]:
            expt_Text = lstMapTestData.get(colName)
            act_Text = context.dashboard_page.validate_batchTbl_data(colName, setupInstances.strCreatedBatchName)
            expect(act_Text == expt_Text, "\n Data not as expected for the Column : [ " + colName + " ]\n")
    delayed_assert.assert_expectations()


@when('User clicks on the batch which was created')
def User_clicks_on_the_batch_which_was_created(context):
    context.dashboard_page.clickOn_createdBatch(setupInstances.strCreatedBatchName)


@when('User lands on the Explore Batch Page')
def test_User_lands_on_the_Explore_Batch_Page(context):
    expt_Text = "Explore: " + setupInstances.strCreatedBatchName
    act_Text = context.explore_batch_page.get_exploreBatchName()
    expect(act_Text == expt_Text, "\n User not landed on explore batch page. Actual Text : [ " + act_Text + " ]\n")
    delayed_assert.assert_expectations()


@then('User clicks on Export button on the Explore Batch Page')
def User_clicks_on_Export_button_on_the_Explore_Batch_Page(context):
    context.explore_batch_page.clickOnExportBtn()
    setupInstances.downloaded_fileName = setupInstances.strCreatedBatchName + "_" + Date_Utils.get_currentDate_in_YYYMMDD().replace(
        "/", "_")


@then('User checks if the L1 categories are created as per the csv which was uploaded')
def test_User_checks_if_the_L1_categories_are_created_as_per_the_csv_which_was_uploaded(context):
    boolResult = context.explore_batch_page.validate_l1Category_isCreated(
        "toViewProductAndAttributes\\" + setupInstances.strFileName)
    expect(boolResult == True,
           "\n L1 categories not displayed as expected in the explore batch page as per the csv which was uploaded\n")
    delayed_assert.assert_expectations()


@then('User checks if the L2 categories are created under the respective L1\'s as per the csv which was uploaded')
def test_User_checks_if_the_L2_categories_are_created_under_the_respective_L1s_as_per_the_csv_which_was_uploaded(
        context):
    boolResult = context.explore_batch_page.validate_l2Category_createdUnder_l1Category(
        "toViewProductAndAttributes\\" + setupInstances.strFileName)
    expect(boolResult == True,
           "\n L2 categories are not created under the respective L1\'s as expected in the explore batch page as per the csv which was uploaded\n")
    delayed_assert.assert_expectations()
