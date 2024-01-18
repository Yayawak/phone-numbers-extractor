import selenium
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from InputsManager import InputsManager
from Nexter import Nexter
import re
from Utils import no_list_to_str
from file_manipulator import writefile, readfile, listnumbers_to_encoded_string
import time
import pyautogui 
# from selenium.webdriver.safari.options import Options
import threading

def preventNotIdlingMouseThreadFn():
# def preventNotIdlingMouseThreadFn(tname):
    ...
    while (True):
        # print(f"Start Prevent Idling... tname = {tname}")
        print(f"Start Prevent Idling... ")
        pyautogui.move(-1, 0)
        time.sleep(30)
        pyautogui.move(+1, 0)
        time.sleep(30)

class AisMain:

    
                
    def __init__(self):
        print("Entered constructure.")
        # self.driver = webdriver.Safari()
        opt = webdriver.ChromeOptions()
        opt.add_argument("--headless")
        opt.add_argument("--disable-gpu")
        # opt.add_experimental_option(
        #     "pref", {
        #         "profile.managed_default_content_settings.images": 2,
        #     }
        # )
        self.driver = webdriver.Chrome(
            options=opt
        )


        self.ais_url = "https://become-ais-family.ais.co.th/find-by-mobile?fbclid=IwAR0tdUm1xq_8GPh0XzSukKbbFx0htKg23MIs6Ns6d2zXFEEtH_HrT8togvo"
        self.driver.get(self.ais_url)

        self.inputManager = InputsManager(self.driver)
        self.inputManager.retriveInputs()

        self.nexter = Nexter(self.driver)
        
        
        # time.sleep(2)

        # self.current_page_acitve_index = '1'
        # tx = threading.Thread(target=preventNotIdlingMouseThreadFn, args=("TTread TTTT"))
        tx = threading.Thread(target=preventNotIdlingMouseThreadFn)
        tx.start()


        self.autorun()
    


    
    def autorun(self):
        print("auto running...")
        # pms = permutation("1234")
        # pms = self.permutation("7812")
        # print("PMS...")
        # print(pms)

        # input_no = [9, 2, 8]
        # input_no = [9, 2, 8, 1]
        # input_no = [9]
        # self.inputManager.browseFirstNDigits(input_no) 
        # nos = self.getAvailableNumbers()
        # print(f"input no is {input_no} -> get nos = {nos}.")

        # ต้องมีค่าต่ำกว่า 500 ถึงจะเก็บเลขลง db
        # threshold_no = 500
        # no_list = []
        # if nos > 0 and nos < threshold_no:
        #     no_sub_list = self.nexter.get_all_numbers_in_page()
        #     no_list.append(no_sub_list)

        # print("no list = ", no_list)

        # numbers = self.nexter.get_all_numbers()
        # print(f"#nos = {len(numbers)}")
        # print("All number is ", numbers)


        nos = -1
        no_list = []

        no_sub_list = self.nexter.get_all_numbers_in_page()
        no_list.extend(no_sub_list)
        # self.nexter.go_next_page()

        # while nos != 0:
        i = 0
        N = self.getAvailableNumbers()
        # while self.nexter._can_go_next_page():
        # while True:
        end_page_idx = N // 20
        while i < end_page_idx:
            
            # no_sub_list = self.nexter.get_all_numbers_in_page()
            # no_list.extend(no_sub_list)
            self.nexter.go_next_page()


            no_sub_list = self.nexter.get_all_numbers_in_page()
            no_list.extend(no_sub_list)


            # while self.current_page_acitve_index
            # print(f"Go next page with current numbers len = {nos}")
            print(f"Go next page [{self.nexter.current_page_acitve_index}] with current numbers len = {len(no_list)}")
            # print(no_list)
            print("----------------")
            i += 1

            s = listnumbers_to_encoded_string(no_list)
            writefile(s)

            # if (i > 10):
            #     break
        
        # for x in no_list:
        #     # print(x)
        #     print(no_list_to_str(x))
        # for nb in no_list:
        print("n = {}".format(i))

        # s = listnumbers_to_encoded_string(no_list)
        # writefile(s)



            

    def getAvailableNumbers(self) -> int:
        # print("Gettting Available Number")
        try:
            x = self.driver.find_element(By.CLASS_NAME, "font_green")
            # print("font green : ", x)
            assert x is not None
            if x.text.find("เบอร์") != -1:
                # found ! 
                num = re.findall(r"\d+", x.text)[0]
                # print(num)
                return int(num)
            # self.driver.close()
        except Exception as e:
            print("Error getting avialable number due to can't find font_green element which is for retrive available number ---> ", e)
            return -1

    
    
        

    def is_found_onwebsite(self, nolist:list) -> bool:
        self.inputManager.browseFirstNDigits(nolist)
        nos = self.getAvailableNumbers();
        print(nolist, " -> Got Available Number = ", nos)
        if nos == -1:
            print("Error find element font_green (available number element)")
            return False
        elif nos == 0:
            return False
        elif nos > 0:

            return True
        return False

    
    def is_number_pass_condition(self, nolist:list):
        # ไม่มีเลขระหว่าง 0 ถึง 7 อยู่เป็นตำแหน่งที่สองเช่น 01x-xxx-xxx -> 07x-xxx-xxx ไม่มีจ้า
        if nolist[0] < 7:
            return False
        # if len(nolist) > 4:
        #     if nolist[2] == '3' and nolist[3] == '4':
        #         return False
        return True

    
    def permutation(self, s):
        if len(s) == 1:
            return [s]
    
        perm_list = [] # resulting list
        for a in s:
            remaining_elements = [x for x in s if x != a]
            z = self.permutation(remaining_elements) # permutations of sublist

            # print("Z = ", z)
            for t in z:
                # print(t)
                p = [a] + t
                no_int_list = [int(x) for x in p]
                print("p -> ", p)
                # if not self.is_found_onwebsite(p):
                # print(no_int_list)
                if not self.is_number_pass_condition(no_int_list):
                    continue
                if not self.is_found_onwebsite(no_int_list):
                    continue
                    
                numbers = self.nexter.get_all_numbers_in_page()
                # if is_number_pass_condition(p) and is_found_onwebsite(p):
                perm_list.append(p)

        return perm_list