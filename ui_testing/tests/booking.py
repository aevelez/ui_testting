import unittest

from ui_testing.tests.initialize_test import InitializeTest
from selenium.webdriver.support.ui import Select


class BookingFlyTest(unittest.TestCase):

    # Este método se ejecuta la primera vez para instanciar el navegador
    @classmethod
    def setUpClass(cls):
        cls.driver = InitializeTest.start_driver()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("prueba completada con éxito")

    def fillPersonalInformation(self):
        self.driver.find_element_by_name('passFirst0').send_keys('Estudiante')
        self.driver.find_element_by_name('passLast0').send_keys('Eafit')

    def fillCreditCard(self):
        self.driver.find_element_by_name('creditnumber').send_keys('123456789')
        self.driver.find_element_by_name('cc_frst_name').send_keys('Estudiante')
        self.driver.find_element_by_name('cc_last_name').send_keys('Eafit')

    def fillBillingAddress(self):
        self.driver.find_element_by_name('billAddress1').clear()
        self.driver.find_element_by_name('billAddress1').send_keys('108 MAIN ST')
        self.driver.find_element_by_name('billCity').clear()
        self.driver.find_element_by_name('billState').clear()
        self.driver.find_element_by_name('billCity').send_keys('Medellin')
        self.driver.find_element_by_name('billState').send_keys('Antioquia')
        select = Select(self.driver.find_element_by_name('billCountry'))
        select.select_by_visible_text('COLOMBIA')

    def fillDeliveryAddress(self):
        self.driver.find_element_by_name('delAddress1').clear()
        self.driver.find_element_by_name('delAddress1').send_keys('200 MAIN ST')
        self.driver.find_element_by_name('delCity').clear()
        self.driver.find_element_by_name('delState').clear()
        self.driver.find_element_by_name('delCity').send_keys('Medellin')
        self.driver.find_element_by_name('delState').send_keys('Antioquia')


    def purchaseFly(self):
        self.driver.find_element_by_name('buyFlights').click()

    def test_image(self):
        image = self.driver.find_element_by_xpath("//img[contains(@src,'mast_confirmation.gif')]").is_displayed()
        self.assertTrue(image)


