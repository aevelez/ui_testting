import time
import unittest
from selenium.webdriver.support.ui import Select

from ui_testing.tests.initialize_test import InitializeTest


class SearchFlyTest(unittest.TestCase):

    # Este método se ejecuta la primera vez para instanciar el navegador
    @classmethod
    def setUpClass(cls):
        cls.driver = InitializeTest.start_driver()

        # Este método recibe como parámetro el login y password y hace clic en el botin Sign - In

    def test_search(self):
        self.driver.find_element_by_xpath("//input[contains(@value,'oneway')]").click()
        select = Select(self.driver.find_element_by_name('passCount'))
        select.select_by_visible_text('1')
        select = Select(self.driver.find_element_by_name('fromPort'))
        select.select_by_visible_text('London')
        select = Select(self.driver.find_element_by_name('fromMonth'))
        select.select_by_visible_text('June')
        select = Select(self.driver.find_element_by_name('fromDay'))
        select.select_by_visible_text('15')
        select = Select(self.driver.find_element_by_name('toPort'))
        select.select_by_visible_text('Paris')
        select = Select(self.driver.find_element_by_name('toMonth'))
        select.select_by_visible_text('October')
        select = Select(self.driver.find_element_by_name('toDay'))
        select.select_by_visible_text('1')
        select = Select(self.driver.find_element_by_name('airline'))
        select.select_by_visible_text('Pangea Airlines')
        self.driver.find_element_by_name('findFlights').click()
        time.sleep(2)

    def test_image(self):
        image = self.driver.find_element_by_xpath("//img[contains(@src,'mast_selectflight.gif')]").is_displayed()
        self.assertTrue(image)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("prueba completada con éxito")

