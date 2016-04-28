import time
from selenium.webdriver.common.keys import Keys

from py_test_methods.conf_ui import *
from py_test_methods.pages import Wiki, Tesla


def test_search_in_wiki():
    wiki = Wiki()
    wiki.setUp()
    wiki.open_url(wiki_url)
    wiki.wiki_home()
    wiki.search_field.send_keys(wikipedia_text)
    wiki.search_field.send_keys(Keys.ENTER)
    wiki.search_titile_page()
    try:
        assert wiki.title_name == wikipedia_text
        wiki.tearQuit()
    except:
        wiki.tearQuit()
        assert False


def test_test_drive():
    tesla = Tesla()
    tesla.setUp()
    tesla.open_url(tesla_motors)
    tesla.schedule_test_drive()
    tesla.schedule.click()
    tesla.fill_data()
    name = tesla.random_string(7)
    try:
        tesla.first_name.send_keys(name)
        tesla.last_name.send_keys(name)
        tesla.email.send_keys(test_email)
        tesla.phone.send_keys(test_phone)
        tesla.zip.send_keys(test_zip)
        tesla.next_btn.click()
        tesla.success()
        while not tesla.success_msg.is_displayed():
            time.sleep(5)
            tesla.success_msg = tesla.wait_until_find_by_css(success_css)
        assert tesla.success_msg.text == success_text
        tesla.tearQuit()
    except:
        tesla.tearQuit()
        assert False