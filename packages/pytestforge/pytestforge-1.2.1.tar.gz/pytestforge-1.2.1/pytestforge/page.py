import re
import time
import traceback
import allure
from selenium.webdriver.common.action_chains import ActionChains
from seleniumwrapper import SeleniumWrapper
from selenium.common.exceptions import WebDriverException, InvalidElementStateException
from selenium.webdriver.common.keys import Keys
from allure_commons.types import AttachmentType


class Page(SeleniumWrapper):
    def _move_to_element(self, xpath):
        """
        Shifts the focus to the necessary web element
        :param xpath: xpath of element
        """
        time.sleep(0.5)
        action = ActionChains(self.driver)
        element = self.xpath(xpath)
        action.move_to_element(element).perform()

    def scroll(self, x=0, y=500):
        self.scroll_by(x, y)

    def scroll_to_element(self, xpath):
        """
        Scrolls the page to the element
        :param xpath: xpath of element
        """
        element = self.xpath(xpath).unwrap
        x = int(element.location_once_scrolled_into_view['x'])
        y = int(element.location_once_scrolled_into_view['y'])
        self.scroll_to(x, y)

    @staticmethod
    def get_tag_number(element):
        """
        Gets the element number from the tag
        :param element:
        :return: number
        """
        reg = re.compile(r'(\d+)')
        num = int(re.search(reg, element).group())
        return num

    def clear_xpath(self, xpath):
        """
        Trying to clear the input form
        :param xpath: xpath of form
        """
        try:
            self.xpath(xpath).clear()
        except InvalidElementStateException:
            pass

    def is_xpath_present(self, xpath, eager=False, timeout=1):
        """
        Checks whether the specified element exists
        :param xpath: xpath of element
        :param eager:
        :param timeout: waiting
        :return: elements
        """
        self.silent = True
        elements = self.xpath(xpath, eager=eager, timeout=timeout)
        self.silent = False
        if elements:
            return elements
        return []

    def clear_backspace(self, xpath, count=20):
        """
        Deletes the contents of the inputs using Backspace
        :param xpath: xpath of forme
        :param count: count of backspaces
        """
        for _ in range(count):
            self.xpath(xpath).send_keys(Keys.BACKSPACE)

    def is_exists(self, xpath, eager=False):
        try:
            if eager:
                if self.xpath(xpath, eager=eager, timeout=1).size:
                    return True
                else:
                    return False
            else:
                return self.xpath(xpath, timeout=1).is_displayed()
        except WebDriverException:
            return False

    def make_screen(self, screen_name='screenshot'):
        """
        Attach screenshot to allure report
        :param screen_name: name of screen in report
        """
        try:
            screen = self.get_screenshot_as_png()
            allure.attach(screen, screen_name, attachment_type=AttachmentType.PNG)
        except WebDriverException:
            print(traceback.format_exc())

    def send_keys(self, xpath, text):
        self.xpath(xpath).clear()
        self.xpath(xpath).clear()
        self.xpath(xpath).send_keys(text)

    def slow_send_keys(self, xpath, keys):
        for k in keys:
            self.xpath(xpath).send_keys(k)
            time.sleep(0.2)


class NotFound(Exception):
    pass
