from configurations.setupConfig import *
from src.pages_AS import *
from src.pages_MP import *


def before_feature(context, feature):
    print("Before feature\n")


def before_scenario(context, scenario):
    print("\nScenario Name: " + scenario.name + "\n")

    """ Launch the App And Initializing Driver """
    context.driver = launchApp()

    """ Creating page objects for Multitenant Platform """
    context.base_page = BasePage(context)
    context.login_page = LoginPage(context.base_page)

    """ Creating page objects for Attribute Smart """
    context.dashboard_page = DashboardPage(context.base_page)
    context.explore_batch_page = ExploreBatchPage(context.base_page)


def after_scenario(context, scenario):
    if scenario.status == "failed":
        print("Scenario: " + scenario.name + " ----------------------------------------------------------FAILED\n")
        save_screenshots_on_failedScenarios(context.driver, scenario.name)
    elif scenario.status == "passed":
        print("Scenario: " + scenario.name + " ----------------------------------------------------------PASSED\n")
    context.driver.quit()


def after_feature(context, feature):
    print("\nAfter Feature")
