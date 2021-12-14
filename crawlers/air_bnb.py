from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from crawlers.constant_air_bnb import AIRBNB_URL
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
        header = ["Place", "Hotel", "Room_Detail", "Price"]
        f_name = f'airbnb_{name}.csv'
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
        self.driver.get(AIRBNB_URL[name])

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
                EC.element_to_be_clickable((By.XPATH, '//*[@id="site-content"]/div[1]/div/div/div/div/div/section/h1/div'))).text

            pages = int(total_records.replace("+", " ").split(" ")[0])/20
            pages = math.ceil(pages)
            airbnb_list = []
            next_page = 'a._1bfat5l'
            for page in range(1, pages+1):
                print("page", page)
                text = self.driver.find_elements_by_css_selector('div._8s3ctt')
                for z in text:
                    row_data = []
                    place_title = z.find_element_by_css_selector('div._1xzimiid')
                    hotel_title = z.find_element_by_css_selector('span._1whrsux9')
                    if len(place_title.text) > 0:
                        row_data.append(place_title.text)
                    if len(hotel_title.text) > 0:
                        row_data.append(hotel_title.text)
                    room_title = z.find_elements_by_css_selector('span._3hmsj')
                    r_detail = ''
                    for i in room_title:
                        room_detail = i.text
                        if len(room_detail) > 0:
                            r_detail += f"{room_detail} \n "
                    row_data.append(r_detail)
                    reating = z.find_elements_by_css_selector('div._h34mg6')
                    for rate in reating:
                        reating_detail = rate.text
                        row_data.append(reating_detail)
                    airbnb_list.append(row_data)
                print(airbnb_list)
                if page < pages:
                    self.driver.find_element_by_css_selector(next_page).click()
                    time.sleep(4)
            return airbnb_list
        except Exception as e:
            print("DSf", e)
            return []


def scrap_airbnb():
    locations = ["murree", "naran", "kagan","shogran","sawat", "kalam","skardu","Gilgit","Hunza", "Chitral",
                 "Kailash","Galiyat", "Karachi","Lahore","Islamabad","Hyderabad","Multan","Faisalabad","Peshawar",
                 "Quetta","Bahawalpur","Sahiwal", "Abbotabad"]
    for location in locations:
        # print("location",location ,"url",AIRBNB_URL[location])
        AirbnbCrawler().query(location)
    print("done")
