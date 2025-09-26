from faker import Faker
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import random

# we need some application that give one thing that help us to do some thing

# firstly u want to fill forms with a lote of data


# and a method that we can go directly to some page -> and if have some login page u can pass your password and username.
fake = Faker()


class Application():

    driver = None
    webdriverWaiter = None
    credencials = {}

    def __init__(self):
        pass

    @staticmethod
    def Give_Fake_Data_toInput(type_input: str, setMadedata: dict = {}):
        it = type_input.lower()

        if "mail" in it:
            return fake.email()
        if it in ("tel", "phone"):
            return fake.phone_number()
        if it in ("number", "range"):
            return str(random.randint(0, 100))
        if "date" in it:
            return fake.date().isoformat()
        return fake.sentence(nb_words=3)

    @staticmethod
    def Chrome_options():
        return webdriver.ChromeOptions()

    def Start_Driver(self, navagator="chrome", options=webdriver.ChromeOptions()):

        if navagator == "chrome":
            self.driver = webdriver.Chrome(service=Service(
                ChromeDriverManager().install()), options=options)

    def webdriver_wait(self, seconds=10):
        self.webdriverWaiter = WebDriverWait(self.driver, seconds)

    def Delimite_Container(self):
        # can be by idname or classname and section
        return self.webdriverWaiter.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.op--task-view-sections")))

    def setCredencials(self, credencials={}):
        self.credencials = credencials

    def findThisTypesInputs(self, lista: list):

        command = []
        for i in lista:
            command.append(f"input[type='{i}']")
        command = ", ".join(command)
        print(command)

        # self.driver.find_elements(By.CSS_SELECTOR, command)

    def Find_somekindOF(self):
        pass

    def performLogin(self, login_url: str):

        self.driver.get(login_url)

        try:
            self.webdriver_wait()
            self.webdriverWaiter.until(
                EC.presence_of_element_located((By.TAG_NAME, "input")))
        except:
            pass


# Appplication
