import os
import shutil
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from configurations import baseConfig

"""WebDriver Configurations"""
chromeOptions = Options()
chromeOptions.add_experimental_option("prefs", {"download.default_directory": baseConfig.DOWNLOADEDFILES_FLD_PATH})


def initWebBrowserDriver(strBrowserName):
    """ Initializing Driver """
    if strBrowserName == "":
        driver = webdriver.Chrome(executable_path=baseConfig.CHROME_DRIVER_PATH, chrome_options=chromeOptions)
    elif strBrowserName == "Chrome":
        driver = webdriver.Chrome(executable_path=baseConfig.CHROME_DRIVER_PATH, chrome_options=chromeOptions)
    elif strBrowserName == "Firefox":
        driver = webdriver.Firefox(baseConfig.FIREFOX_DRIVER_PATH)
    driver.implicitly_wait(10)
    return driver


def navigateToApp(driver, strAppUrl):
    """ To maximize, set timeouts, delete cookies from browser and launch the App Url """
    driver.maximize_window()
    driver.delete_all_cookies()
    driver.get(strAppUrl)
    time.sleep(5)


def launchApp():
    """ Deleting and Creating Folders """
    delete_recreating_Folders()
    """ Initializing Driver """
    driver = initWebBrowserDriver(baseConfig.BROWSER)
    """ Launch Application Based on the Config Passed """
    if baseConfig.RUN_FOR == "":
        navigateToApp(driver, baseConfig.BASE_URL)
    elif baseConfig.RUN_FOR == "AS":
        navigateToApp(driver, baseConfig.AS_BASE_URL)
    elif baseConfig.RUN_FOR == "MTP":
        navigateToApp(driver, baseConfig.MTP_BASE_URL)
    return driver


def delete_recreating_Folders():
    """ Deleting and Creating a Files Download Folder """
    if not os.path.exists(baseConfig.DOWNLOADEDFILES_FLD_PATH):
        os.makedirs(baseConfig.DOWNLOADEDFILES_FLD_PATH)
    else:
        shutil.rmtree(baseConfig.DOWNLOADEDFILES_FLD_PATH)
        os.makedirs(baseConfig.DOWNLOADEDFILES_FLD_PATH)
    """ Deleting and Creating a Extracted Data Folder """
    if not os.path.exists(baseConfig.EXTRACTEDDATAFILES_FLD_PATH):
        os.makedirs(baseConfig.EXTRACTEDDATAFILES_FLD_PATH)
    else:
        shutil.rmtree(baseConfig.EXTRACTEDDATAFILES_FLD_PATH)
        os.makedirs(baseConfig.EXTRACTEDDATAFILES_FLD_PATH)


def save_screenshots_on_failedScenarios(driver, strScenarioName):
    """ Folder for failed scenario screenshots | Save screenshots on failed scenarios """
    if not os.path.exists(baseConfig.FAILED_SCENARIO_SCREENSHOT_FLD):
        os.makedirs(baseConfig.FAILED_SCENARIO_SCREENSHOT_FLD)
    if not os.path.isfile(baseConfig.FAILED_SCENARIO_SCREENSHOT_FLD + "\\" + strScenarioName + "_failed.png"):
        driver.save_screenshot(baseConfig.FAILED_SCENARIO_SCREENSHOT_FLD + "\\" + strScenarioName + "_failed.png")
    else:
        os.remove(baseConfig.FAILED_SCENARIO_SCREENSHOT_FLD + "\\" + strScenarioName + "_failed.png")
        driver.save_screenshot(baseConfig.FAILED_SCENARIO_SCREENSHOT_FLD + "\\" + strScenarioName + "_failed.png")
