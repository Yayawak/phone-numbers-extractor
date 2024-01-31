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
        aismain = AisMain()
        # aismain.driver.close()
    except Exception as e:
        print("Exception from base __main__.py....", e)



if __name__ == '__main__':
    test01()

