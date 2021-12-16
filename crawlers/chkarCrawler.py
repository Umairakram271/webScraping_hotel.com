from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from crawlers.constant_chkar import chkar_URL
import time
import math
import csv


class AirbnbCrawler():
    def __init__(self, ):
        self.driver = None
        self.wait = WebDriverWait(self.driver, 60)
        self.page_status = False
        self.page_source = ""
        self.status = "warm"
        self.request_time = None

    def write_cvs(self, data, name):
        header = ["hotel_title", "address_hotel", "Room_condition", "Guest", "Bed_room", "Beds", "price"]
        f_name = f'chkar.csv'
        print(name)
        with open(f_name,    'w') as data_file:
            writer = csv.writer(data_file)
            writer.writerow(header)
            for row in data:
                writer.writerow(row)
            data_file.close()
        return True

    def query(self, name):
        self.driver = webdriver.Chrome('/Users/umair/Desktop/Selenium/airbnb/chromedriver')
        self.wait = WebDriverWait(self.driver, 60)
        self.status = "initialized"
        self.driver.get(chkar_URL[name])
        time.sleep(5)
        import pdb;pdb.set_trace()

        try:
            results = self.parse_result()
            if self.write_cvs(results, name):
                print("data inserted")
            return results
        except Exception as e:
            print(e)
        finally:
            self.driver.quit()

    def parse_result(self):
        time.sleep(4)
        try:
            total_records = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH,
                                                '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div/div[2]'
                                                '/div/div/div/ul/li[1]/div/span[6]/span'))).text
            chkar_list = []
            # text = self.driver.find_elements_by_css_selector('div._1DzFT._21uJd')
            page = 1
            while True:
                print("umair")
                text = self.driver.find_elements_by_css_selector('div._1DzFT._21uJd')
                for z in text:
                    row_data = []
                    detail_page = z.find_element_by_css_selector('a._3CQrd')
                    link = detail_page.get_attribute('href')
                    self.driver.execute_script(f'window.open("{link}","_blank")')

                    self.driver.switch_to.window(self.driver.window_handles[1])
                    time.sleep(5)
                    try:
                        hotel_title = self.driver.find_element_by_css_selector('h1._314yM._1dsEp').text
                        if hotel_title == '':
                            hotel_title = "N/A"
                        if len(hotel_title) > 0:
                            row_data.append(hotel_title)
                    except:
                        hotel_title = "N/A"
                    try:
                        address_hotel = self.driver.find_element_by_css_selector('span._1qXCG').text
                        if address_hotel == '':
                            address_hotel = "N/A"
                        if len(address_hotel) > 0:
                            row_data.append(address_hotel)
                    except:
                        address_hotel = "N/A"
                    try:
                        var = self.driver.find_elements_by_css_selector('div._2mAA1')
                        for room in var:
                            room_title = room.find_element_by_css_selector('div._3hbKy.tQGsV').text
                            room_title = room_title.replace("\n", " ")
                            row_data.append(room_title)
                            row_data = list(dict.fromkeys(row_data))
                        if room_title == '':
                            room_title = "N/A"
                    except:
                        room_title = "N/A"
                    try:
                        price = self.driver.find_element_by_css_selector('span._1KfvX').text
                        if price == '':
                            price = "N/A"
                        if len(price) > 0:
                            row_data.append(price)
                    except:
                        price = "N/A"

                    list(dict.fromkeys(row_data))
                    chkar_list.append(row_data)
                    print(chkar_list)
                    self.driver.close()
                    self.driver.switch_to.window(self.driver.window_handles[0])
                    time.sleep(4)
                import pdb; pdb.set_trace()
                next = self.driver.find_element_by_css_selector('li.rc-pagination-next')
                page_number = self.driver.find_elements_by_css_selector('li.rc-pagination-item')
                page_lenght = len(page_number)
                try:
                    if page == page_lenght:
                        break
                    else:
                        self.driver.execute_script("arguments[0].click();", next)
                        page = page+1
                except:
                    print("page not found")

            return chkar_list

        except Exception as e:
            print("DSf", e)
            return []


def scrap_hotel():
    locations = ["murree","Hunza","skardu","Gilgit","Gojal"]
    for location in locations:
        # print("location",location ,"url",Hotel_URL[location])
        AirbnbCrawler().query(location)
    print("done")


