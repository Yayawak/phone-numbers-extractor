import threading 
from selenium import webdriver 
    
class ScrapeThread(threading.Thread): 
    def __init__(self, url): 
        threading.Thread.__init__(self) 
        self.url = url 

    def run(self): 
        print("running on url = {}".format(self.url))
        # driver = webdriver.Chrome() 
        driver = webdriver.Safari()
        driver.get(self.url) 
        page_source = driver.page_source 

        print("try to get data from url = {}".format(self.url))
        driver.close() 
        # do something with the page source 

urls = [ 
    'https://en.wikipedia.org/wiki/0', 
    'https://en.wikipedia.org/wiki/1', 
    'https://en.wikipedia.org/wiki/2', 
    'https://en.wikipedia.org/wiki/3', 
] 


if __name__ == "__main__":
    # print("Start running multithreaing...")
    # threads = [] 
    # for url in urls: 
    #     t = ScrapeThread(url) 
    #     t.start() 
    #     threads.append(t) 

    # for t in threads: 
    #     t.join()
    # print("End of all thread ... joined all thread.")


    driver = webdriver.Safari()
    driver.get(urls[0])
    print(driver.page_source)

    dv = webdriver.Safari()
    dv.get(urls[1])

    print(dv.page_source)
