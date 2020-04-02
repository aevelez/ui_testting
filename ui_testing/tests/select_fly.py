import time
import unittest

from ui_testing.tests.initialize_test import InitializeTest

class SelectFlyTest(unittest.TestCase):

    # Este método se ejecuta la primera vez para instanciar el navegador
    @classmethod
    def setUpClass(cls):
        cls.driver = InitializeTest.start_driver()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("prueba completada con éxito")

    def select_fly_test(self):
        self.driver.find_element_by_name('reserveFlights').click()

    def test_image(self):
        image = self.driver.find_element_by_xpath("//img[contains(@src,'mast_book.gif')]").is_displayed()
        self.assertTrue(image)