from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from crawlers.constant_hotel import hotel_cites

# Establish chrome driver and go to report site URL

class Crawler():
    def __init__(self):
        self.driver = None
        self.wait = WebDriverWait(self.driver, 60)
        self.base_url = None
        self.page_status = False
        self.page_source = ""


    def query(self, name):
        # self.driver = webdriver.Chrome('/mysite/crawlers/chromedriver.exe')
        self.driver = webdriver.Chrome(executable_path='/home/akmal/Desktop/crawler/mysite/crawlers/chromedriver.exe')
        self.wait = WebDriverWait(self.driver, 60)
        try:
            self.page_source = self.driver.page_source
            result = self.parse_result()
            csvFile = self.csvWrite()
            return result
        except Exception as e:
            print(e)
        finally:
            self.driver.quit()
    def csvWrite(self):
        pass

    def parse_result(self):
        self.driver = webdriver.Chrome()
        driver = self.driver()
        import pdb; pdb.set_trace()
        driver.get('https://www.hotels.com/search.do?destination-id=1693203&q-'
                         'check-in=2021-11-24&q-check-out=2021-11-25&q-rooms=1&q-room-0-'
                         'adults=2&q-room-0-children=0&sort-order=BEST_SELLER')
        blockData= driver.find_elements_by_css_selector('div.-RcIiD')
        print(blockData)
        row_data = []
        hotel_list = []
        for z in blockData:
            try:
                hotelTitile = z.find_element_by_css_selector('h2._3zH0kn').text
                if hotelTitile == '':
                    hotelTitile = "N/A"
                print(hotelTitile)
            except:
                hotelTitile = "N/A"
            try:
                address = z.find_element_by_css_selector('p._2oHhXM').text
                if address == '':
                    address = "N/A"
                print(address)
            except:
                address = "N/A"
            try:
                placeTitle = z.find_element_by_css_selector('p._2LH_yj').text
                if placeTitle == '' :
                    placeTitle = "N/A"
                print(placeTitle)
            except:
                placeTitle="N/A"
            try:
                rang_title = z.find_element_by_css_selector('ul._2sHYiJ._3JLCGC').text
                if rang_title == '':
                    rang_title = "N/A"
                print(rang_title)
            except:
                rang_title = "N/A"
            try:
                reating = z.find_element_by_css_selector('span._1biq31').text
                if reating == "":
                    reating = "N/A"
                print(reating)
            except:
                reating = "N/A"
            try:
                status = z.find_element_by_css_selector('span._3XN8b8').text
                if status == "":
                    status = "N/A"
                print(status)
            except:
                status = "N/A"
            try:
                parking = z.find_element_by_css_selector('ul._1CyeN6').text
                if parking == "":
                    parking = "N/A"
                print(parking)
            except:
                parking = "N/A"
            try:
                price = z.find_element_by_css_selector("span._2R4dw5").text
                if price == "":
                    price = "N/A"
                print(price)
            except:
                price = "N/A"
            if len(hotelTitile) > 0:
                row_data.append(hotelTitile)
            if len(address) > 0:
                row_data.append(address)
            if len(placeTitle) > 0:
                row_data.append(placeTitle)
            if len(rang_title) > 0:
                row_data.append(rang_title)
            if len(reating) > 0:
                row_data.append(reating)
            if len(status) > 0:
                row_data.append(status)
            if len(parking) > 0:
                row_data.append(parking)
            if len(price) > 0:
                row_data.append(price)
        return hotel_list.append(row_data)





    def scrap_hotel(self, hotel_cites):
        for data in ['murree']:
            self.query()



