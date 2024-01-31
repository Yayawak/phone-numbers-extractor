from selenium.webdriver.remote.webdriver import WebDriver
from typing import Type, List, Dict, Tuple
import re
from selenium.webdriver.common.by import By
from Utils import condense, no_list_to_str
import time
import random
import pyautogui as pag
import pyautogui
import threading

# 0.5 * 0.5, 0.45
# 0.75, 0.45

class Nexter:
    numbers = []
    
    def __init__(self, driver:WebDriver):
        self.driver = driver
        self.current_page_acitve_index = self.get_current_page_acitve_index()

    def _test_sequences(self):
        # A = self.get_all_numbers_in_page()
        # # print("A = ", A)
        # self.go_next_page()
        
        # B = self.get_all_numbers_in_page()
        # print("B = ", B)
        # self.go_next_page()
        # time.sleep(1)
        
        # ret.extend(A)
        # ret.extend(B)
        ...


    def get_all_numbers(self):
        # ...
        ret = []


    
        # while self.can_go_next_page():
        #     sub_list = self.get_all_numbers_in_page()
        #     self.go_next_page()
            
        #     ret.extend(sub_list)
        while True:
            sub_list = self.get_all_numbers_in_page()
            if self.can_go_next_page():
                self.go_next_page()
            else:
                ret.extend(sub_list)
                break
            ret.extend(sub_list)
            print(ret)

        
        return ret
        
            
        

    
    # def get_all_numbers_in_page(self) -> List[Tuple[int]]:
    def get_all_numbers_in_page(self) -> List[List[int]]:
        numbers = []
        
        xs = self.driver.find_elements(By.CLASS_NAME, "step3-box-detail_num")
        # print(len(xs))
        # get only digits
        rx = "[0-9]+"
        for div in xs:
            # print(div.text)
            m = re.findall(rx, div.text)
            num_list = condense(m)
            # print("number founded is ", no_list_to_str(num_list))
            numbers.append(num_list)
        return numbers

    # def can_go_next_page(self) -> bool:
    def _can_go_next_page(self) -> bool:
        # self.next_btn = self.driver.find_element(By.CLASS_NAME, "page-btn-next")
        # if self.next_btn is not None:
        #     return True
        # else:
        #     return False
        try:
            self.next_btn = self.driver.find_element(By.CLASS_NAME, "page-btn-next")
            return True
        except:
            print("element page-btn-next not found")
            print("END OF SCRAPPING ALL NUMBERS.")
            print("\n\n\n")
            return False

    def get_current_page_acitve_index(self):
        try:
            current_page_index = self.driver.find_element(By.XPATH, "//a[@class='page active']")
            # print(current_page_index.text)
            return int(current_page_index.text)
        except:
            return -1

    def autoclick_afew_times_thread_func(name):
        # print("thread {} started for autoclicking".format())
        print("thread started for autoclicking")
        for i in range(9):
            pyautogui.click(1125, 419)
            time.sleep(1)

    def go_next_page(self) -> None:
        # next_btn = self.driver.find_element(By.CLASS_NAME, "page page-btn-next")


        try:
            self.next_btn = self.driver.find_element(By.CLASS_NAME, "page-btn-next")
            # self.next_btn.click()
            self.driver.execute_script("arguments[0].click();", self.next_btn)
        except Exception as err:
            print(err)
        # for i in range(10):
        #     self.next_btn = self.driver.find_element(By.CLASS_NAME, "page-btn-next")
        #     self.next_btn.click()

        # time.sleep(2)
        # interval = (random.random() * 2)
        # time.sleep(1 + interval)
        # time.sleep(1)
        time.sleep(0.5)


        test_page_index = self.get_current_page_acitve_index()
        while self.current_page_acitve_index == test_page_index:
            # test_page_index = self.go_next_page()
            # test_page_index = self.get_current_page_acitve_index()
            # print("retry go next !!! {} vs {}".format(self.current_page_acitve_index, test_page_index))
            self.driver.refresh()
            # # self.driver.find_element(By.)
            # for i in range(5):
            #     pag.click()
            #     time.sleep(.5)

            # try:
            #     self.next_next_btn = self.driver.find_element(
            #         By.XPATH, 
            #         "//a[onclick='gotoPage(this, {})']".format(
            #             self.current_page_acitve_index + 1
            #         )
            #     )
            #     self.next_next_btn.click()
            # except:
            #     print("tag a next next not found.")

            # * usable
            # x = threading.Thread(target=self.autoclick_afew_times_thread_func)
            # x.start()
            # time.sleep(3)
            # x.join()

            # time.sleep(.5)

            # test_page_index = self.get_current_page_acitve_index()
            # try:
            #     w, h = pag.size()
            #     x = w * 0.75,
            #     y = h * 0.45
            #     pag.click(x, y)
            # except Exception as e:
            #     print(e)
            # try:
            #     self.back_btn = self.driver.find_element(By.CLASS_NAME, "page-arr-back")
            #     self.back_btn.click()
            #     # time.sleep(1)
            #     time.sleep(0.5)
            # except Exception as err:
            #     print(err)

                # e.
                # print(e.with_traceback())


            self.go_next_page()

            # time.sleep(2)
        print(f"page change to page {test_page_index}")

        self.current_page_acitve_index = test_page_index

        # if self._can_go_next_page():
        #     self.next_btn.click()
        #     # time.sleep(2)
        #     # time.sleep(0.5)
        #     time.sleep(1)
        # else:
        #     print("END OF SCRAPPING ALL NUMBERS.")
        