import time
import unittest

from ui_testing.tests.initialize_test import InitializeTest


class LoginTest(unittest.TestCase):
    # Este método se ejecuta la primera vez para instanciar el navegador
    @classmethod
    def setUpClass(cls):
        cls.driver = InitializeTest.start_driver()

    # Este método recibe como parámetro la URL del sitio
    def test_go_url(self, url):
        self.driver.get(url)

    # Este método recibe como parámetro el login y password y hace clic en el botin Sign - In
    def test_login(self, user, password):
        self.driver.find_element_by_name("userName").send_keys(user)
        self.driver.find_element_by_name("password").send_keys(password)
        self.driver.find_element_by_name("login").click()





def test_image(self):
    image =self.driver.find_element_by_xpath("//img[contains(@src,'mast_flightfinder.gif')]").is_displayed()
    self.assertTrue(image)

# Este método se ejecuta al final y cierra el navegador
@ classmethod
def tearDownClass(cls):
    cls.driver.quit()
    print("prueba completada con éxito")
