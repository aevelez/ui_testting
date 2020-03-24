import time
import unittest

from selenium import webdriver

from ui_testing.tests.initialize_test import InitializeTest
from ui_testing.tests.login import LoginTest


class LogoutTest(unittest.TestCase):

    # Este método se ejecuta la primera vez para instanciar el navegador
    @classmethod
    def setUpClass(cls):
        cls.driver = InitializeTest.start_driver()

    # Este método hace clic en el botón SIGN-OFF
    def test_singoff(self):
        self.driver.find_element_by_link_text("SIGN-OFF").click()
        time.sleep(2)

    # Este método busca la imagen sing ON
    def test_logout(self):
        image = self.driver.find_element_by_xpath("//img[contains(@src,'mast_signon.gif')]").is_displayed()
        self.assertTrue(image)

    def tearDownClass(cls):
        cls.driver.quit()
        print("prueba completada con éxito")