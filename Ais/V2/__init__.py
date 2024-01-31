from AisMain import AisMain
import threading
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


def test00():
    ais_url = "https://become-ais-family.ais.co.th/find-by-mobile?fbclid=IwAR0tdUm1xq_8GPh0XzSukKbbFx0htKg23MIs6Ns6d2zXFEEtH_HrT8togvo"
    driver = webdriver.Chrome()
    driver.get(ais_url)
    while(True):
        ...
        try:
            next_btn = driver.find_element(By.XPATH, "//a[@class='page page-btn-next']")
            # next_btn.click()
            driver.execute_script("arguments[0].click();", next_btn)
        
            # ActionChains(driver).click(next_btn).perform()
            print("success click to next page")
        # except:
        except Exception as e:
            print("Error founded can't find element next or can't click")
            print(e)
        
        time.sleep(3)
    driver.close()


def test01():
    try:
        # aismain = AisMain()
        for firstdigit in range(10):
            # 0 to 9
            ...
            for seconddigit in range(10):
                ...
                ais_branch = AisMain([firstdigit, seconddigit])
                # nos = self.getAvailableNumbers()
                # if (nos == 0)
        aismain = AisMain([9, 3])
        # aismain.driver.close()
    except Exception as e:
        print("Exception from base __main__.py....", e)

def test02():
    def subthread(firstdigit, seconddigit):
        ais_branch = None
        try:
            numlist = [firstdigit, seconddigit]
            name = str(numlist)
            ais_branch = AisMain(numlist, name)
            nos = ais_branch.getAvailableNumbers()
            if (nos == 0):
                print(f"branch {name} not found numbers")
                ...
            else:
                # found *
                print(f"auto running on branch {name}")
                ais_branch.autorun()
        except Exception as err:
            print("Exception on create subthread of Ais branch first 2 digits {}".format(name))
            print(err)
            if ais_branch is not None:
                ais_branch.driver.close()



    try:
        ts = []
        # for firstdigit in range(10):
        #     for seconddigit in range(10):
        for firstdigit in [8,9]:
            for seconddigit in [8,9]:
                t = threading.Thread(target=subthread, args=(firstdigit, seconddigit))
                ts += [t]
                t.start()
        for t in ts:
            t.join()

        # aismain.driver.close()
    except Exception as e:
        print("Exception from base __main__.py....", e)



if __name__ == '__main__':
    # test01()
    test02()

