from selenium import webdriver


class InitializeTest:
    driver = None

    # Este método se ejecuta la primera vez para instanciar el navegador
    @classmethod
    def start_driver(cls):
        if cls.driver is None:
            cls.driver = webdriver.Chrome(executable_path="C:\\Users\\avelez\\PycharmProjects\\UITest\\ui_testing\\drivers\\chromedriver.exe")
            cls.driver.maximize_window()
        return cls.driver
