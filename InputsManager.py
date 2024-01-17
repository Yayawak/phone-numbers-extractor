from selenium.webdriver.remote.webdriver import WebDriver
import time
from selenium.webdriver.common.by import By

class InputsManager:
    def __init__(self, driver:WebDriver):
        self.driver = driver
    
    def retriveInputs(self):
        inputs = self.driver.find_elements(By.TAG_NAME, "input")
        self.digit_inputs = []
        name_inputs = ["num" + str(i) for i in range(1, 10)]
        for ip in inputs:
            # if 
            if ip.get_property("name") in name_inputs:
                self.digit_inputs += [ip]


    # def browseFirst2Digits(self, first:int, second:int) -> None:
    # def browseFirstNDigits(self, nointList:list, n:int) -> None:
    def browseFirstNDigits(self, nointList:list) -> None:
        # print('first & second -> ' ,first, ":", second)
        no_len = len(nointList)
        # print("no len = " , no_len)
        assert no_len > 0 and no_len < 10
        try:
            # clear inputs (otherwise we would supply false input to 9 digits)
            for i in range(len(self.digit_inputs)):
                # self.digit_inputs[i].send_keys("")
                self.digit_inputs[i].clear()
            for i in range(no_len):
                s = str( nointList[i] )
                self.digit_inputs[i].send_keys(s)

            
            self.sumbit_btn = self.driver.find_element(By.ID, "btn-newsim-search")
            self.sumbit_btn.click()
            # self.driver.implicitly_wait(10)
            # time.sleep(5)
            # time.sleep(2)
            time.sleep(1)
            self.retriveInputs()
            # self.driver.timeouts.implicit_wait
            # print("ready to see no.")
        except Exception as e:
            print("Error about selenium driver.", e)
            # self.driver.close()
    