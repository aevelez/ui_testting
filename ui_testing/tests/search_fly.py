import time
import unittest

from ui_testing.tests.initialize_test import InitializeTest


class SearchFlyTest(unittest.TestCase):

    # Este método se ejecuta la primera vez para instanciar el navegador
    @classmethod
    def setUpClass(cls):
        cls.driver = InitializeTest.start_driver()