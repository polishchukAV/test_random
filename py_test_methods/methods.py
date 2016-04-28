import random
import string
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

UPPER_BOUND_WAIT_TIME = 20 * 60
sleep_until_wait_for_changing_status = 20


class AbstractTest(object):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.start_client()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def tearQuit(self):
        self.driver.quit()
        self.driver.stop_client()

    def tearDown(self):
        self.driver.close()

    def wait_until_find(self, method, selector, timeout, driver):
        if driver is None:
            driver = self.driver
        return WebDriverWait(driver, timeout).until(
            lambda driver: getattr(driver, method)(selector)
        )

    def wait_until_find_by_xpath(self, xpath, timeout=25, driver=None):
        return self.wait_until_find(method="find_element_by_xpath",
                                    selector=xpath, timeout=timeout,
                                    driver=driver)

    def wait_until_find_by_xpath_list(self, xpath, timeout=25, driver=None):
        return self.wait_until_find(method="find_elements_by_xpath",
                                    selector=xpath, timeout=timeout,
                                    driver=driver)

    def wait_until_find_by_name(self, name, timeout=25, driver=None):
        return self.wait_until_find(method="find_element_by_name",
                                    selector=name, timeout=timeout,
                                    driver=driver)

    def wait_until_find_by_id(self, id_element, timeout=25, driver=None):
        return self.wait_until_find(method="find_element_by_id",
                                    selector=id_element, timeout=timeout,
                                    driver=driver)

    def wait_until_find_by_link_text(self, link_text, timeout=25, driver=None):
        return self.wait_until_find(method="find_element_by_link_text",
                                    selector=link_text, timeout=timeout,
                                    driver=driver)

    def wait_until_find_by_css(self, css_path, timeout=25, driver=None):
        return self.wait_until_find(method="find_element_by_css_selector",
                                    selector=css_path, timeout=timeout,
                                    driver=driver)

    def wait_until_find_by_css_list(self, css_path, timeout=25, driver=None):
        return self.wait_until_find(method="find_elements_by_css_selector",
                                    selector=css_path, timeout=timeout,
                                    driver=driver)

    def wait_until_find_by_class(self, class_name, timeout=25, driver=None):
        return self.wait_until_find(method="find_element_by_class_name",
                                    selector=class_name, timeout=timeout,
                                    driver=driver)

    def wait_until_find_by(self, selector, by_what, timeout=25, driver=None):
        if driver is None:
            driver = self.driver
        return WebDriverWait(driver, timeout).until(
            lambda driver: driver.find_elements(by_what, selector)
        )

    def random_string(self, length):
        return ''.join(random.choice(string.ascii_lowercase)
                       for _ in range(length))

    def random_integer(self, length):
        return ''.join(random.choice(string.digits)
                       for _ in range(length))

    def isEnabled_ID(self, locator):
        return self.driver.find_element_by_id(locator).is_enabled()
