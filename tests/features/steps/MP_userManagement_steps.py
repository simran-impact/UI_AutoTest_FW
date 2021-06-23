from behave import *

from configurations.baseConfig import *
from tests.instances import setupInstances
from utilities.Driver_Utils import Driver_Utils


@given('User is on Mark Smart login page')
def user_is_on_mark_smart_login_page(context):
    expt_title = "React App"
    act_title = context.base_page.get_loginPage_title(expt_title)
    if act_title == expt_title:
        assert True
    else:
        print("\n[ " + expt_title + " ]----- title not displayed\n")
        print("\n Expected: [ " + expt_title + " ], but found [ " + act_title + " ]\n")
        assert False


@when('User wants to log in')
def user_wants_to_log_in(context):
    print("User wants to log in")


@given('User logs into the application')
def user_logs_into_the_application(context):
    context.login_page.enter_username_and_password(USER_EMAIL, USER_PWD)
    context.login_page.clickSignIn()


@when('User clicks on "{application}" button in IA Smart Platform application page')
def user_clicks_on_app_button_in_IA_Smart_Platform_application_page(context, application):
    strAppName = application
    # context.login_page.clickOn_application_btn(strAppName)


@when('Enters email and password')
def enters_email_and_password(context):
    context.login_page.enter_username_and_password(USER_EMAIL, USER_PWD)


@then('Clicks on Sign in button')
def clicks_on_signIn_button(context):
    context.login_page.clickSignIn()


@then('Is directed to the IA Smart Platform Page of the application')
def is_directed_to_the_IA_Smart_Platform_Page_of_the_application(context):
    assert context.base_page.aiSmartPlatformHeader_isDisplayed(), \
        "\nLogin Failure: IA Smart Platform not displayed\n "


@when('User enters only the email which is valid and forgets the password')
def user_enters_only_the_email_which_is_valid_and_forgets_the_password(context):
    context.login_page.enter_username_and_password(USER_EMAIL, "")


@when('User enters only the email which is invalid and forgets the password')
def user_enters_only_the_email_which_is_invalid_and_forgets_the_password(context):
    context.login_page.enter_username_and_password(Driver_Utils.random_email(), "")


@then('User clicks on Forgot your password link and sends verification email')
def user_clicks_on_Forgot_your_password_link_and_sends_verification_email(context):
    context.login_page.clickForgotPassword()


@when('Enters invalid email and password')
def enters_invalid_email_and_password(context):
    context.login_page.enter_username_and_password(Driver_Utils.random_email(), Driver_Utils.random_string())


@then('User validates if "{msg}" error message pops up ')
def user_validates_if_error_message_pops_up(context, msg):
    expt_text = msg
    act_text = context.base_page.get_displayed_error_msg()
    if act_text == expt_text:
        print("[ " + expt_text + " ]: Error message is displayed.")
        assert True
    else:
        print("\n Expected: [ " + expt_text + " ], but found [ " + act_text + " ]\n")
        assert False


@then('User validates if "{msg}" error message pops up in upload tab')
def user_validates_if_error_message_pops_up_in_uploadTab(context, msg):
    expt_text = msg.replace(": ", "")
    act_text = context.base_page.get_displayed_tab_error_msg()
    if act_text == expt_text:
        print("[ " + expt_text + " ]: Error message is displayed.")
        assert True
    else:
        print("\n Expected: [ " + expt_text + " ], but found [ " + act_text + " ]\n")
        assert False


@then('User validates if "{msg}" success message pops up')
def success_Message_popUp(context, msg):
    if "<Batch Name>" in msg:
        expt_text = msg.replace("<Batch Name>", setupInstances.strCreatedBatchName)
    else:
        expt_text = msg
    act_text = context.base_page.get_displayed_success_msg()
    if act_text == expt_text:
        print("[ " + expt_text + " ]: Success message is displayed.")
        assert True
    else:
        print("\n Expected: [ " + expt_text + " ], but found [ " + act_text + " ]\n")
        assert False


@then('User validates if "{msg}" success message pops up on upload tab')
def success_msg_on_uploadTab(context, msg):
    if "<Batch Name>" in msg:
        expt_text = msg.replace("<Batch Name>", setupInstances.strCreatedBatchName)
    else:
        expt_text = msg.replace(": ", "")
    act_text = context.base_page.get_displayed_tab_success_msg()
    if act_text == expt_text:
        print("[ " + expt_text + " ]: Success message is displayed.")
        assert True
    else:
        print("\n Expected: [ " + expt_text + " ], but found [ " + act_text + " ]\n")
        assert False


@when('User does not enter the email and password')
def user_does_not_enter_the_email_and_password(context):
    context.login_page.enter_username_and_password("", "")


@then('User checks that the Sign in Button is disabled')
def user_checks_that_the_Sign_in_Button_is_disabled(context):
    bool_result = context.base_page.check_button_enabled_or_disabled(context.login_page.wb_btn_signIn_id)
    if bool_result is False:
        assert True
    else:
        print("\nSign in button is not disabled\n")
        assert False


@then('checks that the Sign in Button is enabled')
def checks_that_the_Sign_in_Button_is_enabled(context):
    bool_result = context.base_page.check_button_enabled_or_disabled(context.login_page.wb_btn_signIn_id)
    if bool_result is True:
        assert True
    else:
        print("\nSign in button is not enabled\n")
        assert False


@then('User checks that the forgot your password link is disabled')
def step_impl(context):
    bool_result = context.base_page.check_button_enabled_or_disabled(context.login_page.wb_btn_forgotPwd_id)
    if bool_result is False:
        assert True
    else:
        print("\nForgot your password link is not disabled\n")
        assert False


@then('User checks that the forgot your password link is enabled')
def step_impl(context):
    bool_result = context.base_page.check_button_enabled_or_disabled(context.login_page.wb_btn_forgotPwd_id)
    if bool_result is True:
        assert True
    else:
        print("\nForgot your password link is not enabled\n")
        assert False


""""@given('User checks the table')
def step_impl(context):
    lstMapTestData = dict(context.table)
    print(lstMapTestData)
    print(lstMapTestData.keys())
    print(lstMapTestData.values())
    print(lstMapTestData.get("UserName"))
    for x in lstMapTestData:
        print(x)
    for x in lstMapTestData.values():
        print(x)
    for x,y in lstMapTestData.items():
        print(x, y)"""
