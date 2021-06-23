from datetime import *


def get_currentDate_in_DDMMYYYY():
    currentDate = date.today().strftime("%d/%m/%Y")
    return currentDate


def get_currentDate_in_MMDDYYY():
    currentDate = date.today().strftime("%m/%d/%Y")
    return currentDate


def get_currentDate_in_Textual():
    currentDate = date.today().strftime("%B %d, %Y")
    return currentDate


def get_currentDate_in_DDMMYY():
    currentDate = date.today().strftime("%m/%d/%y")
    return currentDate


def get_currentDate_in_DDDMMYYYY():
    currentDate = date.today().strftime("%b-%d-%Y")
    return currentDate


def get_current_date_time():
    current_date_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    return current_date_time


def get_currentDate_in_YYYMMDD():
    currentDate = date.today().strftime("%Y/%m/%d")
    return currentDate
