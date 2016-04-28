from methods import AbstractTest
from conf_ui import *


class Wiki(AbstractTest):
    def setUp(self):
        super(Wiki, self).setUp()

    def tearDown(self):
        super(Wiki, self).tearDown()

    def open_url(self, url):
        self.driver.get(url)

    def wiki_home(self):
        self.search_field = self.wait_until_find_by_id(search_input_field_id)

    def search_titile_page(self):
        self.title_name = self.wait_until_find_by_id(title_id).text.lower()


class Tesla(AbstractTest):
    def setUp(self):
        super(Tesla, self).setUp()

    def tearDown(self):
        super(Tesla, self).tearDown()

    def open_url(self, url):
        self.driver.get(url)

    def schedule_test_drive(self):
        self.schedule = self.wait_until_find_by_css(schedule_test_drive_css)

    def fill_data(self):
        self.first_name = self.wait_until_find_by_id(first_name_id)
        self.last_name = self.wait_until_find_by_id(last_name_id)
        self.email = self.wait_until_find_by_id(email_id)
        self.phone = self.wait_until_find_by_id(phone_id)
        self.zip = self.wait_until_find_by_id(zip_id)
        self.next_btn = self.wait_until_find_by_id(next_btn_id)

    def success(self):
        self.success_msg = self.wait_until_find_by_css(success_css)