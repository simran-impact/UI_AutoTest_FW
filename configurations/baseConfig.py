import os

"""URL's"""
BASE_URL = "https://dsg-dot-dev-dot-multi-tenant-markdown.uc.r.appspot.com/login"
AS_BASE_URL = "https://dsg-dot-asqa-dot-multi-tenant-markdown.uc.r.appspot.com/"
# AS_BASE_URL = "https://dsg-dot-as5-dot-multi-tenant-markdown.uc.r.appspot.com/"
MTP_BASE_URL = "https://dsg-dot-mp5-dot-multi-tenant-markdown.uc.r.appspot.com/login"

"""USER CREDENTIALS"""
USER_EMAIL = "autoUItest.MTP@impact.com"
USER_PWD = "AutoUiTest123"
# USER_EMAIL = "test_terrance@impactanalytics.co"
# AS_USEREMAIL = "test_teranc@impactanalytics.co"
# USER_PWD = "terrance@123"

"""FOLDER/FILE PATHS"""
PROJ_FOLDER_PATH = os.path.dirname(os.path.abspath("UI_AutoTest_FW"))
FILES2UPLOAD_FLD_PATH = PROJ_FOLDER_PATH + "\\resources\\filesToUpload\\"
DOWNLOADEDFILES_FLD_PATH = PROJ_FOLDER_PATH + "\\resources\\downloadedFiles\\"
EXTRACTEDDATAFILES_FLD_PATH = PROJ_FOLDER_PATH + "\\resources\\extractedDataFiles\\"
FAILED_SCENARIO_SCREENSHOT_FLD = PROJ_FOLDER_PATH + "\\reports\\screenshots\\failed_scenarios_screenshots"

CHROME_DRIVER_PATH = PROJ_FOLDER_PATH + "\\resources\\drivers\\chromedriver_win32\\chromedriver.exe"
FIREFOX_DRIVER_PATH = PROJ_FOLDER_PATH + "\\resources\\drivers\\geckodriver_win32\\geckodriver.exe"

"""RunTime Configurations"""
BROWSER = ""
RUN_FOR = "AS"  ## MTP, AS
