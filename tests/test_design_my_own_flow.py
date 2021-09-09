import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import os
import time

class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""
    def __init__(self, driver):
        self.driver = driver

class StandingDesksPage(BasePage):
    """Home page action methods come here. I.e. Python.org"""
    def click_jarvish_bamboo_standing_desk(self):
        """Triggers the search"""
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '#product-item-info_233 a')))
        jarvish_bamboo_standing_desk_link = self.driver.find_element_by_css_selector('#product-item-info_233 a')
        jarvish_bamboo_standing_desk_link.click()

class ProductPage(BasePage):
    STICKY_ACTION_SELECTOR = '.sticky-travel-bar-container a.action'
    MAIN_BODY_ACTION = '.product-add-form a.action.primary.toconfigurator'

    def click_sticky_primary_action(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, self.STICKY_ACTION_SELECTOR)))
        design_my_own_button = self.driver.find_element_by_css_selector(self.STICKY_ACTION_SELECTOR)
        design_my_own_button.click()

    def click_body_primary_action(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, self.MAIN_BODY_ACTION)))

        self.driver.execute_script("window.scrollTo(0, 100)")
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, self.MAIN_BODY_ACTION)))

        self.driver.find_element_by_css_selector(self.MAIN_BODY_ACTION).click()



class DesignPage(BasePage):
    ADD_TO_CART_SELECTOR = '.fixed-bottom .conf-addtocart--addtocart-button button.btn.btn-primary'

    def is_add_to_cart_visible(self):
        WebDriverWait(self.driver, 10).until(
        expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, self.ADD_TO_CART_SELECTOR)))
        return self.driver.find_element_by_css_selector(self.ADD_TO_CART_SELECTOR).is_displayed()
        #time.sleep(2)
        #return displayed

class BasicTests(unittest.TestCase):
    def setUp(self):
        chromedriver_path = os.environ['USERPROFILE'] + "\\SeleniumWebDrivers\\chromedriver.exe"
        caps = DesiredCapabilities().CHROME
        caps["pageLoadStrategy"] = "none"  # Do not wait for full page load
        self.chrome = webdriver.Chrome(desired_capabilities=caps, executable_path=chromedriver_path)
        self.chrome.implicitly_wait(10)

    def tearDown(self):
        self.chrome.close()

    def test_complete_your_setup_stick_button_flow(self):
        self.chrome.get("https://www.fully.com/standing-desks.html")
        StandingDesksPage(self.chrome).click_jarvish_bamboo_standing_desk()
        ProductPage(self.chrome).click_sticky_primary_action()
        assert not DesignPage(self.chrome).is_add_to_cart_visible(), "Make sure add to cart is not visible"

    def test_complete_your_setup_primary_button_flow(self):
        self.chrome.get("https://www.fully.com/standing-desks.html")
        StandingDesksPage(self.chrome).click_jarvish_bamboo_standing_desk()
        ProductPage(self.chrome).click_body_primary_action()
        assert not DesignPage(self.chrome).is_add_to_cart_visible(), "Make sure add to cart is not visible"

