__author__ = 'trepository'


def print_func(par):
    print("Hello : ", par)
    return


def on(page_class):
    if page_class in globals().keys():
        print("in if loop")
        page = globals()[page_class]()
    else:
        print("Page Object:" + page_class + " does not exist")
    return page
