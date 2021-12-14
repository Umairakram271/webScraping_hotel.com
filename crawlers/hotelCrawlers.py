from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from crawlers.constant_hotel import Hotel_URL
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
        header = ["hotel_title", "address_hotel", "place_title", "rang_title","status_title","condition",
                  "parking","price"]
        f_name = f'hoetl_{name}.csv'
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
        self.driver.get(Hotel_URL[name])
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
                EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div[2]/div/div/div[1]/div/div/div/h2'))).text
            text = self.driver.find_elements_by_css_selector('div.-RcIiD')
            time.sleep(2)
            hotel_list = []
            for z in text:
                row_data = []
                try:
                    hotel_title = z.find_element_by_css_selector('h2._3zH0kn').text
                    if hotel_title == '':
                        hotel_title = "N/A"
                except:
                    hotel_title = "N/A"
                try:
                    address_hotel = z.find_element_by_css_selector("p._2oHhXM").text
                    if address_hotel == '':
                        address_hotel = "N/A"
                except:
                    address_hotel = "N/A"
                try:
                    place_title = z.find_element_by_css_selector('p._2LH_yj').text
                    if place_title == '':
                        place_title = "N/A"
                except:
                    place_title = "N/A"
                try:
                    rang_title = z.find_element_by_css_selector('ul._2sHYiJ._3JLCGC').text
                    if rang_title == '':
                        rang_title = "N/A"
                except:
                    rang_title = "N/A"
                try:
                    reating_title = z.find_element_by_css_selector('span._1biq31').text
                    if reating_title == '':
                        reating_title = "N/A"
                except:
                    reating_title = "N/A"
                try:
                    condition = z.find_element_by_css_selector('span._3XN8b8').text
                    if condition == '':
                        condition = "N/A"
                except:
                    condition = "N/A"
                try:
                    parking = z.find_element_by_css_selector('ul._1CyeN6').text
                    parking_detail = parking.replace("\ue950\n", " ")
                    parking_detail = parking_detail.replace("\ue940\n", " ")
                    parking_detail = parking_detail.replace("\ue935\n", " ")
                    parking_detail = parking_detail.replace("\ue95b\n", " ")
                    parking_detail = parking_detail.replace("\ue9b2\n", " ")
                    parking_detail = parking_detail.replace("\ue93e\n", " ")
                    parking_detail = parking_detail.replace("\ue933\n", " ")
                    parking_detail = parking_detail.replace("\ue949\n", " ")
                    parking_detail = parking_detail.replace("\ue90a\n", " ")
                    parking_detail = parking_detail.replace("\ue93f\n", " ")
                    parking_detail = parking_detail.replace("\ue945\n", " ")
                    parking_detail = parking_detail.replace("\ue92f\n", " ")


                except:
                    parking_detail = "N/A"
                # parking_detail = parking_detail.replace("\ue935\n", " ")
                try:
                    price = z.find_element_by_css_selector('span._2R4dw5').text
                    if condition == '':
                        condition = "N/A"
                except:
                    price = "N/A"

                if len(hotel_title) > 0:
                    row_data.append(hotel_title)
                if len(address_hotel) > 0:
                    row_data.append(address_hotel)
                if len(place_title) > 0:
                    row_data.append(place_title)
                if len(rang_title) > 0:
                    row_data.append(rang_title)
                if len(reating_title) > 0:
                    row_data.append(reating_title)
                if len(condition) > 0:
                    row_data.append(condition)
                if len(parking_detail) > 0:
                    row_data.append(parking_detail)
                if len(price) > 0:
                    row_data.append(price)
                hotel_list.append(row_data)
                print(hotel_list)
            return hotel_list

        except Exception as e:
            print("DSf", e)
            return []


def scrap_hotel():
    locations = ["murree","Lahore"]
    for location in locations:
        # print("location",location ,"url",Hotel_URL[location])
        AirbnbCrawler().query(location)
    print("done")


